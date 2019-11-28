import os
import pygame
from discord.ext import commands
from discord.ext.commands import group, Cog
from .i18n import embed
from .utils import lone_group
from .tmpfiles import sendsurf

WIDTH, HEIGHT = SIZE = 1000, 1000
SMOLW, SMOLH = SMOLS = WIDTH // 20, HEIGHT // 20

try:
    PLACE = pygame.image.load(os.path.join('resources', 'place.png'))
except pygame.error:
    PLACE = pygame.Surface(SIZE)
    PLACE.fill((255, 255, 255))

class Place(Cog):
    """place/cmd-desc"""

    def __del__(self):
        pygame.image.save(PLACE, os.path.join('resources', 'place.png'))

    @group(invoke_without_command=True, description='place/cmd-desc')
    @lone_group(False)
    async def place(self, ctx):
        """place/cmd-help"""
        pass

    @staticmethod
    def around(x, y):
        surf = pygame.Surface(SMOLS, pygame.SRCALPHA)
        surf.fill((0, 0, 0, 0))
        surf.blit(PLACE, (SMOLW // 2 - x, SMOLH // 2 - y))
        return surf

    @place.command(description='place/get-desc')
    async def get(self, ctx, x: int = None, y: int = None):
        if y is None:
            return await sendsurf(ctx.send, PLACE, 'place', 'place.png')
        if not (0 <= x < WIDTH and 0 <= y < HEIGHT):
            return await ctx.send(embed=embed(ctx,
                title=('error',),
                description=('place/coord-error', x, y),
                color=0xff0000
            ))
        surf = self.around(x, y)
        surf = pygame.transform.scale(surf, SIZE)
        await sendsurf(ctx.send, surf, 'place', 'portion.png')

    @commands.cooldown(1, 300.0, commands.BucketType.user)
    @place.command(description='place/set-desc')
    async def set(self, ctx, x: int, y: int, r: int, g: int, b: int):
        CHECK, CROSS = '\u2705\u274e'
        if not (0 <= x < WIDTH and 0 <= y < HEIGHT):
            return await ctx.send(embed=embed(ctx,
                title=('error',),
                description=('place/coord-error', x, y),
                color=0xff0000
            ))
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return await ctx.send(embed=embed(ctx,
                title=('error',),
                description=('place/color-error', r, g, b),
                color=0xff0000
            ))
        surf = self.around(x, y)
        surf.set_at((SMOLW // 2, SMOLH // 2), (r, g, b))
        surf = pygame.transform.scale(surf, SIZE)
        msg = await sendsurf(ctx.send, surf, 'place', 'confirm.png', embed=embed(ctx,
            title=('place/confirm-title',),
            description=('place/confirm',),
            color=0xffff00
        ))
        await msg.add_reaction(CHECK)
        await msg.add_reaction(CROSS)
        reaction, user = await ctx.bot.wait_for('reaction_add', check=lambda r, u: (
            r.message.id == msg.id
            and u.id == ctx.author.id
            and str(r) in (CHECK, CROSS)
        ))
        if str(reaction) == CHECK:
            PLACE.set_at((x, y), (r, g, b))
            await ctx.send(embed=embed(ctx,
                title=('success',),
                description=('place/set', x, y, r, g, b),
                color=0x55acee
            ))
        else:
            await ctx.send(embed=embed(ctx,
                title=('place/cancelled-title',),
                description=('place/cancelled',),
                color=0xff0000
            ))
