from discord.ext.commands import group, Cog
from .i18n import i18n

class Units(Cog):
    """units/cog-desc"""

    @group(aliases=[], invoke_without_command=True, description='units/area-desc')
    async def area(self, ctx):
        pass


    @area.group(invoke_without_command=True, description='units/area-sqkm-desc')
    async def sqkm(ctx):
        pass


    @sqkm.command(invoke_without_command=True, description='units/area-sqkm-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @sqkm.command(invoke_without_command=True, description='units/area-sqkm-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * 1e6 / 2.59e6)

    @sqkm.command(invoke_without_command=True, description='units/area-sqkm-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1/1.196))

    @sqkm.command(invoke_without_command=True, description='units/area-sqkm-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1/10.764))

    @sqkm.command(invoke_without_command=True, description='units/area-sqkm-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1/1550.003))

    @sqkm.command(invoke_without_command=True, description='units/area-sqkm-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * 1e6 / 10000)

    @sqkm.command(invoke_without_command=True, description='units/area-sqkm-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * 1e6 / 4046.856)

    @area.group(invoke_without_command=True, description='units/area-sqm-desc')
    async def sqm(ctx):
        pass


    @sqm.command(invoke_without_command=True, description='units/area-sqm-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @sqm.command(invoke_without_command=True, description='units/area-sqm-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * 1 / 2.59e6)

    @sqm.command(invoke_without_command=True, description='units/area-sqm-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.196))

    @sqm.command(invoke_without_command=True, description='units/area-sqm-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 1 / (1/10.764))

    @sqm.command(invoke_without_command=True, description='units/area-sqm-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1550.003))

    @sqm.command(invoke_without_command=True, description='units/area-sqm-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * 1 / 10000)

    @sqm.command(invoke_without_command=True, description='units/area-sqm-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * 1 / 4046.856)

    @area.group(invoke_without_command=True, description='units/area-sqmil-desc')
    async def sqmil(ctx):
        pass


    @sqmil.command(invoke_without_command=True, description='units/area-sqmil-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / 1e6)

    @sqmil.command(invoke_without_command=True, description='units/area-sqmil-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / 1)

    @sqmil.command(invoke_without_command=True, description='units/area-sqmil-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / (1/1.196))

    @sqmil.command(invoke_without_command=True, description='units/area-sqmil-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / (1/10.764))

    @sqmil.command(invoke_without_command=True, description='units/area-sqmil-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / (1/1550.003))

    @sqmil.command(invoke_without_command=True, description='units/area-sqmil-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / 10000)

    @sqmil.command(invoke_without_command=True, description='units/area-sqmil-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / 4046.856)

    @area.group(invoke_without_command=True, description='units/area-sqyard-desc')
    async def sqyard(ctx):
        pass


    @sqyard.command(invoke_without_command=True, description='units/area-sqyard-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 1e6)

    @sqyard.command(invoke_without_command=True, description='units/area-sqyard-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 1)

    @sqyard.command(invoke_without_command=True, description='units/area-sqyard-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 2.59e6)

    @sqyard.command(invoke_without_command=True, description='units/area-sqyard-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / (1/10.764))

    @sqyard.command(invoke_without_command=True, description='units/area-sqyard-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / (1/1550.003))

    @sqyard.command(invoke_without_command=True, description='units/area-sqyard-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 10000)

    @sqyard.command(invoke_without_command=True, description='units/area-sqyard-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 4046.856)

    @area.group(invoke_without_command=True, description='units/area-sqft-desc')
    async def sqft(ctx):
        pass


    @sqft.command(invoke_without_command=True, description='units/area-sqft-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 1e6)

    @sqft.command(invoke_without_command=True, description='units/area-sqft-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 1)

    @sqft.command(invoke_without_command=True, description='units/area-sqft-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 2.59e6)

    @sqft.command(invoke_without_command=True, description='units/area-sqft-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / (1/1.196))

    @sqft.command(invoke_without_command=True, description='units/area-sqft-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / (1/1550.003))

    @sqft.command(invoke_without_command=True, description='units/area-sqft-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 10000)

    @sqft.command(invoke_without_command=True, description='units/area-sqft-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 4046.856)

    @area.group(invoke_without_command=True, description='units/area-sqin-desc')
    async def sqin(ctx):
        pass


    @sqin.command(invoke_without_command=True, description='units/area-sqin-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 1e6)

    @sqin.command(invoke_without_command=True, description='units/area-sqin-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 1)

    @sqin.command(invoke_without_command=True, description='units/area-sqin-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 2.59e6)

    @sqin.command(invoke_without_command=True, description='units/area-sqin-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / (1/1.196))

    @sqin.command(invoke_without_command=True, description='units/area-sqin-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / (1/10.764))

    @sqin.command(invoke_without_command=True, description='units/area-sqin-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 10000)

    @sqin.command(invoke_without_command=True, description='units/area-sqin-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 4046.856)

    @area.group(invoke_without_command=True, description='units/area-hectare-desc')
    async def hectare(ctx):
        pass


    @hectare.command(invoke_without_command=True, description='units/area-hectare-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * 10000 / 1e6)

    @hectare.command(invoke_without_command=True, description='units/area-hectare-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * 10000 / 1)

    @hectare.command(invoke_without_command=True, description='units/area-hectare-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * 10000 / 2.59e6)

    @hectare.command(invoke_without_command=True, description='units/area-hectare-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 10000 / (1/1.196))

    @hectare.command(invoke_without_command=True, description='units/area-hectare-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 10000 / (1/10.764))

    @hectare.command(invoke_without_command=True, description='units/area-hectare-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 10000 / (1/1550.003))

    @hectare.command(invoke_without_command=True, description='units/area-hectare-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * 10000 / 4046.856)

    @area.group(invoke_without_command=True, description='units/area-acre-desc')
    async def acre(ctx):
        pass


    @acre.command(invoke_without_command=True, description='units/area-acre-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * 4046.856 / 1e6)

    @acre.command(invoke_without_command=True, description='units/area-acre-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * 4046.856 / 1)

    @acre.command(invoke_without_command=True, description='units/area-acre-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * 4046.856 / 2.59e6)

    @acre.command(invoke_without_command=True, description='units/area-acre-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 4046.856 / (1/1.196))

    @acre.command(invoke_without_command=True, description='units/area-acre-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 4046.856 / (1/10.764))

    @acre.command(invoke_without_command=True, description='units/area-acre-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 4046.856 / (1/1550.003))

    @acre.command(invoke_without_command=True, description='units/area-acre-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * 4046.856 / 10000)


    @group(aliases=[], invoke_without_command=True, description='units/data-desc')
    async def data(self, ctx):
        pass


    @data.group(invoke_without_command=True, description='units/data-bps-desc')
    async def bps(ctx):
        pass


    @bps.command(invoke_without_command=True, description='units/data-bps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @bps.command(invoke_without_command=True, description='units/data-bps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1 / 8e3)

    @bps.command(invoke_without_command=True, description='units/data-bps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1 / 1024)

    @bps.command(invoke_without_command=True, description='units/data-bps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @bps.command(invoke_without_command=True, description='units/data-bps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1 / 8e6)

    @bps.command(invoke_without_command=True, description='units/data-bps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**2))

    @bps.command(invoke_without_command=True, description='units/data-bps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1 / 1e9)

    @bps.command(invoke_without_command=True, description='units/data-bps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1 / 8e9)

    @bps.command(invoke_without_command=True, description='units/data-bps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**3))

    @bps.command(invoke_without_command=True, description='units/data-bps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1 / 1e12)

    @bps.command(invoke_without_command=True, description='units/data-bps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1 / 8e12)

    @bps.command(invoke_without_command=True, description='units/data-bps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-kbps-desc')
    async def kbps(ctx):
        pass


    @kbps.command(invoke_without_command=True, description='units/data-kbps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @kbps.command(invoke_without_command=True, description='units/data-kbps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e3)

    @kbps.command(invoke_without_command=True, description='units/data-kbps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1024)

    @kbps.command(invoke_without_command=True, description='units/data-kbps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e6)

    @kbps.command(invoke_without_command=True, description='units/data-kbps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e6)

    @kbps.command(invoke_without_command=True, description='units/data-kbps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**2))

    @kbps.command(invoke_without_command=True, description='units/data-kbps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e9)

    @kbps.command(invoke_without_command=True, description='units/data-kbps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e9)

    @kbps.command(invoke_without_command=True, description='units/data-kbps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**3))

    @kbps.command(invoke_without_command=True, description='units/data-kbps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e12)

    @kbps.command(invoke_without_command=True, description='units/data-kbps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e12)

    @kbps.command(invoke_without_command=True, description='units/data-kbps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-KBps-desc')
    async def KBps(ctx):
        pass


    @KBps.command(invoke_without_command=True, description='units/data-KBps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1)

    @KBps.command(invoke_without_command=True, description='units/data-KBps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e3)

    @KBps.command(invoke_without_command=True, description='units/data-KBps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1024)

    @KBps.command(invoke_without_command=True, description='units/data-KBps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e6)

    @KBps.command(invoke_without_command=True, description='units/data-KBps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e6)

    @KBps.command(invoke_without_command=True, description='units/data-KBps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**2))

    @KBps.command(invoke_without_command=True, description='units/data-KBps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e9)

    @KBps.command(invoke_without_command=True, description='units/data-KBps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e9)

    @KBps.command(invoke_without_command=True, description='units/data-KBps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**3))

    @KBps.command(invoke_without_command=True, description='units/data-KBps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e12)

    @KBps.command(invoke_without_command=True, description='units/data-KBps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e12)

    @KBps.command(invoke_without_command=True, description='units/data-KBps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-kibps-desc')
    async def kibps(ctx):
        pass


    @kibps.command(invoke_without_command=True, description='units/data-kibps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1)

    @kibps.command(invoke_without_command=True, description='units/data-kibps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e3)

    @kibps.command(invoke_without_command=True, description='units/data-kibps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e3)

    @kibps.command(invoke_without_command=True, description='units/data-kibps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e6)

    @kibps.command(invoke_without_command=True, description='units/data-kibps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e6)

    @kibps.command(invoke_without_command=True, description='units/data-kibps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**2))

    @kibps.command(invoke_without_command=True, description='units/data-kibps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e9)

    @kibps.command(invoke_without_command=True, description='units/data-kibps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e9)

    @kibps.command(invoke_without_command=True, description='units/data-kibps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**3))

    @kibps.command(invoke_without_command=True, description='units/data-kibps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e12)

    @kibps.command(invoke_without_command=True, description='units/data-kibps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e12)

    @kibps.command(invoke_without_command=True, description='units/data-kibps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-mbps-desc')
    async def mbps(ctx):
        pass


    @mbps.command(invoke_without_command=True, description='units/data-mbps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @mbps.command(invoke_without_command=True, description='units/data-mbps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e3)

    @mbps.command(invoke_without_command=True, description='units/data-mbps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e3)

    @mbps.command(invoke_without_command=True, description='units/data-mbps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1024)

    @mbps.command(invoke_without_command=True, description='units/data-mbps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e6)

    @mbps.command(invoke_without_command=True, description='units/data-mbps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**2))

    @mbps.command(invoke_without_command=True, description='units/data-mbps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e9)

    @mbps.command(invoke_without_command=True, description='units/data-mbps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e9)

    @mbps.command(invoke_without_command=True, description='units/data-mbps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**3))

    @mbps.command(invoke_without_command=True, description='units/data-mbps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e12)

    @mbps.command(invoke_without_command=True, description='units/data-mbps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e12)

    @mbps.command(invoke_without_command=True, description='units/data-mbps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-MBps-desc')
    async def MBps(ctx):
        pass


    @MBps.command(invoke_without_command=True, description='units/data-MBps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1)

    @MBps.command(invoke_without_command=True, description='units/data-MBps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e3)

    @MBps.command(invoke_without_command=True, description='units/data-MBps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e3)

    @MBps.command(invoke_without_command=True, description='units/data-MBps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1024)

    @MBps.command(invoke_without_command=True, description='units/data-MBps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e6)

    @MBps.command(invoke_without_command=True, description='units/data-MBps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**2))

    @MBps.command(invoke_without_command=True, description='units/data-MBps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e9)

    @MBps.command(invoke_without_command=True, description='units/data-MBps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e9)

    @MBps.command(invoke_without_command=True, description='units/data-MBps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**3))

    @MBps.command(invoke_without_command=True, description='units/data-MBps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e12)

    @MBps.command(invoke_without_command=True, description='units/data-MBps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e12)

    @MBps.command(invoke_without_command=True, description='units/data-MBps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-mibps-desc')
    async def mibps(ctx):
        pass


    @mibps.command(invoke_without_command=True, description='units/data-mibps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e3)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e3)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1024)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e6)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e6)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e9)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e9)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**3))

    @mibps.command(invoke_without_command=True, description='units/data-mibps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e12)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e12)

    @mibps.command(invoke_without_command=True, description='units/data-mibps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-gbps-desc')
    async def gbps(ctx):
        pass


    @gbps.command(invoke_without_command=True, description='units/data-gbps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1)

    @gbps.command(invoke_without_command=True, description='units/data-gbps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e3)

    @gbps.command(invoke_without_command=True, description='units/data-gbps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e3)

    @gbps.command(invoke_without_command=True, description='units/data-gbps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1024)

    @gbps.command(invoke_without_command=True, description='units/data-gbps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e6)

    @gbps.command(invoke_without_command=True, description='units/data-gbps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e6)

    @gbps.command(invoke_without_command=True, description='units/data-gbps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**2))

    @gbps.command(invoke_without_command=True, description='units/data-gbps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e9)

    @gbps.command(invoke_without_command=True, description='units/data-gbps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**3))

    @gbps.command(invoke_without_command=True, description='units/data-gbps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e12)

    @gbps.command(invoke_without_command=True, description='units/data-gbps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e12)

    @gbps.command(invoke_without_command=True, description='units/data-gbps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-GBps-desc')
    async def GBps(ctx):
        pass


    @GBps.command(invoke_without_command=True, description='units/data-GBps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1)

    @GBps.command(invoke_without_command=True, description='units/data-GBps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e3)

    @GBps.command(invoke_without_command=True, description='units/data-GBps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e3)

    @GBps.command(invoke_without_command=True, description='units/data-GBps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1024)

    @GBps.command(invoke_without_command=True, description='units/data-GBps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e6)

    @GBps.command(invoke_without_command=True, description='units/data-GBps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e6)

    @GBps.command(invoke_without_command=True, description='units/data-GBps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**2))

    @GBps.command(invoke_without_command=True, description='units/data-GBps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e9)

    @GBps.command(invoke_without_command=True, description='units/data-GBps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**3))

    @GBps.command(invoke_without_command=True, description='units/data-GBps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e12)

    @GBps.command(invoke_without_command=True, description='units/data-GBps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e12)

    @GBps.command(invoke_without_command=True, description='units/data-GBps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-gibps-desc')
    async def gibps(ctx):
        pass


    @gibps.command(invoke_without_command=True, description='units/data-gibps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e3)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e3)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1024)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e6)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e6)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**2))

    @gibps.command(invoke_without_command=True, description='units/data-gibps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e9)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e9)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e12)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e12)

    @gibps.command(invoke_without_command=True, description='units/data-gibps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-tbps-desc')
    async def tbps(ctx):
        pass


    @tbps.command(invoke_without_command=True, description='units/data-tbps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1)

    @tbps.command(invoke_without_command=True, description='units/data-tbps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e3)

    @tbps.command(invoke_without_command=True, description='units/data-tbps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e3)

    @tbps.command(invoke_without_command=True, description='units/data-tbps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1024)

    @tbps.command(invoke_without_command=True, description='units/data-tbps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e6)

    @tbps.command(invoke_without_command=True, description='units/data-tbps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e6)

    @tbps.command(invoke_without_command=True, description='units/data-tbps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**2))

    @tbps.command(invoke_without_command=True, description='units/data-tbps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e9)

    @tbps.command(invoke_without_command=True, description='units/data-tbps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e9)

    @tbps.command(invoke_without_command=True, description='units/data-tbps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**3))

    @tbps.command(invoke_without_command=True, description='units/data-tbps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e12)

    @tbps.command(invoke_without_command=True, description='units/data-tbps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-TBps-desc')
    async def TBps(ctx):
        pass


    @TBps.command(invoke_without_command=True, description='units/data-TBps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1)

    @TBps.command(invoke_without_command=True, description='units/data-TBps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e3)

    @TBps.command(invoke_without_command=True, description='units/data-TBps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e3)

    @TBps.command(invoke_without_command=True, description='units/data-TBps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1024)

    @TBps.command(invoke_without_command=True, description='units/data-TBps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e6)

    @TBps.command(invoke_without_command=True, description='units/data-TBps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e6)

    @TBps.command(invoke_without_command=True, description='units/data-TBps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**2))

    @TBps.command(invoke_without_command=True, description='units/data-TBps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e9)

    @TBps.command(invoke_without_command=True, description='units/data-TBps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e9)

    @TBps.command(invoke_without_command=True, description='units/data-TBps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**3))

    @TBps.command(invoke_without_command=True, description='units/data-TBps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e12)

    @TBps.command(invoke_without_command=True, description='units/data-TBps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**4))

    @data.group(invoke_without_command=True, description='units/data-tibps-desc')
    async def tibps(ctx):
        pass


    @tibps.command(invoke_without_command=True, description='units/data-tibps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1)

    @tibps.command(invoke_without_command=True, description='units/data-tibps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e3)

    @tibps.command(invoke_without_command=True, description='units/data-tibps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e3)

    @tibps.command(invoke_without_command=True, description='units/data-tibps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1024)

    @tibps.command(invoke_without_command=True, description='units/data-tibps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e6)

    @tibps.command(invoke_without_command=True, description='units/data-tibps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e6)

    @tibps.command(invoke_without_command=True, description='units/data-tibps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**2))

    @tibps.command(invoke_without_command=True, description='units/data-tibps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e9)

    @tibps.command(invoke_without_command=True, description='units/data-tibps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e9)

    @tibps.command(invoke_without_command=True, description='units/data-tibps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**3))

    @tibps.command(invoke_without_command=True, description='units/data-tibps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e12)

    @tibps.command(invoke_without_command=True, description='units/data-tibps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e12)


    @group(aliases=[], invoke_without_command=True, description='units/storage-desc')
    async def storage(self, ctx):
        pass


    @storage.group(invoke_without_command=True, description='units/storage-b-desc')
    async def b(ctx):
        pass


    @b.command(invoke_without_command=True, description='units/storage-b-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @b.command(invoke_without_command=True, description='units/storage-b-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1 / 1024)

    @b.command(invoke_without_command=True, description='units/storage-b-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @b.command(invoke_without_command=True, description='units/storage-b-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**2))

    @b.command(invoke_without_command=True, description='units/storage-b-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e9)

    @b.command(invoke_without_command=True, description='units/storage-b-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**3))

    @b.command(invoke_without_command=True, description='units/storage-b-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e12)

    @b.command(invoke_without_command=True, description='units/storage-b-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**4))

    @b.command(invoke_without_command=True, description='units/storage-b-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e15)

    @b.command(invoke_without_command=True, description='units/storage-b-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**5))

    @b.command(invoke_without_command=True, description='units/storage-b-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1 / 8)

    @b.command(invoke_without_command=True, description='units/storage-b-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e3)

    @b.command(invoke_without_command=True, description='units/storage-b-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024))

    @b.command(invoke_without_command=True, description='units/storage-b-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e6)

    @b.command(invoke_without_command=True, description='units/storage-b-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024 ** 2))

    @b.command(invoke_without_command=True, description='units/storage-b-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e9)

    @b.command(invoke_without_command=True, description='units/storage-b-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024 ** 3))

    @b.command(invoke_without_command=True, description='units/storage-b-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e12)

    @b.command(invoke_without_command=True, description='units/storage-b-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024 ** 4))

    @b.command(invoke_without_command=True, description='units/storage-b-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e15)

    @b.command(invoke_without_command=True, description='units/storage-b-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-kb-desc')
    async def kb(ctx):
        pass


    @kb.command(invoke_without_command=True, description='units/storage-kb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @kb.command(invoke_without_command=True, description='units/storage-kb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1024)

    @kb.command(invoke_without_command=True, description='units/storage-kb-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e6)

    @kb.command(invoke_without_command=True, description='units/storage-kb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**2))

    @kb.command(invoke_without_command=True, description='units/storage-kb-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e9)

    @kb.command(invoke_without_command=True, description='units/storage-kb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**3))

    @kb.command(invoke_without_command=True, description='units/storage-kb-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e12)

    @kb.command(invoke_without_command=True, description='units/storage-kb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**4))

    @kb.command(invoke_without_command=True, description='units/storage-kb-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e15)

    @kb.command(invoke_without_command=True, description='units/storage-kb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**5))

    @kb.command(invoke_without_command=True, description='units/storage-kb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8)

    @kb.command(invoke_without_command=True, description='units/storage-kb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e3)

    @kb.command(invoke_without_command=True, description='units/storage-kb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024))

    @kb.command(invoke_without_command=True, description='units/storage-kb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e6)

    @kb.command(invoke_without_command=True, description='units/storage-kb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024 ** 2))

    @kb.command(invoke_without_command=True, description='units/storage-kb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e9)

    @kb.command(invoke_without_command=True, description='units/storage-kb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024 ** 3))

    @kb.command(invoke_without_command=True, description='units/storage-kb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e12)

    @kb.command(invoke_without_command=True, description='units/storage-kb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024 ** 4))

    @kb.command(invoke_without_command=True, description='units/storage-kb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e15)

    @kb.command(invoke_without_command=True, description='units/storage-kb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-kib-desc')
    async def kib(ctx):
        pass


    @kib.command(invoke_without_command=True, description='units/storage-kib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1024 / 1)

    @kib.command(invoke_without_command=True, description='units/storage-kib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e3)

    @kib.command(invoke_without_command=True, description='units/storage-kib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e6)

    @kib.command(invoke_without_command=True, description='units/storage-kib-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**2))

    @kib.command(invoke_without_command=True, description='units/storage-kib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e9)

    @kib.command(invoke_without_command=True, description='units/storage-kib-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**3))

    @kib.command(invoke_without_command=True, description='units/storage-kib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e12)

    @kib.command(invoke_without_command=True, description='units/storage-kib-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**4))

    @kib.command(invoke_without_command=True, description='units/storage-kib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e15)

    @kib.command(invoke_without_command=True, description='units/storage-kib-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**5))

    @kib.command(invoke_without_command=True, description='units/storage-kib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1024 / 8)

    @kib.command(invoke_without_command=True, description='units/storage-kib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e3)

    @kib.command(invoke_without_command=True, description='units/storage-kib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024))

    @kib.command(invoke_without_command=True, description='units/storage-kib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e6)

    @kib.command(invoke_without_command=True, description='units/storage-kib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024 ** 2))

    @kib.command(invoke_without_command=True, description='units/storage-kib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e9)

    @kib.command(invoke_without_command=True, description='units/storage-kib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024 ** 3))

    @kib.command(invoke_without_command=True, description='units/storage-kib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e12)

    @kib.command(invoke_without_command=True, description='units/storage-kib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024 ** 4))

    @kib.command(invoke_without_command=True, description='units/storage-kib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e15)

    @kib.command(invoke_without_command=True, description='units/storage-kib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-mb-desc')
    async def mb(ctx):
        pass


    @mb.command(invoke_without_command=True, description='units/storage-mb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @mb.command(invoke_without_command=True, description='units/storage-mb-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e3)

    @mb.command(invoke_without_command=True, description='units/storage-mb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1024)

    @mb.command(invoke_without_command=True, description='units/storage-mb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**2))

    @mb.command(invoke_without_command=True, description='units/storage-mb-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e9)

    @mb.command(invoke_without_command=True, description='units/storage-mb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**3))

    @mb.command(invoke_without_command=True, description='units/storage-mb-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e12)

    @mb.command(invoke_without_command=True, description='units/storage-mb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**4))

    @mb.command(invoke_without_command=True, description='units/storage-mb-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e15)

    @mb.command(invoke_without_command=True, description='units/storage-mb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**5))

    @mb.command(invoke_without_command=True, description='units/storage-mb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8)

    @mb.command(invoke_without_command=True, description='units/storage-mb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e3)

    @mb.command(invoke_without_command=True, description='units/storage-mb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024))

    @mb.command(invoke_without_command=True, description='units/storage-mb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e6)

    @mb.command(invoke_without_command=True, description='units/storage-mb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024 ** 2))

    @mb.command(invoke_without_command=True, description='units/storage-mb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e9)

    @mb.command(invoke_without_command=True, description='units/storage-mb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024 ** 3))

    @mb.command(invoke_without_command=True, description='units/storage-mb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e12)

    @mb.command(invoke_without_command=True, description='units/storage-mb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024 ** 4))

    @mb.command(invoke_without_command=True, description='units/storage-mb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e15)

    @mb.command(invoke_without_command=True, description='units/storage-mb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-mib-desc')
    async def mib(ctx):
        pass


    @mib.command(invoke_without_command=True, description='units/storage-mib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1)

    @mib.command(invoke_without_command=True, description='units/storage-mib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e3)

    @mib.command(invoke_without_command=True, description='units/storage-mib-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1024)

    @mib.command(invoke_without_command=True, description='units/storage-mib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e6)

    @mib.command(invoke_without_command=True, description='units/storage-mib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e9)

    @mib.command(invoke_without_command=True, description='units/storage-mib-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**3))

    @mib.command(invoke_without_command=True, description='units/storage-mib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e12)

    @mib.command(invoke_without_command=True, description='units/storage-mib-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**4))

    @mib.command(invoke_without_command=True, description='units/storage-mib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e15)

    @mib.command(invoke_without_command=True, description='units/storage-mib-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**5))

    @mib.command(invoke_without_command=True, description='units/storage-mib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8)

    @mib.command(invoke_without_command=True, description='units/storage-mib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e3)

    @mib.command(invoke_without_command=True, description='units/storage-mib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024))

    @mib.command(invoke_without_command=True, description='units/storage-mib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e6)

    @mib.command(invoke_without_command=True, description='units/storage-mib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024 ** 2))

    @mib.command(invoke_without_command=True, description='units/storage-mib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e9)

    @mib.command(invoke_without_command=True, description='units/storage-mib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024 ** 3))

    @mib.command(invoke_without_command=True, description='units/storage-mib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e12)

    @mib.command(invoke_without_command=True, description='units/storage-mib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024 ** 4))

    @mib.command(invoke_without_command=True, description='units/storage-mib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e15)

    @mib.command(invoke_without_command=True, description='units/storage-mib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-gb-desc')
    async def gb(ctx):
        pass


    @gb.command(invoke_without_command=True, description='units/storage-gb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1)

    @gb.command(invoke_without_command=True, description='units/storage-gb-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e3)

    @gb.command(invoke_without_command=True, description='units/storage-gb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1024)

    @gb.command(invoke_without_command=True, description='units/storage-gb-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e6)

    @gb.command(invoke_without_command=True, description='units/storage-gb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**2))

    @gb.command(invoke_without_command=True, description='units/storage-gb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**3))

    @gb.command(invoke_without_command=True, description='units/storage-gb-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e12)

    @gb.command(invoke_without_command=True, description='units/storage-gb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**4))

    @gb.command(invoke_without_command=True, description='units/storage-gb-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e15)

    @gb.command(invoke_without_command=True, description='units/storage-gb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**5))

    @gb.command(invoke_without_command=True, description='units/storage-gb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8)

    @gb.command(invoke_without_command=True, description='units/storage-gb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e3)

    @gb.command(invoke_without_command=True, description='units/storage-gb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024))

    @gb.command(invoke_without_command=True, description='units/storage-gb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e6)

    @gb.command(invoke_without_command=True, description='units/storage-gb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024 ** 2))

    @gb.command(invoke_without_command=True, description='units/storage-gb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e9)

    @gb.command(invoke_without_command=True, description='units/storage-gb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024 ** 3))

    @gb.command(invoke_without_command=True, description='units/storage-gb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e12)

    @gb.command(invoke_without_command=True, description='units/storage-gb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024 ** 4))

    @gb.command(invoke_without_command=True, description='units/storage-gb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e15)

    @gb.command(invoke_without_command=True, description='units/storage-gb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-gib-desc')
    async def gib(ctx):
        pass


    @gib.command(invoke_without_command=True, description='units/storage-gib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1)

    @gib.command(invoke_without_command=True, description='units/storage-gib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e3)

    @gib.command(invoke_without_command=True, description='units/storage-gib-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1024)

    @gib.command(invoke_without_command=True, description='units/storage-gib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e6)

    @gib.command(invoke_without_command=True, description='units/storage-gib-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**2))

    @gib.command(invoke_without_command=True, description='units/storage-gib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e9)

    @gib.command(invoke_without_command=True, description='units/storage-gib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e12)

    @gib.command(invoke_without_command=True, description='units/storage-gib-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**4))

    @gib.command(invoke_without_command=True, description='units/storage-gib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e15)

    @gib.command(invoke_without_command=True, description='units/storage-gib-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**5))

    @gib.command(invoke_without_command=True, description='units/storage-gib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8)

    @gib.command(invoke_without_command=True, description='units/storage-gib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e3)

    @gib.command(invoke_without_command=True, description='units/storage-gib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024))

    @gib.command(invoke_without_command=True, description='units/storage-gib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e6)

    @gib.command(invoke_without_command=True, description='units/storage-gib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024 ** 2))

    @gib.command(invoke_without_command=True, description='units/storage-gib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e9)

    @gib.command(invoke_without_command=True, description='units/storage-gib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024 ** 3))

    @gib.command(invoke_without_command=True, description='units/storage-gib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e12)

    @gib.command(invoke_without_command=True, description='units/storage-gib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024 ** 4))

    @gib.command(invoke_without_command=True, description='units/storage-gib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e15)

    @gib.command(invoke_without_command=True, description='units/storage-gib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-tb-desc')
    async def tb(ctx):
        pass


    @tb.command(invoke_without_command=True, description='units/storage-tb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1)

    @tb.command(invoke_without_command=True, description='units/storage-tb-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e3)

    @tb.command(invoke_without_command=True, description='units/storage-tb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1024)

    @tb.command(invoke_without_command=True, description='units/storage-tb-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e6)

    @tb.command(invoke_without_command=True, description='units/storage-tb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**2))

    @tb.command(invoke_without_command=True, description='units/storage-tb-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e9)

    @tb.command(invoke_without_command=True, description='units/storage-tb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**3))

    @tb.command(invoke_without_command=True, description='units/storage-tb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**4))

    @tb.command(invoke_without_command=True, description='units/storage-tb-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e15)

    @tb.command(invoke_without_command=True, description='units/storage-tb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**5))

    @tb.command(invoke_without_command=True, description='units/storage-tb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8)

    @tb.command(invoke_without_command=True, description='units/storage-tb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e3)

    @tb.command(invoke_without_command=True, description='units/storage-tb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024))

    @tb.command(invoke_without_command=True, description='units/storage-tb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e6)

    @tb.command(invoke_without_command=True, description='units/storage-tb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024 ** 2))

    @tb.command(invoke_without_command=True, description='units/storage-tb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e9)

    @tb.command(invoke_without_command=True, description='units/storage-tb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024 ** 3))

    @tb.command(invoke_without_command=True, description='units/storage-tb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e12)

    @tb.command(invoke_without_command=True, description='units/storage-tb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024 ** 4))

    @tb.command(invoke_without_command=True, description='units/storage-tb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e15)

    @tb.command(invoke_without_command=True, description='units/storage-tb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-tib-desc')
    async def tib(ctx):
        pass


    @tib.command(invoke_without_command=True, description='units/storage-tib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1)

    @tib.command(invoke_without_command=True, description='units/storage-tib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e3)

    @tib.command(invoke_without_command=True, description='units/storage-tib-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1024)

    @tib.command(invoke_without_command=True, description='units/storage-tib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e6)

    @tib.command(invoke_without_command=True, description='units/storage-tib-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**2))

    @tib.command(invoke_without_command=True, description='units/storage-tib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e9)

    @tib.command(invoke_without_command=True, description='units/storage-tib-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**3))

    @tib.command(invoke_without_command=True, description='units/storage-tib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e12)

    @tib.command(invoke_without_command=True, description='units/storage-tib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e15)

    @tib.command(invoke_without_command=True, description='units/storage-tib-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**5))

    @tib.command(invoke_without_command=True, description='units/storage-tib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8)

    @tib.command(invoke_without_command=True, description='units/storage-tib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e3)

    @tib.command(invoke_without_command=True, description='units/storage-tib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024))

    @tib.command(invoke_without_command=True, description='units/storage-tib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e6)

    @tib.command(invoke_without_command=True, description='units/storage-tib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024 ** 2))

    @tib.command(invoke_without_command=True, description='units/storage-tib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e9)

    @tib.command(invoke_without_command=True, description='units/storage-tib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024 ** 3))

    @tib.command(invoke_without_command=True, description='units/storage-tib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e12)

    @tib.command(invoke_without_command=True, description='units/storage-tib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024 ** 4))

    @tib.command(invoke_without_command=True, description='units/storage-tib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e15)

    @tib.command(invoke_without_command=True, description='units/storage-tib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-pb-desc')
    async def pb(ctx):
        pass


    @pb.command(invoke_without_command=True, description='units/storage-pb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1)

    @pb.command(invoke_without_command=True, description='units/storage-pb-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1e3)

    @pb.command(invoke_without_command=True, description='units/storage-pb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1024)

    @pb.command(invoke_without_command=True, description='units/storage-pb-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1e6)

    @pb.command(invoke_without_command=True, description='units/storage-pb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e15 / (1024**2))

    @pb.command(invoke_without_command=True, description='units/storage-pb-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1e9)

    @pb.command(invoke_without_command=True, description='units/storage-pb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e15 / (1024**3))

    @pb.command(invoke_without_command=True, description='units/storage-pb-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1e12)

    @pb.command(invoke_without_command=True, description='units/storage-pb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e15 / (1024**4))

    @pb.command(invoke_without_command=True, description='units/storage-pb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e15 / (1024**5))

    @pb.command(invoke_without_command=True, description='units/storage-pb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8)

    @pb.command(invoke_without_command=True, description='units/storage-pb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e3)

    @pb.command(invoke_without_command=True, description='units/storage-pb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024))

    @pb.command(invoke_without_command=True, description='units/storage-pb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e6)

    @pb.command(invoke_without_command=True, description='units/storage-pb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024 ** 2))

    @pb.command(invoke_without_command=True, description='units/storage-pb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e9)

    @pb.command(invoke_without_command=True, description='units/storage-pb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024 ** 3))

    @pb.command(invoke_without_command=True, description='units/storage-pb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e12)

    @pb.command(invoke_without_command=True, description='units/storage-pb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024 ** 4))

    @pb.command(invoke_without_command=True, description='units/storage-pb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e15)

    @pb.command(invoke_without_command=True, description='units/storage-pb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-pib-desc')
    async def pib(ctx):
        pass


    @pib.command(invoke_without_command=True, description='units/storage-pib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1)

    @pib.command(invoke_without_command=True, description='units/storage-pib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e3)

    @pib.command(invoke_without_command=True, description='units/storage-pib-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1024)

    @pib.command(invoke_without_command=True, description='units/storage-pib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e6)

    @pib.command(invoke_without_command=True, description='units/storage-pib-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (1024**2))

    @pib.command(invoke_without_command=True, description='units/storage-pib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e9)

    @pib.command(invoke_without_command=True, description='units/storage-pib-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (1024**3))

    @pib.command(invoke_without_command=True, description='units/storage-pib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e12)

    @pib.command(invoke_without_command=True, description='units/storage-pib-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (1024**4))

    @pib.command(invoke_without_command=True, description='units/storage-pib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e15)

    @pib.command(invoke_without_command=True, description='units/storage-pib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8)

    @pib.command(invoke_without_command=True, description='units/storage-pib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e3)

    @pib.command(invoke_without_command=True, description='units/storage-pib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024))

    @pib.command(invoke_without_command=True, description='units/storage-pib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e6)

    @pib.command(invoke_without_command=True, description='units/storage-pib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024 ** 2))

    @pib.command(invoke_without_command=True, description='units/storage-pib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e9)

    @pib.command(invoke_without_command=True, description='units/storage-pib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024 ** 3))

    @pib.command(invoke_without_command=True, description='units/storage-pib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e12)

    @pib.command(invoke_without_command=True, description='units/storage-pib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024 ** 4))

    @pib.command(invoke_without_command=True, description='units/storage-pib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e15)

    @pib.command(invoke_without_command=True, description='units/storage-pib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-B-desc')
    async def B(ctx):
        pass


    @B.command(invoke_without_command=True, description='units/storage-B-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8 / 1)

    @B.command(invoke_without_command=True, description='units/storage-B-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e3)

    @B.command(invoke_without_command=True, description='units/storage-B-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8 / 1024)

    @B.command(invoke_without_command=True, description='units/storage-B-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e6)

    @B.command(invoke_without_command=True, description='units/storage-B-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8 / (1024**2))

    @B.command(invoke_without_command=True, description='units/storage-B-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e9)

    @B.command(invoke_without_command=True, description='units/storage-B-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8 / (1024**3))

    @B.command(invoke_without_command=True, description='units/storage-B-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e12)

    @B.command(invoke_without_command=True, description='units/storage-B-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8 / (1024**4))

    @B.command(invoke_without_command=True, description='units/storage-B-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e15)

    @B.command(invoke_without_command=True, description='units/storage-B-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8 / (1024**5))

    @B.command(invoke_without_command=True, description='units/storage-B-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e3)

    @B.command(invoke_without_command=True, description='units/storage-B-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024))

    @B.command(invoke_without_command=True, description='units/storage-B-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e6)

    @B.command(invoke_without_command=True, description='units/storage-B-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024 ** 2))

    @B.command(invoke_without_command=True, description='units/storage-B-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e9)

    @B.command(invoke_without_command=True, description='units/storage-B-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024 ** 3))

    @B.command(invoke_without_command=True, description='units/storage-B-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e12)

    @B.command(invoke_without_command=True, description='units/storage-B-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024 ** 4))

    @B.command(invoke_without_command=True, description='units/storage-B-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e15)

    @B.command(invoke_without_command=True, description='units/storage-B-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-KB-desc')
    async def KB(ctx):
        pass


    @KB.command(invoke_without_command=True, description='units/storage-KB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1)

    @KB.command(invoke_without_command=True, description='units/storage-KB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e3)

    @KB.command(invoke_without_command=True, description='units/storage-KB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1024)

    @KB.command(invoke_without_command=True, description='units/storage-KB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e6)

    @KB.command(invoke_without_command=True, description='units/storage-KB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**2))

    @KB.command(invoke_without_command=True, description='units/storage-KB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e9)

    @KB.command(invoke_without_command=True, description='units/storage-KB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**3))

    @KB.command(invoke_without_command=True, description='units/storage-KB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e12)

    @KB.command(invoke_without_command=True, description='units/storage-KB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**4))

    @KB.command(invoke_without_command=True, description='units/storage-KB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e15)

    @KB.command(invoke_without_command=True, description='units/storage-KB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**5))

    @KB.command(invoke_without_command=True, description='units/storage-KB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8)

    @KB.command(invoke_without_command=True, description='units/storage-KB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024))

    @KB.command(invoke_without_command=True, description='units/storage-KB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e6)

    @KB.command(invoke_without_command=True, description='units/storage-KB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024 ** 2))

    @KB.command(invoke_without_command=True, description='units/storage-KB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e9)

    @KB.command(invoke_without_command=True, description='units/storage-KB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024 ** 3))

    @KB.command(invoke_without_command=True, description='units/storage-KB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e12)

    @KB.command(invoke_without_command=True, description='units/storage-KB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024 ** 4))

    @KB.command(invoke_without_command=True, description='units/storage-KB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e15)

    @KB.command(invoke_without_command=True, description='units/storage-KB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-KiB-desc')
    async def KiB(ctx):
        pass


    @KiB.command(invoke_without_command=True, description='units/storage-KiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e3)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1024)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e6)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (1024**2))

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e9)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (1024**3))

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e12)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (1024**4))

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e15)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (1024**5))

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e3)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e6)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 2))

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e9)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 3))

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e12)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 4))

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e15)

    @KiB.command(invoke_without_command=True, description='units/storage-KiB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-MB-desc')
    async def MB(ctx):
        pass


    @MB.command(invoke_without_command=True, description='units/storage-MB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1)

    @MB.command(invoke_without_command=True, description='units/storage-MB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e3)

    @MB.command(invoke_without_command=True, description='units/storage-MB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1024)

    @MB.command(invoke_without_command=True, description='units/storage-MB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e6)

    @MB.command(invoke_without_command=True, description='units/storage-MB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**2))

    @MB.command(invoke_without_command=True, description='units/storage-MB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e9)

    @MB.command(invoke_without_command=True, description='units/storage-MB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**3))

    @MB.command(invoke_without_command=True, description='units/storage-MB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e12)

    @MB.command(invoke_without_command=True, description='units/storage-MB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**4))

    @MB.command(invoke_without_command=True, description='units/storage-MB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e15)

    @MB.command(invoke_without_command=True, description='units/storage-MB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**5))

    @MB.command(invoke_without_command=True, description='units/storage-MB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8)

    @MB.command(invoke_without_command=True, description='units/storage-MB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e3)

    @MB.command(invoke_without_command=True, description='units/storage-MB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024))

    @MB.command(invoke_without_command=True, description='units/storage-MB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024 ** 2))

    @MB.command(invoke_without_command=True, description='units/storage-MB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e9)

    @MB.command(invoke_without_command=True, description='units/storage-MB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024 ** 3))

    @MB.command(invoke_without_command=True, description='units/storage-MB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e12)

    @MB.command(invoke_without_command=True, description='units/storage-MB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024 ** 4))

    @MB.command(invoke_without_command=True, description='units/storage-MB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e15)

    @MB.command(invoke_without_command=True, description='units/storage-MB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-MiB-desc')
    async def MiB(ctx):
        pass


    @MiB.command(invoke_without_command=True, description='units/storage-MiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e3)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1024)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e6)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (1024**2))

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e9)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (1024**3))

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e12)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (1024**4))

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e15)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (1024**5))

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e3)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024))

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e6)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e9)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024 ** 3))

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e12)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024 ** 4))

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e15)

    @MiB.command(invoke_without_command=True, description='units/storage-MiB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-GB-desc')
    async def GB(ctx):
        pass


    @GB.command(invoke_without_command=True, description='units/storage-GB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1)

    @GB.command(invoke_without_command=True, description='units/storage-GB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e3)

    @GB.command(invoke_without_command=True, description='units/storage-GB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1024)

    @GB.command(invoke_without_command=True, description='units/storage-GB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e6)

    @GB.command(invoke_without_command=True, description='units/storage-GB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**2))

    @GB.command(invoke_without_command=True, description='units/storage-GB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e9)

    @GB.command(invoke_without_command=True, description='units/storage-GB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**3))

    @GB.command(invoke_without_command=True, description='units/storage-GB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e12)

    @GB.command(invoke_without_command=True, description='units/storage-GB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**4))

    @GB.command(invoke_without_command=True, description='units/storage-GB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e15)

    @GB.command(invoke_without_command=True, description='units/storage-GB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**5))

    @GB.command(invoke_without_command=True, description='units/storage-GB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8)

    @GB.command(invoke_without_command=True, description='units/storage-GB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e3)

    @GB.command(invoke_without_command=True, description='units/storage-GB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024))

    @GB.command(invoke_without_command=True, description='units/storage-GB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e6)

    @GB.command(invoke_without_command=True, description='units/storage-GB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024 ** 2))

    @GB.command(invoke_without_command=True, description='units/storage-GB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024 ** 3))

    @GB.command(invoke_without_command=True, description='units/storage-GB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e12)

    @GB.command(invoke_without_command=True, description='units/storage-GB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024 ** 4))

    @GB.command(invoke_without_command=True, description='units/storage-GB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e15)

    @GB.command(invoke_without_command=True, description='units/storage-GB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-GiB-desc')
    async def GiB(ctx):
        pass


    @GiB.command(invoke_without_command=True, description='units/storage-GiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e3)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1024)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e6)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (1024**2))

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e9)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (1024**3))

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e12)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (1024**4))

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e15)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (1024**5))

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e3)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024))

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e6)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024 ** 2))

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e9)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e12)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024 ** 4))

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e15)

    @GiB.command(invoke_without_command=True, description='units/storage-GiB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-TB-desc')
    async def TB(ctx):
        pass


    @TB.command(invoke_without_command=True, description='units/storage-TB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1)

    @TB.command(invoke_without_command=True, description='units/storage-TB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e3)

    @TB.command(invoke_without_command=True, description='units/storage-TB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1024)

    @TB.command(invoke_without_command=True, description='units/storage-TB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e6)

    @TB.command(invoke_without_command=True, description='units/storage-TB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**2))

    @TB.command(invoke_without_command=True, description='units/storage-TB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e9)

    @TB.command(invoke_without_command=True, description='units/storage-TB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**3))

    @TB.command(invoke_without_command=True, description='units/storage-TB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e12)

    @TB.command(invoke_without_command=True, description='units/storage-TB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**4))

    @TB.command(invoke_without_command=True, description='units/storage-TB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e15)

    @TB.command(invoke_without_command=True, description='units/storage-TB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**5))

    @TB.command(invoke_without_command=True, description='units/storage-TB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8)

    @TB.command(invoke_without_command=True, description='units/storage-TB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e3)

    @TB.command(invoke_without_command=True, description='units/storage-TB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024))

    @TB.command(invoke_without_command=True, description='units/storage-TB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e6)

    @TB.command(invoke_without_command=True, description='units/storage-TB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024 ** 2))

    @TB.command(invoke_without_command=True, description='units/storage-TB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e9)

    @TB.command(invoke_without_command=True, description='units/storage-TB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024 ** 3))

    @TB.command(invoke_without_command=True, description='units/storage-TB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024 ** 4))

    @TB.command(invoke_without_command=True, description='units/storage-TB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e15)

    @TB.command(invoke_without_command=True, description='units/storage-TB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-TiB-desc')
    async def TiB(ctx):
        pass


    @TiB.command(invoke_without_command=True, description='units/storage-TiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e3)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1024)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e6)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (1024**2))

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e9)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (1024**3))

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e12)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (1024**4))

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e15)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (1024**5))

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e3)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024))

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e6)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024 ** 2))

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e9)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024 ** 3))

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e12)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e15)

    @TiB.command(invoke_without_command=True, description='units/storage-TiB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-PB-desc')
    async def PB(ctx):
        pass


    @PB.command(invoke_without_command=True, description='units/storage-PB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1)

    @PB.command(invoke_without_command=True, description='units/storage-PB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e3)

    @PB.command(invoke_without_command=True, description='units/storage-PB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1024)

    @PB.command(invoke_without_command=True, description='units/storage-PB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e6)

    @PB.command(invoke_without_command=True, description='units/storage-PB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e15 / (1024**2))

    @PB.command(invoke_without_command=True, description='units/storage-PB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e9)

    @PB.command(invoke_without_command=True, description='units/storage-PB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e15 / (1024**3))

    @PB.command(invoke_without_command=True, description='units/storage-PB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e12)

    @PB.command(invoke_without_command=True, description='units/storage-PB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e15 / (1024**4))

    @PB.command(invoke_without_command=True, description='units/storage-PB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e15)

    @PB.command(invoke_without_command=True, description='units/storage-PB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e15 / (1024**5))

    @PB.command(invoke_without_command=True, description='units/storage-PB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8)

    @PB.command(invoke_without_command=True, description='units/storage-PB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8e3)

    @PB.command(invoke_without_command=True, description='units/storage-PB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024))

    @PB.command(invoke_without_command=True, description='units/storage-PB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8e6)

    @PB.command(invoke_without_command=True, description='units/storage-PB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024 ** 2))

    @PB.command(invoke_without_command=True, description='units/storage-PB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8e9)

    @PB.command(invoke_without_command=True, description='units/storage-PB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024 ** 3))

    @PB.command(invoke_without_command=True, description='units/storage-PB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8e12)

    @PB.command(invoke_without_command=True, description='units/storage-PB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024 ** 4))

    @PB.command(invoke_without_command=True, description='units/storage-PB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024 ** 5))

    @storage.group(invoke_without_command=True, description='units/storage-PiB-desc')
    async def PiB(ctx):
        pass


    @PiB.command(invoke_without_command=True, description='units/storage-PiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e3)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1024)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e6)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (1024**2))

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e9)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (1024**3))

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e12)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (1024**4))

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e15)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (1024**5))

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e3)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024))

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e6)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024 ** 2))

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e9)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024 ** 3))

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e12)

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024 ** 4))

    @PiB.command(invoke_without_command=True, description='units/storage-PiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e15)


    @group(aliases=[], invoke_without_command=True, description='units/energy-desc')
    async def energy(self, ctx):
        pass


    @energy.group(invoke_without_command=True, description='units/energy-joule-desc')
    async def joule(ctx):
        pass


    @joule.command(invoke_without_command=True, description='units/energy-joule-kilojoule-desc')
    async def kilojoule(ctx, amount: float):
        await ctx.send(amount * 1 / 1000)

    @joule.command(invoke_without_command=True, description='units/energy-joule-calorie-desc')
    async def calorie(ctx, amount: float):
        await ctx.send(amount * 1 / 4.184)

    @joule.command(invoke_without_command=True, description='units/energy-joule-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1 / 4184)

    @joule.command(invoke_without_command=True, description='units/energy-joule-watthour-desc')
    async def watthour(ctx, amount: float):
        await ctx.send(amount * 1 / 3600)

    @joule.command(invoke_without_command=True, description='units/energy-joule-kwh-desc')
    async def kwh(ctx, amount: float):
        await ctx.send(amount * 1 / 3.6e6)

    @joule.command(invoke_without_command=True, description='units/energy-joule-ev-desc')
    async def ev(ctx, amount: float):
        await ctx.send(amount * 1 / (1/6.242e18))

    @joule.command(invoke_without_command=True, description='units/energy-joule-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 1 / 1055.06)

    @joule.command(invoke_without_command=True, description='units/energy-joule-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 1 / 1.05506e8)

    @joule.command(invoke_without_command=True, description='units/energy-joule-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 1 / 1.35582)

    @energy.group(invoke_without_command=True, description='units/energy-kilojoule-desc')
    async def kilojoule(ctx):
        pass


    @kilojoule.command(invoke_without_command=True, description='units/energy-kilojoule-joule-desc')
    async def joule(ctx, amount: float):
        await ctx.send(amount * 1000 / 1)

    @kilojoule.command(invoke_without_command=True, description='units/energy-kilojoule-calorie-desc')
    async def calorie(ctx, amount: float):
        await ctx.send(amount * 1000 / 4.184)

    @kilojoule.command(invoke_without_command=True, description='units/energy-kilojoule-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1000 / 4184)

    @kilojoule.command(invoke_without_command=True, description='units/energy-kilojoule-watthour-desc')
    async def watthour(ctx, amount: float):
        await ctx.send(amount * 1000 / 3600)

    @kilojoule.command(invoke_without_command=True, description='units/energy-kilojoule-kwh-desc')
    async def kwh(ctx, amount: float):
        await ctx.send(amount * 1000 / 3.6e6)

    @kilojoule.command(invoke_without_command=True, description='units/energy-kilojoule-ev-desc')
    async def ev(ctx, amount: float):
        await ctx.send(amount * 1000 / (1/6.242e18))

    @kilojoule.command(invoke_without_command=True, description='units/energy-kilojoule-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 1000 / 1055.06)

    @kilojoule.command(invoke_without_command=True, description='units/energy-kilojoule-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 1000 / 1.05506e8)

    @kilojoule.command(invoke_without_command=True, description='units/energy-kilojoule-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 1000 / 1.35582)

    @energy.group(invoke_without_command=True, description='units/energy-calorie-desc')
    async def calorie(ctx):
        pass


    @calorie.command(invoke_without_command=True, description='units/energy-calorie-joule-desc')
    async def joule(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1)

    @calorie.command(invoke_without_command=True, description='units/energy-calorie-kilojoule-desc')
    async def kilojoule(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1000)

    @calorie.command(invoke_without_command=True, description='units/energy-calorie-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 4.184 / 4184)

    @calorie.command(invoke_without_command=True, description='units/energy-calorie-watthour-desc')
    async def watthour(ctx, amount: float):
        await ctx.send(amount * 4.184 / 3600)

    @calorie.command(invoke_without_command=True, description='units/energy-calorie-kwh-desc')
    async def kwh(ctx, amount: float):
        await ctx.send(amount * 4.184 / 3.6e6)

    @calorie.command(invoke_without_command=True, description='units/energy-calorie-ev-desc')
    async def ev(ctx, amount: float):
        await ctx.send(amount * 4.184 / (1/6.242e18))

    @calorie.command(invoke_without_command=True, description='units/energy-calorie-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1055.06)

    @calorie.command(invoke_without_command=True, description='units/energy-calorie-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1.05506e8)

    @calorie.command(invoke_without_command=True, description='units/energy-calorie-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1.35582)

    @energy.group(invoke_without_command=True, description='units/energy-kcal-desc')
    async def kcal(ctx):
        pass


    @kcal.command(invoke_without_command=True, description='units/energy-kcal-joule-desc')
    async def joule(ctx, amount: float):
        await ctx.send(amount * 4184 / 1)

    @kcal.command(invoke_without_command=True, description='units/energy-kcal-kilojoule-desc')
    async def kilojoule(ctx, amount: float):
        await ctx.send(amount * 4184 / 1000)

    @kcal.command(invoke_without_command=True, description='units/energy-kcal-calorie-desc')
    async def calorie(ctx, amount: float):
        await ctx.send(amount * 4184 / 4.184)

    @kcal.command(invoke_without_command=True, description='units/energy-kcal-watthour-desc')
    async def watthour(ctx, amount: float):
        await ctx.send(amount * 4184 / 3600)

    @kcal.command(invoke_without_command=True, description='units/energy-kcal-kwh-desc')
    async def kwh(ctx, amount: float):
        await ctx.send(amount * 4184 / 3.6e6)

    @kcal.command(invoke_without_command=True, description='units/energy-kcal-ev-desc')
    async def ev(ctx, amount: float):
        await ctx.send(amount * 4184 / (1/6.242e18))

    @kcal.command(invoke_without_command=True, description='units/energy-kcal-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 4184 / 1055.06)

    @kcal.command(invoke_without_command=True, description='units/energy-kcal-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 4184 / 1.05506e8)

    @kcal.command(invoke_without_command=True, description='units/energy-kcal-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 4184 / 1.35582)

    @energy.group(invoke_without_command=True, description='units/energy-watthour-desc')
    async def watthour(ctx):
        pass


    @watthour.command(invoke_without_command=True, description='units/energy-watthour-joule-desc')
    async def joule(ctx, amount: float):
        await ctx.send(amount * 3600 / 1)

    @watthour.command(invoke_without_command=True, description='units/energy-watthour-kilojoule-desc')
    async def kilojoule(ctx, amount: float):
        await ctx.send(amount * 3600 / 1000)

    @watthour.command(invoke_without_command=True, description='units/energy-watthour-calorie-desc')
    async def calorie(ctx, amount: float):
        await ctx.send(amount * 3600 / 4.184)

    @watthour.command(invoke_without_command=True, description='units/energy-watthour-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 3600 / 4184)

    @watthour.command(invoke_without_command=True, description='units/energy-watthour-kwh-desc')
    async def kwh(ctx, amount: float):
        await ctx.send(amount * 3600 / 3.6e6)

    @watthour.command(invoke_without_command=True, description='units/energy-watthour-ev-desc')
    async def ev(ctx, amount: float):
        await ctx.send(amount * 3600 / (1/6.242e18))

    @watthour.command(invoke_without_command=True, description='units/energy-watthour-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 3600 / 1055.06)

    @watthour.command(invoke_without_command=True, description='units/energy-watthour-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 3600 / 1.05506e8)

    @watthour.command(invoke_without_command=True, description='units/energy-watthour-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 3600 / 1.35582)

    @energy.group(invoke_without_command=True, description='units/energy-kwh-desc')
    async def kwh(ctx):
        pass


    @kwh.command(invoke_without_command=True, description='units/energy-kwh-joule-desc')
    async def joule(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1)

    @kwh.command(invoke_without_command=True, description='units/energy-kwh-kilojoule-desc')
    async def kilojoule(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1000)

    @kwh.command(invoke_without_command=True, description='units/energy-kwh-calorie-desc')
    async def calorie(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 4.184)

    @kwh.command(invoke_without_command=True, description='units/energy-kwh-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 4184)

    @kwh.command(invoke_without_command=True, description='units/energy-kwh-watthour-desc')
    async def watthour(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 3600)

    @kwh.command(invoke_without_command=True, description='units/energy-kwh-ev-desc')
    async def ev(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / (1/6.242e18))

    @kwh.command(invoke_without_command=True, description='units/energy-kwh-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1055.06)

    @kwh.command(invoke_without_command=True, description='units/energy-kwh-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1.05506e8)

    @kwh.command(invoke_without_command=True, description='units/energy-kwh-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1.35582)

    @energy.group(invoke_without_command=True, description='units/energy-ev-desc')
    async def ev(ctx):
        pass


    @ev.command(invoke_without_command=True, description='units/energy-ev-joule-desc')
    async def joule(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1)

    @ev.command(invoke_without_command=True, description='units/energy-ev-kilojoule-desc')
    async def kilojoule(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1000)

    @ev.command(invoke_without_command=True, description='units/energy-ev-calorie-desc')
    async def calorie(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 4.184)

    @ev.command(invoke_without_command=True, description='units/energy-ev-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 4184)

    @ev.command(invoke_without_command=True, description='units/energy-ev-watthour-desc')
    async def watthour(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 3600)

    @ev.command(invoke_without_command=True, description='units/energy-ev-kwh-desc')
    async def kwh(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 3.6e6)

    @ev.command(invoke_without_command=True, description='units/energy-ev-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1055.06)

    @ev.command(invoke_without_command=True, description='units/energy-ev-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1.05506e8)

    @ev.command(invoke_without_command=True, description='units/energy-ev-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1.35582)

    @energy.group(invoke_without_command=True, description='units/energy-btu-desc')
    async def btu(ctx):
        pass


    @btu.command(invoke_without_command=True, description='units/energy-btu-joule-desc')
    async def joule(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 1)

    @btu.command(invoke_without_command=True, description='units/energy-btu-kilojoule-desc')
    async def kilojoule(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 1000)

    @btu.command(invoke_without_command=True, description='units/energy-btu-calorie-desc')
    async def calorie(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 4.184)

    @btu.command(invoke_without_command=True, description='units/energy-btu-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 4184)

    @btu.command(invoke_without_command=True, description='units/energy-btu-watthour-desc')
    async def watthour(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 3600)

    @btu.command(invoke_without_command=True, description='units/energy-btu-kwh-desc')
    async def kwh(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 3.6e6)

    @btu.command(invoke_without_command=True, description='units/energy-btu-ev-desc')
    async def ev(ctx, amount: float):
        await ctx.send(amount * 1055.06 / (1/6.242e18))

    @btu.command(invoke_without_command=True, description='units/energy-btu-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 1.05506e8)

    @btu.command(invoke_without_command=True, description='units/energy-btu-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 1.35582)

    @energy.group(invoke_without_command=True, description='units/energy-ust-desc')
    async def ust(ctx):
        pass


    @ust.command(invoke_without_command=True, description='units/energy-ust-joule-desc')
    async def joule(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 1)

    @ust.command(invoke_without_command=True, description='units/energy-ust-kilojoule-desc')
    async def kilojoule(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 1000)

    @ust.command(invoke_without_command=True, description='units/energy-ust-calorie-desc')
    async def calorie(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 4.184)

    @ust.command(invoke_without_command=True, description='units/energy-ust-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 4184)

    @ust.command(invoke_without_command=True, description='units/energy-ust-watthour-desc')
    async def watthour(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 3600)

    @ust.command(invoke_without_command=True, description='units/energy-ust-kwh-desc')
    async def kwh(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 3.6e6)

    @ust.command(invoke_without_command=True, description='units/energy-ust-ev-desc')
    async def ev(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / (1/6.242e18))

    @ust.command(invoke_without_command=True, description='units/energy-ust-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 1055.06)

    @ust.command(invoke_without_command=True, description='units/energy-ust-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 1.35582)

    @energy.group(invoke_without_command=True, description='units/energy-ftlb-desc')
    async def ftlb(ctx):
        pass


    @ftlb.command(invoke_without_command=True, description='units/energy-ftlb-joule-desc')
    async def joule(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 1)

    @ftlb.command(invoke_without_command=True, description='units/energy-ftlb-kilojoule-desc')
    async def kilojoule(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 1000)

    @ftlb.command(invoke_without_command=True, description='units/energy-ftlb-calorie-desc')
    async def calorie(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 4.184)

    @ftlb.command(invoke_without_command=True, description='units/energy-ftlb-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 4184)

    @ftlb.command(invoke_without_command=True, description='units/energy-ftlb-watthour-desc')
    async def watthour(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 3600)

    @ftlb.command(invoke_without_command=True, description='units/energy-ftlb-kwh-desc')
    async def kwh(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 3.6e6)

    @ftlb.command(invoke_without_command=True, description='units/energy-ftlb-ev-desc')
    async def ev(ctx, amount: float):
        await ctx.send(amount * 1.35582 / (1/6.242e18))

    @ftlb.command(invoke_without_command=True, description='units/energy-ftlb-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 1055.06)

    @ftlb.command(invoke_without_command=True, description='units/energy-ftlb-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 1.05506e8)


    @group(aliases=['freq'], invoke_without_command=True, description='units/frequency-desc')
    async def frequency(self, ctx):
        pass


    @frequency.group(invoke_without_command=True, description='units/frequency-hz-desc')
    async def hz(ctx):
        pass


    @hz.command(invoke_without_command=True, description='units/frequency-hz-khz-desc')
    async def khz(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @hz.command(invoke_without_command=True, description='units/frequency-hz-mhz-desc')
    async def mhz(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @hz.command(invoke_without_command=True, description='units/frequency-hz-ghz-desc')
    async def ghz(ctx, amount: float):
        await ctx.send(amount * 1 / 1e9)

    @frequency.group(invoke_without_command=True, description='units/frequency-khz-desc')
    async def khz(ctx):
        pass


    @khz.command(invoke_without_command=True, description='units/frequency-khz-hz-desc')
    async def hz(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @khz.command(invoke_without_command=True, description='units/frequency-khz-mhz-desc')
    async def mhz(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e6)

    @khz.command(invoke_without_command=True, description='units/frequency-khz-ghz-desc')
    async def ghz(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e9)

    @frequency.group(invoke_without_command=True, description='units/frequency-mhz-desc')
    async def mhz(ctx):
        pass


    @mhz.command(invoke_without_command=True, description='units/frequency-mhz-hz-desc')
    async def hz(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @mhz.command(invoke_without_command=True, description='units/frequency-mhz-khz-desc')
    async def khz(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e3)

    @mhz.command(invoke_without_command=True, description='units/frequency-mhz-ghz-desc')
    async def ghz(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e9)

    @frequency.group(invoke_without_command=True, description='units/frequency-ghz-desc')
    async def ghz(ctx):
        pass


    @ghz.command(invoke_without_command=True, description='units/frequency-ghz-hz-desc')
    async def hz(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1)

    @ghz.command(invoke_without_command=True, description='units/frequency-ghz-khz-desc')
    async def khz(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e3)

    @ghz.command(invoke_without_command=True, description='units/frequency-ghz-mhz-desc')
    async def mhz(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e6)


    @group(aliases=[], invoke_without_command=True, description='units/fuel-desc')
    async def fuel(self, ctx):
        pass


    @fuel.group(invoke_without_command=True, description='units/fuel-umpg-desc')
    async def umpg(ctx):
        pass


    @umpg.command(invoke_without_command=True, description='units/fuel-umpg-impg-desc')
    async def impg(ctx, amount: float):
        await ctx.send(amount * (1/2.352) / (1/2.825))

    @umpg.command(invoke_without_command=True, description='units/fuel-umpg-kmpl-desc')
    async def kmpl(ctx, amount: float):
        await ctx.send(amount * (1/2.352) / 1)

    @umpg.command(invoke_without_command=True, description='units/fuel-umpg-lphkm-desc')
    async def lphkm(ctx, amount: float):
        await ctx.send(amount * (1/2.352) / 100)

    @fuel.group(invoke_without_command=True, description='units/fuel-impg-desc')
    async def impg(ctx):
        pass


    @impg.command(invoke_without_command=True, description='units/fuel-impg-umpg-desc')
    async def umpg(ctx, amount: float):
        await ctx.send(amount * (1/2.825) / (1/2.352))

    @impg.command(invoke_without_command=True, description='units/fuel-impg-kmpl-desc')
    async def kmpl(ctx, amount: float):
        await ctx.send(amount * (1/2.825) / 1)

    @impg.command(invoke_without_command=True, description='units/fuel-impg-lphkm-desc')
    async def lphkm(ctx, amount: float):
        await ctx.send(amount * (1/2.825) / 100)

    @fuel.group(invoke_without_command=True, description='units/fuel-kmpl-desc')
    async def kmpl(ctx):
        pass


    @kmpl.command(invoke_without_command=True, description='units/fuel-kmpl-umpg-desc')
    async def umpg(ctx, amount: float):
        await ctx.send(amount * 1 / (1/2.352))

    @kmpl.command(invoke_without_command=True, description='units/fuel-kmpl-impg-desc')
    async def impg(ctx, amount: float):
        await ctx.send(amount * 1 / (1/2.825))

    @kmpl.command(invoke_without_command=True, description='units/fuel-kmpl-lphkm-desc')
    async def lphkm(ctx, amount: float):
        await ctx.send(amount * 1 / 100)

    @fuel.group(invoke_without_command=True, description='units/fuel-lphkm-desc')
    async def lphkm(ctx):
        pass


    @lphkm.command(invoke_without_command=True, description='units/fuel-lphkm-umpg-desc')
    async def umpg(ctx, amount: float):
        await ctx.send(amount * 100 / (1/2.352))

    @lphkm.command(invoke_without_command=True, description='units/fuel-lphkm-impg-desc')
    async def impg(ctx, amount: float):
        await ctx.send(amount * 100 / (1/2.825))

    @lphkm.command(invoke_without_command=True, description='units/fuel-lphkm-kmpl-desc')
    async def kmpl(ctx, amount: float):
        await ctx.send(amount * 100 / 1)


    @group(aliases=[], invoke_without_command=True, description='units/length-desc')
    async def length(self, ctx):
        pass


    @length.group(invoke_without_command=True, description='units/length-km-desc')
    async def km(ctx):
        pass


    @km.command(invoke_without_command=True, description='units/length-km-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1000 / 1)

    @km.command(invoke_without_command=True, description='units/length-km-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1000 / 1e-2)

    @km.command(invoke_without_command=True, description='units/length-km-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1000 / 1e-3)

    @km.command(invoke_without_command=True, description='units/length-km-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1000 / 1e-6)

    @km.command(invoke_without_command=True, description='units/length-km-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1000 / 1e-9)

    @km.command(invoke_without_command=True, description='units/length-km-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1000 / 1609.344)

    @km.command(invoke_without_command=True, description='units/length-km-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1000 / (1/1.094))

    @km.command(invoke_without_command=True, description='units/length-km-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1000 / (1/3.281))

    @km.command(invoke_without_command=True, description='units/length-km-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1000 / 2.54e-2)

    @km.command(invoke_without_command=True, description='units/length-km-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1000 / 1852)

    @length.group(invoke_without_command=True, description='units/length-m-desc')
    async def m(ctx):
        pass


    @m.command(invoke_without_command=True, description='units/length-m-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1 / 1000)

    @m.command(invoke_without_command=True, description='units/length-m-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-2)

    @m.command(invoke_without_command=True, description='units/length-m-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-3)

    @m.command(invoke_without_command=True, description='units/length-m-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-6)

    @m.command(invoke_without_command=True, description='units/length-m-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-9)

    @m.command(invoke_without_command=True, description='units/length-m-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1 / 1609.344)

    @m.command(invoke_without_command=True, description='units/length-m-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.094))

    @m.command(invoke_without_command=True, description='units/length-m-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3.281))

    @m.command(invoke_without_command=True, description='units/length-m-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1 / 2.54e-2)

    @m.command(invoke_without_command=True, description='units/length-m-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1 / 1852)

    @length.group(invoke_without_command=True, description='units/length-cm-desc')
    async def cm(ctx):
        pass


    @cm.command(invoke_without_command=True, description='units/length-cm-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1000)

    @cm.command(invoke_without_command=True, description='units/length-cm-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1)

    @cm.command(invoke_without_command=True, description='units/length-cm-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1e-3)

    @cm.command(invoke_without_command=True, description='units/length-cm-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1e-6)

    @cm.command(invoke_without_command=True, description='units/length-cm-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1e-9)

    @cm.command(invoke_without_command=True, description='units/length-cm-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1609.344)

    @cm.command(invoke_without_command=True, description='units/length-cm-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1e-2 / (1/1.094))

    @cm.command(invoke_without_command=True, description='units/length-cm-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1e-2 / (1/3.281))

    @cm.command(invoke_without_command=True, description='units/length-cm-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 2.54e-2)

    @cm.command(invoke_without_command=True, description='units/length-cm-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1852)

    @length.group(invoke_without_command=True, description='units/length-mm-desc')
    async def mm(ctx):
        pass


    @mm.command(invoke_without_command=True, description='units/length-mm-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1000)

    @mm.command(invoke_without_command=True, description='units/length-mm-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1)

    @mm.command(invoke_without_command=True, description='units/length-mm-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-2)

    @mm.command(invoke_without_command=True, description='units/length-mm-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-6)

    @mm.command(invoke_without_command=True, description='units/length-mm-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-9)

    @mm.command(invoke_without_command=True, description='units/length-mm-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1609.344)

    @mm.command(invoke_without_command=True, description='units/length-mm-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/1.094))

    @mm.command(invoke_without_command=True, description='units/length-mm-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/3.281))

    @mm.command(invoke_without_command=True, description='units/length-mm-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 2.54e-2)

    @mm.command(invoke_without_command=True, description='units/length-mm-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1852)

    @length.group(invoke_without_command=True, description='units/length-micron-desc')
    async def micron(ctx):
        pass


    @micron.command(invoke_without_command=True, description='units/length-micron-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1000)

    @micron.command(invoke_without_command=True, description='units/length-micron-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1)

    @micron.command(invoke_without_command=True, description='units/length-micron-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-2)

    @micron.command(invoke_without_command=True, description='units/length-micron-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-3)

    @micron.command(invoke_without_command=True, description='units/length-micron-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-9)

    @micron.command(invoke_without_command=True, description='units/length-micron-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1609.344)

    @micron.command(invoke_without_command=True, description='units/length-micron-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1e-6 / (1/1.094))

    @micron.command(invoke_without_command=True, description='units/length-micron-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1e-6 / (1/3.281))

    @micron.command(invoke_without_command=True, description='units/length-micron-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 2.54e-2)

    @micron.command(invoke_without_command=True, description='units/length-micron-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1852)

    @length.group(invoke_without_command=True, description='units/length-nm-desc')
    async def nm(ctx):
        pass


    @nm.command(invoke_without_command=True, description='units/length-nm-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1000)

    @nm.command(invoke_without_command=True, description='units/length-nm-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1)

    @nm.command(invoke_without_command=True, description='units/length-nm-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-2)

    @nm.command(invoke_without_command=True, description='units/length-nm-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-3)

    @nm.command(invoke_without_command=True, description='units/length-nm-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-6)

    @nm.command(invoke_without_command=True, description='units/length-nm-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1609.344)

    @nm.command(invoke_without_command=True, description='units/length-nm-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1e-9 / (1/1.094))

    @nm.command(invoke_without_command=True, description='units/length-nm-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1e-9 / (1/3.281))

    @nm.command(invoke_without_command=True, description='units/length-nm-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 2.54e-2)

    @nm.command(invoke_without_command=True, description='units/length-nm-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1852)

    @length.group(invoke_without_command=True, description='units/length-mile-desc')
    async def mile(ctx):
        pass


    @mile.command(invoke_without_command=True, description='units/length-mile-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1000)

    @mile.command(invoke_without_command=True, description='units/length-mile-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1)

    @mile.command(invoke_without_command=True, description='units/length-mile-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1e-2)

    @mile.command(invoke_without_command=True, description='units/length-mile-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1e-3)

    @mile.command(invoke_without_command=True, description='units/length-mile-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1e-6)

    @mile.command(invoke_without_command=True, description='units/length-mile-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1e-9)

    @mile.command(invoke_without_command=True, description='units/length-mile-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1609.344 / (1/1.094))

    @mile.command(invoke_without_command=True, description='units/length-mile-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1609.344 / (1/3.281))

    @mile.command(invoke_without_command=True, description='units/length-mile-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 2.54e-2)

    @mile.command(invoke_without_command=True, description='units/length-mile-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1852)

    @length.group(invoke_without_command=True, description='units/length-yard-desc')
    async def yard(ctx):
        pass


    @yard.command(invoke_without_command=True, description='units/length-yard-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1000)

    @yard.command(invoke_without_command=True, description='units/length-yard-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1)

    @yard.command(invoke_without_command=True, description='units/length-yard-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1e-2)

    @yard.command(invoke_without_command=True, description='units/length-yard-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1e-3)

    @yard.command(invoke_without_command=True, description='units/length-yard-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1e-6)

    @yard.command(invoke_without_command=True, description='units/length-yard-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1e-9)

    @yard.command(invoke_without_command=True, description='units/length-yard-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1609.344)

    @yard.command(invoke_without_command=True, description='units/length-yard-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / (1/3.281))

    @yard.command(invoke_without_command=True, description='units/length-yard-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 2.54e-2)

    @yard.command(invoke_without_command=True, description='units/length-yard-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1852)

    @length.group(invoke_without_command=True, description='units/length-foot-desc')
    async def foot(ctx):
        pass


    @foot.command(invoke_without_command=True, description='units/length-foot-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1000)

    @foot.command(invoke_without_command=True, description='units/length-foot-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1)

    @foot.command(invoke_without_command=True, description='units/length-foot-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1e-2)

    @foot.command(invoke_without_command=True, description='units/length-foot-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1e-3)

    @foot.command(invoke_without_command=True, description='units/length-foot-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1e-6)

    @foot.command(invoke_without_command=True, description='units/length-foot-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1e-9)

    @foot.command(invoke_without_command=True, description='units/length-foot-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1609.344)

    @foot.command(invoke_without_command=True, description='units/length-foot-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / (1/1.094))

    @foot.command(invoke_without_command=True, description='units/length-foot-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 2.54e-2)

    @foot.command(invoke_without_command=True, description='units/length-foot-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1852)

    @length.group(invoke_without_command=True, description='units/length-inch-desc')
    async def inch(ctx):
        pass


    @inch.command(invoke_without_command=True, description='units/length-inch-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1000)

    @inch.command(invoke_without_command=True, description='units/length-inch-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1)

    @inch.command(invoke_without_command=True, description='units/length-inch-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1e-2)

    @inch.command(invoke_without_command=True, description='units/length-inch-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1e-3)

    @inch.command(invoke_without_command=True, description='units/length-inch-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1e-6)

    @inch.command(invoke_without_command=True, description='units/length-inch-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1e-9)

    @inch.command(invoke_without_command=True, description='units/length-inch-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1609.344)

    @inch.command(invoke_without_command=True, description='units/length-inch-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / (1/1.094))

    @inch.command(invoke_without_command=True, description='units/length-inch-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / (1/3.281))

    @inch.command(invoke_without_command=True, description='units/length-inch-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1852)

    @length.group(invoke_without_command=True, description='units/length-nautmil-desc')
    async def nautmil(ctx):
        pass


    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1852 / 1000)

    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1852 / 1)

    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1852 / 1e-2)

    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1852 / 1e-3)

    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1852 / 1e-6)

    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1852 / 1e-9)

    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1852 / 1609.344)

    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1852 / (1/1.094))

    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1852 / (1/3.281))

    @nautmil.command(invoke_without_command=True, description='units/length-nautmil-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1852 / 2.54e-2)


    @group(aliases=[], invoke_without_command=True, description='units/mass-desc')
    async def mass(self, ctx):
        pass


    @mass.group(invoke_without_command=True, description='units/mass-tonne-desc')
    async def tonne(ctx):
        pass


    @tonne.command(invoke_without_command=True, description='units/mass-tonne-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e3)

    @tonne.command(invoke_without_command=True, description='units/mass-tonne-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @tonne.command(invoke_without_command=True, description='units/mass-tonne-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e-3)

    @tonne.command(invoke_without_command=True, description='units/mass-tonne-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e-6)

    @tonne.command(invoke_without_command=True, description='units/mass-tonne-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1.016e6)

    @tonne.command(invoke_without_command=True, description='units/mass-tonne-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1e6 / 907184.74)

    @tonne.command(invoke_without_command=True, description='units/mass-tonne-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1e6 / 6350.293)

    @tonne.command(invoke_without_command=True, description='units/mass-tonne-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 453.592)

    @tonne.command(invoke_without_command=True, description='units/mass-tonne-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1e6 / 28.3495)

    @mass.group(invoke_without_command=True, description='units/mass-kg-desc')
    async def kg(ctx):
        pass


    @kg.command(invoke_without_command=True, description='units/mass-kg-tonne-desc')
    async def tonne(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e6)

    @kg.command(invoke_without_command=True, description='units/mass-kg-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @kg.command(invoke_without_command=True, description='units/mass-kg-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e-3)

    @kg.command(invoke_without_command=True, description='units/mass-kg-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e-6)

    @kg.command(invoke_without_command=True, description='units/mass-kg-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1.016e6)

    @kg.command(invoke_without_command=True, description='units/mass-kg-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1e3 / 907184.74)

    @kg.command(invoke_without_command=True, description='units/mass-kg-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1e3 / 6350.293)

    @kg.command(invoke_without_command=True, description='units/mass-kg-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 453.592)

    @kg.command(invoke_without_command=True, description='units/mass-kg-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1e3 / 28.3495)

    @mass.group(invoke_without_command=True, description='units/mass-g-desc')
    async def g(ctx):
        pass


    @g.command(invoke_without_command=True, description='units/mass-g-tonne-desc')
    async def tonne(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @g.command(invoke_without_command=True, description='units/mass-g-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @g.command(invoke_without_command=True, description='units/mass-g-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-3)

    @g.command(invoke_without_command=True, description='units/mass-g-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-6)

    @g.command(invoke_without_command=True, description='units/mass-g-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1 / 1.016e6)

    @g.command(invoke_without_command=True, description='units/mass-g-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1 / 907184.74)

    @g.command(invoke_without_command=True, description='units/mass-g-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1 / 6350.293)

    @g.command(invoke_without_command=True, description='units/mass-g-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1 / 453.592)

    @g.command(invoke_without_command=True, description='units/mass-g-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1 / 28.3495)

    @mass.group(invoke_without_command=True, description='units/mass-mg-desc')
    async def mg(ctx):
        pass


    @mg.command(invoke_without_command=True, description='units/mass-mg-tonne-desc')
    async def tonne(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e6)

    @mg.command(invoke_without_command=True, description='units/mass-mg-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e3)

    @mg.command(invoke_without_command=True, description='units/mass-mg-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1)

    @mg.command(invoke_without_command=True, description='units/mass-mg-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-6)

    @mg.command(invoke_without_command=True, description='units/mass-mg-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1.016e6)

    @mg.command(invoke_without_command=True, description='units/mass-mg-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 907184.74)

    @mg.command(invoke_without_command=True, description='units/mass-mg-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 6350.293)

    @mg.command(invoke_without_command=True, description='units/mass-mg-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 453.592)

    @mg.command(invoke_without_command=True, description='units/mass-mg-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 28.3495)

    @mass.group(invoke_without_command=True, description='units/mass-microg-desc')
    async def microg(ctx):
        pass


    @microg.command(invoke_without_command=True, description='units/mass-microg-tonne-desc')
    async def tonne(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e6)

    @microg.command(invoke_without_command=True, description='units/mass-microg-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e3)

    @microg.command(invoke_without_command=True, description='units/mass-microg-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1)

    @microg.command(invoke_without_command=True, description='units/mass-microg-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-3)

    @microg.command(invoke_without_command=True, description='units/mass-microg-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1.016e6)

    @microg.command(invoke_without_command=True, description='units/mass-microg-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 907184.74)

    @microg.command(invoke_without_command=True, description='units/mass-microg-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 6350.293)

    @microg.command(invoke_without_command=True, description='units/mass-microg-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 453.592)

    @microg.command(invoke_without_command=True, description='units/mass-microg-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 28.3495)

    @mass.group(invoke_without_command=True, description='units/mass-ton-desc')
    async def ton(ctx):
        pass


    @ton.command(invoke_without_command=True, description='units/mass-ton-tonne-desc')
    async def tonne(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1e6)

    @ton.command(invoke_without_command=True, description='units/mass-ton-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1e3)

    @ton.command(invoke_without_command=True, description='units/mass-ton-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1)

    @ton.command(invoke_without_command=True, description='units/mass-ton-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1e-3)

    @ton.command(invoke_without_command=True, description='units/mass-ton-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1e-6)

    @ton.command(invoke_without_command=True, description='units/mass-ton-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 907184.74)

    @ton.command(invoke_without_command=True, description='units/mass-ton-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 6350.293)

    @ton.command(invoke_without_command=True, description='units/mass-ton-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 453.592)

    @ton.command(invoke_without_command=True, description='units/mass-ton-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 28.3495)

    @mass.group(invoke_without_command=True, description='units/mass-uston-desc')
    async def uston(ctx):
        pass


    @uston.command(invoke_without_command=True, description='units/mass-uston-tonne-desc')
    async def tonne(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1e6)

    @uston.command(invoke_without_command=True, description='units/mass-uston-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1e3)

    @uston.command(invoke_without_command=True, description='units/mass-uston-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1)

    @uston.command(invoke_without_command=True, description='units/mass-uston-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1e-3)

    @uston.command(invoke_without_command=True, description='units/mass-uston-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1e-6)

    @uston.command(invoke_without_command=True, description='units/mass-uston-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1.016e6)

    @uston.command(invoke_without_command=True, description='units/mass-uston-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 6350.293)

    @uston.command(invoke_without_command=True, description='units/mass-uston-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 453.592)

    @uston.command(invoke_without_command=True, description='units/mass-uston-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 28.3495)

    @mass.group(invoke_without_command=True, description='units/mass-stone-desc')
    async def stone(ctx):
        pass


    @stone.command(invoke_without_command=True, description='units/mass-stone-tonne-desc')
    async def tonne(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1e6)

    @stone.command(invoke_without_command=True, description='units/mass-stone-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1e3)

    @stone.command(invoke_without_command=True, description='units/mass-stone-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1)

    @stone.command(invoke_without_command=True, description='units/mass-stone-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1e-3)

    @stone.command(invoke_without_command=True, description='units/mass-stone-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1e-6)

    @stone.command(invoke_without_command=True, description='units/mass-stone-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1.016e6)

    @stone.command(invoke_without_command=True, description='units/mass-stone-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 907184.74)

    @stone.command(invoke_without_command=True, description='units/mass-stone-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 453.592)

    @stone.command(invoke_without_command=True, description='units/mass-stone-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 28.3495)

    @mass.group(invoke_without_command=True, description='units/mass-lb-desc')
    async def lb(ctx):
        pass


    @lb.command(invoke_without_command=True, description='units/mass-lb-tonne-desc')
    async def tonne(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1e6)

    @lb.command(invoke_without_command=True, description='units/mass-lb-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1e3)

    @lb.command(invoke_without_command=True, description='units/mass-lb-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1)

    @lb.command(invoke_without_command=True, description='units/mass-lb-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1e-3)

    @lb.command(invoke_without_command=True, description='units/mass-lb-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1e-6)

    @lb.command(invoke_without_command=True, description='units/mass-lb-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1.016e6)

    @lb.command(invoke_without_command=True, description='units/mass-lb-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 453.592 / 907184.74)

    @lb.command(invoke_without_command=True, description='units/mass-lb-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 453.592 / 6350.293)

    @lb.command(invoke_without_command=True, description='units/mass-lb-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 453.592 / 28.3495)

    @mass.group(invoke_without_command=True, description='units/mass-oz-desc')
    async def oz(ctx):
        pass


    @oz.command(invoke_without_command=True, description='units/mass-oz-tonne-desc')
    async def tonne(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1e6)

    @oz.command(invoke_without_command=True, description='units/mass-oz-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1e3)

    @oz.command(invoke_without_command=True, description='units/mass-oz-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1)

    @oz.command(invoke_without_command=True, description='units/mass-oz-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1e-3)

    @oz.command(invoke_without_command=True, description='units/mass-oz-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1e-6)

    @oz.command(invoke_without_command=True, description='units/mass-oz-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1.016e6)

    @oz.command(invoke_without_command=True, description='units/mass-oz-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 907184.74)

    @oz.command(invoke_without_command=True, description='units/mass-oz-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 6350.293)

    @oz.command(invoke_without_command=True, description='units/mass-oz-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 453.592)


    @group(aliases=[], invoke_without_command=True, description='units/angle-desc')
    async def angle(self, ctx):
        pass


    @angle.group(invoke_without_command=True, description='units/angle-deg-desc')
    async def deg(ctx):
        pass


    @deg.command(invoke_without_command=True, description='units/angle-deg-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * 1 / 0.9)

    @deg.command(invoke_without_command=True, description='units/angle-deg-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * 1 / (180/(1000 * math.pi)))

    @deg.command(invoke_without_command=True, description='units/angle-deg-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * 1 / (1/60))

    @deg.command(invoke_without_command=True, description='units/angle-deg-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * 1 / (180/math.pi))

    @deg.command(invoke_without_command=True, description='units/angle-deg-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3600))

    @angle.group(invoke_without_command=True, description='units/angle-grad-desc')
    async def grad(ctx):
        pass


    @grad.command(invoke_without_command=True, description='units/angle-grad-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * 0.9 / 1)

    @grad.command(invoke_without_command=True, description='units/angle-grad-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * 0.9 / (180/(1000 * math.pi)))

    @grad.command(invoke_without_command=True, description='units/angle-grad-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * 0.9 / (1/60))

    @grad.command(invoke_without_command=True, description='units/angle-grad-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * 0.9 / (180/math.pi))

    @grad.command(invoke_without_command=True, description='units/angle-grad-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * 0.9 / (1/3600))

    @angle.group(invoke_without_command=True, description='units/angle-mrad-desc')
    async def mrad(ctx):
        pass


    @mrad.command(invoke_without_command=True, description='units/angle-mrad-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * math.pi)) / 1)

    @mrad.command(invoke_without_command=True, description='units/angle-mrad-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * math.pi)) / 0.9)

    @mrad.command(invoke_without_command=True, description='units/angle-mrad-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * math.pi)) / (1/60))

    @mrad.command(invoke_without_command=True, description='units/angle-mrad-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * math.pi)) / (180/math.pi))

    @mrad.command(invoke_without_command=True, description='units/angle-mrad-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * math.pi)) / (1/3600))

    @angle.group(invoke_without_command=True, description='units/angle-arcmin-desc')
    async def arcmin(ctx):
        pass


    @arcmin.command(invoke_without_command=True, description='units/angle-arcmin-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * (1/60) / 1)

    @arcmin.command(invoke_without_command=True, description='units/angle-arcmin-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * (1/60) / 0.9)

    @arcmin.command(invoke_without_command=True, description='units/angle-arcmin-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * (1/60) / (180/(1000 * math.pi)))

    @arcmin.command(invoke_without_command=True, description='units/angle-arcmin-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * (1/60) / (180/math.pi))

    @arcmin.command(invoke_without_command=True, description='units/angle-arcmin-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * (1/60) / (1/3600))

    @angle.group(invoke_without_command=True, description='units/angle-rad-desc')
    async def rad(ctx):
        pass


    @rad.command(invoke_without_command=True, description='units/angle-rad-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * (180/math.pi) / 1)

    @rad.command(invoke_without_command=True, description='units/angle-rad-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * (180/math.pi) / 0.9)

    @rad.command(invoke_without_command=True, description='units/angle-rad-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * (180/math.pi) / (180/(1000 * math.pi)))

    @rad.command(invoke_without_command=True, description='units/angle-rad-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * (180/math.pi) / (1/60))

    @rad.command(invoke_without_command=True, description='units/angle-rad-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * (180/math.pi) / (1/3600))

    @angle.group(invoke_without_command=True, description='units/angle-arcsec-desc')
    async def arcsec(ctx):
        pass


    @arcsec.command(invoke_without_command=True, description='units/angle-arcsec-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * (1/3600) / 1)

    @arcsec.command(invoke_without_command=True, description='units/angle-arcsec-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * (1/3600) / 0.9)

    @arcsec.command(invoke_without_command=True, description='units/angle-arcsec-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * (1/3600) / (180/(1000 * math.pi)))

    @arcsec.command(invoke_without_command=True, description='units/angle-arcsec-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * (1/3600) / (1/60))

    @arcsec.command(invoke_without_command=True, description='units/angle-arcsec-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * (1/3600) / (180/math.pi))


    @group(aliases=[], invoke_without_command=True, description='units/pressure-desc')
    async def pressure(self, ctx):
        pass


    @pressure.group(invoke_without_command=True, description='units/pressure-atm-desc')
    async def atm(ctx):
        pass


    @atm.command(invoke_without_command=True, description='units/pressure-atm-bar-desc')
    async def bar(ctx, amount: float):
        await ctx.send(amount * 101325 / 1e5)

    @atm.command(invoke_without_command=True, description='units/pressure-atm-pa-desc')
    async def pa(ctx, amount: float):
        await ctx.send(amount * 101325 / 1)

    @atm.command(invoke_without_command=True, description='units/pressure-atm-psi-desc')
    async def psi(ctx, amount: float):
        await ctx.send(amount * 101325 / 6894.757)

    @atm.command(invoke_without_command=True, description='units/pressure-atm-torr-desc')
    async def torr(ctx, amount: float):
        await ctx.send(amount * 101325 / 133.322)

    @pressure.group(invoke_without_command=True, description='units/pressure-bar-desc')
    async def bar(ctx):
        pass


    @bar.command(invoke_without_command=True, description='units/pressure-bar-atm-desc')
    async def atm(ctx, amount: float):
        await ctx.send(amount * 1e5 / 101325)

    @bar.command(invoke_without_command=True, description='units/pressure-bar-pa-desc')
    async def pa(ctx, amount: float):
        await ctx.send(amount * 1e5 / 1)

    @bar.command(invoke_without_command=True, description='units/pressure-bar-psi-desc')
    async def psi(ctx, amount: float):
        await ctx.send(amount * 1e5 / 6894.757)

    @bar.command(invoke_without_command=True, description='units/pressure-bar-torr-desc')
    async def torr(ctx, amount: float):
        await ctx.send(amount * 1e5 / 133.322)

    @pressure.group(invoke_without_command=True, description='units/pressure-pa-desc')
    async def pa(ctx):
        pass


    @pa.command(invoke_without_command=True, description='units/pressure-pa-atm-desc')
    async def atm(ctx, amount: float):
        await ctx.send(amount * 1 / 101325)

    @pa.command(invoke_without_command=True, description='units/pressure-pa-bar-desc')
    async def bar(ctx, amount: float):
        await ctx.send(amount * 1 / 1e5)

    @pa.command(invoke_without_command=True, description='units/pressure-pa-psi-desc')
    async def psi(ctx, amount: float):
        await ctx.send(amount * 1 / 6894.757)

    @pa.command(invoke_without_command=True, description='units/pressure-pa-torr-desc')
    async def torr(ctx, amount: float):
        await ctx.send(amount * 1 / 133.322)

    @pressure.group(invoke_without_command=True, description='units/pressure-psi-desc')
    async def psi(ctx):
        pass


    @psi.command(invoke_without_command=True, description='units/pressure-psi-atm-desc')
    async def atm(ctx, amount: float):
        await ctx.send(amount * 6894.757 / 101325)

    @psi.command(invoke_without_command=True, description='units/pressure-psi-bar-desc')
    async def bar(ctx, amount: float):
        await ctx.send(amount * 6894.757 / 1e5)

    @psi.command(invoke_without_command=True, description='units/pressure-psi-pa-desc')
    async def pa(ctx, amount: float):
        await ctx.send(amount * 6894.757 / 1)

    @psi.command(invoke_without_command=True, description='units/pressure-psi-torr-desc')
    async def torr(ctx, amount: float):
        await ctx.send(amount * 6894.757 / 133.322)

    @pressure.group(invoke_without_command=True, description='units/pressure-torr-desc')
    async def torr(ctx):
        pass


    @torr.command(invoke_without_command=True, description='units/pressure-torr-atm-desc')
    async def atm(ctx, amount: float):
        await ctx.send(amount * 133.322 / 101325)

    @torr.command(invoke_without_command=True, description='units/pressure-torr-bar-desc')
    async def bar(ctx, amount: float):
        await ctx.send(amount * 133.322 / 1e5)

    @torr.command(invoke_without_command=True, description='units/pressure-torr-pa-desc')
    async def pa(ctx, amount: float):
        await ctx.send(amount * 133.322 / 1)

    @torr.command(invoke_without_command=True, description='units/pressure-torr-psi-desc')
    async def psi(ctx, amount: float):
        await ctx.send(amount * 133.322 / 6894.757)


    @group(aliases=[], invoke_without_command=True, description='units/speed-desc')
    async def speed(self, ctx):
        pass


    @speed.group(invoke_without_command=True, description='units/speed-mph-desc')
    async def mph(ctx):
        pass


    @mph.command(invoke_without_command=True, description='units/speed-mph-fps-desc')
    async def fps(ctx, amount: float):
        await ctx.send(amount * (1/2.237) / (1/3.281))

    @mph.command(invoke_without_command=True, description='units/speed-mph-mps-desc')
    async def mps(ctx, amount: float):
        await ctx.send(amount * (1/2.237) / 1)

    @mph.command(invoke_without_command=True, description='units/speed-mph-kmph-desc')
    async def kmph(ctx, amount: float):
        await ctx.send(amount * (1/2.237) / (1/3.6))

    @mph.command(invoke_without_command=True, description='units/speed-mph-knot-desc')
    async def knot(ctx, amount: float):
        await ctx.send(amount * (1/2.237) / (1/1.944))

    @speed.group(invoke_without_command=True, description='units/speed-fps-desc')
    async def fps(ctx):
        pass


    @fps.command(invoke_without_command=True, description='units/speed-fps-mph-desc')
    async def mph(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / (1/2.237))

    @fps.command(invoke_without_command=True, description='units/speed-fps-mps-desc')
    async def mps(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1)

    @fps.command(invoke_without_command=True, description='units/speed-fps-kmph-desc')
    async def kmph(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / (1/3.6))

    @fps.command(invoke_without_command=True, description='units/speed-fps-knot-desc')
    async def knot(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / (1/1.944))

    @speed.group(invoke_without_command=True, description='units/speed-mps-desc')
    async def mps(ctx):
        pass


    @mps.command(invoke_without_command=True, description='units/speed-mps-mph-desc')
    async def mph(ctx, amount: float):
        await ctx.send(amount * 1 / (1/2.237))

    @mps.command(invoke_without_command=True, description='units/speed-mps-fps-desc')
    async def fps(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3.281))

    @mps.command(invoke_without_command=True, description='units/speed-mps-kmph-desc')
    async def kmph(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3.6))

    @mps.command(invoke_without_command=True, description='units/speed-mps-knot-desc')
    async def knot(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.944))

    @speed.group(invoke_without_command=True, description='units/speed-kmph-desc')
    async def kmph(ctx):
        pass


    @kmph.command(invoke_without_command=True, description='units/speed-kmph-mph-desc')
    async def mph(ctx, amount: float):
        await ctx.send(amount * (1/3.6) / (1/2.237))

    @kmph.command(invoke_without_command=True, description='units/speed-kmph-fps-desc')
    async def fps(ctx, amount: float):
        await ctx.send(amount * (1/3.6) / (1/3.281))

    @kmph.command(invoke_without_command=True, description='units/speed-kmph-mps-desc')
    async def mps(ctx, amount: float):
        await ctx.send(amount * (1/3.6) / 1)

    @kmph.command(invoke_without_command=True, description='units/speed-kmph-knot-desc')
    async def knot(ctx, amount: float):
        await ctx.send(amount * (1/3.6) / (1/1.944))

    @speed.group(invoke_without_command=True, description='units/speed-knot-desc')
    async def knot(ctx):
        pass


    @knot.command(invoke_without_command=True, description='units/speed-knot-mph-desc')
    async def mph(ctx, amount: float):
        await ctx.send(amount * (1/1.944) / (1/2.237))

    @knot.command(invoke_without_command=True, description='units/speed-knot-fps-desc')
    async def fps(ctx, amount: float):
        await ctx.send(amount * (1/1.944) / (1/3.281))

    @knot.command(invoke_without_command=True, description='units/speed-knot-mps-desc')
    async def mps(ctx, amount: float):
        await ctx.send(amount * (1/1.944) / 1)

    @knot.command(invoke_without_command=True, description='units/speed-knot-kmph-desc')
    async def kmph(ctx, amount: float):
        await ctx.send(amount * (1/1.944) / (1/3.6))


    @group(aliases=['temp'], invoke_without_command=True, description='units/temperature-desc')
    async def temperature(self, ctx):
        pass


    @group(aliases=['temp'], invoke_without_command=True, description='units/temperature-desc')
    async def temperature(self, ctx):
        pass


    @temperature.group(invoke_without_command=True, description='units/temperature-C-desc')
    async def C(ctx):
        pass


    @C.command(invoke_without_command=True, description='units/temperature-C-F-desc')
    async def F(ctx, amount: float):
        await ctx.send((amount * 9 / 5) + 32)

    @C.command(invoke_without_command=True, description='units/temperature-C-K-desc')
    async def K(ctx, amount: float):
        await ctx.send(amount + 273.15)

    @temperature.group(invoke_without_command=True, description='units/temperature-F-desc')
    async def F(ctx):
        pass


    @F.command(invoke_without_command=True, description='units/temperature-F-C-desc')
    async def C(ctx, amount: float):
        await ctx.send((amount - 32) * 5 / 9)

    @F.command(invoke_without_command=True, description='units/temperature-F-K-desc')
    async def K(ctx, amount: float):
        await ctx.send((amount - 32) * 5 / 9 + 273.15)

    @temperature.group(invoke_without_command=True, description='units/temperature-K-desc')
    async def K(ctx):
        pass


    @K.command(invoke_without_command=True, description='units/temperature-K-C-desc')
    async def C(ctx, amount: float):
        await ctx.send(amount - 273.15)

    @K.command(invoke_without_command=True, description='units/temperature-K-F-desc')
    async def F(ctx, amount: float):
        await ctx.send((amount - 273.15) * 9 / 5 + 32)



    @group(aliases=[], invoke_without_command=True, description='units/time-desc')
    async def time(self, ctx):
        pass


    @time.group(invoke_without_command=True, description='units/time-ns-desc')
    async def ns(ctx):
        pass


    @ns.command(invoke_without_command=True, description='units/time-ns-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-6)

    @ns.command(invoke_without_command=True, description='units/time-ns-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-3)

    @ns.command(invoke_without_command=True, description='units/time-ns-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1)

    @ns.command(invoke_without_command=True, description='units/time-ns-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 60)

    @ns.command(invoke_without_command=True, description='units/time-ns-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 3600)

    @ns.command(invoke_without_command=True, description='units/time-ns-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 86400)

    @ns.command(invoke_without_command=True, description='units/time-ns-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 604800)

    @ns.command(invoke_without_command=True, description='units/time-ns-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 2.628e6)

    @ns.command(invoke_without_command=True, description='units/time-ns-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 3.154e7)

    @ns.command(invoke_without_command=True, description='units/time-ns-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 3.154e8)

    @ns.command(invoke_without_command=True, description='units/time-ns-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-micros-desc')
    async def micros(ctx):
        pass


    @micros.command(invoke_without_command=True, description='units/time-micros-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-9)

    @micros.command(invoke_without_command=True, description='units/time-micros-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-3)

    @micros.command(invoke_without_command=True, description='units/time-micros-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1)

    @micros.command(invoke_without_command=True, description='units/time-micros-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 60)

    @micros.command(invoke_without_command=True, description='units/time-micros-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 3600)

    @micros.command(invoke_without_command=True, description='units/time-micros-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 86400)

    @micros.command(invoke_without_command=True, description='units/time-micros-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 604800)

    @micros.command(invoke_without_command=True, description='units/time-micros-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 2.628e6)

    @micros.command(invoke_without_command=True, description='units/time-micros-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 3.154e7)

    @micros.command(invoke_without_command=True, description='units/time-micros-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 3.154e8)

    @micros.command(invoke_without_command=True, description='units/time-micros-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-ms-desc')
    async def ms(ctx):
        pass


    @ms.command(invoke_without_command=True, description='units/time-ms-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-9)

    @ms.command(invoke_without_command=True, description='units/time-ms-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-6)

    @ms.command(invoke_without_command=True, description='units/time-ms-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1)

    @ms.command(invoke_without_command=True, description='units/time-ms-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 60)

    @ms.command(invoke_without_command=True, description='units/time-ms-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3600)

    @ms.command(invoke_without_command=True, description='units/time-ms-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 86400)

    @ms.command(invoke_without_command=True, description='units/time-ms-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 604800)

    @ms.command(invoke_without_command=True, description='units/time-ms-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 2.628e6)

    @ms.command(invoke_without_command=True, description='units/time-ms-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3.154e7)

    @ms.command(invoke_without_command=True, description='units/time-ms-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3.154e8)

    @ms.command(invoke_without_command=True, description='units/time-ms-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-s-desc')
    async def s(ctx):
        pass


    @s.command(invoke_without_command=True, description='units/time-s-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-9)

    @s.command(invoke_without_command=True, description='units/time-s-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-6)

    @s.command(invoke_without_command=True, description='units/time-s-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-3)

    @s.command(invoke_without_command=True, description='units/time-s-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 1 / 60)

    @s.command(invoke_without_command=True, description='units/time-s-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 1 / 3600)

    @s.command(invoke_without_command=True, description='units/time-s-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 1 / 86400)

    @s.command(invoke_without_command=True, description='units/time-s-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 1 / 604800)

    @s.command(invoke_without_command=True, description='units/time-s-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 1 / 2.628e6)

    @s.command(invoke_without_command=True, description='units/time-s-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 1 / 3.154e7)

    @s.command(invoke_without_command=True, description='units/time-s-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 1 / 3.154e8)

    @s.command(invoke_without_command=True, description='units/time-s-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 1 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-min-desc')
    async def min(ctx):
        pass


    @min.command(invoke_without_command=True, description='units/time-min-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 60 / 1e-9)

    @min.command(invoke_without_command=True, description='units/time-min-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 60 / 1e-6)

    @min.command(invoke_without_command=True, description='units/time-min-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 60 / 1e-3)

    @min.command(invoke_without_command=True, description='units/time-min-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 60 / 1)

    @min.command(invoke_without_command=True, description='units/time-min-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 60 / 3600)

    @min.command(invoke_without_command=True, description='units/time-min-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 60 / 86400)

    @min.command(invoke_without_command=True, description='units/time-min-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 60 / 604800)

    @min.command(invoke_without_command=True, description='units/time-min-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 60 / 2.628e6)

    @min.command(invoke_without_command=True, description='units/time-min-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 60 / 3.154e7)

    @min.command(invoke_without_command=True, description='units/time-min-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 60 / 3.154e8)

    @min.command(invoke_without_command=True, description='units/time-min-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 60 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-h-desc')
    async def h(ctx):
        pass


    @h.command(invoke_without_command=True, description='units/time-h-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 3600 / 1e-9)

    @h.command(invoke_without_command=True, description='units/time-h-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 3600 / 1e-6)

    @h.command(invoke_without_command=True, description='units/time-h-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 3600 / 1e-3)

    @h.command(invoke_without_command=True, description='units/time-h-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 3600 / 1)

    @h.command(invoke_without_command=True, description='units/time-h-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 3600 / 60)

    @h.command(invoke_without_command=True, description='units/time-h-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 3600 / 86400)

    @h.command(invoke_without_command=True, description='units/time-h-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 3600 / 604800)

    @h.command(invoke_without_command=True, description='units/time-h-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 3600 / 2.628e6)

    @h.command(invoke_without_command=True, description='units/time-h-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 3600 / 3.154e7)

    @h.command(invoke_without_command=True, description='units/time-h-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 3600 / 3.154e8)

    @h.command(invoke_without_command=True, description='units/time-h-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 3600 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-day-desc')
    async def day(ctx):
        pass


    @day.command(invoke_without_command=True, description='units/time-day-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 86400 / 1e-9)

    @day.command(invoke_without_command=True, description='units/time-day-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 86400 / 1e-6)

    @day.command(invoke_without_command=True, description='units/time-day-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 86400 / 1e-3)

    @day.command(invoke_without_command=True, description='units/time-day-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 86400 / 1)

    @day.command(invoke_without_command=True, description='units/time-day-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 86400 / 60)

    @day.command(invoke_without_command=True, description='units/time-day-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 86400 / 3600)

    @day.command(invoke_without_command=True, description='units/time-day-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 86400 / 604800)

    @day.command(invoke_without_command=True, description='units/time-day-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 86400 / 2.628e6)

    @day.command(invoke_without_command=True, description='units/time-day-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 86400 / 3.154e7)

    @day.command(invoke_without_command=True, description='units/time-day-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 86400 / 3.154e8)

    @day.command(invoke_without_command=True, description='units/time-day-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 86400 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-week-desc')
    async def week(ctx):
        pass


    @week.command(invoke_without_command=True, description='units/time-week-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 604800 / 1e-9)

    @week.command(invoke_without_command=True, description='units/time-week-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 604800 / 1e-6)

    @week.command(invoke_without_command=True, description='units/time-week-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 604800 / 1e-3)

    @week.command(invoke_without_command=True, description='units/time-week-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 604800 / 1)

    @week.command(invoke_without_command=True, description='units/time-week-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 604800 / 60)

    @week.command(invoke_without_command=True, description='units/time-week-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 604800 / 3600)

    @week.command(invoke_without_command=True, description='units/time-week-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 604800 / 86400)

    @week.command(invoke_without_command=True, description='units/time-week-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 604800 / 2.628e6)

    @week.command(invoke_without_command=True, description='units/time-week-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 604800 / 3.154e7)

    @week.command(invoke_without_command=True, description='units/time-week-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 604800 / 3.154e8)

    @week.command(invoke_without_command=True, description='units/time-week-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 604800 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-month-desc')
    async def month(ctx):
        pass


    @month.command(invoke_without_command=True, description='units/time-month-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 1e-9)

    @month.command(invoke_without_command=True, description='units/time-month-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 1e-6)

    @month.command(invoke_without_command=True, description='units/time-month-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 1e-3)

    @month.command(invoke_without_command=True, description='units/time-month-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 1)

    @month.command(invoke_without_command=True, description='units/time-month-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 60)

    @month.command(invoke_without_command=True, description='units/time-month-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 3600)

    @month.command(invoke_without_command=True, description='units/time-month-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 86400)

    @month.command(invoke_without_command=True, description='units/time-month-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 604800)

    @month.command(invoke_without_command=True, description='units/time-month-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 3.154e7)

    @month.command(invoke_without_command=True, description='units/time-month-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 3.154e8)

    @month.command(invoke_without_command=True, description='units/time-month-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-year-desc')
    async def year(ctx):
        pass


    @year.command(invoke_without_command=True, description='units/time-year-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 1e-9)

    @year.command(invoke_without_command=True, description='units/time-year-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 1e-6)

    @year.command(invoke_without_command=True, description='units/time-year-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 1e-3)

    @year.command(invoke_without_command=True, description='units/time-year-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 1)

    @year.command(invoke_without_command=True, description='units/time-year-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 60)

    @year.command(invoke_without_command=True, description='units/time-year-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 3600)

    @year.command(invoke_without_command=True, description='units/time-year-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 86400)

    @year.command(invoke_without_command=True, description='units/time-year-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 604800)

    @year.command(invoke_without_command=True, description='units/time-year-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 2.628e6)

    @year.command(invoke_without_command=True, description='units/time-year-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 3.154e8)

    @year.command(invoke_without_command=True, description='units/time-year-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-decade-desc')
    async def decade(ctx):
        pass


    @decade.command(invoke_without_command=True, description='units/time-decade-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 1e-9)

    @decade.command(invoke_without_command=True, description='units/time-decade-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 1e-6)

    @decade.command(invoke_without_command=True, description='units/time-decade-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 1e-3)

    @decade.command(invoke_without_command=True, description='units/time-decade-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 1)

    @decade.command(invoke_without_command=True, description='units/time-decade-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 60)

    @decade.command(invoke_without_command=True, description='units/time-decade-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 3600)

    @decade.command(invoke_without_command=True, description='units/time-decade-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 86400)

    @decade.command(invoke_without_command=True, description='units/time-decade-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 604800)

    @decade.command(invoke_without_command=True, description='units/time-decade-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 2.628e6)

    @decade.command(invoke_without_command=True, description='units/time-decade-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 3.154e7)

    @decade.command(invoke_without_command=True, description='units/time-decade-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 3.154e9)

    @time.group(invoke_without_command=True, description='units/time-century-desc')
    async def century(ctx):
        pass


    @century.command(invoke_without_command=True, description='units/time-century-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 1e-9)

    @century.command(invoke_without_command=True, description='units/time-century-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 1e-6)

    @century.command(invoke_without_command=True, description='units/time-century-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 1e-3)

    @century.command(invoke_without_command=True, description='units/time-century-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 1)

    @century.command(invoke_without_command=True, description='units/time-century-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 60)

    @century.command(invoke_without_command=True, description='units/time-century-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 3600)

    @century.command(invoke_without_command=True, description='units/time-century-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 86400)

    @century.command(invoke_without_command=True, description='units/time-century-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 604800)

    @century.command(invoke_without_command=True, description='units/time-century-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 2.628e6)

    @century.command(invoke_without_command=True, description='units/time-century-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 3.154e7)

    @century.command(invoke_without_command=True, description='units/time-century-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 3.154e8)


    @group(aliases=[], invoke_without_command=True, description='units/volume-desc')
    async def volume(self, ctx):
        pass


    @volume.group(invoke_without_command=True, description='units/volume-lgallon-desc')
    async def lgallon(ctx):
        pass


    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/1.057))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/4.167))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/4.167))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/33.814))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/67.628))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/202.884))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 1e3)

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 1)

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 1e-3)

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 4.546)

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 1.3652)

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/1.76))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/3.52))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/35.195))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/56.312))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/168.936))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/28.317))

    @lgallon.command(invoke_without_command=True, description='units/volume-lgallon-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-lquart-desc')
    async def lquart(ctx):
        pass


    @lquart.command(invoke_without_command=True, description='units/volume-lquart-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 3.78541)

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/4.167))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/4.167))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/33.814))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/67.628))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/202.884))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 1e3)

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 1)

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 1e-3)

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 4.546)

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 1.3652)

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/1.76))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/3.52))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/35.195))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/56.312))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/168.936))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/28.317))

    @lquart.command(invoke_without_command=True, description='units/volume-lquart-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-lpint-desc')
    async def lpint(ctx):
        pass


    @lpint.command(invoke_without_command=True, description='units/volume-lpint-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 3.78541)

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/1.057))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/4.167))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/33.814))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/67.628))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/202.884))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1e3)

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1)

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1e-3)

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 4.546)

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1.3652)

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/1.76))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/3.52))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/35.195))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/56.312))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/168.936))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/28.317))

    @lpint.command(invoke_without_command=True, description='units/volume-lpint-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-uscup-desc')
    async def uscup(ctx):
        pass


    @uscup.command(invoke_without_command=True, description='units/volume-uscup-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 3.78541)

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/1.057))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/4.167))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/33.814))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/67.628))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/202.884))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1e3)

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1)

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1e-3)

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 4.546)

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1.3652)

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/1.76))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/3.52))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/35.195))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/56.312))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/168.936))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/28.317))

    @uscup.command(invoke_without_command=True, description='units/volume-uscup-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-usfloz-desc')
    async def usfloz(ctx):
        pass


    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 3.78541)

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/1.057))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/4.167))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/4.167))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/67.628))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/202.884))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 1e3)

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 1)

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 1e-3)

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 4.546)

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 1.3652)

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/1.76))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/3.52))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/35.195))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/56.312))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/168.936))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/28.317))

    @usfloz.command(invoke_without_command=True, description='units/volume-usfloz-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-ustbsp-desc')
    async def ustbsp(ctx):
        pass


    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 3.78541)

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/1.057))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/4.167))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/4.167))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/33.814))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/202.884))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 1e3)

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 1)

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 1e-3)

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 4.546)

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 1.3652)

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/1.76))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/3.52))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/35.195))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/56.312))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/168.936))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/28.317))

    @ustbsp.command(invoke_without_command=True, description='units/volume-ustbsp-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-ustsp-desc')
    async def ustsp(ctx):
        pass


    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 3.78541)

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/1.057))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/4.167))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/4.167))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/33.814))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/67.628))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 1e3)

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 1)

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 1e-3)

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 4.546)

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 1.3652)

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/1.76))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/3.52))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/35.195))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/56.312))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/168.936))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/28.317))

    @ustsp.command(invoke_without_command=True, description='units/volume-ustsp-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-m3-desc')
    async def m3(ctx):
        pass


    @m3.command(invoke_without_command=True, description='units/volume-m3-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 1e3 / 3.78541)

    @m3.command(invoke_without_command=True, description='units/volume-m3-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/1.057))

    @m3.command(invoke_without_command=True, description='units/volume-m3-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/4.167))

    @m3.command(invoke_without_command=True, description='units/volume-m3-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/4.167))

    @m3.command(invoke_without_command=True, description='units/volume-m3-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/33.814))

    @m3.command(invoke_without_command=True, description='units/volume-m3-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/67.628))

    @m3.command(invoke_without_command=True, description='units/volume-m3-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/202.884))

    @m3.command(invoke_without_command=True, description='units/volume-m3-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @m3.command(invoke_without_command=True, description='units/volume-m3-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e-3)

    @m3.command(invoke_without_command=True, description='units/volume-m3-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 1e3 / 4.546)

    @m3.command(invoke_without_command=True, description='units/volume-m3-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1.3652)

    @m3.command(invoke_without_command=True, description='units/volume-m3-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/1.76))

    @m3.command(invoke_without_command=True, description='units/volume-m3-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/3.52))

    @m3.command(invoke_without_command=True, description='units/volume-m3-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/35.195))

    @m3.command(invoke_without_command=True, description='units/volume-m3-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/56.312))

    @m3.command(invoke_without_command=True, description='units/volume-m3-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/168.936))

    @m3.command(invoke_without_command=True, description='units/volume-m3-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/28.317))

    @m3.command(invoke_without_command=True, description='units/volume-m3-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-l-desc')
    async def l(ctx):
        pass


    @l.command(invoke_without_command=True, description='units/volume-l-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 1 / 3.78541)

    @l.command(invoke_without_command=True, description='units/volume-l-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.057))

    @l.command(invoke_without_command=True, description='units/volume-l-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 1 / (1/4.167))

    @l.command(invoke_without_command=True, description='units/volume-l-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 1 / (1/4.167))

    @l.command(invoke_without_command=True, description='units/volume-l-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 1 / (1/33.814))

    @l.command(invoke_without_command=True, description='units/volume-l-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 1 / (1/67.628))

    @l.command(invoke_without_command=True, description='units/volume-l-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 1 / (1/202.884))

    @l.command(invoke_without_command=True, description='units/volume-l-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @l.command(invoke_without_command=True, description='units/volume-l-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-3)

    @l.command(invoke_without_command=True, description='units/volume-l-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 1 / 4.546)

    @l.command(invoke_without_command=True, description='units/volume-l-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 1 / 1.3652)

    @l.command(invoke_without_command=True, description='units/volume-l-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.76))

    @l.command(invoke_without_command=True, description='units/volume-l-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3.52))

    @l.command(invoke_without_command=True, description='units/volume-l-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 1 / (1/35.195))

    @l.command(invoke_without_command=True, description='units/volume-l-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 1 / (1/56.312))

    @l.command(invoke_without_command=True, description='units/volume-l-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 1 / (1/168.936))

    @l.command(invoke_without_command=True, description='units/volume-l-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 1 / (1/28.317))

    @l.command(invoke_without_command=True, description='units/volume-l-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 1 / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-ml-desc')
    async def ml(ctx):
        pass


    @ml.command(invoke_without_command=True, description='units/volume-ml-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3.78541)

    @ml.command(invoke_without_command=True, description='units/volume-ml-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/1.057))

    @ml.command(invoke_without_command=True, description='units/volume-ml-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/4.167))

    @ml.command(invoke_without_command=True, description='units/volume-ml-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/4.167))

    @ml.command(invoke_without_command=True, description='units/volume-ml-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/33.814))

    @ml.command(invoke_without_command=True, description='units/volume-ml-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/67.628))

    @ml.command(invoke_without_command=True, description='units/volume-ml-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/202.884))

    @ml.command(invoke_without_command=True, description='units/volume-ml-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e3)

    @ml.command(invoke_without_command=True, description='units/volume-ml-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1)

    @ml.command(invoke_without_command=True, description='units/volume-ml-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 4.546)

    @ml.command(invoke_without_command=True, description='units/volume-ml-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1.3652)

    @ml.command(invoke_without_command=True, description='units/volume-ml-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/1.76))

    @ml.command(invoke_without_command=True, description='units/volume-ml-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/3.52))

    @ml.command(invoke_without_command=True, description='units/volume-ml-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/35.195))

    @ml.command(invoke_without_command=True, description='units/volume-ml-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/56.312))

    @ml.command(invoke_without_command=True, description='units/volume-ml-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/168.936))

    @ml.command(invoke_without_command=True, description='units/volume-ml-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/28.317))

    @ml.command(invoke_without_command=True, description='units/volume-ml-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-gallon-desc')
    async def gallon(ctx):
        pass


    @gallon.command(invoke_without_command=True, description='units/volume-gallon-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 4.546 / 3.78541)

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/1.057))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/4.167))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/4.167))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/33.814))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/67.628))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/202.884))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 4.546 / 1e3)

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * 4.546 / 1)

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * 4.546 / 1e-3)

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 4.546 / 1.3652)

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/1.76))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/3.52))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/35.195))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/56.312))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/168.936))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/28.317))

    @gallon.command(invoke_without_command=True, description='units/volume-gallon-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-quart-desc')
    async def quart(ctx):
        pass


    @quart.command(invoke_without_command=True, description='units/volume-quart-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 3.78541)

    @quart.command(invoke_without_command=True, description='units/volume-quart-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/1.057))

    @quart.command(invoke_without_command=True, description='units/volume-quart-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/4.167))

    @quart.command(invoke_without_command=True, description='units/volume-quart-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/4.167))

    @quart.command(invoke_without_command=True, description='units/volume-quart-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/33.814))

    @quart.command(invoke_without_command=True, description='units/volume-quart-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/67.628))

    @quart.command(invoke_without_command=True, description='units/volume-quart-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/202.884))

    @quart.command(invoke_without_command=True, description='units/volume-quart-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 1e3)

    @quart.command(invoke_without_command=True, description='units/volume-quart-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 1)

    @quart.command(invoke_without_command=True, description='units/volume-quart-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 1e-3)

    @quart.command(invoke_without_command=True, description='units/volume-quart-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 4.546)

    @quart.command(invoke_without_command=True, description='units/volume-quart-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/1.76))

    @quart.command(invoke_without_command=True, description='units/volume-quart-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/3.52))

    @quart.command(invoke_without_command=True, description='units/volume-quart-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/35.195))

    @quart.command(invoke_without_command=True, description='units/volume-quart-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/56.312))

    @quart.command(invoke_without_command=True, description='units/volume-quart-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/168.936))

    @quart.command(invoke_without_command=True, description='units/volume-quart-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/28.317))

    @quart.command(invoke_without_command=True, description='units/volume-quart-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-pint-desc')
    async def pint(ctx):
        pass


    @pint.command(invoke_without_command=True, description='units/volume-pint-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 3.78541)

    @pint.command(invoke_without_command=True, description='units/volume-pint-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/1.057))

    @pint.command(invoke_without_command=True, description='units/volume-pint-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/4.167))

    @pint.command(invoke_without_command=True, description='units/volume-pint-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/4.167))

    @pint.command(invoke_without_command=True, description='units/volume-pint-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/33.814))

    @pint.command(invoke_without_command=True, description='units/volume-pint-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/67.628))

    @pint.command(invoke_without_command=True, description='units/volume-pint-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/202.884))

    @pint.command(invoke_without_command=True, description='units/volume-pint-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 1e3)

    @pint.command(invoke_without_command=True, description='units/volume-pint-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 1)

    @pint.command(invoke_without_command=True, description='units/volume-pint-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 1e-3)

    @pint.command(invoke_without_command=True, description='units/volume-pint-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 4.546)

    @pint.command(invoke_without_command=True, description='units/volume-pint-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 1.3652)

    @pint.command(invoke_without_command=True, description='units/volume-pint-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/3.52))

    @pint.command(invoke_without_command=True, description='units/volume-pint-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/35.195))

    @pint.command(invoke_without_command=True, description='units/volume-pint-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/56.312))

    @pint.command(invoke_without_command=True, description='units/volume-pint-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/168.936))

    @pint.command(invoke_without_command=True, description='units/volume-pint-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/28.317))

    @pint.command(invoke_without_command=True, description='units/volume-pint-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-cup-desc')
    async def cup(ctx):
        pass


    @cup.command(invoke_without_command=True, description='units/volume-cup-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 3.78541)

    @cup.command(invoke_without_command=True, description='units/volume-cup-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/1.057))

    @cup.command(invoke_without_command=True, description='units/volume-cup-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/4.167))

    @cup.command(invoke_without_command=True, description='units/volume-cup-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/4.167))

    @cup.command(invoke_without_command=True, description='units/volume-cup-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/33.814))

    @cup.command(invoke_without_command=True, description='units/volume-cup-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/67.628))

    @cup.command(invoke_without_command=True, description='units/volume-cup-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/202.884))

    @cup.command(invoke_without_command=True, description='units/volume-cup-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 1e3)

    @cup.command(invoke_without_command=True, description='units/volume-cup-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 1)

    @cup.command(invoke_without_command=True, description='units/volume-cup-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 1e-3)

    @cup.command(invoke_without_command=True, description='units/volume-cup-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 4.546)

    @cup.command(invoke_without_command=True, description='units/volume-cup-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 1.3652)

    @cup.command(invoke_without_command=True, description='units/volume-cup-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/1.76))

    @cup.command(invoke_without_command=True, description='units/volume-cup-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/35.195))

    @cup.command(invoke_without_command=True, description='units/volume-cup-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/56.312))

    @cup.command(invoke_without_command=True, description='units/volume-cup-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/168.936))

    @cup.command(invoke_without_command=True, description='units/volume-cup-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/28.317))

    @cup.command(invoke_without_command=True, description='units/volume-cup-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-floz-desc')
    async def floz(ctx):
        pass


    @floz.command(invoke_without_command=True, description='units/volume-floz-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 3.78541)

    @floz.command(invoke_without_command=True, description='units/volume-floz-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/1.057))

    @floz.command(invoke_without_command=True, description='units/volume-floz-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/4.167))

    @floz.command(invoke_without_command=True, description='units/volume-floz-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/4.167))

    @floz.command(invoke_without_command=True, description='units/volume-floz-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/33.814))

    @floz.command(invoke_without_command=True, description='units/volume-floz-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/67.628))

    @floz.command(invoke_without_command=True, description='units/volume-floz-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/202.884))

    @floz.command(invoke_without_command=True, description='units/volume-floz-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 1e3)

    @floz.command(invoke_without_command=True, description='units/volume-floz-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 1)

    @floz.command(invoke_without_command=True, description='units/volume-floz-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 1e-3)

    @floz.command(invoke_without_command=True, description='units/volume-floz-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 4.546)

    @floz.command(invoke_without_command=True, description='units/volume-floz-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 1.3652)

    @floz.command(invoke_without_command=True, description='units/volume-floz-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/1.76))

    @floz.command(invoke_without_command=True, description='units/volume-floz-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/3.52))

    @floz.command(invoke_without_command=True, description='units/volume-floz-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/56.312))

    @floz.command(invoke_without_command=True, description='units/volume-floz-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/168.936))

    @floz.command(invoke_without_command=True, description='units/volume-floz-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/28.317))

    @floz.command(invoke_without_command=True, description='units/volume-floz-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-tbsp-desc')
    async def tbsp(ctx):
        pass


    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 3.78541)

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/1.057))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/4.167))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/4.167))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/33.814))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/67.628))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/202.884))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 1e3)

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 1)

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 1e-3)

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 4.546)

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 1.3652)

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/1.76))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/3.52))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/35.195))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/168.936))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/28.317))

    @tbsp.command(invoke_without_command=True, description='units/volume-tbsp-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-tsp-desc')
    async def tsp(ctx):
        pass


    @tsp.command(invoke_without_command=True, description='units/volume-tsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 3.78541)

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/1.057))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/4.167))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/4.167))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/33.814))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/67.628))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/202.884))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 1e3)

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 1)

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 1e-3)

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 4.546)

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 1.3652)

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/1.76))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/3.52))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/35.195))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/56.312))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/28.317))

    @tsp.command(invoke_without_command=True, description='units/volume-tsp-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-ft3-desc')
    async def ft3(ctx):
        pass


    @ft3.command(invoke_without_command=True, description='units/volume-ft3-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 3.78541)

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/1.057))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/4.167))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/4.167))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/33.814))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/67.628))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/202.884))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 1e3)

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 1)

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 1e-3)

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 4.546)

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 1.3652)

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/1.76))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/3.52))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/35.195))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/56.312))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/168.936))

    @ft3.command(invoke_without_command=True, description='units/volume-ft3-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/61.024))

    @volume.group(invoke_without_command=True, description='units/volume-in3-desc')
    async def in3(ctx):
        pass


    @in3.command(invoke_without_command=True, description='units/volume-in3-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 3.78541)

    @in3.command(invoke_without_command=True, description='units/volume-in3-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/1.057))

    @in3.command(invoke_without_command=True, description='units/volume-in3-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/4.167))

    @in3.command(invoke_without_command=True, description='units/volume-in3-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/4.167))

    @in3.command(invoke_without_command=True, description='units/volume-in3-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/33.814))

    @in3.command(invoke_without_command=True, description='units/volume-in3-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/67.628))

    @in3.command(invoke_without_command=True, description='units/volume-in3-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/202.884))

    @in3.command(invoke_without_command=True, description='units/volume-in3-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 1e3)

    @in3.command(invoke_without_command=True, description='units/volume-in3-l-desc')
    async def l(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 1)

    @in3.command(invoke_without_command=True, description='units/volume-in3-ml-desc')
    async def ml(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 1e-3)

    @in3.command(invoke_without_command=True, description='units/volume-in3-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 4.546)

    @in3.command(invoke_without_command=True, description='units/volume-in3-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 1.3652)

    @in3.command(invoke_without_command=True, description='units/volume-in3-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/1.76))

    @in3.command(invoke_without_command=True, description='units/volume-in3-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/3.52))

    @in3.command(invoke_without_command=True, description='units/volume-in3-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/35.195))

    @in3.command(invoke_without_command=True, description='units/volume-in3-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/56.312))

    @in3.command(invoke_without_command=True, description='units/volume-in3-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/168.936))

    @in3.command(invoke_without_command=True, description='units/volume-in3-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/28.317))
