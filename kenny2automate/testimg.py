from pygame import Surface
import pygame.image
import pygame.draw
from discord import File
from discord.ext.commands import command, Cog
from .tmpfiles import tmpf

class TestImg(Cog):
    @staticmethod
    async def sendsurf(meth, surf):
        with tmpf('testimg-', '.png') as name:
            pygame.image.save(surf, name)
            await meth(file=File(name, 'image.png'))

    @command()
    async def testimg(self, ctx, w: int, h: int, x: int, y: int, r: int, v: int):
        surf = Surface((w, h))
        surf.fill((255, 255, 255))
        pygame.draw.rect(surf, (0, 0, 0), (x, y, r, v))
        await self.sendsurf(ctx.send, surf)
