import random
import discord as d
from contextlib import contextmanager
from discord.ext.commands import group, check, is_owner
from ..games import Games, DummyCtx
from ..i18n import i18n
from .data import Weapon, weapons, Armor, armors, Item, items, monsters, Player

FIGHT = '\N{CROSSED SWORDS}'
ITEM = '\N{PILL}'

locked = set()
@contextmanager
def lock(leid):
    if leid in locked:
        yield True
        return
    locked.add(leid)
    try:
        yield False
    finally:
        locked.remove(leid)

class Fight(Games):
    """fight/cog-desc"""
    async def load_player(self, ctx):
        res = self.db.execute(
            'SELECT fight_health, fight_weapons, fight_armors, \
fight_gold, fight_items FROM users WHERE user_id=?',
            (ctx.author.id,)
        ).fetchone()
        if res is None or res['fight_health'] is None:
            await ctx.send(i18n(ctx, 'fight/creating-profile'))
            if res is None:
                self.db.execute(
                    'INSERT INTO users (user_id, fight_health, fight_weapons, \
fight_armors, fight_gold, fight_items) VALUES (?, ?, ?, ?, ?, ?)',
                    (ctx.author.id, 5, weapons['fist'].name,
                        armors['clothes'].name, 0, '')
                )
            else:
                self.db.execute(
                    'UPDATE users SET fight_health=?, fight_weapons=?, \
fight_armors=?, fight_gold=?, fight_items=? WHERE user_id=?',
                    (5, weapons['fist'].name, armors['clothes'].name, 0, '',
                        ctx.author.id)
                )
            return Player(ctx.author.display_name, 5)
        return Player(
            ctx.author.display_name,
            res['fight_health'],
            res['fight_gold'],
            [weapons[w[13:]].copy() for w in res['fight_weapons'].split(';')],
            [armors[a[12:]].copy() for a in res['fight_armors'].split(';')],
            [items[i[11:]].copy() for i in res['fight_items'].split(';')]
            if res['fight_items']
            else []
        )

    def dump_player(self, ctx, player):
        self.db.execute(
            'UPDATE users SET fight_health=?, fight_weapons=?, fight_armors=?, \
fight_gold=?, fight_items=? WHERE user_id=?', (
                player.health, ';'.join(w.name for w in player.weapons),
                ';'.join(a.name for a in player.armors),
                player.gold, ';'.join(i.name for i in player.items),
                ctx.author.id
            )
        )

    def damag(self, damaged, damager):
        if (
            isinstance(damager.weapon.damage, int)
            and isinstance(damaged.armor.defense, int)
        ):
            damage = max(0, damager.weapon.damage
                - damaged.armor.defense)
            damaged.health -= damage
        elif isinstance(damager.weapon.damage, int):
            damaged.health -= damager.weapon.damage
            damage = damaged.armor.defense(
                damaged, damager, damager.weapon.damage
            )
        elif isinstance(damaged.armor.defense, int):
            damage = damager.weapon.damage(damager, damaged)
        else:
            damage = damager.weapon.damage(damager, damaged)
            damage = damaged.armor.defense(damaged, damager, damage)
        return damage

    def do_fight(self, player, enemy):
        loops = 0
        while player.health > 0 and enemy.health > 0 and loops < 50:
            damage = self.damag(enemy, player)
            if player.health <= 0 or enemy.health <= 0:
                break
            yield {
                'damaged': enemy,
                'damage': damage,
                'damager': player
            }
            damage = self.damag(player, enemy)
            if player.health <= 0 or enemy.health <= 0:
                break
            yield {
                'damaged': player,
                'damage': damage,
                'damager': enemy
            }
            loops += 1
        yield {
            'winner': player if player.health > enemy.health else enemy,
            'loser': enemy if player.health > enemy.health else player
        }

    @group(description='fight/fight-desc')
    async def fight(self, ctx):
        """fight/fight-help"""
        pass

    async def use_item(self, ctx, checc, player, enemy):
        await ctx.send(embed=d.Embed(
            title=i18n(ctx, 'fight/items-title'),
            description='\n'.join(
                '{} ({})'.format(i.name[11:], i.nam(ctx))
                for i in player.items
            )
        ).set_footer(text=i18n(ctx, 'fight/items-instructions')))
        msg = await self.bot.wait_for('message', check=checc)
        if msg.content != 'nvm':
            for i in player.items:
                if i.name[11:].lower().startswith(msg.content.lower()):
                    item = i
                    break
            item.action(player, enemy)
            player.items.remove(item)

    async def fight_npc(self, ctx, enemy):
        GREEN, RED, BLUE, YELLOW = 0x77b255, 0xff0000, 0x00aaff, 0xffff00
        player = await self.load_player(ctx)
        def checc(msg):
            if (
                msg.channel.id != ctx.channel.id
                or msg.author.id != ctx.author.id
            ):
                return False
            if msg.content == 'nvm':
                return True
            for i in player.items:
                if i.name[11:].lower().startswith(msg.content.lower()):
                    return True
            return False
        msg = await ctx.send(embed=d.Embed(
            title=i18n(ctx, 'fight/battle-started-title'),
            description=i18n(ctx, 'fight/battle-started', FIGHT, ITEM),
            color=BLUE
        ))
        await msg.add_reaction(FIGHT)
        await msg.add_reaction(ITEM)
        reaction, user = await self.bot.wait_for('reaction_add',
            check=lambda r, u: (
                r.emoji in (FIGHT, ITEM)
                and r.message.id == msg.id
                and u.id == ctx.author.id
            )
        )
        if reaction.emoji == ITEM:
            await self.use_item(ctx, checc, player, enemy)
        for event in self.do_fight(player, enemy):
            if 'damaged' not in event:
                # winner and loser
                await ctx.send(embed=d.Embed(
                    title=i18n(ctx, 'fight/battle-ended-title'),
                    description=i18n(ctx, 'fight/battle-ended'),
                    color=(
                        RED
                        if event['loser'] == player
                        else GREEN
                    )
                ).add_field(
                    name=i18n(ctx, 'fight/winner'),
                    value=event['winner'].nam(ctx)
                ).add_field(
                    name=i18n(ctx, 'fight/loser'),
                    value=event['loser'].nam(ctx)
                ))
                winner, loser = event['winner'], event['loser']
                break
            if event['damage'] <= 0:
                continue
            msg = await ctx.send(embed=d.Embed(
                title=i18n(ctx, 'fight/damage-done-title'),
                description=i18n(
                    ctx,
                    'fight/damage-done',
                    event['damager'].nam(ctx),
                    event['damage'],
                    event['damaged'].nam(ctx),
                    event['damager'].weapon.nam(ctx)
                ),
                color=(
                    RED
                    if event['damaged'] == player
                    else GREEN
                )
            ).add_field(
                name=i18n(ctx, 'fight/your-health'),
                value=player.health
            ).add_field(
                name=i18n(ctx, 'fight/enemys-health'),
                value=enemy.health
            ))
            await msg.add_reaction(FIGHT)
            await msg.add_reaction(ITEM)
            reaction, user = await self.bot.wait_for('reaction_add',
                check=lambda r, u: (
                    r.emoji in (FIGHT, ITEM)
                    and r.message.id == msg.id
                    and u.id == ctx.author.id
                )
            )
            if reaction.emoji == ITEM:
                await self.use_item(ctx, checc, player, enemy)
        if loser == player: # :(
            self.db.execute('UPDATE users SET fight_health=NULL, \
fight_weapons=NULL, fight_armors=NULL, fight_gold=NULL, fight_items=NULL WHERE \
user_id=?', (ctx.author.id,))
            await ctx.send(embed=d.Embed(
                title=i18n(ctx, 'fight/death-title'),
                description=i18n(ctx, 'fight/death'),
                color=0
            ))
            return
        if winner == player:
            player.gold += enemy.reward
            self.dump_player(ctx, player)
            await ctx.send(embed=d.Embed(
                title=i18n(ctx, 'fight/reward-title'),
                description=i18n(
                    ctx, 'fight/reward', enemy.reward, enemy.nam(ctx), player.gold
                ),
                color=YELLOW
            ))

    async def fight_player(self, player1, player2, at_stake):
        GREEN, RED, BLUE, YELLOW = 0x77b255, 0xff0000, 0x00aaff, 0xffff00
        dmx1 = DummyCtx(
            author=player1,
            channel=player1.dm_channel,
            send=player1.dm_channel.send
        )
        dmx2 = DummyCtx(
            author=player2,
            channel=player2.dm_channel,
            send=player2.dm_channel.send
        )
        p1 = await self.load_player(dmx1)
        p2 = await self.load_player(dmx2)
        def checc1(msg):
            if (
                msg.channel.id != dmx1.channel.id
                or msg.author.id != dmx1.author.id
            ):
                return False
            if msg.content == 'nvm':
                return True
            for i in p1.items:
                if i.name[11:].lower().startswith(msg.content.lower()):
                    return True
            return False
        def checc2(msg):
            if (
                msg.channel.id != dmx2.channel.id
                or msg.author.id != dmx2.author.id
            ):
                return False
            if msg.content == 'nvm':
                return True
            for i in p2.items:
                if i.name[11:].lower().startswith(msg.content.lower()):
                    return True
            return False
        await dmx1.send(embed=await self.profile_embed(dmx2))
        await dmx2.send(embed=await self.profile_embed(dmx1))
        await dmx2.send(embed=d.Embed(
            title=i18n(dmx2, 'fight/battle-started-title'),
            description=i18n(dmx2, 'fight/battle-started-second', FIGHT, ITEM),
            color=BLUE
        ))
        msg = await dmx1.send(embed=d.Embed(
            title=i18n(dmx1, 'fight/battle-started-title'),
            description=i18n(dmx1, 'fight/battle-started', FIGHT, ITEM),
            color=BLUE
        ))
        await msg.add_reaction(FIGHT)
        await msg.add_reaction(ITEM)
        reaction, user = await self.bot.wait_for('reaction_add',
            check=lambda r, u: (
                r.emoji in (FIGHT, ITEM)
                and r.message.id == msg.id
                and u.id == player1.id
            )
        )
        if reaction.emoji == ITEM:
            await self.use_item(dmx1, checc1, p1, p2)
        for event in self.do_fight(p1, p2):
            if 'damaged' not in event:
                await dmx1.send(embed=d.Embed(
                    title=i18n(dmx1, 'fight/battle-ended-title'),
                    description=i18n(dmx1, 'fight/battle-ended'),
                    color=RED if event['loser'] == p1 else GREEN
                ).add_field(
                    name=i18n(dmx1, 'fight/winner'),
                    value=event['winner'].nam(dmx1)
                ).add_field(
                    name=i18n(dmx1, 'fight/loser'),
                    value=event['loser'].nam(dmx1)
                ))
                await dmx2.send(embed=d.Embed(
                    title=i18n(dmx2, 'fight/battle-ended-title'),
                    description=i18n(dmx2, 'fight/battle-ended'),
                    color=RED if event['loser'] == p2 else GREEN
                ).add_field(
                    name=i18n(dmx2, 'fight/winner'),
                    value=event['winner'].nam(dmx2)
                ).add_field(
                    name=i18n(dmx2, 'fight/loser'),
                    value=event['loser'].nam(dmx2)
                ))
                winner, loser = event['winner'], event['loser']
                break
            if event['damage'] <= 0:
                continue
            # damager msg
            dmx = (dmx1 if event['damager'] == p1 else dmx2)
            await dmx.send(embed=d.Embed(
                title=i18n(dmx, 'fight/damage-done-title'),
                description=i18n(
                    dmx,
                    'fight/damage-done',
                    event['damager'].nam(dmx),
                    event['damage'],
                    event['damaged'].nam(dmx),
                    event['damager'].weapon.nam(dmx)
                ),
                color=GREEN
            ).add_field(
                name=i18n(dmx, 'fight/your-health'),
                value=event['damager'].health
            ).add_field(
                name=i18n(dmx, 'fight/enemys-health'),
                value=event['damaged'].health
            ))
            # damaged msg
            dmx = (dmx1 if event['damaged'] == p1 else dmx2)
            msg = await dmx.send(embed=d.Embed(
                title=i18n(dmx, 'fight/damage-done-title'),
                description=i18n(
                    dmx,
                    'fight/damage-done',
                    event['damager'].nam(dmx),
                    event['damage'],
                    event['damaged'].nam(dmx),
                    event['damager'].weapon.nam(dmx)
                ),
                color=RED
            ).add_field(
                name=i18n(dmx, 'fight/your-health'),
                value=event['damaged'].health
            ).add_field(
                name=i18n(dmx, 'fight/enemys-health'),
                value=event['damager'].health
            ))
            await msg.add_reaction(FIGHT)
            await msg.add_reaction(ITEM)
            reaction, user = await self.bot.wait_for('reaction_add',
                check=lambda r, u: (
                    r.emoji in (FIGHT, ITEM)
                    and r.message.id == msg.id
                    and u.id == dmx.author.id
                )
            )
            if reaction.emoji == ITEM:
                await self.use_item(
                    dmx, (checc1 if event['damaged'] == p1 else checc2),
                    event['damaged'], event['damager']
                )
        wmx = (dmx1 if winner == p1 else dmx2)
        lmx = (dmx1 if loser == p1 else dmx2)
        winner.gold += at_stake
        loser.gold -= at_stake
        loser.health = 5
        self.dump_player(wmx, winner)
        self.dump_player(lmx, loser)
        await wmx.send(embed=d.Embed(
            title=i18n(wmx, 'fight/reward-title'),
            description=i18n(
                wmx, 'fight/reward', at_stake, loser.nam(wmx), winner.gold
            ),
            color=YELLOW
        ))
        await lmx.send(embed=d.Embed(
            title=i18n(lmx, 'fight/loss-title'),
            description=i18n(
                lmx, 'fight/loss', at_stake, winner.nam(lmx), loser.gold
            ),
            color=0
        ))

    name = 'Fight'

    @check(lambda ctx: ctx.guild is not None)
    @fight.command(description='fight/player-desc')
    async def player(self, ctx, gold_at_stake: int, against: d.Member = None):
        """fight/player-help"""
        player1, player2 = await self._gather_game(ctx, against)
        with lock(player1.dm_channel.id) as stopq:
            if stopq:
                await ctx.send(i18n(ctx, 'fight/battle-cancelled', 1))
                return
            with lock(player2.dm_channel.id) as stopq:
                if stopq:
                    await ctx.send(i18n(ctx, 'fight/battle-cancelled', 2))
                    return
                await self.fight_player(player1, player2, gold_at_stake)

    @check(lambda ctx: ctx.guild is None)
    @fight.group(description='fight/npc-desc')
    async def npc(self, ctx):
        """fight/npc-help"""
        pass

    @npc.command(description='fight/random-desc')
    async def random(self, ctx):
        with lock(ctx.channel.id) as stopq:
            if stopq:
                return
            await self.fight_npc(ctx, random.choice(list(monsters.values())).copy())

    @npc.command(description='fight/named-desc')
    async def named(self, ctx, *, enemy):
        with lock(ctx.channel.id) as stopq:
            if stopq:
                return
            if enemy not in monsters:
                await ctx.send(i18n(ctx, 'fight/invalid-enemy', enemy))
                return
            enemy = monsters[enemy].copy()
            await self.fight_npc(ctx, enemy)

    @npc.command(description='fight/list-desc')
    async def list(self, ctx):
        """fight/list-help"""
        with lock(ctx.channel.id) as stopq:
            if stopq:
                return
            await ctx.send('\n'.join(monsters.keys()))

    @npc.command(description='fight/info-desc')
    async def info(self, ctx, enemy):
        with lock(ctx.channel.id) as stopq:
            if stopq:
                return
            if enemy not in monsters:
                await ctx.send(i18n(ctx, 'fight/invalid-enemy', enemy))
                return
            enemy = monsters[enemy].copy()
            await ctx.send(embed=d.Embed(
                title=enemy.nam(ctx)
            ).add_field(
                name=i18n(ctx, 'fight/shop-name'),
                value=enemy.name[14:]
            ).add_field(
                name=i18n(ctx, 'fight/enemy-health'),
                value=enemy.health
            ).add_field(
                name=i18n(ctx, 'fight/enemy-reward'),
                value=enemy.reward
            ).add_field(
                name=i18n(ctx, 'fight/enemy-weapon'),
                value=enemy.weapon.nam(ctx)
            ).add_field(
                name=i18n(ctx, 'fight/enemy-armor'),
                value=enemy.armor.nam(ctx)
            ))

    @is_owner()
    @check(lambda ctx: ctx.guild is None)
    @fight.command()
    async def add_item(self, ctx, item: Item):
        player = await self.load_player(ctx)
        player.items.append(item)
        self.db.execute('UPDATE users SET fight_items=? WHERE user_id=?',
            (';'.join(i.name for i in player.items), ctx.author.id))
        await ctx.send('Success')

    async def profile_embed(self, ctx):
        player = await self.load_player(ctx)
        return d.Embed(
            title=i18n(ctx, 'fight/profile-title', player.nam(ctx))
        ).add_field(
            name=i18n(ctx, 'fight/profile-name'),
            value=player.nam(ctx)
        ).add_field(
            name=i18n(ctx, 'fight/profile-health'),
            value=player.health
        ).add_field(
            name=i18n(ctx, 'fight/profile-gold'),
            value=player.gold
        ).add_field(
            name=i18n(ctx, 'fight/profile-weapons'),
            value='\n'.join(w.nam(ctx) for w in player.weapons[:-1])
                + '\n' + player.weapon.nam(ctx) + ' '
                + i18n(ctx, 'fight/equipped')
        ).add_field(
            name=i18n(ctx, 'fight/profile-armors'),
            value='\n'.join(a.nam(ctx) for a in player.armors[:-1])
                + '\n' + player.armor.nam(ctx) + ' '
                + i18n(ctx, 'fight/equipped')
        ).add_field(
            name=i18n(ctx, 'fight/profile-items'),
            value='\n'.join(i.nam(ctx) for i in player.items) or 'None',
            inline=False
        )

    @check(lambda ctx: ctx.guild is None)
    @fight.command(description='fight/profile-desc')
    async def profile(self, ctx):
        with lock(ctx.channel.id) as stopq:
            if stopq:
                return
            await ctx.send(embed=await self.profile_embed(ctx))

    @check(lambda ctx: ctx.guild is None)
    @fight.group(description='fight/equip-desc')
    async def equip(self, ctx):
        pass

    @equip.command(description='fight/weapon-desc')
    async def weapon(self, ctx, *, weapon: Weapon):
        with lock(ctx.channel.id) as stopq:
            if stopq:
                return
            player = await self.load_player(ctx)
            if weapon not in player.weapons:
                await ctx.send(i18n(ctx, 'fight/equip-unowned'))
                return
            player.weapons.append(player.weapons.pop(player.weapons.index(weapon)))
            self.dump_player(ctx, player)
            await ctx.send(i18n(ctx, 'fight/equip-success'))

    @equip.command(description='fight/armor-desc')
    async def armor(self, ctx, *, armor: Armor):
        with lock(ctx.channel.id) as stopq:
            if stopq:
                return
            player = await self.load_player(ctx)
            if armor not in player.armors:
                await ctx.send(i18n(ctx, 'fight/equip-unowned'))
                return
            player.armors.append(player.armors.pop(player.armors.index(armor)))
            self.dump_player(ctx, player)
            await ctx.send(i18n(ctx, 'fight/equip-success'))

    @check(lambda ctx: ctx.guild is None)
    @fight.command(description='fight/shop-desc')
    async def shop(self, ctx, things):
        """fight/shop-help"""
        with lock(ctx.channel.id) as stopq:
            if stopq:
                return
            if things not in ('items', 'weapons', 'armors'):
                await ctx.send(i18n(ctx, 'fight/shop-error'))
                return
            player = await self.load_player(ctx)
            if things == 'items':
                things = items
                embed = d.Embed(title=i18n(ctx, 'fight/shop-items'))
                for i in items.values():
                    embed.add_field(
                        name=i18n(ctx, 'fight/shop-name'),
                        value=i18n(
                            ctx, 'fight/name-localized', i.name[11:], i.nam(ctx)
                        ),
                        inline=False
                    ).add_field(
                        name=i18n(ctx, 'fight/shop-action'),
                        value=i18n(ctx, i.action.__doc__)
                    ).add_field(
                        name=i18n(ctx, 'fight/shop-price'),
                        value=i.price
                    )
            elif things == 'weapons':
                things = weapons
                embed = d.Embed(title=i18n(ctx, 'fight/shop-weapons'))
                print(weapons)
                for w in weapons.values():
                    print(w.name, w.price)
                    if w.price is None:
                        continue # not for sale
                    print(w.name, w.price)
                    embed.add_field(
                        name=i18n(ctx, 'fight/shop-name'),
                        value=i18n(
                            ctx, 'fight/name-localized', w.name[13:], w.nam(ctx)
                        ),
                        inline=False
                    ).add_field(
                        name=i18n(ctx, 'fight/shop-damage'),
                        value=(
                            w.damage
                            if isinstance(w.damage, int)
                            else i18n(ctx, w.damage.__doc__)
                        )
                    ).add_field(
                        name=i18n(ctx, 'fight/shop-price'),
                        value=w.price
                    )
            elif things == 'armors':
                things = armors
                embed = d.Embed(title=i18n(ctx, 'fight/shop-armors'))
                for a in armors.values():
                    embed.add_field(
                        name=i18n(ctx, 'fight/shop-name'),
                        value=i18n(
                            ctx, 'fight/name-localized', a.name[12:], a.nam(ctx)
                        ),
                        inline=False
                    ).add_field(
                        name=i18n(ctx, 'fight/shop-defense'),
                        value=(
                            a.defense
                            if isinstance(a.defense, int)
                            else i18n(ctx, a.defense.__doc__)
                        )
                    ).add_field(
                        name=i18n(ctx, 'fight/shop-price'),
                        value=a.price
                    )

            embed.set_footer(text=i18n(ctx, 'fight/shop-footer'))
            last_thing = None
            while last_thing != 'quit':
                await ctx.send(embed=embed)
                msg = await self.bot.wait_for('message', check=lambda m: (
                    m.content in tuple(things.keys()) + ('quit',)
                    and m.channel.id == ctx.channel.id
                ))
                last_thing = msg.content
                if last_thing == 'quit':
                    break
                if things[last_thing].price > player.gold:
                    await ctx.send(i18n(ctx, 'fight/shop-expensive'))
                    continue
                player.gold -= things[last_thing].price
                if things is items:
                    player.items.append(things[last_thing])
                    await ctx.send(i18n(ctx, 'fight/shop-bought', player.gold))
                elif things is armors:
                    player.armors.append(things[last_thing])
                    await ctx.send(i18n(ctx, 'fight/shop-equipped', player.gold))
                else:
                    player.weapons.append(things[last_thing])
                    await ctx.send(i18n(ctx, 'fight/shop-equipped', player.gold))
            self.dump_player(ctx, player)
            await ctx.send(i18n(ctx, 'fight/shop-done'))
