from math import pi
from discord.ext.commands import group, Cog
from .utils import lone_group

class Units(Cog):
    """units/cog-desc"""

    @group(invoke_without_command=True, description='units/convert-desc')
    @lone_group(True)
    async def convert(self, ctx):
        pass


    @convert.group(aliases=[], invoke_without_command=True, description='units/area-desc')
    @lone_group(True)
    async def area(self, ctx):
        pass


    @area.group(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqkm-desc')
    @lone_group(True)
    async def sqkm(ctx):
        pass


    @sqkm.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqkm-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @sqkm.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqkm-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * 1e6 / 2.59e6)

    @sqkm.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqkm-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1/1.196))

    @sqkm.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqkm-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1/10.764))

    @sqkm.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqkm-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1/1550.003))

    @sqkm.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqkm-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * 1e6 / 10000)

    @sqkm.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqkm-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * 1e6 / 4046.856)

    @area.group(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqm-desc')
    @lone_group(True)
    async def sqm(ctx):
        pass


    @sqm.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqm-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @sqm.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqm-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * 1 / 2.59e6)

    @sqm.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqm-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.196))

    @sqm.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqm-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 1 / (1/10.764))

    @sqm.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqm-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1550.003))

    @sqm.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqm-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * 1 / 10000)

    @sqm.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqm-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * 1 / 4046.856)

    @area.group(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqmil-desc')
    @lone_group(True)
    async def sqmil(ctx):
        pass


    @sqmil.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqmil-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / 1e6)

    @sqmil.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqmil-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / 1)

    @sqmil.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqmil-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / (1/1.196))

    @sqmil.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqmil-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / (1/10.764))

    @sqmil.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqmil-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / (1/1550.003))

    @sqmil.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqmil-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / 10000)

    @sqmil.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqmil-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * 2.59e6 / 4046.856)

    @area.group(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqyard-desc')
    @lone_group(True)
    async def sqyard(ctx):
        pass


    @sqyard.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqyard-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 1e6)

    @sqyard.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqyard-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 1)

    @sqyard.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqyard-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 2.59e6)

    @sqyard.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqyard-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / (1/10.764))

    @sqyard.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqyard-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / (1/1550.003))

    @sqyard.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqyard-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 10000)

    @sqyard.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqyard-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * (1/1.196) / 4046.856)

    @area.group(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqft-desc')
    @lone_group(True)
    async def sqft(ctx):
        pass


    @sqft.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqft-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 1e6)

    @sqft.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqft-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 1)

    @sqft.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqft-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 2.59e6)

    @sqft.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqft-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / (1/1.196))

    @sqft.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqft-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / (1/1550.003))

    @sqft.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqft-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 10000)

    @sqft.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqft-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * (1/10.764) / 4046.856)

    @area.group(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqin-desc')
    @lone_group(True)
    async def sqin(ctx):
        pass


    @sqin.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqin-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 1e6)

    @sqin.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqin-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 1)

    @sqin.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqin-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 2.59e6)

    @sqin.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqin-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / (1/1.196))

    @sqin.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqin-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / (1/10.764))

    @sqin.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqin-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 10000)

    @sqin.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqin-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * (1/1550.003) / 4046.856)

    @area.group(aliases=['hectares'], invoke_without_command=True, description='units/area-hectare-desc')
    @lone_group(True)
    async def hectare(ctx):
        pass


    @hectare.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-hectare-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * 10000 / 1e6)

    @hectare.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-hectare-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * 10000 / 1)

    @hectare.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-hectare-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * 10000 / 2.59e6)

    @hectare.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-hectare-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 10000 / (1/1.196))

    @hectare.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-hectare-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 10000 / (1/10.764))

    @hectare.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-hectare-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 10000 / (1/1550.003))

    @hectare.command(aliases=['acres'], invoke_without_command=True, description='units/area-hectare-acre-desc')
    async def acre(ctx, amount: float):
        await ctx.send(amount * 10000 / 4046.856)

    @area.group(aliases=['acres'], invoke_without_command=True, description='units/area-acre-desc')
    @lone_group(True)
    async def acre(ctx):
        pass


    @acre.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-acre-sqkm-desc')
    async def sqkm(ctx, amount: float):
        await ctx.send(amount * 4046.856 / 1e6)

    @acre.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-acre-sqm-desc')
    async def sqm(ctx, amount: float):
        await ctx.send(amount * 4046.856 / 1)

    @acre.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-acre-sqmil-desc')
    async def sqmil(ctx, amount: float):
        await ctx.send(amount * 4046.856 / 2.59e6)

    @acre.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-acre-sqyard-desc')
    async def sqyard(ctx, amount: float):
        await ctx.send(amount * 4046.856 / (1/1.196))

    @acre.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-acre-sqft-desc')
    async def sqft(ctx, amount: float):
        await ctx.send(amount * 4046.856 / (1/10.764))

    @acre.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-acre-sqin-desc')
    async def sqin(ctx, amount: float):
        await ctx.send(amount * 4046.856 / (1/1550.003))

    @acre.command(aliases=['hectares'], invoke_without_command=True, description='units/area-acre-hectare-desc')
    async def hectare(ctx, amount: float):
        await ctx.send(amount * 4046.856 / 10000)


    @convert.group(aliases=[], invoke_without_command=True, description='units/data-desc')
    @lone_group(True)
    async def data(self, ctx):
        pass


    @data.group(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-bps-desc')
    @lone_group(True)
    async def bps(ctx):
        pass


    @bps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-bps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @bps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-bps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1 / 8e3)

    @bps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-bps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1 / 1024)

    @bps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-bps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @bps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-bps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1 / 8e6)

    @bps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-bps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**2))

    @bps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-bps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1 / 1e9)

    @bps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-bps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1 / 8e9)

    @bps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-bps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**3))

    @bps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-bps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1 / 1e12)

    @bps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-bps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1 / 8e12)

    @bps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-bps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**4))

    @data.group(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-kbps-desc')
    @lone_group(True)
    async def kbps(ctx):
        pass


    @kbps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-kbps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @kbps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-kbps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e3)

    @kbps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-kbps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1024)

    @kbps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-kbps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e6)

    @kbps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-kbps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e6)

    @kbps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-kbps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**2))

    @kbps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-kbps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e9)

    @kbps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-kbps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e9)

    @kbps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-kbps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**3))

    @kbps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-kbps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e12)

    @kbps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-kbps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e12)

    @kbps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-kbps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**4))

    @data.group(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-KBps-desc')
    @lone_group(True)
    async def KBps(ctx):
        pass


    @KBps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-KBps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1)

    @KBps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-KBps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e3)

    @KBps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-KBps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1024)

    @KBps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-KBps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e6)

    @KBps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-KBps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e6)

    @KBps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-KBps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**2))

    @KBps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-KBps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e9)

    @KBps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-KBps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e9)

    @KBps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-KBps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**3))

    @KBps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-KBps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e12)

    @KBps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-KBps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e12)

    @KBps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-KBps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**4))

    @data.group(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-kibps-desc')
    @lone_group(True)
    async def kibps(ctx):
        pass


    @kibps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-kibps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1)

    @kibps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-kibps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e3)

    @kibps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-kibps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e3)

    @kibps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-kibps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e6)

    @kibps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-kibps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e6)

    @kibps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-kibps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**2))

    @kibps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-kibps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e9)

    @kibps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-kibps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e9)

    @kibps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-kibps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**3))

    @kibps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-kibps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e12)

    @kibps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-kibps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e12)

    @kibps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-kibps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**4))

    @data.group(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-mbps-desc')
    @lone_group(True)
    async def mbps(ctx):
        pass


    @mbps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-mbps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @mbps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-mbps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e3)

    @mbps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-mbps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e3)

    @mbps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-mbps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1024)

    @mbps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-mbps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e6)

    @mbps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-mbps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**2))

    @mbps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-mbps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e9)

    @mbps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-mbps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e9)

    @mbps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-mbps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**3))

    @mbps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-mbps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e12)

    @mbps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-mbps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e12)

    @mbps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-mbps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**4))

    @data.group(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-MBps-desc')
    @lone_group(True)
    async def MBps(ctx):
        pass


    @MBps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-MBps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1)

    @MBps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-MBps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e3)

    @MBps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-MBps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e3)

    @MBps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-MBps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1024)

    @MBps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-MBps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e6)

    @MBps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-MBps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**2))

    @MBps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-MBps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e9)

    @MBps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-MBps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e9)

    @MBps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-MBps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**3))

    @MBps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-MBps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e12)

    @MBps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-MBps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e12)

    @MBps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-MBps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**4))

    @data.group(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-mibps-desc')
    @lone_group(True)
    async def mibps(ctx):
        pass


    @mibps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-mibps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1)

    @mibps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-mibps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e3)

    @mibps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-mibps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e3)

    @mibps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-mibps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1024)

    @mibps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-mibps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e6)

    @mibps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-mibps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e6)

    @mibps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-mibps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e9)

    @mibps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-mibps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e9)

    @mibps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-mibps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**3))

    @mibps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-mibps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e12)

    @mibps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-mibps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e12)

    @mibps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-mibps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**4))

    @data.group(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-gbps-desc')
    @lone_group(True)
    async def gbps(ctx):
        pass


    @gbps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-gbps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1)

    @gbps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-gbps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e3)

    @gbps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-gbps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e3)

    @gbps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-gbps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1024)

    @gbps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-gbps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e6)

    @gbps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-gbps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e6)

    @gbps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-gbps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**2))

    @gbps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-gbps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e9)

    @gbps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-gbps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**3))

    @gbps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-gbps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e12)

    @gbps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-gbps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e12)

    @gbps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-gbps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**4))

    @data.group(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-GBps-desc')
    @lone_group(True)
    async def GBps(ctx):
        pass


    @GBps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-GBps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1)

    @GBps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-GBps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e3)

    @GBps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-GBps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e3)

    @GBps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-GBps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1024)

    @GBps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-GBps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e6)

    @GBps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-GBps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e6)

    @GBps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-GBps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**2))

    @GBps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-GBps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e9)

    @GBps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-GBps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**3))

    @GBps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-GBps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e12)

    @GBps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-GBps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e12)

    @GBps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-GBps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**4))

    @data.group(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-gibps-desc')
    @lone_group(True)
    async def gibps(ctx):
        pass


    @gibps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-gibps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1)

    @gibps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-gibps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e3)

    @gibps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-gibps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e3)

    @gibps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-gibps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1024)

    @gibps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-gibps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e6)

    @gibps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-gibps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e6)

    @gibps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-gibps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**2))

    @gibps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-gibps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e9)

    @gibps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-gibps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e9)

    @gibps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-gibps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e12)

    @gibps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-gibps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e12)

    @gibps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-gibps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**4))

    @data.group(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-tbps-desc')
    @lone_group(True)
    async def tbps(ctx):
        pass


    @tbps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-tbps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1)

    @tbps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-tbps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e3)

    @tbps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-tbps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e3)

    @tbps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-tbps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1024)

    @tbps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-tbps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e6)

    @tbps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-tbps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e6)

    @tbps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-tbps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**2))

    @tbps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-tbps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e9)

    @tbps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-tbps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e9)

    @tbps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-tbps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**3))

    @tbps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-tbps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e12)

    @tbps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-tbps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**4))

    @data.group(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-TBps-desc')
    @lone_group(True)
    async def TBps(ctx):
        pass


    @TBps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-TBps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1)

    @TBps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-TBps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e3)

    @TBps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-TBps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e3)

    @TBps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-TBps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1024)

    @TBps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-TBps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e6)

    @TBps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-TBps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e6)

    @TBps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-TBps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**2))

    @TBps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-TBps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e9)

    @TBps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-TBps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e9)

    @TBps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-TBps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**3))

    @TBps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-TBps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e12)

    @TBps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-TBps-tibps-desc')
    async def tibps(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**4))

    @data.group(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-tibps-desc')
    @lone_group(True)
    async def tibps(ctx):
        pass


    @tibps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-tibps-bps-desc')
    async def bps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1)

    @tibps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-tibps-kbps-desc')
    async def kbps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e3)

    @tibps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-tibps-KBps-desc')
    async def KBps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e3)

    @tibps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-tibps-kibps-desc')
    async def kibps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1024)

    @tibps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-tibps-mbps-desc')
    async def mbps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e6)

    @tibps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-tibps-MBps-desc')
    async def MBps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e6)

    @tibps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-tibps-mibps-desc')
    async def mibps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**2))

    @tibps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-tibps-gbps-desc')
    async def gbps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e9)

    @tibps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-tibps-GBps-desc')
    async def GBps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e9)

    @tibps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-tibps-gibps-desc')
    async def gibps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**3))

    @tibps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-tibps-tbps-desc')
    async def tbps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e12)

    @tibps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-tibps-TBps-desc')
    async def TBps(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e12)


    @convert.group(aliases=[], invoke_without_command=True, description='units/storage-desc')
    @lone_group(True)
    async def storage(self, ctx):
        pass


    @storage.group(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-b-desc')
    @lone_group(True)
    async def b(ctx):
        pass


    @b.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-b-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @b.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-b-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1 / 1024)

    @b.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-b-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @b.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-b-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**2))

    @b.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-b-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e9)

    @b.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-b-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**3))

    @b.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-b-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e12)

    @b.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-b-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**4))

    @b.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-b-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1 / 1e15)

    @b.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-b-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1 / (1024**5))

    @b.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-b-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1 / 8)

    @b.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-b-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e3)

    @b.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-b-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024))

    @b.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-b-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e6)

    @b.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-b-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024 ** 2))

    @b.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-b-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e9)

    @b.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-b-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024 ** 3))

    @b.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-b-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e12)

    @b.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-b-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024 ** 4))

    @b.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-b-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1 / 8e15)

    @b.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-b-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1 / (8 * 1024 ** 5))

    @storage.group(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-kb-desc')
    @lone_group(True)
    async def kb(ctx):
        pass


    @kb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-kb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @kb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-kb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1024)

    @kb.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-kb-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e6)

    @kb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-kb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**2))

    @kb.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-kb-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e9)

    @kb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-kb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**3))

    @kb.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-kb-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e12)

    @kb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-kb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**4))

    @kb.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-kb-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e15)

    @kb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-kb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1024**5))

    @kb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-kb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8)

    @kb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-kb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e3)

    @kb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-kb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024))

    @kb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-kb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e6)

    @kb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-kb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024 ** 2))

    @kb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-kb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e9)

    @kb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-kb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024 ** 3))

    @kb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-kb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e12)

    @kb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-kb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024 ** 4))

    @kb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-kb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e3 / 8e15)

    @kb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-kb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e3 / (8 * 1024 ** 5))

    @storage.group(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-kib-desc')
    @lone_group(True)
    async def kib(ctx):
        pass


    @kib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-kib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1024 / 1)

    @kib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-kib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e3)

    @kib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-kib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e6)

    @kib.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-kib-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**2))

    @kib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-kib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e9)

    @kib.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-kib-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**3))

    @kib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-kib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e12)

    @kib.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-kib-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**4))

    @kib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-kib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1024 / 1e15)

    @kib.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-kib-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1024 / (1024**5))

    @kib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-kib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1024 / 8)

    @kib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-kib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e3)

    @kib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-kib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024))

    @kib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-kib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e6)

    @kib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-kib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024 ** 2))

    @kib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-kib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e9)

    @kib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-kib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024 ** 3))

    @kib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-kib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e12)

    @kib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-kib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024 ** 4))

    @kib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-kib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1024 / 8e15)

    @kib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-kib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1024 / (8 * 1024 ** 5))

    @storage.group(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-mb-desc')
    @lone_group(True)
    async def mb(ctx):
        pass


    @mb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-mb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @mb.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-mb-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e3)

    @mb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-mb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1024)

    @mb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-mb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**2))

    @mb.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-mb-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e9)

    @mb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-mb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**3))

    @mb.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-mb-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e12)

    @mb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-mb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**4))

    @mb.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-mb-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e15)

    @mb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-mb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e6 / (1024**5))

    @mb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-mb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8)

    @mb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-mb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e3)

    @mb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-mb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024))

    @mb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-mb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e6)

    @mb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-mb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024 ** 2))

    @mb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-mb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e9)

    @mb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-mb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024 ** 3))

    @mb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-mb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e12)

    @mb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-mb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024 ** 4))

    @mb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-mb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e6 / 8e15)

    @mb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-mb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e6 / (8 * 1024 ** 5))

    @storage.group(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-mib-desc')
    @lone_group(True)
    async def mib(ctx):
        pass


    @mib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-mib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1)

    @mib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-mib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e3)

    @mib.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-mib-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1024)

    @mib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-mib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e6)

    @mib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-mib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e9)

    @mib.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-mib-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**3))

    @mib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-mib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e12)

    @mib.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-mib-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**4))

    @mib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-mib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 1e15)

    @mib.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-mib-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (1024**5))

    @mib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-mib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8)

    @mib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-mib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e3)

    @mib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-mib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024))

    @mib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-mib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e6)

    @mib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-mib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024 ** 2))

    @mib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-mib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e9)

    @mib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-mib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024 ** 3))

    @mib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-mib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e12)

    @mib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-mib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024 ** 4))

    @mib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-mib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / 8e15)

    @mib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-mib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (1024**2) / (8 * 1024 ** 5))

    @storage.group(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-gb-desc')
    @lone_group(True)
    async def gb(ctx):
        pass


    @gb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-gb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1)

    @gb.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-gb-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e3)

    @gb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-gb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1024)

    @gb.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-gb-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e6)

    @gb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-gb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**2))

    @gb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-gb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**3))

    @gb.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-gb-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e12)

    @gb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-gb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**4))

    @gb.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-gb-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e15)

    @gb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-gb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e9 / (1024**5))

    @gb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-gb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8)

    @gb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-gb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e3)

    @gb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-gb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024))

    @gb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-gb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e6)

    @gb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-gb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024 ** 2))

    @gb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-gb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e9)

    @gb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-gb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024 ** 3))

    @gb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-gb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e12)

    @gb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-gb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024 ** 4))

    @gb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-gb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e9 / 8e15)

    @gb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-gb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e9 / (8 * 1024 ** 5))

    @storage.group(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-gib-desc')
    @lone_group(True)
    async def gib(ctx):
        pass


    @gib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-gib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1)

    @gib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-gib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e3)

    @gib.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-gib-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1024)

    @gib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-gib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e6)

    @gib.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-gib-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**2))

    @gib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-gib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e9)

    @gib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-gib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e12)

    @gib.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-gib-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**4))

    @gib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-gib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 1e15)

    @gib.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-gib-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (1024**5))

    @gib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-gib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8)

    @gib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-gib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e3)

    @gib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-gib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024))

    @gib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-gib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e6)

    @gib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-gib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024 ** 2))

    @gib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-gib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e9)

    @gib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-gib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024 ** 3))

    @gib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-gib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e12)

    @gib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-gib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024 ** 4))

    @gib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-gib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / 8e15)

    @gib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-gib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (1024**3) / (8 * 1024 ** 5))

    @storage.group(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-tb-desc')
    @lone_group(True)
    async def tb(ctx):
        pass


    @tb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-tb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1)

    @tb.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-tb-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e3)

    @tb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-tb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1024)

    @tb.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-tb-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e6)

    @tb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-tb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**2))

    @tb.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-tb-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e9)

    @tb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-tb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**3))

    @tb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-tb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**4))

    @tb.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-tb-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 1e12 / 1e15)

    @tb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-tb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e12 / (1024**5))

    @tb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-tb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8)

    @tb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-tb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e3)

    @tb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-tb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024))

    @tb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-tb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e6)

    @tb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-tb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024 ** 2))

    @tb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-tb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e9)

    @tb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-tb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024 ** 3))

    @tb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-tb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e12)

    @tb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-tb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024 ** 4))

    @tb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-tb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e12 / 8e15)

    @tb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-tb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e12 / (8 * 1024 ** 5))

    @storage.group(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-tib-desc')
    @lone_group(True)
    async def tib(ctx):
        pass


    @tib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-tib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1)

    @tib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-tib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e3)

    @tib.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-tib-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1024)

    @tib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-tib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e6)

    @tib.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-tib-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**2))

    @tib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-tib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e9)

    @tib.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-tib-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**3))

    @tib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-tib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e12)

    @tib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-tib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 1e15)

    @tib.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-tib-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (1024**5))

    @tib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-tib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8)

    @tib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-tib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e3)

    @tib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-tib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024))

    @tib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-tib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e6)

    @tib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-tib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024 ** 2))

    @tib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-tib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e9)

    @tib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-tib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024 ** 3))

    @tib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-tib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e12)

    @tib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-tib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024 ** 4))

    @tib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-tib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / 8e15)

    @tib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-tib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (1024**4) / (8 * 1024 ** 5))

    @storage.group(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-pb-desc')
    @lone_group(True)
    async def pb(ctx):
        pass


    @pb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-pb-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1)

    @pb.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-pb-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1e3)

    @pb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-pb-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1024)

    @pb.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-pb-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1e6)

    @pb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-pb-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 1e15 / (1024**2))

    @pb.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-pb-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1e9)

    @pb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-pb-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 1e15 / (1024**3))

    @pb.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-pb-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 1e15 / 1e12)

    @pb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-pb-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 1e15 / (1024**4))

    @pb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-pb-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 1e15 / (1024**5))

    @pb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-pb-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8)

    @pb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-pb-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e3)

    @pb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-pb-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024))

    @pb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-pb-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e6)

    @pb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-pb-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024 ** 2))

    @pb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-pb-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e9)

    @pb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-pb-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024 ** 3))

    @pb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-pb-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e12)

    @pb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-pb-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024 ** 4))

    @pb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-pb-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 1e15 / 8e15)

    @pb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-pb-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 1e15 / (8 * 1024 ** 5))

    @storage.group(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-pib-desc')
    @lone_group(True)
    async def pib(ctx):
        pass


    @pib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-pib-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1)

    @pib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-pib-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e3)

    @pib.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-pib-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1024)

    @pib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-pib-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e6)

    @pib.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-pib-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (1024**2))

    @pib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-pib-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e9)

    @pib.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-pib-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (1024**3))

    @pib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-pib-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e12)

    @pib.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-pib-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (1024**4))

    @pib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-pib-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 1e15)

    @pib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-pib-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8)

    @pib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-pib-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e3)

    @pib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-pib-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024))

    @pib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-pib-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e6)

    @pib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-pib-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024 ** 2))

    @pib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-pib-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e9)

    @pib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-pib-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024 ** 3))

    @pib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-pib-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e12)

    @pib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-pib-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024 ** 4))

    @pib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-pib-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / 8e15)

    @pib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-pib-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (1024**5) / (8 * 1024 ** 5))

    @storage.group(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-B-desc')
    @lone_group(True)
    async def B(ctx):
        pass


    @B.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-B-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8 / 1)

    @B.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-B-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e3)

    @B.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-B-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8 / 1024)

    @B.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-B-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e6)

    @B.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-B-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8 / (1024**2))

    @B.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-B-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e9)

    @B.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-B-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8 / (1024**3))

    @B.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-B-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e12)

    @B.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-B-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8 / (1024**4))

    @B.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-B-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8 / 1e15)

    @B.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-B-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8 / (1024**5))

    @B.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-B-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e3)

    @B.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-B-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024))

    @B.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-B-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e6)

    @B.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-B-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024 ** 2))

    @B.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-B-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e9)

    @B.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-B-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024 ** 3))

    @B.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-B-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e12)

    @B.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-B-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024 ** 4))

    @B.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-B-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8 / 8e15)

    @B.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-B-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8 / (8 * 1024 ** 5))

    @storage.group(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-KB-desc')
    @lone_group(True)
    async def KB(ctx):
        pass


    @KB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-KB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1)

    @KB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-KB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e3)

    @KB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-KB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1024)

    @KB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-KB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e6)

    @KB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-KB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**2))

    @KB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-KB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e9)

    @KB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-KB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**3))

    @KB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-KB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e12)

    @KB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-KB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**4))

    @KB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-KB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e3 / 1e15)

    @KB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-KB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e3 / (1024**5))

    @KB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-KB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8)

    @KB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-KB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024))

    @KB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-KB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e6)

    @KB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-KB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024 ** 2))

    @KB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-KB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e9)

    @KB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-KB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024 ** 3))

    @KB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-KB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e12)

    @KB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-KB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024 ** 4))

    @KB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-KB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8e3 / 8e15)

    @KB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-KB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e3 / (8 * 1024 ** 5))

    @storage.group(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-KiB-desc')
    @lone_group(True)
    async def KiB(ctx):
        pass


    @KiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-KiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1)

    @KiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-KiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e3)

    @KiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-KiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1024)

    @KiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-KiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e6)

    @KiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-KiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (1024**2))

    @KiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-KiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e9)

    @KiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-KiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (1024**3))

    @KiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-KiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e12)

    @KiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-KiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (1024**4))

    @KiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-KiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 1e15)

    @KiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-KiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (1024**5))

    @KiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-KiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8)

    @KiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-KiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e3)

    @KiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-KiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e6)

    @KiB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-KiB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 2))

    @KiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-KiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e9)

    @KiB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-KiB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 3))

    @KiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-KiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e12)

    @KiB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-KiB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 4))

    @KiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-KiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / 8e15)

    @KiB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-KiB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 5))

    @storage.group(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-MB-desc')
    @lone_group(True)
    async def MB(ctx):
        pass


    @MB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-MB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1)

    @MB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-MB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e3)

    @MB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-MB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1024)

    @MB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-MB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e6)

    @MB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-MB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**2))

    @MB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-MB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e9)

    @MB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-MB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**3))

    @MB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-MB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e12)

    @MB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-MB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**4))

    @MB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-MB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e6 / 1e15)

    @MB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-MB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e6 / (1024**5))

    @MB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-MB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8)

    @MB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-MB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e3)

    @MB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-MB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024))

    @MB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-MB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024 ** 2))

    @MB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-MB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e9)

    @MB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-MB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024 ** 3))

    @MB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-MB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e12)

    @MB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-MB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024 ** 4))

    @MB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-MB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8e6 / 8e15)

    @MB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-MB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e6 / (8 * 1024 ** 5))

    @storage.group(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-MiB-desc')
    @lone_group(True)
    async def MiB(ctx):
        pass


    @MiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-MiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1)

    @MiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-MiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e3)

    @MiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-MiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1024)

    @MiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-MiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e6)

    @MiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-MiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (1024**2))

    @MiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-MiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e9)

    @MiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-MiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (1024**3))

    @MiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-MiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e12)

    @MiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-MiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (1024**4))

    @MiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-MiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 1e15)

    @MiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-MiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (1024**5))

    @MiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-MiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8)

    @MiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-MiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e3)

    @MiB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-MiB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024))

    @MiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-MiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e6)

    @MiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-MiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e9)

    @MiB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-MiB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024 ** 3))

    @MiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-MiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e12)

    @MiB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-MiB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024 ** 4))

    @MiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-MiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / 8e15)

    @MiB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-MiB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024 ** 5))

    @storage.group(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-GB-desc')
    @lone_group(True)
    async def GB(ctx):
        pass


    @GB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-GB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1)

    @GB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-GB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e3)

    @GB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-GB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1024)

    @GB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-GB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e6)

    @GB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-GB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**2))

    @GB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-GB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e9)

    @GB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-GB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**3))

    @GB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-GB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e12)

    @GB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-GB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**4))

    @GB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-GB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e9 / 1e15)

    @GB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-GB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e9 / (1024**5))

    @GB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-GB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8)

    @GB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-GB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e3)

    @GB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-GB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024))

    @GB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-GB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e6)

    @GB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-GB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024 ** 2))

    @GB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-GB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024 ** 3))

    @GB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-GB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e12)

    @GB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-GB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024 ** 4))

    @GB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-GB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8e9 / 8e15)

    @GB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-GB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e9 / (8 * 1024 ** 5))

    @storage.group(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-GiB-desc')
    @lone_group(True)
    async def GiB(ctx):
        pass


    @GiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-GiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1)

    @GiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-GiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e3)

    @GiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-GiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1024)

    @GiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-GiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e6)

    @GiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-GiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (1024**2))

    @GiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-GiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e9)

    @GiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-GiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (1024**3))

    @GiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-GiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e12)

    @GiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-GiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (1024**4))

    @GiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-GiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 1e15)

    @GiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-GiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (1024**5))

    @GiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-GiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8)

    @GiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-GiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e3)

    @GiB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-GiB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024))

    @GiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-GiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e6)

    @GiB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-GiB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024 ** 2))

    @GiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-GiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e9)

    @GiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-GiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e12)

    @GiB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-GiB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024 ** 4))

    @GiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-GiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / 8e15)

    @GiB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-GiB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024 ** 5))

    @storage.group(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-TB-desc')
    @lone_group(True)
    async def TB(ctx):
        pass


    @TB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-TB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1)

    @TB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-TB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e3)

    @TB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-TB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1024)

    @TB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-TB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e6)

    @TB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-TB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**2))

    @TB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-TB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e9)

    @TB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-TB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**3))

    @TB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-TB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e12)

    @TB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-TB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**4))

    @TB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-TB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e12 / 1e15)

    @TB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-TB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e12 / (1024**5))

    @TB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-TB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8)

    @TB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-TB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e3)

    @TB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-TB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024))

    @TB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-TB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e6)

    @TB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-TB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024 ** 2))

    @TB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-TB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e9)

    @TB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-TB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024 ** 3))

    @TB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-TB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024 ** 4))

    @TB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-TB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * 8e12 / 8e15)

    @TB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-TB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e12 / (8 * 1024 ** 5))

    @storage.group(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-TiB-desc')
    @lone_group(True)
    async def TiB(ctx):
        pass


    @TiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-TiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1)

    @TiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-TiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e3)

    @TiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-TiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1024)

    @TiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-TiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e6)

    @TiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-TiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (1024**2))

    @TiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-TiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e9)

    @TiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-TiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (1024**3))

    @TiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-TiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e12)

    @TiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-TiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (1024**4))

    @TiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-TiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 1e15)

    @TiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-TiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (1024**5))

    @TiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-TiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8)

    @TiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-TiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e3)

    @TiB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-TiB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024))

    @TiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-TiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e6)

    @TiB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-TiB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024 ** 2))

    @TiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-TiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e9)

    @TiB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-TiB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024 ** 3))

    @TiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-TiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e12)

    @TiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-TiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / 8e15)

    @TiB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-TiB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024 ** 5))

    @storage.group(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-PB-desc')
    @lone_group(True)
    async def PB(ctx):
        pass


    @PB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-PB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1)

    @PB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-PB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e3)

    @PB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-PB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1024)

    @PB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-PB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e6)

    @PB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-PB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * 8e15 / (1024**2))

    @PB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-PB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e9)

    @PB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-PB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * 8e15 / (1024**3))

    @PB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-PB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e12)

    @PB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-PB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * 8e15 / (1024**4))

    @PB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-PB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * 8e15 / 1e15)

    @PB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-PB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * 8e15 / (1024**5))

    @PB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-PB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8)

    @PB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-PB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8e3)

    @PB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-PB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024))

    @PB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-PB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8e6)

    @PB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-PB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024 ** 2))

    @PB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-PB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8e9)

    @PB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-PB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024 ** 3))

    @PB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-PB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * 8e15 / 8e12)

    @PB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-PB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024 ** 4))

    @PB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-PB-PiB-desc')
    async def PiB(ctx, amount: float):
        await ctx.send(amount * 8e15 / (8 * 1024 ** 5))

    @storage.group(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-PiB-desc')
    @lone_group(True)
    async def PiB(ctx):
        pass


    @PiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-PiB-b-desc')
    async def b(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1)

    @PiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-PiB-kb-desc')
    async def kb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e3)

    @PiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-PiB-kib-desc')
    async def kib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1024)

    @PiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-PiB-mb-desc')
    async def mb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e6)

    @PiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-PiB-mib-desc')
    async def mib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (1024**2))

    @PiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-PiB-gb-desc')
    async def gb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e9)

    @PiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-PiB-gib-desc')
    async def gib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (1024**3))

    @PiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-PiB-tb-desc')
    async def tb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e12)

    @PiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-PiB-tib-desc')
    async def tib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (1024**4))

    @PiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-PiB-pb-desc')
    async def pb(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 1e15)

    @PiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-PiB-pib-desc')
    async def pib(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (1024**5))

    @PiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-PiB-B-desc')
    async def B(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8)

    @PiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-PiB-KB-desc')
    async def KB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e3)

    @PiB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-PiB-KiB-desc')
    async def KiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024))

    @PiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-PiB-MB-desc')
    async def MB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e6)

    @PiB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-PiB-MiB-desc')
    async def MiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024 ** 2))

    @PiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-PiB-GB-desc')
    async def GB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e9)

    @PiB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-PiB-GiB-desc')
    async def GiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024 ** 3))

    @PiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-PiB-TB-desc')
    async def TB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e12)

    @PiB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-PiB-TiB-desc')
    async def TiB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024 ** 4))

    @PiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-PiB-PB-desc')
    async def PB(ctx, amount: float):
        await ctx.send(amount * (8 * 1024 ** 5) / 8e15)


    @convert.group(aliases=[], invoke_without_command=True, description='units/energy-desc')
    @lone_group(True)
    async def energy(self, ctx):
        pass


    @energy.group(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-J-desc')
    @lone_group(True)
    async def J(ctx):
        pass


    @J.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-J-kJ-desc')
    async def kJ(ctx, amount: float):
        await ctx.send(amount * 1 / 1000)

    @J.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-J-cal-desc')
    async def cal(ctx, amount: float):
        await ctx.send(amount * 1 / 4.184)

    @J.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-J-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1 / 4184)

    @J.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-J-Wh-desc')
    async def Wh(ctx, amount: float):
        await ctx.send(amount * 1 / 3600)

    @J.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-J-kWh-desc')
    async def kWh(ctx, amount: float):
        await ctx.send(amount * 1 / 3.6e6)

    @J.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-J-eV-desc')
    async def eV(ctx, amount: float):
        await ctx.send(amount * 1 / (1/6.242e18))

    @J.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-J-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 1 / 1055.06)

    @J.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-J-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 1 / 1.05506e8)

    @J.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-J-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 1 / 1.35582)

    @energy.group(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-kJ-desc')
    @lone_group(True)
    async def kJ(ctx):
        pass


    @kJ.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-kJ-J-desc')
    async def J(ctx, amount: float):
        await ctx.send(amount * 1000 / 1)

    @kJ.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-kJ-cal-desc')
    async def cal(ctx, amount: float):
        await ctx.send(amount * 1000 / 4.184)

    @kJ.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-kJ-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1000 / 4184)

    @kJ.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-kJ-Wh-desc')
    async def Wh(ctx, amount: float):
        await ctx.send(amount * 1000 / 3600)

    @kJ.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-kJ-kWh-desc')
    async def kWh(ctx, amount: float):
        await ctx.send(amount * 1000 / 3.6e6)

    @kJ.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-kJ-eV-desc')
    async def eV(ctx, amount: float):
        await ctx.send(amount * 1000 / (1/6.242e18))

    @kJ.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-kJ-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 1000 / 1055.06)

    @kJ.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-kJ-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 1000 / 1.05506e8)

    @kJ.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-kJ-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 1000 / 1.35582)

    @energy.group(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-cal-desc')
    @lone_group(True)
    async def cal(ctx):
        pass


    @cal.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-cal-J-desc')
    async def J(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1)

    @cal.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-cal-kJ-desc')
    async def kJ(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1000)

    @cal.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-cal-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 4.184 / 4184)

    @cal.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-cal-Wh-desc')
    async def Wh(ctx, amount: float):
        await ctx.send(amount * 4.184 / 3600)

    @cal.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-cal-kWh-desc')
    async def kWh(ctx, amount: float):
        await ctx.send(amount * 4.184 / 3.6e6)

    @cal.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-cal-eV-desc')
    async def eV(ctx, amount: float):
        await ctx.send(amount * 4.184 / (1/6.242e18))

    @cal.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-cal-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1055.06)

    @cal.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-cal-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1.05506e8)

    @cal.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-cal-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 4.184 / 1.35582)

    @energy.group(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-kcal-desc')
    @lone_group(True)
    async def kcal(ctx):
        pass


    @kcal.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-kcal-J-desc')
    async def J(ctx, amount: float):
        await ctx.send(amount * 4184 / 1)

    @kcal.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-kcal-kJ-desc')
    async def kJ(ctx, amount: float):
        await ctx.send(amount * 4184 / 1000)

    @kcal.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-kcal-cal-desc')
    async def cal(ctx, amount: float):
        await ctx.send(amount * 4184 / 4.184)

    @kcal.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-kcal-Wh-desc')
    async def Wh(ctx, amount: float):
        await ctx.send(amount * 4184 / 3600)

    @kcal.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-kcal-kWh-desc')
    async def kWh(ctx, amount: float):
        await ctx.send(amount * 4184 / 3.6e6)

    @kcal.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-kcal-eV-desc')
    async def eV(ctx, amount: float):
        await ctx.send(amount * 4184 / (1/6.242e18))

    @kcal.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-kcal-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 4184 / 1055.06)

    @kcal.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-kcal-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 4184 / 1.05506e8)

    @kcal.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-kcal-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 4184 / 1.35582)

    @energy.group(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-Wh-desc')
    @lone_group(True)
    async def Wh(ctx):
        pass


    @Wh.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-Wh-J-desc')
    async def J(ctx, amount: float):
        await ctx.send(amount * 3600 / 1)

    @Wh.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-Wh-kJ-desc')
    async def kJ(ctx, amount: float):
        await ctx.send(amount * 3600 / 1000)

    @Wh.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-Wh-cal-desc')
    async def cal(ctx, amount: float):
        await ctx.send(amount * 3600 / 4.184)

    @Wh.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-Wh-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 3600 / 4184)

    @Wh.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-Wh-kWh-desc')
    async def kWh(ctx, amount: float):
        await ctx.send(amount * 3600 / 3.6e6)

    @Wh.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-Wh-eV-desc')
    async def eV(ctx, amount: float):
        await ctx.send(amount * 3600 / (1/6.242e18))

    @Wh.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-Wh-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 3600 / 1055.06)

    @Wh.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-Wh-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 3600 / 1.05506e8)

    @Wh.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-Wh-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 3600 / 1.35582)

    @energy.group(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-kWh-desc')
    @lone_group(True)
    async def kWh(ctx):
        pass


    @kWh.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-kWh-J-desc')
    async def J(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1)

    @kWh.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-kWh-kJ-desc')
    async def kJ(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1000)

    @kWh.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-kWh-cal-desc')
    async def cal(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 4.184)

    @kWh.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-kWh-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 4184)

    @kWh.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-kWh-Wh-desc')
    async def Wh(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 3600)

    @kWh.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-kWh-eV-desc')
    async def eV(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / (1/6.242e18))

    @kWh.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-kWh-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1055.06)

    @kWh.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-kWh-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1.05506e8)

    @kWh.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-kWh-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 3.6e6 / 1.35582)

    @energy.group(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-eV-desc')
    @lone_group(True)
    async def eV(ctx):
        pass


    @eV.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-eV-J-desc')
    async def J(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1)

    @eV.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-eV-kJ-desc')
    async def kJ(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1000)

    @eV.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-eV-cal-desc')
    async def cal(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 4.184)

    @eV.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-eV-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 4184)

    @eV.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-eV-Wh-desc')
    async def Wh(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 3600)

    @eV.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-eV-kWh-desc')
    async def kWh(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 3.6e6)

    @eV.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-eV-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1055.06)

    @eV.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-eV-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1.05506e8)

    @eV.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-eV-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * (1/6.242e18) / 1.35582)

    @energy.group(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-btu-desc')
    @lone_group(True)
    async def btu(ctx):
        pass


    @btu.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-btu-J-desc')
    async def J(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 1)

    @btu.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-btu-kJ-desc')
    async def kJ(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 1000)

    @btu.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-btu-cal-desc')
    async def cal(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 4.184)

    @btu.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-btu-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 4184)

    @btu.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-btu-Wh-desc')
    async def Wh(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 3600)

    @btu.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-btu-kWh-desc')
    async def kWh(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 3.6e6)

    @btu.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-btu-eV-desc')
    async def eV(ctx, amount: float):
        await ctx.send(amount * 1055.06 / (1/6.242e18))

    @btu.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-btu-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 1.05506e8)

    @btu.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-btu-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 1055.06 / 1.35582)

    @energy.group(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-ust-desc')
    @lone_group(True)
    async def ust(ctx):
        pass


    @ust.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-ust-J-desc')
    async def J(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 1)

    @ust.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-ust-kJ-desc')
    async def kJ(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 1000)

    @ust.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-ust-cal-desc')
    async def cal(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 4.184)

    @ust.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-ust-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 4184)

    @ust.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-ust-Wh-desc')
    async def Wh(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 3600)

    @ust.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-ust-kWh-desc')
    async def kWh(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 3.6e6)

    @ust.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-ust-eV-desc')
    async def eV(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / (1/6.242e18))

    @ust.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-ust-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 1055.06)

    @ust.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-ust-ftlb-desc')
    async def ftlb(ctx, amount: float):
        await ctx.send(amount * 1.05506e8 / 1.35582)

    @energy.group(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-ftlb-desc')
    @lone_group(True)
    async def ftlb(ctx):
        pass


    @ftlb.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-ftlb-J-desc')
    async def J(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 1)

    @ftlb.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-ftlb-kJ-desc')
    async def kJ(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 1000)

    @ftlb.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-ftlb-cal-desc')
    async def cal(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 4.184)

    @ftlb.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-ftlb-kcal-desc')
    async def kcal(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 4184)

    @ftlb.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-ftlb-Wh-desc')
    async def Wh(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 3600)

    @ftlb.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-ftlb-kWh-desc')
    async def kWh(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 3.6e6)

    @ftlb.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-ftlb-eV-desc')
    async def eV(ctx, amount: float):
        await ctx.send(amount * 1.35582 / (1/6.242e18))

    @ftlb.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-ftlb-btu-desc')
    async def btu(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 1055.06)

    @ftlb.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-ftlb-ust-desc')
    async def ust(ctx, amount: float):
        await ctx.send(amount * 1.35582 / 1.05506e8)


    @convert.group(aliases=['freq'], invoke_without_command=True, description='units/frequency-desc')
    @lone_group(True)
    async def frequency(self, ctx):
        pass


    @frequency.group(aliases=['hertz'], invoke_without_command=True, description='units/frequency-Hz-desc')
    @lone_group(True)
    async def Hz(ctx):
        pass


    @Hz.command(aliases=['kilohertz'], invoke_without_command=True, description='units/frequency-Hz-kHz-desc')
    async def kHz(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @Hz.command(aliases=['megahertz'], invoke_without_command=True, description='units/frequency-Hz-mHz-desc')
    async def mHz(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @Hz.command(aliases=['gigahertz'], invoke_without_command=True, description='units/frequency-Hz-gHz-desc')
    async def gHz(ctx, amount: float):
        await ctx.send(amount * 1 / 1e9)

    @frequency.group(aliases=['kilohertz'], invoke_without_command=True, description='units/frequency-kHz-desc')
    @lone_group(True)
    async def kHz(ctx):
        pass


    @kHz.command(aliases=['hertz'], invoke_without_command=True, description='units/frequency-kHz-Hz-desc')
    async def Hz(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @kHz.command(aliases=['megahertz'], invoke_without_command=True, description='units/frequency-kHz-mHz-desc')
    async def mHz(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e6)

    @kHz.command(aliases=['gigahertz'], invoke_without_command=True, description='units/frequency-kHz-gHz-desc')
    async def gHz(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e9)

    @frequency.group(aliases=['megahertz'], invoke_without_command=True, description='units/frequency-mHz-desc')
    @lone_group(True)
    async def mHz(ctx):
        pass


    @mHz.command(aliases=['hertz'], invoke_without_command=True, description='units/frequency-mHz-Hz-desc')
    async def Hz(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @mHz.command(aliases=['kilohertz'], invoke_without_command=True, description='units/frequency-mHz-kHz-desc')
    async def kHz(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e3)

    @mHz.command(aliases=['gigahertz'], invoke_without_command=True, description='units/frequency-mHz-gHz-desc')
    async def gHz(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e9)

    @frequency.group(aliases=['gigahertz'], invoke_without_command=True, description='units/frequency-gHz-desc')
    @lone_group(True)
    async def gHz(ctx):
        pass


    @gHz.command(aliases=['hertz'], invoke_without_command=True, description='units/frequency-gHz-Hz-desc')
    async def Hz(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1)

    @gHz.command(aliases=['kilohertz'], invoke_without_command=True, description='units/frequency-gHz-kHz-desc')
    async def kHz(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e3)

    @gHz.command(aliases=['megahertz'], invoke_without_command=True, description='units/frequency-gHz-mHz-desc')
    async def mHz(ctx, amount: float):
        await ctx.send(amount * 1e9 / 1e6)


    @convert.group(aliases=[], invoke_without_command=True, description='units/fuel-desc')
    @lone_group(True)
    async def fuel(self, ctx):
        pass


    @fuel.group(aliases=['us-miles-per-gallon', 'us-mile-per-gallon'], invoke_without_command=True, description='units/fuel-umpg-desc')
    @lone_group(True)
    async def umpg(ctx):
        pass


    @umpg.command(aliases=['imperial-miles-per-gallon', 'imperial-mile-per-gallon', 'mile-per-gallon', 'miles-per-gallon'], invoke_without_command=True, description='units/fuel-umpg-impg-desc')
    async def impg(ctx, amount: float):
        await ctx.send(amount * (1/2.352) / (1/2.825))

    @umpg.command(aliases=['kilometer-per-liter', 'kilometers-per-liter', 'kilometre-per-litre', 'kilometres-per-litre'], invoke_without_command=True, description='units/fuel-umpg-kmpL-desc')
    async def kmpL(ctx, amount: float):
        await ctx.send(amount * (1/2.352) / 1)

    @umpg.command(aliases=['liters-per-hundred-kilometers', 'liter-per-hundred-kilometers', 'litres-per-hundred-kilometres', 'litre-per-hundred-kilometres'], invoke_without_command=True, description='units/fuel-umpg-Lphkm-desc')
    async def Lphkm(ctx, amount: float):
        await ctx.send(amount * (1/2.352) / amount * 100 / amount)

    @fuel.group(aliases=['imperial-miles-per-gallon', 'imperial-mile-per-gallon', 'mile-per-gallon', 'miles-per-gallon'], invoke_without_command=True, description='units/fuel-impg-desc')
    @lone_group(True)
    async def impg(ctx):
        pass


    @impg.command(aliases=['us-miles-per-gallon', 'us-mile-per-gallon'], invoke_without_command=True, description='units/fuel-impg-umpg-desc')
    async def umpg(ctx, amount: float):
        await ctx.send(amount * (1/2.825) / (1/2.352))

    @impg.command(aliases=['kilometer-per-liter', 'kilometers-per-liter', 'kilometre-per-litre', 'kilometres-per-litre'], invoke_without_command=True, description='units/fuel-impg-kmpL-desc')
    async def kmpL(ctx, amount: float):
        await ctx.send(amount * (1/2.825) / 1)

    @impg.command(aliases=['liters-per-hundred-kilometers', 'liter-per-hundred-kilometers', 'litres-per-hundred-kilometres', 'litre-per-hundred-kilometres'], invoke_without_command=True, description='units/fuel-impg-Lphkm-desc')
    async def Lphkm(ctx, amount: float):
        await ctx.send(amount * (1/2.825) / amount * 100 / amount)

    @fuel.group(aliases=['kilometer-per-liter', 'kilometers-per-liter', 'kilometre-per-litre', 'kilometres-per-litre'], invoke_without_command=True, description='units/fuel-kmpL-desc')
    @lone_group(True)
    async def kmpL(ctx):
        pass


    @kmpL.command(aliases=['us-miles-per-gallon', 'us-mile-per-gallon'], invoke_without_command=True, description='units/fuel-kmpL-umpg-desc')
    async def umpg(ctx, amount: float):
        await ctx.send(amount * 1 / (1/2.352))

    @kmpL.command(aliases=['imperial-miles-per-gallon', 'imperial-mile-per-gallon', 'mile-per-gallon', 'miles-per-gallon'], invoke_without_command=True, description='units/fuel-kmpL-impg-desc')
    async def impg(ctx, amount: float):
        await ctx.send(amount * 1 / (1/2.825))

    @kmpL.command(aliases=['liters-per-hundred-kilometers', 'liter-per-hundred-kilometers', 'litres-per-hundred-kilometres', 'litre-per-hundred-kilometres'], invoke_without_command=True, description='units/fuel-kmpL-Lphkm-desc')
    async def Lphkm(ctx, amount: float):
        await ctx.send(amount * 1 / amount * 100 / amount)

    @fuel.group(aliases=['liters-per-hundred-kilometers', 'liter-per-hundred-kilometers', 'litres-per-hundred-kilometres', 'litre-per-hundred-kilometres'], invoke_without_command=True, description='units/fuel-Lphkm-desc')
    @lone_group(True)
    async def Lphkm(ctx):
        pass


    @Lphkm.command(aliases=['us-miles-per-gallon', 'us-mile-per-gallon'], invoke_without_command=True, description='units/fuel-Lphkm-umpg-desc')
    async def umpg(ctx, amount: float):
        await ctx.send(amount * amount * 100 / amount / (1/2.352))

    @Lphkm.command(aliases=['imperial-miles-per-gallon', 'imperial-mile-per-gallon', 'mile-per-gallon', 'miles-per-gallon'], invoke_without_command=True, description='units/fuel-Lphkm-impg-desc')
    async def impg(ctx, amount: float):
        await ctx.send(amount * amount * 100 / amount / (1/2.825))

    @Lphkm.command(aliases=['kilometer-per-liter', 'kilometers-per-liter', 'kilometre-per-litre', 'kilometres-per-litre'], invoke_without_command=True, description='units/fuel-Lphkm-kmpL-desc')
    async def kmpL(ctx, amount: float):
        await ctx.send(amount * amount * 100 / amount / 1)


    @convert.group(aliases=[], invoke_without_command=True, description='units/length-desc')
    @lone_group(True)
    async def length(self, ctx):
        pass


    @length.group(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-km-desc')
    @lone_group(True)
    async def km(ctx):
        pass


    @km.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-km-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1000 / 1)

    @km.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-km-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1000 / 1e-2)

    @km.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-km-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1000 / 1e-3)

    @km.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-km-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1000 / 1e-6)

    @km.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-km-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1000 / 1e-9)

    @km.command(aliases=['miles'], invoke_without_command=True, description='units/length-km-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1000 / 1609.344)

    @km.command(aliases=['yards'], invoke_without_command=True, description='units/length-km-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1000 / (1/1.094))

    @km.command(aliases=['feet'], invoke_without_command=True, description='units/length-km-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1000 / (1/3.281))

    @km.command(aliases=['inches'], invoke_without_command=True, description='units/length-km-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1000 / 2.54e-2)

    @km.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-km-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1000 / 1852)

    @length.group(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-m-desc')
    @lone_group(True)
    async def m(ctx):
        pass


    @m.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-m-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1 / 1000)

    @m.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-m-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-2)

    @m.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-m-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-3)

    @m.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-m-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-6)

    @m.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-m-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-9)

    @m.command(aliases=['miles'], invoke_without_command=True, description='units/length-m-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1 / 1609.344)

    @m.command(aliases=['yards'], invoke_without_command=True, description='units/length-m-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.094))

    @m.command(aliases=['feet'], invoke_without_command=True, description='units/length-m-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3.281))

    @m.command(aliases=['inches'], invoke_without_command=True, description='units/length-m-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1 / 2.54e-2)

    @m.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-m-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1 / 1852)

    @length.group(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-cm-desc')
    @lone_group(True)
    async def cm(ctx):
        pass


    @cm.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-cm-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1000)

    @cm.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-cm-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1)

    @cm.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-cm-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1e-3)

    @cm.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-cm-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1e-6)

    @cm.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-cm-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1e-9)

    @cm.command(aliases=['miles'], invoke_without_command=True, description='units/length-cm-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1609.344)

    @cm.command(aliases=['yards'], invoke_without_command=True, description='units/length-cm-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1e-2 / (1/1.094))

    @cm.command(aliases=['feet'], invoke_without_command=True, description='units/length-cm-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1e-2 / (1/3.281))

    @cm.command(aliases=['inches'], invoke_without_command=True, description='units/length-cm-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 2.54e-2)

    @cm.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-cm-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1e-2 / 1852)

    @length.group(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-mm-desc')
    @lone_group(True)
    async def mm(ctx):
        pass


    @mm.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-mm-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1000)

    @mm.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-mm-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1)

    @mm.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-mm-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-2)

    @mm.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-mm-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-6)

    @mm.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-mm-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-9)

    @mm.command(aliases=['miles'], invoke_without_command=True, description='units/length-mm-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1609.344)

    @mm.command(aliases=['yards'], invoke_without_command=True, description='units/length-mm-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/1.094))

    @mm.command(aliases=['feet'], invoke_without_command=True, description='units/length-mm-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/3.281))

    @mm.command(aliases=['inches'], invoke_without_command=True, description='units/length-mm-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 2.54e-2)

    @mm.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-mm-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1852)

    @length.group(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-micron-desc')
    @lone_group(True)
    async def micron(ctx):
        pass


    @micron.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-micron-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1000)

    @micron.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-micron-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1)

    @micron.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-micron-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-2)

    @micron.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-micron-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-3)

    @micron.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-micron-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-9)

    @micron.command(aliases=['miles'], invoke_without_command=True, description='units/length-micron-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1609.344)

    @micron.command(aliases=['yards'], invoke_without_command=True, description='units/length-micron-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1e-6 / (1/1.094))

    @micron.command(aliases=['feet'], invoke_without_command=True, description='units/length-micron-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1e-6 / (1/3.281))

    @micron.command(aliases=['inches'], invoke_without_command=True, description='units/length-micron-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 2.54e-2)

    @micron.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-micron-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1852)

    @length.group(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-nm-desc')
    @lone_group(True)
    async def nm(ctx):
        pass


    @nm.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-nm-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1000)

    @nm.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-nm-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1)

    @nm.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-nm-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-2)

    @nm.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-nm-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-3)

    @nm.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-nm-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-6)

    @nm.command(aliases=['miles'], invoke_without_command=True, description='units/length-nm-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1609.344)

    @nm.command(aliases=['yards'], invoke_without_command=True, description='units/length-nm-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1e-9 / (1/1.094))

    @nm.command(aliases=['feet'], invoke_without_command=True, description='units/length-nm-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1e-9 / (1/3.281))

    @nm.command(aliases=['inches'], invoke_without_command=True, description='units/length-nm-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 2.54e-2)

    @nm.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-nm-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1852)

    @length.group(aliases=['miles'], invoke_without_command=True, description='units/length-mile-desc')
    @lone_group(True)
    async def mile(ctx):
        pass


    @mile.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-mile-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1000)

    @mile.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-mile-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1)

    @mile.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-mile-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1e-2)

    @mile.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-mile-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1e-3)

    @mile.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-mile-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1e-6)

    @mile.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-mile-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1e-9)

    @mile.command(aliases=['yards'], invoke_without_command=True, description='units/length-mile-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1609.344 / (1/1.094))

    @mile.command(aliases=['feet'], invoke_without_command=True, description='units/length-mile-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1609.344 / (1/3.281))

    @mile.command(aliases=['inches'], invoke_without_command=True, description='units/length-mile-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 2.54e-2)

    @mile.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-mile-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 1609.344 / 1852)

    @length.group(aliases=['yards'], invoke_without_command=True, description='units/length-yard-desc')
    @lone_group(True)
    async def yard(ctx):
        pass


    @yard.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-yard-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1000)

    @yard.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-yard-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1)

    @yard.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-yard-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1e-2)

    @yard.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-yard-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1e-3)

    @yard.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-yard-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1e-6)

    @yard.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-yard-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1e-9)

    @yard.command(aliases=['miles'], invoke_without_command=True, description='units/length-yard-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1609.344)

    @yard.command(aliases=['feet'], invoke_without_command=True, description='units/length-yard-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / (1/3.281))

    @yard.command(aliases=['inches'], invoke_without_command=True, description='units/length-yard-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 2.54e-2)

    @yard.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-yard-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * (1/1.094) / 1852)

    @length.group(aliases=['feet'], invoke_without_command=True, description='units/length-foot-desc')
    @lone_group(True)
    async def foot(ctx):
        pass


    @foot.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-foot-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1000)

    @foot.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-foot-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1)

    @foot.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-foot-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1e-2)

    @foot.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-foot-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1e-3)

    @foot.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-foot-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1e-6)

    @foot.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-foot-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1e-9)

    @foot.command(aliases=['miles'], invoke_without_command=True, description='units/length-foot-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1609.344)

    @foot.command(aliases=['yards'], invoke_without_command=True, description='units/length-foot-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / (1/1.094))

    @foot.command(aliases=['inches'], invoke_without_command=True, description='units/length-foot-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 2.54e-2)

    @foot.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-foot-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1852)

    @length.group(aliases=['inches'], invoke_without_command=True, description='units/length-inch-desc')
    @lone_group(True)
    async def inch(ctx):
        pass


    @inch.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-inch-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1000)

    @inch.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-inch-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1)

    @inch.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-inch-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1e-2)

    @inch.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-inch-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1e-3)

    @inch.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-inch-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1e-6)

    @inch.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-inch-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1e-9)

    @inch.command(aliases=['miles'], invoke_without_command=True, description='units/length-inch-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1609.344)

    @inch.command(aliases=['yards'], invoke_without_command=True, description='units/length-inch-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / (1/1.094))

    @inch.command(aliases=['feet'], invoke_without_command=True, description='units/length-inch-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / (1/3.281))

    @inch.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-inch-nautmil-desc')
    async def nautmil(ctx, amount: float):
        await ctx.send(amount * 2.54e-2 / 1852)

    @length.group(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-nautmil-desc')
    @lone_group(True)
    async def nautmil(ctx):
        pass


    @nautmil.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-nautmil-km-desc')
    async def km(ctx, amount: float):
        await ctx.send(amount * 1852 / 1000)

    @nautmil.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-nautmil-m-desc')
    async def m(ctx, amount: float):
        await ctx.send(amount * 1852 / 1)

    @nautmil.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-nautmil-cm-desc')
    async def cm(ctx, amount: float):
        await ctx.send(amount * 1852 / 1e-2)

    @nautmil.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-nautmil-mm-desc')
    async def mm(ctx, amount: float):
        await ctx.send(amount * 1852 / 1e-3)

    @nautmil.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-nautmil-micron-desc')
    async def micron(ctx, amount: float):
        await ctx.send(amount * 1852 / 1e-6)

    @nautmil.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-nautmil-nm-desc')
    async def nm(ctx, amount: float):
        await ctx.send(amount * 1852 / 1e-9)

    @nautmil.command(aliases=['miles'], invoke_without_command=True, description='units/length-nautmil-mile-desc')
    async def mile(ctx, amount: float):
        await ctx.send(amount * 1852 / 1609.344)

    @nautmil.command(aliases=['yards'], invoke_without_command=True, description='units/length-nautmil-yard-desc')
    async def yard(ctx, amount: float):
        await ctx.send(amount * 1852 / (1/1.094))

    @nautmil.command(aliases=['feet'], invoke_without_command=True, description='units/length-nautmil-foot-desc')
    async def foot(ctx, amount: float):
        await ctx.send(amount * 1852 / (1/3.281))

    @nautmil.command(aliases=['inches'], invoke_without_command=True, description='units/length-nautmil-inch-desc')
    async def inch(ctx, amount: float):
        await ctx.send(amount * 1852 / 2.54e-2)


    @convert.group(aliases=[], invoke_without_command=True, description='units/mass-desc')
    @lone_group(True)
    async def mass(self, ctx):
        pass


    @mass.group(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-t-desc')
    @lone_group(True)
    async def t(ctx):
        pass


    @t.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-t-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e3)

    @t.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-t-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1)

    @t.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-t-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e-3)

    @t.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-t-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1e-6)

    @t.command(aliases=[], invoke_without_command=True, description='units/mass-t-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1e6 / 1.016e6)

    @t.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-t-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1e6 / 907184.74)

    @t.command(aliases=[], invoke_without_command=True, description='units/mass-t-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1e6 / 6350.293)

    @t.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-t-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1e6 / 453.592)

    @t.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-t-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1e6 / 28.3495)

    @mass.group(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-kg-desc')
    @lone_group(True)
    async def kg(ctx):
        pass


    @kg.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-kg-t-desc')
    async def t(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e6)

    @kg.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-kg-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @kg.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-kg-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e-3)

    @kg.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-kg-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e-6)

    @kg.command(aliases=[], invoke_without_command=True, description='units/mass-kg-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1.016e6)

    @kg.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-kg-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1e3 / 907184.74)

    @kg.command(aliases=[], invoke_without_command=True, description='units/mass-kg-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1e3 / 6350.293)

    @kg.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-kg-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1e3 / 453.592)

    @kg.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-kg-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1e3 / 28.3495)

    @mass.group(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-g-desc')
    @lone_group(True)
    async def g(ctx):
        pass


    @g.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-g-t-desc')
    async def t(ctx, amount: float):
        await ctx.send(amount * 1 / 1e6)

    @g.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-g-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @g.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-g-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-3)

    @g.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-g-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-6)

    @g.command(aliases=[], invoke_without_command=True, description='units/mass-g-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1 / 1.016e6)

    @g.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-g-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1 / 907184.74)

    @g.command(aliases=[], invoke_without_command=True, description='units/mass-g-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1 / 6350.293)

    @g.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-g-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1 / 453.592)

    @g.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-g-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1 / 28.3495)

    @mass.group(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-mg-desc')
    @lone_group(True)
    async def mg(ctx):
        pass


    @mg.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-mg-t-desc')
    async def t(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e6)

    @mg.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-mg-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e3)

    @mg.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-mg-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1)

    @mg.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-mg-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-6)

    @mg.command(aliases=[], invoke_without_command=True, description='units/mass-mg-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1.016e6)

    @mg.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-mg-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 907184.74)

    @mg.command(aliases=[], invoke_without_command=True, description='units/mass-mg-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 6350.293)

    @mg.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-mg-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 453.592)

    @mg.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-mg-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 28.3495)

    @mass.group(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-microg-desc')
    @lone_group(True)
    async def microg(ctx):
        pass


    @microg.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-microg-t-desc')
    async def t(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e6)

    @microg.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-microg-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e3)

    @microg.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-microg-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1)

    @microg.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-microg-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-3)

    @microg.command(aliases=[], invoke_without_command=True, description='units/mass-microg-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1.016e6)

    @microg.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-microg-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 907184.74)

    @microg.command(aliases=[], invoke_without_command=True, description='units/mass-microg-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 6350.293)

    @microg.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-microg-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 453.592)

    @microg.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-microg-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 28.3495)

    @mass.group(aliases=[], invoke_without_command=True, description='units/mass-ton-desc')
    @lone_group(True)
    async def ton(ctx):
        pass


    @ton.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-ton-t-desc')
    async def t(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1e6)

    @ton.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-ton-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1e3)

    @ton.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-ton-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1)

    @ton.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-ton-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1e-3)

    @ton.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-ton-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 1e-6)

    @ton.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-ton-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 907184.74)

    @ton.command(aliases=[], invoke_without_command=True, description='units/mass-ton-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 6350.293)

    @ton.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-ton-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 453.592)

    @ton.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-ton-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 1.016e6 / 28.3495)

    @mass.group(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-uston-desc')
    @lone_group(True)
    async def uston(ctx):
        pass


    @uston.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-uston-t-desc')
    async def t(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1e6)

    @uston.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-uston-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1e3)

    @uston.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-uston-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1)

    @uston.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-uston-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1e-3)

    @uston.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-uston-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1e-6)

    @uston.command(aliases=[], invoke_without_command=True, description='units/mass-uston-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 1.016e6)

    @uston.command(aliases=[], invoke_without_command=True, description='units/mass-uston-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 6350.293)

    @uston.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-uston-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 453.592)

    @uston.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-uston-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 907184.74 / 28.3495)

    @mass.group(aliases=[], invoke_without_command=True, description='units/mass-stone-desc')
    @lone_group(True)
    async def stone(ctx):
        pass


    @stone.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-stone-t-desc')
    async def t(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1e6)

    @stone.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-stone-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1e3)

    @stone.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-stone-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1)

    @stone.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-stone-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1e-3)

    @stone.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-stone-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1e-6)

    @stone.command(aliases=[], invoke_without_command=True, description='units/mass-stone-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 1.016e6)

    @stone.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-stone-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 907184.74)

    @stone.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-stone-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 453.592)

    @stone.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-stone-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 6350.293 / 28.3495)

    @mass.group(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-lb-desc')
    @lone_group(True)
    async def lb(ctx):
        pass


    @lb.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-lb-t-desc')
    async def t(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1e6)

    @lb.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-lb-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1e3)

    @lb.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-lb-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1)

    @lb.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-lb-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1e-3)

    @lb.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-lb-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1e-6)

    @lb.command(aliases=[], invoke_without_command=True, description='units/mass-lb-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 453.592 / 1.016e6)

    @lb.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-lb-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 453.592 / 907184.74)

    @lb.command(aliases=[], invoke_without_command=True, description='units/mass-lb-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 453.592 / 6350.293)

    @lb.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-lb-oz-desc')
    async def oz(ctx, amount: float):
        await ctx.send(amount * 453.592 / 28.3495)

    @mass.group(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-oz-desc')
    @lone_group(True)
    async def oz(ctx):
        pass


    @oz.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-oz-t-desc')
    async def t(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1e6)

    @oz.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-oz-kg-desc')
    async def kg(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1e3)

    @oz.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-oz-g-desc')
    async def g(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1)

    @oz.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-oz-mg-desc')
    async def mg(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1e-3)

    @oz.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-oz-microg-desc')
    async def microg(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1e-6)

    @oz.command(aliases=[], invoke_without_command=True, description='units/mass-oz-ton-desc')
    async def ton(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 1.016e6)

    @oz.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-oz-uston-desc')
    async def uston(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 907184.74)

    @oz.command(aliases=[], invoke_without_command=True, description='units/mass-oz-stone-desc')
    async def stone(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 6350.293)

    @oz.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-oz-lb-desc')
    async def lb(ctx, amount: float):
        await ctx.send(amount * 28.3495 / 453.592)


    @convert.group(aliases=[], invoke_without_command=True, description='units/angle-desc')
    @lone_group(True)
    async def angle(self, ctx):
        pass


    @angle.group(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-deg-desc')
    @lone_group(True)
    async def deg(ctx):
        pass


    @deg.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-deg-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * 1 / 0.9)

    @deg.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-deg-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * 1 / (180/(1000 * pi)))

    @deg.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-deg-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * 1 / (1/60))

    @deg.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-deg-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * 1 / (180/pi))

    @deg.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-deg-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3600))

    @angle.group(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-grad-desc')
    @lone_group(True)
    async def grad(ctx):
        pass


    @grad.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-grad-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * 0.9 / 1)

    @grad.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-grad-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * 0.9 / (180/(1000 * pi)))

    @grad.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-grad-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * 0.9 / (1/60))

    @grad.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-grad-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * 0.9 / (180/pi))

    @grad.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-grad-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * 0.9 / (1/3600))

    @angle.group(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-mrad-desc')
    @lone_group(True)
    async def mrad(ctx):
        pass


    @mrad.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-mrad-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * pi)) / 1)

    @mrad.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-mrad-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * pi)) / 0.9)

    @mrad.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-mrad-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * pi)) / (1/60))

    @mrad.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-mrad-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * pi)) / (180/pi))

    @mrad.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-mrad-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * (180/(1000 * pi)) / (1/3600))

    @angle.group(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-arcmin-desc')
    @lone_group(True)
    async def arcmin(ctx):
        pass


    @arcmin.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-arcmin-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * (1/60) / 1)

    @arcmin.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-arcmin-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * (1/60) / 0.9)

    @arcmin.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-arcmin-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * (1/60) / (180/(1000 * pi)))

    @arcmin.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-arcmin-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * (1/60) / (180/pi))

    @arcmin.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-arcmin-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * (1/60) / (1/3600))

    @angle.group(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-rad-desc')
    @lone_group(True)
    async def rad(ctx):
        pass


    @rad.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-rad-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * (180/pi) / 1)

    @rad.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-rad-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * (180/pi) / 0.9)

    @rad.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-rad-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * (180/pi) / (180/(1000 * pi)))

    @rad.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-rad-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * (180/pi) / (1/60))

    @rad.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-rad-arcsec-desc')
    async def arcsec(ctx, amount: float):
        await ctx.send(amount * (180/pi) / (1/3600))

    @angle.group(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-arcsec-desc')
    @lone_group(True)
    async def arcsec(ctx):
        pass


    @arcsec.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-arcsec-deg-desc')
    async def deg(ctx, amount: float):
        await ctx.send(amount * (1/3600) / 1)

    @arcsec.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-arcsec-grad-desc')
    async def grad(ctx, amount: float):
        await ctx.send(amount * (1/3600) / 0.9)

    @arcsec.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-arcsec-mrad-desc')
    async def mrad(ctx, amount: float):
        await ctx.send(amount * (1/3600) / (180/(1000 * pi)))

    @arcsec.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-arcsec-arcmin-desc')
    async def arcmin(ctx, amount: float):
        await ctx.send(amount * (1/3600) / (1/60))

    @arcsec.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-arcsec-rad-desc')
    async def rad(ctx, amount: float):
        await ctx.send(amount * (1/3600) / (180/pi))


    @convert.group(aliases=[], invoke_without_command=True, description='units/pressure-desc')
    @lone_group(True)
    async def pressure(self, ctx):
        pass


    @pressure.group(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-atm-desc')
    @lone_group(True)
    async def atm(ctx):
        pass


    @atm.command(aliases=[], invoke_without_command=True, description='units/pressure-atm-bar-desc')
    async def bar(ctx, amount: float):
        await ctx.send(amount * 101325 / 1e5)

    @atm.command(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-atm-Pa-desc')
    async def Pa(ctx, amount: float):
        await ctx.send(amount * 101325 / 1)

    @atm.command(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-atm-psi-desc')
    async def psi(ctx, amount: float):
        await ctx.send(amount * 101325 / 6894.757)

    @atm.command(aliases=[], invoke_without_command=True, description='units/pressure-atm-torr-desc')
    async def torr(ctx, amount: float):
        await ctx.send(amount * 101325 / 133.322)

    @pressure.group(aliases=[], invoke_without_command=True, description='units/pressure-bar-desc')
    @lone_group(True)
    async def bar(ctx):
        pass


    @bar.command(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-bar-atm-desc')
    async def atm(ctx, amount: float):
        await ctx.send(amount * 1e5 / 101325)

    @bar.command(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-bar-Pa-desc')
    async def Pa(ctx, amount: float):
        await ctx.send(amount * 1e5 / 1)

    @bar.command(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-bar-psi-desc')
    async def psi(ctx, amount: float):
        await ctx.send(amount * 1e5 / 6894.757)

    @bar.command(aliases=[], invoke_without_command=True, description='units/pressure-bar-torr-desc')
    async def torr(ctx, amount: float):
        await ctx.send(amount * 1e5 / 133.322)

    @pressure.group(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-Pa-desc')
    @lone_group(True)
    async def Pa(ctx):
        pass


    @Pa.command(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-Pa-atm-desc')
    async def atm(ctx, amount: float):
        await ctx.send(amount * 1 / 101325)

    @Pa.command(aliases=[], invoke_without_command=True, description='units/pressure-Pa-bar-desc')
    async def bar(ctx, amount: float):
        await ctx.send(amount * 1 / 1e5)

    @Pa.command(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-Pa-psi-desc')
    async def psi(ctx, amount: float):
        await ctx.send(amount * 1 / 6894.757)

    @Pa.command(aliases=[], invoke_without_command=True, description='units/pressure-Pa-torr-desc')
    async def torr(ctx, amount: float):
        await ctx.send(amount * 1 / 133.322)

    @pressure.group(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-psi-desc')
    @lone_group(True)
    async def psi(ctx):
        pass


    @psi.command(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-psi-atm-desc')
    async def atm(ctx, amount: float):
        await ctx.send(amount * 6894.757 / 101325)

    @psi.command(aliases=[], invoke_without_command=True, description='units/pressure-psi-bar-desc')
    async def bar(ctx, amount: float):
        await ctx.send(amount * 6894.757 / 1e5)

    @psi.command(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-psi-Pa-desc')
    async def Pa(ctx, amount: float):
        await ctx.send(amount * 6894.757 / 1)

    @psi.command(aliases=[], invoke_without_command=True, description='units/pressure-psi-torr-desc')
    async def torr(ctx, amount: float):
        await ctx.send(amount * 6894.757 / 133.322)

    @pressure.group(aliases=[], invoke_without_command=True, description='units/pressure-torr-desc')
    @lone_group(True)
    async def torr(ctx):
        pass


    @torr.command(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-torr-atm-desc')
    async def atm(ctx, amount: float):
        await ctx.send(amount * 133.322 / 101325)

    @torr.command(aliases=[], invoke_without_command=True, description='units/pressure-torr-bar-desc')
    async def bar(ctx, amount: float):
        await ctx.send(amount * 133.322 / 1e5)

    @torr.command(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-torr-Pa-desc')
    async def Pa(ctx, amount: float):
        await ctx.send(amount * 133.322 / 1)

    @torr.command(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-torr-psi-desc')
    async def psi(ctx, amount: float):
        await ctx.send(amount * 133.322 / 6894.757)


    @convert.group(aliases=[], invoke_without_command=True, description='units/speed-desc')
    @lone_group(True)
    async def speed(self, ctx):
        pass


    @speed.group(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-mph-desc')
    @lone_group(True)
    async def mph(ctx):
        pass


    @mph.command(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-mph-fps-desc')
    async def fps(ctx, amount: float):
        await ctx.send(amount * (1/2.237) / (1/3.281))

    @mph.command(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-mph-mps-desc')
    async def mps(ctx, amount: float):
        await ctx.send(amount * (1/2.237) / 1)

    @mph.command(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-mph-kmph-desc')
    async def kmph(ctx, amount: float):
        await ctx.send(amount * (1/2.237) / (1/3.6))

    @mph.command(aliases=['knots'], invoke_without_command=True, description='units/speed-mph-knot-desc')
    async def knot(ctx, amount: float):
        await ctx.send(amount * (1/2.237) / (1/1.944))

    @speed.group(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-fps-desc')
    @lone_group(True)
    async def fps(ctx):
        pass


    @fps.command(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-fps-mph-desc')
    async def mph(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / (1/2.237))

    @fps.command(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-fps-mps-desc')
    async def mps(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / 1)

    @fps.command(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-fps-kmph-desc')
    async def kmph(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / (1/3.6))

    @fps.command(aliases=['knots'], invoke_without_command=True, description='units/speed-fps-knot-desc')
    async def knot(ctx, amount: float):
        await ctx.send(amount * (1/3.281) / (1/1.944))

    @speed.group(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-mps-desc')
    @lone_group(True)
    async def mps(ctx):
        pass


    @mps.command(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-mps-mph-desc')
    async def mph(ctx, amount: float):
        await ctx.send(amount * 1 / (1/2.237))

    @mps.command(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-mps-fps-desc')
    async def fps(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3.281))

    @mps.command(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-mps-kmph-desc')
    async def kmph(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3.6))

    @mps.command(aliases=['knots'], invoke_without_command=True, description='units/speed-mps-knot-desc')
    async def knot(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.944))

    @speed.group(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-kmph-desc')
    @lone_group(True)
    async def kmph(ctx):
        pass


    @kmph.command(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-kmph-mph-desc')
    async def mph(ctx, amount: float):
        await ctx.send(amount * (1/3.6) / (1/2.237))

    @kmph.command(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-kmph-fps-desc')
    async def fps(ctx, amount: float):
        await ctx.send(amount * (1/3.6) / (1/3.281))

    @kmph.command(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-kmph-mps-desc')
    async def mps(ctx, amount: float):
        await ctx.send(amount * (1/3.6) / 1)

    @kmph.command(aliases=['knots'], invoke_without_command=True, description='units/speed-kmph-knot-desc')
    async def knot(ctx, amount: float):
        await ctx.send(amount * (1/3.6) / (1/1.944))

    @speed.group(aliases=['knots'], invoke_without_command=True, description='units/speed-knot-desc')
    @lone_group(True)
    async def knot(ctx):
        pass


    @knot.command(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-knot-mph-desc')
    async def mph(ctx, amount: float):
        await ctx.send(amount * (1/1.944) / (1/2.237))

    @knot.command(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-knot-fps-desc')
    async def fps(ctx, amount: float):
        await ctx.send(amount * (1/1.944) / (1/3.281))

    @knot.command(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-knot-mps-desc')
    async def mps(ctx, amount: float):
        await ctx.send(amount * (1/1.944) / 1)

    @knot.command(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-knot-kmph-desc')
    async def kmph(ctx, amount: float):
        await ctx.send(amount * (1/1.944) / (1/3.6))


    @convert.group(aliases=['temp'], invoke_without_command=True, description='units/temperature-desc')
    @lone_group(True)
    async def temperature(self, ctx):
        pass


    @temperature.group(aliases=['Celsius'], invoke_without_command=True, description='units/temperature-C-desc')
    @lone_group(True)
    async def C(ctx):
        pass


    @C.command(aliases=['Farenheit'], invoke_without_command=True, description='units/temperature-C-F-desc')
    async def F(ctx, amount: float):
        await ctx.send(amount * 9 / 5 + 32)

    @C.command(aliases=['Kelvin'], invoke_without_command=True, description='units/temperature-C-K-desc')
    async def K(ctx, amount: float):
        await ctx.send(amount + 273.15)

    @temperature.group(aliases=['Farenheit'], invoke_without_command=True, description='units/temperature-F-desc')
    @lone_group(True)
    async def F(ctx):
        pass


    @F.command(aliases=['Celsius'], invoke_without_command=True, description='units/temperature-F-C-desc')
    async def C(ctx, amount: float):
        await ctx.send((amount - 32) * 5 / 9)

    @F.command(aliases=['Kelvin'], invoke_without_command=True, description='units/temperature-F-K-desc')
    async def K(ctx, amount: float):
        await ctx.send((amount - 32) * 5 / 9 + 273.15)

    @temperature.group(aliases=['Kelvin'], invoke_without_command=True, description='units/temperature-K-desc')
    @lone_group(True)
    async def K(ctx):
        pass


    @K.command(aliases=['Celsius'], invoke_without_command=True, description='units/temperature-K-C-desc')
    async def C(ctx, amount: float):
        await ctx.send((amount - 273.15))

    @K.command(aliases=['Farenheit'], invoke_without_command=True, description='units/temperature-K-F-desc')
    async def F(ctx, amount: float):
        await ctx.send((amount - 273.15)* 9 / 5 + 32)


    @convert.group(aliases=[], invoke_without_command=True, description='units/time-desc')
    @lone_group(True)
    async def time(self, ctx):
        pass


    @time.group(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-ns-desc')
    @lone_group(True)
    async def ns(ctx):
        pass


    @ns.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-ns-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-6)

    @ns.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-ns-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1e-3)

    @ns.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-ns-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 1)

    @ns.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-ns-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 60)

    @ns.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-ns-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 3600)

    @ns.command(aliases=['days'], invoke_without_command=True, description='units/time-ns-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 86400)

    @ns.command(aliases=['weeks'], invoke_without_command=True, description='units/time-ns-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 604800)

    @ns.command(aliases=['months'], invoke_without_command=True, description='units/time-ns-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 2.628e6)

    @ns.command(aliases=['years'], invoke_without_command=True, description='units/time-ns-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 3.154e7)

    @ns.command(aliases=['decades'], invoke_without_command=True, description='units/time-ns-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 3.154e8)

    @ns.command(aliases=['centuries'], invoke_without_command=True, description='units/time-ns-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 1e-9 / 3.154e9)

    @time.group(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-micros-desc')
    @lone_group(True)
    async def micros(ctx):
        pass


    @micros.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-micros-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-9)

    @micros.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-micros-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1e-3)

    @micros.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-micros-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 1)

    @micros.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-micros-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 60)

    @micros.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-micros-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 3600)

    @micros.command(aliases=['days'], invoke_without_command=True, description='units/time-micros-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 86400)

    @micros.command(aliases=['weeks'], invoke_without_command=True, description='units/time-micros-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 604800)

    @micros.command(aliases=['months'], invoke_without_command=True, description='units/time-micros-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 2.628e6)

    @micros.command(aliases=['years'], invoke_without_command=True, description='units/time-micros-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 3.154e7)

    @micros.command(aliases=['decades'], invoke_without_command=True, description='units/time-micros-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 3.154e8)

    @micros.command(aliases=['centuries'], invoke_without_command=True, description='units/time-micros-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 1e-6 / 3.154e9)

    @time.group(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-ms-desc')
    @lone_group(True)
    async def ms(ctx):
        pass


    @ms.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-ms-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-9)

    @ms.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-ms-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e-6)

    @ms.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-ms-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1)

    @ms.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-ms-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 60)

    @ms.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-ms-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3600)

    @ms.command(aliases=['days'], invoke_without_command=True, description='units/time-ms-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 86400)

    @ms.command(aliases=['weeks'], invoke_without_command=True, description='units/time-ms-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 604800)

    @ms.command(aliases=['months'], invoke_without_command=True, description='units/time-ms-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 2.628e6)

    @ms.command(aliases=['years'], invoke_without_command=True, description='units/time-ms-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3.154e7)

    @ms.command(aliases=['decades'], invoke_without_command=True, description='units/time-ms-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3.154e8)

    @ms.command(aliases=['centuries'], invoke_without_command=True, description='units/time-ms-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3.154e9)

    @time.group(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-s-desc')
    @lone_group(True)
    async def s(ctx):
        pass


    @s.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-s-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-9)

    @s.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-s-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-6)

    @s.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-s-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-3)

    @s.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-s-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 1 / 60)

    @s.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-s-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 1 / 3600)

    @s.command(aliases=['days'], invoke_without_command=True, description='units/time-s-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 1 / 86400)

    @s.command(aliases=['weeks'], invoke_without_command=True, description='units/time-s-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 1 / 604800)

    @s.command(aliases=['months'], invoke_without_command=True, description='units/time-s-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 1 / 2.628e6)

    @s.command(aliases=['years'], invoke_without_command=True, description='units/time-s-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 1 / 3.154e7)

    @s.command(aliases=['decades'], invoke_without_command=True, description='units/time-s-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 1 / 3.154e8)

    @s.command(aliases=['centuries'], invoke_without_command=True, description='units/time-s-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 1 / 3.154e9)

    @time.group(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-min-desc')
    @lone_group(True)
    async def min(ctx):
        pass


    @min.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-min-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 60 / 1e-9)

    @min.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-min-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 60 / 1e-6)

    @min.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-min-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 60 / 1e-3)

    @min.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-min-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 60 / 1)

    @min.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-min-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 60 / 3600)

    @min.command(aliases=['days'], invoke_without_command=True, description='units/time-min-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 60 / 86400)

    @min.command(aliases=['weeks'], invoke_without_command=True, description='units/time-min-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 60 / 604800)

    @min.command(aliases=['months'], invoke_without_command=True, description='units/time-min-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 60 / 2.628e6)

    @min.command(aliases=['years'], invoke_without_command=True, description='units/time-min-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 60 / 3.154e7)

    @min.command(aliases=['decades'], invoke_without_command=True, description='units/time-min-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 60 / 3.154e8)

    @min.command(aliases=['centuries'], invoke_without_command=True, description='units/time-min-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 60 / 3.154e9)

    @time.group(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-h-desc')
    @lone_group(True)
    async def h(ctx):
        pass


    @h.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-h-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 3600 / 1e-9)

    @h.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-h-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 3600 / 1e-6)

    @h.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-h-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 3600 / 1e-3)

    @h.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-h-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 3600 / 1)

    @h.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-h-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 3600 / 60)

    @h.command(aliases=['days'], invoke_without_command=True, description='units/time-h-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 3600 / 86400)

    @h.command(aliases=['weeks'], invoke_without_command=True, description='units/time-h-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 3600 / 604800)

    @h.command(aliases=['months'], invoke_without_command=True, description='units/time-h-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 3600 / 2.628e6)

    @h.command(aliases=['years'], invoke_without_command=True, description='units/time-h-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 3600 / 3.154e7)

    @h.command(aliases=['decades'], invoke_without_command=True, description='units/time-h-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 3600 / 3.154e8)

    @h.command(aliases=['centuries'], invoke_without_command=True, description='units/time-h-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 3600 / 3.154e9)

    @time.group(aliases=['days'], invoke_without_command=True, description='units/time-day-desc')
    @lone_group(True)
    async def day(ctx):
        pass


    @day.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-day-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 86400 / 1e-9)

    @day.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-day-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 86400 / 1e-6)

    @day.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-day-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 86400 / 1e-3)

    @day.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-day-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 86400 / 1)

    @day.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-day-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 86400 / 60)

    @day.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-day-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 86400 / 3600)

    @day.command(aliases=['weeks'], invoke_without_command=True, description='units/time-day-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 86400 / 604800)

    @day.command(aliases=['months'], invoke_without_command=True, description='units/time-day-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 86400 / 2.628e6)

    @day.command(aliases=['years'], invoke_without_command=True, description='units/time-day-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 86400 / 3.154e7)

    @day.command(aliases=['decades'], invoke_without_command=True, description='units/time-day-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 86400 / 3.154e8)

    @day.command(aliases=['centuries'], invoke_without_command=True, description='units/time-day-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 86400 / 3.154e9)

    @time.group(aliases=['weeks'], invoke_without_command=True, description='units/time-week-desc')
    @lone_group(True)
    async def week(ctx):
        pass


    @week.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-week-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 604800 / 1e-9)

    @week.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-week-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 604800 / 1e-6)

    @week.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-week-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 604800 / 1e-3)

    @week.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-week-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 604800 / 1)

    @week.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-week-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 604800 / 60)

    @week.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-week-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 604800 / 3600)

    @week.command(aliases=['days'], invoke_without_command=True, description='units/time-week-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 604800 / 86400)

    @week.command(aliases=['months'], invoke_without_command=True, description='units/time-week-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 604800 / 2.628e6)

    @week.command(aliases=['years'], invoke_without_command=True, description='units/time-week-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 604800 / 3.154e7)

    @week.command(aliases=['decades'], invoke_without_command=True, description='units/time-week-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 604800 / 3.154e8)

    @week.command(aliases=['centuries'], invoke_without_command=True, description='units/time-week-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 604800 / 3.154e9)

    @time.group(aliases=['months'], invoke_without_command=True, description='units/time-month-desc')
    @lone_group(True)
    async def month(ctx):
        pass


    @month.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-month-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 1e-9)

    @month.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-month-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 1e-6)

    @month.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-month-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 1e-3)

    @month.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-month-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 1)

    @month.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-month-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 60)

    @month.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-month-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 3600)

    @month.command(aliases=['days'], invoke_without_command=True, description='units/time-month-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 86400)

    @month.command(aliases=['weeks'], invoke_without_command=True, description='units/time-month-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 604800)

    @month.command(aliases=['years'], invoke_without_command=True, description='units/time-month-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 3.154e7)

    @month.command(aliases=['decades'], invoke_without_command=True, description='units/time-month-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 3.154e8)

    @month.command(aliases=['centuries'], invoke_without_command=True, description='units/time-month-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 2.628e6 / 3.154e9)

    @time.group(aliases=['years'], invoke_without_command=True, description='units/time-year-desc')
    @lone_group(True)
    async def year(ctx):
        pass


    @year.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-year-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 1e-9)

    @year.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-year-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 1e-6)

    @year.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-year-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 1e-3)

    @year.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-year-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 1)

    @year.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-year-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 60)

    @year.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-year-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 3600)

    @year.command(aliases=['days'], invoke_without_command=True, description='units/time-year-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 86400)

    @year.command(aliases=['weeks'], invoke_without_command=True, description='units/time-year-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 604800)

    @year.command(aliases=['months'], invoke_without_command=True, description='units/time-year-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 2.628e6)

    @year.command(aliases=['decades'], invoke_without_command=True, description='units/time-year-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 3.154e8)

    @year.command(aliases=['centuries'], invoke_without_command=True, description='units/time-year-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 3.154e7 / 3.154e9)

    @time.group(aliases=['decades'], invoke_without_command=True, description='units/time-decade-desc')
    @lone_group(True)
    async def decade(ctx):
        pass


    @decade.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-decade-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 1e-9)

    @decade.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-decade-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 1e-6)

    @decade.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-decade-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 1e-3)

    @decade.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-decade-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 1)

    @decade.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-decade-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 60)

    @decade.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-decade-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 3600)

    @decade.command(aliases=['days'], invoke_without_command=True, description='units/time-decade-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 86400)

    @decade.command(aliases=['weeks'], invoke_without_command=True, description='units/time-decade-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 604800)

    @decade.command(aliases=['months'], invoke_without_command=True, description='units/time-decade-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 2.628e6)

    @decade.command(aliases=['years'], invoke_without_command=True, description='units/time-decade-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 3.154e7)

    @decade.command(aliases=['centuries'], invoke_without_command=True, description='units/time-decade-century-desc')
    async def century(ctx, amount: float):
        await ctx.send(amount * 3.154e8 / 3.154e9)

    @time.group(aliases=['centuries'], invoke_without_command=True, description='units/time-century-desc')
    @lone_group(True)
    async def century(ctx):
        pass


    @century.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-century-ns-desc')
    async def ns(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 1e-9)

    @century.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-century-micros-desc')
    async def micros(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 1e-6)

    @century.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-century-ms-desc')
    async def ms(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 1e-3)

    @century.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-century-s-desc')
    async def s(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 1)

    @century.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-century-min-desc')
    async def min(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 60)

    @century.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-century-h-desc')
    async def h(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 3600)

    @century.command(aliases=['days'], invoke_without_command=True, description='units/time-century-day-desc')
    async def day(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 86400)

    @century.command(aliases=['weeks'], invoke_without_command=True, description='units/time-century-week-desc')
    async def week(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 604800)

    @century.command(aliases=['months'], invoke_without_command=True, description='units/time-century-month-desc')
    async def month(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 2.628e6)

    @century.command(aliases=['years'], invoke_without_command=True, description='units/time-century-year-desc')
    async def year(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 3.154e7)

    @century.command(aliases=['decades'], invoke_without_command=True, description='units/time-century-decade-desc')
    async def decade(ctx, amount: float):
        await ctx.send(amount * 3.154e9 / 3.154e8)


    @convert.group(aliases=[], invoke_without_command=True, description='units/volume-desc')
    @lone_group(True)
    async def volume(self, ctx):
        pass


    @volume.group(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-lgallon-desc')
    @lone_group(True)
    async def lgallon(ctx):
        pass


    @lgallon.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-lgallon-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/1.057))

    @lgallon.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-lgallon-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/4.167))

    @lgallon.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-lgallon-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/4.167))

    @lgallon.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-lgallon-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/33.814))

    @lgallon.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-lgallon-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/67.628))

    @lgallon.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-lgallon-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/202.884))

    @lgallon.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-lgallon-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 1e3)

    @lgallon.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-lgallon-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 1)

    @lgallon.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-lgallon-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 1e-3)

    @lgallon.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-lgallon-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 4.546)

    @lgallon.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-lgallon-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 3.78541 / 1.3652)

    @lgallon.command(aliases=['pints'], invoke_without_command=True, description='units/volume-lgallon-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/1.76))

    @lgallon.command(aliases=['cups'], invoke_without_command=True, description='units/volume-lgallon-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/3.52))

    @lgallon.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-lgallon-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/35.195))

    @lgallon.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-lgallon-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/56.312))

    @lgallon.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-lgallon-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/168.936))

    @lgallon.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-lgallon-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/28.317))

    @lgallon.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-lgallon-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 3.78541 / (1/61.024))

    @volume.group(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-lquart-desc')
    @lone_group(True)
    async def lquart(ctx):
        pass


    @lquart.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-lquart-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 3.78541)

    @lquart.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-lquart-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/4.167))

    @lquart.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-lquart-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/4.167))

    @lquart.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-lquart-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/33.814))

    @lquart.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-lquart-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/67.628))

    @lquart.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-lquart-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/202.884))

    @lquart.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-lquart-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 1e3)

    @lquart.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-lquart-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 1)

    @lquart.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-lquart-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 1e-3)

    @lquart.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-lquart-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 4.546)

    @lquart.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-lquart-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / 1.3652)

    @lquart.command(aliases=['pints'], invoke_without_command=True, description='units/volume-lquart-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/1.76))

    @lquart.command(aliases=['cups'], invoke_without_command=True, description='units/volume-lquart-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/3.52))

    @lquart.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-lquart-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/35.195))

    @lquart.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-lquart-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/56.312))

    @lquart.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-lquart-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/168.936))

    @lquart.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-lquart-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/28.317))

    @lquart.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-lquart-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/1.057) / (1/61.024))

    @volume.group(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-lpint-desc')
    @lone_group(True)
    async def lpint(ctx):
        pass


    @lpint.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-lpint-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 3.78541)

    @lpint.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-lpint-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/1.057))

    @lpint.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-lpint-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/4.167))

    @lpint.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-lpint-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/33.814))

    @lpint.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-lpint-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/67.628))

    @lpint.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-lpint-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/202.884))

    @lpint.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-lpint-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1e3)

    @lpint.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-lpint-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1)

    @lpint.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-lpint-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1e-3)

    @lpint.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-lpint-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 4.546)

    @lpint.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-lpint-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1.3652)

    @lpint.command(aliases=['pints'], invoke_without_command=True, description='units/volume-lpint-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/1.76))

    @lpint.command(aliases=['cups'], invoke_without_command=True, description='units/volume-lpint-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/3.52))

    @lpint.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-lpint-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/35.195))

    @lpint.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-lpint-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/56.312))

    @lpint.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-lpint-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/168.936))

    @lpint.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-lpint-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/28.317))

    @lpint.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-lpint-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/61.024))

    @volume.group(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-uscup-desc')
    @lone_group(True)
    async def uscup(ctx):
        pass


    @uscup.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-uscup-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 3.78541)

    @uscup.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-uscup-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/1.057))

    @uscup.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-uscup-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/4.167))

    @uscup.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-uscup-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/33.814))

    @uscup.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-uscup-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/67.628))

    @uscup.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-uscup-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/202.884))

    @uscup.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-uscup-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1e3)

    @uscup.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-uscup-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1)

    @uscup.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-uscup-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1e-3)

    @uscup.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-uscup-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 4.546)

    @uscup.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-uscup-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / 1.3652)

    @uscup.command(aliases=['pints'], invoke_without_command=True, description='units/volume-uscup-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/1.76))

    @uscup.command(aliases=['cups'], invoke_without_command=True, description='units/volume-uscup-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/3.52))

    @uscup.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-uscup-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/35.195))

    @uscup.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-uscup-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/56.312))

    @uscup.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-uscup-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/168.936))

    @uscup.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-uscup-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/28.317))

    @uscup.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-uscup-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/4.167) / (1/61.024))

    @volume.group(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-usfloz-desc')
    @lone_group(True)
    async def usfloz(ctx):
        pass


    @usfloz.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-usfloz-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 3.78541)

    @usfloz.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-usfloz-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/1.057))

    @usfloz.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-usfloz-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/4.167))

    @usfloz.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-usfloz-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/4.167))

    @usfloz.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-usfloz-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/67.628))

    @usfloz.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-usfloz-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/202.884))

    @usfloz.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-usfloz-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 1e3)

    @usfloz.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-usfloz-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 1)

    @usfloz.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-usfloz-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 1e-3)

    @usfloz.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-usfloz-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 4.546)

    @usfloz.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-usfloz-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / 1.3652)

    @usfloz.command(aliases=['pints'], invoke_without_command=True, description='units/volume-usfloz-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/1.76))

    @usfloz.command(aliases=['cups'], invoke_without_command=True, description='units/volume-usfloz-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/3.52))

    @usfloz.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-usfloz-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/35.195))

    @usfloz.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-usfloz-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/56.312))

    @usfloz.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-usfloz-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/168.936))

    @usfloz.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-usfloz-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/28.317))

    @usfloz.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-usfloz-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/33.814) / (1/61.024))

    @volume.group(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-ustbsp-desc')
    @lone_group(True)
    async def ustbsp(ctx):
        pass


    @ustbsp.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-ustbsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 3.78541)

    @ustbsp.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-ustbsp-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/1.057))

    @ustbsp.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-ustbsp-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/4.167))

    @ustbsp.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-ustbsp-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/4.167))

    @ustbsp.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-ustbsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/33.814))

    @ustbsp.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-ustbsp-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/202.884))

    @ustbsp.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-ustbsp-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 1e3)

    @ustbsp.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-ustbsp-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 1)

    @ustbsp.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-ustbsp-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 1e-3)

    @ustbsp.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-ustbsp-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 4.546)

    @ustbsp.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-ustbsp-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / 1.3652)

    @ustbsp.command(aliases=['pints'], invoke_without_command=True, description='units/volume-ustbsp-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/1.76))

    @ustbsp.command(aliases=['cups'], invoke_without_command=True, description='units/volume-ustbsp-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/3.52))

    @ustbsp.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-ustbsp-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/35.195))

    @ustbsp.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-ustbsp-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/56.312))

    @ustbsp.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-ustbsp-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/168.936))

    @ustbsp.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-ustbsp-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/28.317))

    @ustbsp.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-ustbsp-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/67.628) / (1/61.024))

    @volume.group(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-ustsp-desc')
    @lone_group(True)
    async def ustsp(ctx):
        pass


    @ustsp.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-ustsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 3.78541)

    @ustsp.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-ustsp-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/1.057))

    @ustsp.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-ustsp-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/4.167))

    @ustsp.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-ustsp-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/4.167))

    @ustsp.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-ustsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/33.814))

    @ustsp.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-ustsp-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/67.628))

    @ustsp.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-ustsp-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 1e3)

    @ustsp.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-ustsp-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 1)

    @ustsp.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-ustsp-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 1e-3)

    @ustsp.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-ustsp-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 4.546)

    @ustsp.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-ustsp-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / 1.3652)

    @ustsp.command(aliases=['pints'], invoke_without_command=True, description='units/volume-ustsp-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/1.76))

    @ustsp.command(aliases=['cups'], invoke_without_command=True, description='units/volume-ustsp-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/3.52))

    @ustsp.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-ustsp-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/35.195))

    @ustsp.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-ustsp-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/56.312))

    @ustsp.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-ustsp-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/168.936))

    @ustsp.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-ustsp-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/28.317))

    @ustsp.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-ustsp-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/202.884) / (1/61.024))

    @volume.group(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-m3-desc')
    @lone_group(True)
    async def m3(ctx):
        pass


    @m3.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-m3-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 1e3 / 3.78541)

    @m3.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-m3-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/1.057))

    @m3.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-m3-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/4.167))

    @m3.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-m3-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/4.167))

    @m3.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-m3-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/33.814))

    @m3.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-m3-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/67.628))

    @m3.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-m3-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/202.884))

    @m3.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-m3-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1)

    @m3.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-m3-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1e-3)

    @m3.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-m3-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 1e3 / 4.546)

    @m3.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-m3-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 1e3 / 1.3652)

    @m3.command(aliases=['pints'], invoke_without_command=True, description='units/volume-m3-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/1.76))

    @m3.command(aliases=['cups'], invoke_without_command=True, description='units/volume-m3-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/3.52))

    @m3.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-m3-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/35.195))

    @m3.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-m3-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/56.312))

    @m3.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-m3-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/168.936))

    @m3.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-m3-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/28.317))

    @m3.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-m3-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 1e3 / (1/61.024))

    @volume.group(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-L-desc')
    @lone_group(True)
    async def L(ctx):
        pass


    @L.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-L-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 1 / 3.78541)

    @L.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-L-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.057))

    @L.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-L-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 1 / (1/4.167))

    @L.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-L-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 1 / (1/4.167))

    @L.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-L-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 1 / (1/33.814))

    @L.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-L-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 1 / (1/67.628))

    @L.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-L-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 1 / (1/202.884))

    @L.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-L-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 1 / 1e3)

    @L.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-L-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * 1 / 1e-3)

    @L.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-L-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 1 / 4.546)

    @L.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-L-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 1 / 1.3652)

    @L.command(aliases=['pints'], invoke_without_command=True, description='units/volume-L-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 1 / (1/1.76))

    @L.command(aliases=['cups'], invoke_without_command=True, description='units/volume-L-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 1 / (1/3.52))

    @L.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-L-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 1 / (1/35.195))

    @L.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-L-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 1 / (1/56.312))

    @L.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-L-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 1 / (1/168.936))

    @L.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-L-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 1 / (1/28.317))

    @L.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-L-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 1 / (1/61.024))

    @volume.group(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-mL-desc')
    @lone_group(True)
    async def mL(ctx):
        pass


    @mL.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-mL-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 3.78541)

    @mL.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-mL-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/1.057))

    @mL.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-mL-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/4.167))

    @mL.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-mL-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/4.167))

    @mL.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-mL-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/33.814))

    @mL.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-mL-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/67.628))

    @mL.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-mL-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/202.884))

    @mL.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-mL-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1e3)

    @mL.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-mL-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1)

    @mL.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-mL-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 4.546)

    @mL.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-mL-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 1e-3 / 1.3652)

    @mL.command(aliases=['pints'], invoke_without_command=True, description='units/volume-mL-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/1.76))

    @mL.command(aliases=['cups'], invoke_without_command=True, description='units/volume-mL-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/3.52))

    @mL.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-mL-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/35.195))

    @mL.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-mL-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/56.312))

    @mL.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-mL-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/168.936))

    @mL.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-mL-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/28.317))

    @mL.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-mL-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 1e-3 / (1/61.024))

    @volume.group(aliases=['gallons'], invoke_without_command=True, description='units/volume-gallon-desc')
    @lone_group(True)
    async def gallon(ctx):
        pass


    @gallon.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-gallon-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 4.546 / 3.78541)

    @gallon.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-gallon-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/1.057))

    @gallon.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-gallon-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/4.167))

    @gallon.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-gallon-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/4.167))

    @gallon.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-gallon-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/33.814))

    @gallon.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-gallon-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/67.628))

    @gallon.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-gallon-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/202.884))

    @gallon.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-gallon-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 4.546 / 1e3)

    @gallon.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-gallon-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * 4.546 / 1)

    @gallon.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-gallon-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * 4.546 / 1e-3)

    @gallon.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-gallon-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * 4.546 / 1.3652)

    @gallon.command(aliases=['pints'], invoke_without_command=True, description='units/volume-gallon-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/1.76))

    @gallon.command(aliases=['cups'], invoke_without_command=True, description='units/volume-gallon-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/3.52))

    @gallon.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-gallon-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/35.195))

    @gallon.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-gallon-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/56.312))

    @gallon.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-gallon-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/168.936))

    @gallon.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-gallon-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/28.317))

    @gallon.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-gallon-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 4.546 / (1/61.024))

    @volume.group(aliases=['quarts'], invoke_without_command=True, description='units/volume-quart-desc')
    @lone_group(True)
    async def quart(ctx):
        pass


    @quart.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-quart-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 3.78541)

    @quart.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-quart-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/1.057))

    @quart.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-quart-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/4.167))

    @quart.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-quart-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/4.167))

    @quart.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-quart-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/33.814))

    @quart.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-quart-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/67.628))

    @quart.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-quart-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/202.884))

    @quart.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-quart-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 1e3)

    @quart.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-quart-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 1)

    @quart.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-quart-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 1e-3)

    @quart.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-quart-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * 1.3652 / 4.546)

    @quart.command(aliases=['pints'], invoke_without_command=True, description='units/volume-quart-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/1.76))

    @quart.command(aliases=['cups'], invoke_without_command=True, description='units/volume-quart-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/3.52))

    @quart.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-quart-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/35.195))

    @quart.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-quart-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/56.312))

    @quart.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-quart-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/168.936))

    @quart.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-quart-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/28.317))

    @quart.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-quart-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * 1.3652 / (1/61.024))

    @volume.group(aliases=['pints'], invoke_without_command=True, description='units/volume-pint-desc')
    @lone_group(True)
    async def pint(ctx):
        pass


    @pint.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-pint-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 3.78541)

    @pint.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-pint-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/1.057))

    @pint.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-pint-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/4.167))

    @pint.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-pint-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/4.167))

    @pint.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-pint-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/33.814))

    @pint.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-pint-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/67.628))

    @pint.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-pint-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/202.884))

    @pint.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-pint-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 1e3)

    @pint.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-pint-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 1)

    @pint.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-pint-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 1e-3)

    @pint.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-pint-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 4.546)

    @pint.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-pint-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / 1.3652)

    @pint.command(aliases=['cups'], invoke_without_command=True, description='units/volume-pint-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/3.52))

    @pint.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-pint-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/35.195))

    @pint.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-pint-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/56.312))

    @pint.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-pint-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/168.936))

    @pint.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-pint-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/28.317))

    @pint.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-pint-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/1.76) / (1/61.024))

    @volume.group(aliases=['cups'], invoke_without_command=True, description='units/volume-cup-desc')
    @lone_group(True)
    async def cup(ctx):
        pass


    @cup.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-cup-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 3.78541)

    @cup.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-cup-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/1.057))

    @cup.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-cup-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/4.167))

    @cup.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-cup-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/4.167))

    @cup.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-cup-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/33.814))

    @cup.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-cup-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/67.628))

    @cup.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-cup-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/202.884))

    @cup.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-cup-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 1e3)

    @cup.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-cup-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 1)

    @cup.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-cup-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 1e-3)

    @cup.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-cup-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 4.546)

    @cup.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-cup-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / 1.3652)

    @cup.command(aliases=['pints'], invoke_without_command=True, description='units/volume-cup-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/1.76))

    @cup.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-cup-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/35.195))

    @cup.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-cup-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/56.312))

    @cup.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-cup-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/168.936))

    @cup.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-cup-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/28.317))

    @cup.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-cup-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/3.52) / (1/61.024))

    @volume.group(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-floz-desc')
    @lone_group(True)
    async def floz(ctx):
        pass


    @floz.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-floz-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 3.78541)

    @floz.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-floz-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/1.057))

    @floz.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-floz-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/4.167))

    @floz.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-floz-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/4.167))

    @floz.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-floz-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/33.814))

    @floz.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-floz-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/67.628))

    @floz.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-floz-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/202.884))

    @floz.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-floz-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 1e3)

    @floz.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-floz-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 1)

    @floz.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-floz-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 1e-3)

    @floz.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-floz-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 4.546)

    @floz.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-floz-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / 1.3652)

    @floz.command(aliases=['pints'], invoke_without_command=True, description='units/volume-floz-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/1.76))

    @floz.command(aliases=['cups'], invoke_without_command=True, description='units/volume-floz-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/3.52))

    @floz.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-floz-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/56.312))

    @floz.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-floz-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/168.936))

    @floz.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-floz-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/28.317))

    @floz.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-floz-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/35.195) / (1/61.024))

    @volume.group(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-tbsp-desc')
    @lone_group(True)
    async def tbsp(ctx):
        pass


    @tbsp.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-tbsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 3.78541)

    @tbsp.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-tbsp-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/1.057))

    @tbsp.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-tbsp-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/4.167))

    @tbsp.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-tbsp-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/4.167))

    @tbsp.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-tbsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/33.814))

    @tbsp.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-tbsp-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/67.628))

    @tbsp.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-tbsp-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/202.884))

    @tbsp.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-tbsp-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 1e3)

    @tbsp.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-tbsp-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 1)

    @tbsp.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-tbsp-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 1e-3)

    @tbsp.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-tbsp-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 4.546)

    @tbsp.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-tbsp-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / 1.3652)

    @tbsp.command(aliases=['pints'], invoke_without_command=True, description='units/volume-tbsp-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/1.76))

    @tbsp.command(aliases=['cups'], invoke_without_command=True, description='units/volume-tbsp-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/3.52))

    @tbsp.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-tbsp-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/35.195))

    @tbsp.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-tbsp-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/168.936))

    @tbsp.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-tbsp-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/28.317))

    @tbsp.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-tbsp-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/56.312) / (1/61.024))

    @volume.group(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-tsp-desc')
    @lone_group(True)
    async def tsp(ctx):
        pass


    @tsp.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-tsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 3.78541)

    @tsp.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-tsp-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/1.057))

    @tsp.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-tsp-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/4.167))

    @tsp.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-tsp-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/4.167))

    @tsp.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-tsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/33.814))

    @tsp.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-tsp-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/67.628))

    @tsp.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-tsp-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/202.884))

    @tsp.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-tsp-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 1e3)

    @tsp.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-tsp-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 1)

    @tsp.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-tsp-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 1e-3)

    @tsp.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-tsp-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 4.546)

    @tsp.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-tsp-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / 1.3652)

    @tsp.command(aliases=['pints'], invoke_without_command=True, description='units/volume-tsp-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/1.76))

    @tsp.command(aliases=['cups'], invoke_without_command=True, description='units/volume-tsp-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/3.52))

    @tsp.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-tsp-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/35.195))

    @tsp.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-tsp-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/56.312))

    @tsp.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-tsp-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/28.317))

    @tsp.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-tsp-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/168.936) / (1/61.024))

    @volume.group(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-ft3-desc')
    @lone_group(True)
    async def ft3(ctx):
        pass


    @ft3.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-ft3-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 3.78541)

    @ft3.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-ft3-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/1.057))

    @ft3.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-ft3-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/4.167))

    @ft3.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-ft3-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/4.167))

    @ft3.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-ft3-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/33.814))

    @ft3.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-ft3-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/67.628))

    @ft3.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-ft3-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/202.884))

    @ft3.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-ft3-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 1e3)

    @ft3.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-ft3-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 1)

    @ft3.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-ft3-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 1e-3)

    @ft3.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-ft3-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 4.546)

    @ft3.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-ft3-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / 1.3652)

    @ft3.command(aliases=['pints'], invoke_without_command=True, description='units/volume-ft3-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/1.76))

    @ft3.command(aliases=['cups'], invoke_without_command=True, description='units/volume-ft3-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/3.52))

    @ft3.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-ft3-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/35.195))

    @ft3.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-ft3-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/56.312))

    @ft3.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-ft3-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/168.936))

    @ft3.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-ft3-in3-desc')
    async def in3(ctx, amount: float):
        await ctx.send(amount * (1/28.317) / (1/61.024))

    @volume.group(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-in3-desc')
    @lone_group(True)
    async def in3(ctx):
        pass


    @in3.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-in3-lgallon-desc')
    async def lgallon(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 3.78541)

    @in3.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-in3-lquart-desc')
    async def lquart(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/1.057))

    @in3.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-in3-lpint-desc')
    async def lpint(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/4.167))

    @in3.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-in3-uscup-desc')
    async def uscup(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/4.167))

    @in3.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-in3-usfloz-desc')
    async def usfloz(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/33.814))

    @in3.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-in3-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/67.628))

    @in3.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-in3-ustsp-desc')
    async def ustsp(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/202.884))

    @in3.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-in3-m3-desc')
    async def m3(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 1e3)

    @in3.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-in3-L-desc')
    async def L(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 1)

    @in3.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-in3-mL-desc')
    async def mL(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 1e-3)

    @in3.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-in3-gallon-desc')
    async def gallon(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 4.546)

    @in3.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-in3-quart-desc')
    async def quart(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / 1.3652)

    @in3.command(aliases=['pints'], invoke_without_command=True, description='units/volume-in3-pint-desc')
    async def pint(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/1.76))

    @in3.command(aliases=['cups'], invoke_without_command=True, description='units/volume-in3-cup-desc')
    async def cup(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/3.52))

    @in3.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-in3-floz-desc')
    async def floz(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/35.195))

    @in3.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-in3-tbsp-desc')
    async def tbsp(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/56.312))

    @in3.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-in3-tsp-desc')
    async def tsp(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/168.936))

    @in3.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-in3-ft3-desc')
    async def ft3(ctx, amount: float):
        await ctx.send(amount * (1/61.024) / (1/28.317))

