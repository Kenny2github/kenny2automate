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
    async def sqkm(self, ctx):
        pass


    @sqkm.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqkm-sqm-desc')
    async def sqm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqm

    @sqkm.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqkm-sqmil-desc')
    async def sqmil(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 2.59e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqmil

    @sqkm.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqkm-sqyard-desc')
    async def sqyard(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1/1.196))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqyard

    @sqkm.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqkm-sqft-desc')
    async def sqft(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1/10.764))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqft

    @sqkm.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqkm-sqin-desc')
    async def sqin(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1/1550.003))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqin

    @sqkm.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqkm-hectare-desc')
    async def hectare(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 10000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del hectare

    @sqkm.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqkm-acre-desc')
    async def acre(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 4046.856)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del acre

    @area.group(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqm-desc')
    @lone_group(True)
    async def sqm(self, ctx):
        pass


    @sqm.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqm-sqkm-desc')
    async def sqkm(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqkm

    @sqm.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqm-sqmil-desc')
    async def sqmil(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 2.59e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqmil

    @sqm.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqm-sqyard-desc')
    async def sqyard(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/1.196))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqyard

    @sqm.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqm-sqft-desc')
    async def sqft(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/10.764))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqft

    @sqm.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqm-sqin-desc')
    async def sqin(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/1550.003))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqin

    @sqm.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqm-hectare-desc')
    async def hectare(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 10000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del hectare

    @sqm.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqm-acre-desc')
    async def acre(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 4046.856)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del acre

    @area.group(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqmil-desc')
    @lone_group(True)
    async def sqmil(self, ctx):
        pass


    @sqmil.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqmil-sqkm-desc')
    async def sqkm(ctx, amount: float):
        try:
            await ctx.send(amount * 2.59e6 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqkm

    @sqmil.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqmil-sqm-desc')
    async def sqm(ctx, amount: float):
        try:
            await ctx.send(amount * 2.59e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqm

    @sqmil.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqmil-sqyard-desc')
    async def sqyard(ctx, amount: float):
        try:
            await ctx.send(amount * 2.59e6 / (1/1.196))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqyard

    @sqmil.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqmil-sqft-desc')
    async def sqft(ctx, amount: float):
        try:
            await ctx.send(amount * 2.59e6 / (1/10.764))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqft

    @sqmil.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqmil-sqin-desc')
    async def sqin(ctx, amount: float):
        try:
            await ctx.send(amount * 2.59e6 / (1/1550.003))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqin

    @sqmil.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqmil-hectare-desc')
    async def hectare(ctx, amount: float):
        try:
            await ctx.send(amount * 2.59e6 / 10000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del hectare

    @sqmil.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqmil-acre-desc')
    async def acre(ctx, amount: float):
        try:
            await ctx.send(amount * 2.59e6 / 4046.856)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del acre

    @area.group(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqyard-desc')
    @lone_group(True)
    async def sqyard(self, ctx):
        pass


    @sqyard.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqyard-sqkm-desc')
    async def sqkm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.196) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqkm

    @sqyard.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqyard-sqm-desc')
    async def sqm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.196) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqm

    @sqyard.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqyard-sqmil-desc')
    async def sqmil(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.196) / 2.59e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqmil

    @sqyard.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqyard-sqft-desc')
    async def sqft(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.196) / (1/10.764))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqft

    @sqyard.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqyard-sqin-desc')
    async def sqin(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.196) / (1/1550.003))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqin

    @sqyard.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqyard-hectare-desc')
    async def hectare(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.196) / 10000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del hectare

    @sqyard.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqyard-acre-desc')
    async def acre(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.196) / 4046.856)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del acre

    @area.group(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqft-desc')
    @lone_group(True)
    async def sqft(self, ctx):
        pass


    @sqft.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqft-sqkm-desc')
    async def sqkm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/10.764) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqkm

    @sqft.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqft-sqm-desc')
    async def sqm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/10.764) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqm

    @sqft.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqft-sqmil-desc')
    async def sqmil(ctx, amount: float):
        try:
            await ctx.send(amount * (1/10.764) / 2.59e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqmil

    @sqft.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqft-sqyard-desc')
    async def sqyard(ctx, amount: float):
        try:
            await ctx.send(amount * (1/10.764) / (1/1.196))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqyard

    @sqft.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqft-sqin-desc')
    async def sqin(ctx, amount: float):
        try:
            await ctx.send(amount * (1/10.764) / (1/1550.003))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqin

    @sqft.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqft-hectare-desc')
    async def hectare(ctx, amount: float):
        try:
            await ctx.send(amount * (1/10.764) / 10000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del hectare

    @sqft.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqft-acre-desc')
    async def acre(ctx, amount: float):
        try:
            await ctx.send(amount * (1/10.764) / 4046.856)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del acre

    @area.group(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-sqin-desc')
    @lone_group(True)
    async def sqin(self, ctx):
        pass


    @sqin.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-sqin-sqkm-desc')
    async def sqkm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1550.003) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqkm

    @sqin.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-sqin-sqm-desc')
    async def sqm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1550.003) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqm

    @sqin.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-sqin-sqmil-desc')
    async def sqmil(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1550.003) / 2.59e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqmil

    @sqin.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-sqin-sqyard-desc')
    async def sqyard(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1550.003) / (1/1.196))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqyard

    @sqin.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-sqin-sqft-desc')
    async def sqft(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1550.003) / (1/10.764))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqft

    @sqin.command(aliases=['hectares'], invoke_without_command=True, description='units/area-sqin-hectare-desc')
    async def hectare(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1550.003) / 10000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del hectare

    @sqin.command(aliases=['acres'], invoke_without_command=True, description='units/area-sqin-acre-desc')
    async def acre(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1550.003) / 4046.856)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del acre

    @area.group(aliases=['hectares'], invoke_without_command=True, description='units/area-hectare-desc')
    @lone_group(True)
    async def hectare(self, ctx):
        pass


    @hectare.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-hectare-sqkm-desc')
    async def sqkm(ctx, amount: float):
        try:
            await ctx.send(amount * 10000 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqkm

    @hectare.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-hectare-sqm-desc')
    async def sqm(ctx, amount: float):
        try:
            await ctx.send(amount * 10000 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqm

    @hectare.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-hectare-sqmil-desc')
    async def sqmil(ctx, amount: float):
        try:
            await ctx.send(amount * 10000 / 2.59e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqmil

    @hectare.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-hectare-sqyard-desc')
    async def sqyard(ctx, amount: float):
        try:
            await ctx.send(amount * 10000 / (1/1.196))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqyard

    @hectare.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-hectare-sqft-desc')
    async def sqft(ctx, amount: float):
        try:
            await ctx.send(amount * 10000 / (1/10.764))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqft

    @hectare.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-hectare-sqin-desc')
    async def sqin(ctx, amount: float):
        try:
            await ctx.send(amount * 10000 / (1/1550.003))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqin

    @hectare.command(aliases=['acres'], invoke_without_command=True, description='units/area-hectare-acre-desc')
    async def acre(ctx, amount: float):
        try:
            await ctx.send(amount * 10000 / 4046.856)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del acre

    @area.group(aliases=['acres'], invoke_without_command=True, description='units/area-acre-desc')
    @lone_group(True)
    async def acre(self, ctx):
        pass


    @acre.command(aliases=['square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], invoke_without_command=True, description='units/area-acre-sqkm-desc')
    async def sqkm(ctx, amount: float):
        try:
            await ctx.send(amount * 4046.856 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqkm

    @acre.command(aliases=['square-meters', 'square-metres', 'square-meter', 'square-metre'], invoke_without_command=True, description='units/area-acre-sqm-desc')
    async def sqm(ctx, amount: float):
        try:
            await ctx.send(amount * 4046.856 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqm

    @acre.command(aliases=['square-miles', 'square-mile'], invoke_without_command=True, description='units/area-acre-sqmil-desc')
    async def sqmil(ctx, amount: float):
        try:
            await ctx.send(amount * 4046.856 / 2.59e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqmil

    @acre.command(aliases=['square-yards', 'square-yard'], invoke_without_command=True, description='units/area-acre-sqyard-desc')
    async def sqyard(ctx, amount: float):
        try:
            await ctx.send(amount * 4046.856 / (1/1.196))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqyard

    @acre.command(aliases=['square-feet', 'square-foot'], invoke_without_command=True, description='units/area-acre-sqft-desc')
    async def sqft(ctx, amount: float):
        try:
            await ctx.send(amount * 4046.856 / (1/10.764))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqft

    @acre.command(aliases=['square-inches', 'square-inch'], invoke_without_command=True, description='units/area-acre-sqin-desc')
    async def sqin(ctx, amount: float):
        try:
            await ctx.send(amount * 4046.856 / (1/1550.003))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del sqin

    @acre.command(aliases=['hectares'], invoke_without_command=True, description='units/area-acre-hectare-desc')
    async def hectare(ctx, amount: float):
        try:
            await ctx.send(amount * 4046.856 / 10000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del hectare


    @convert.group(aliases=[], invoke_without_command=True, description='units/data-desc')
    @lone_group(True)
    async def data(self, ctx):
        pass


    @data.group(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-bps-desc')
    @lone_group(True)
    async def bps(self, ctx):
        pass


    @bps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-bps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @bps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-bps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @bps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-bps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @bps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-bps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @bps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-bps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @bps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-bps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @bps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-bps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @bps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-bps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @bps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-bps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @bps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-bps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @bps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-bps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @bps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-bps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-kbps-desc')
    @lone_group(True)
    async def kbps(self, ctx):
        pass


    @kbps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-kbps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @kbps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-kbps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @kbps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-kbps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @kbps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-kbps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @kbps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-kbps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @kbps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-kbps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @kbps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-kbps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @kbps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-kbps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @kbps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-kbps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @kbps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-kbps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @kbps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-kbps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @kbps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-kbps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-KBps-desc')
    @lone_group(True)
    async def KBps(self, ctx):
        pass


    @KBps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-KBps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @KBps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-KBps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @KBps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-KBps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @KBps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-KBps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @KBps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-KBps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @KBps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-KBps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @KBps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-KBps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @KBps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-KBps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @KBps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-KBps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @KBps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-KBps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @KBps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-KBps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @KBps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-KBps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-kibps-desc')
    @lone_group(True)
    async def kibps(self, ctx):
        pass


    @kibps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-kibps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @kibps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-kibps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @kibps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-kibps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @kibps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-kibps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @kibps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-kibps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @kibps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-kibps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @kibps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-kibps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @kibps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-kibps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @kibps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-kibps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @kibps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-kibps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @kibps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-kibps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @kibps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-kibps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-mbps-desc')
    @lone_group(True)
    async def mbps(self, ctx):
        pass


    @mbps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-mbps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @mbps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-mbps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @mbps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-mbps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @mbps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-mbps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @mbps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-mbps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @mbps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-mbps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @mbps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-mbps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @mbps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-mbps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @mbps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-mbps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @mbps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-mbps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @mbps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-mbps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @mbps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-mbps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-MBps-desc')
    @lone_group(True)
    async def MBps(self, ctx):
        pass


    @MBps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-MBps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @MBps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-MBps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @MBps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-MBps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @MBps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-MBps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @MBps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-MBps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @MBps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-MBps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @MBps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-MBps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @MBps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-MBps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @MBps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-MBps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @MBps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-MBps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @MBps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-MBps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @MBps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-MBps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-mibps-desc')
    @lone_group(True)
    async def mibps(self, ctx):
        pass


    @mibps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-mibps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @mibps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-mibps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @mibps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-mibps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @mibps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-mibps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @mibps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-mibps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @mibps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-mibps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @mibps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-mibps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @mibps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-mibps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @mibps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-mibps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @mibps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-mibps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @mibps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-mibps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @mibps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-mibps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-gbps-desc')
    @lone_group(True)
    async def gbps(self, ctx):
        pass


    @gbps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-gbps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @gbps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-gbps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @gbps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-gbps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @gbps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-gbps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @gbps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-gbps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @gbps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-gbps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @gbps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-gbps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @gbps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-gbps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @gbps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-gbps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @gbps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-gbps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @gbps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-gbps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @gbps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-gbps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-GBps-desc')
    @lone_group(True)
    async def GBps(self, ctx):
        pass


    @GBps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-GBps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @GBps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-GBps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @GBps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-GBps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @GBps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-GBps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @GBps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-GBps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @GBps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-GBps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @GBps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-GBps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @GBps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-GBps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @GBps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-GBps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @GBps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-GBps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @GBps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-GBps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @GBps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-GBps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-gibps-desc')
    @lone_group(True)
    async def gibps(self, ctx):
        pass


    @gibps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-gibps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @gibps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-gibps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @gibps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-gibps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @gibps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-gibps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @gibps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-gibps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @gibps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-gibps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @gibps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-gibps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @gibps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-gibps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @gibps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-gibps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @gibps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-gibps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @gibps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-gibps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @gibps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-gibps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-tbps-desc')
    @lone_group(True)
    async def tbps(self, ctx):
        pass


    @tbps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-tbps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @tbps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-tbps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @tbps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-tbps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @tbps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-tbps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @tbps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-tbps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @tbps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-tbps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @tbps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-tbps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @tbps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-tbps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @tbps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-tbps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @tbps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-tbps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @tbps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-tbps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps

    @tbps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-tbps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-TBps-desc')
    @lone_group(True)
    async def TBps(self, ctx):
        pass


    @TBps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-TBps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @TBps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-TBps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @TBps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-TBps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @TBps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-TBps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @TBps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-TBps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @TBps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-TBps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @TBps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-TBps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @TBps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-TBps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @TBps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-TBps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @TBps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-TBps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @TBps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-TBps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @TBps.command(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-TBps-tibps-desc')
    async def tibps(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tibps

    @data.group(aliases=['tebibit-per-second', 'tebibits-per-second'], invoke_without_command=True, description='units/data-tibps-desc')
    @lone_group(True)
    async def tibps(self, ctx):
        pass


    @tibps.command(aliases=['bit-per-second', 'bits-per-second'], invoke_without_command=True, description='units/data-tibps-bps-desc')
    async def bps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bps

    @tibps.command(aliases=['kilobit-per-second', 'kilobits-per-second'], invoke_without_command=True, description='units/data-tibps-kbps-desc')
    async def kbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kbps

    @tibps.command(aliases=['kilobyte-per-second', 'kilobytes-per-second'], invoke_without_command=True, description='units/data-tibps-KBps-desc')
    async def KBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KBps

    @tibps.command(aliases=['kibibit-per-second', 'kibibits-per-second'], invoke_without_command=True, description='units/data-tibps-kibps-desc')
    async def kibps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kibps

    @tibps.command(aliases=['megabit-per-second', 'megabits-per-second'], invoke_without_command=True, description='units/data-tibps-mbps-desc')
    async def mbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mbps

    @tibps.command(aliases=['megabyte-per-second', 'megabytes-per-second'], invoke_without_command=True, description='units/data-tibps-MBps-desc')
    async def MBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MBps

    @tibps.command(aliases=['mebibit-per-second', 'mebibits-per-second'], invoke_without_command=True, description='units/data-tibps-mibps-desc')
    async def mibps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mibps

    @tibps.command(aliases=['gigabit-per-second', 'gigabits-per-second'], invoke_without_command=True, description='units/data-tibps-gbps-desc')
    async def gbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gbps

    @tibps.command(aliases=['gigabyte-per-second', 'gigabytes-per-second'], invoke_without_command=True, description='units/data-tibps-GBps-desc')
    async def GBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GBps

    @tibps.command(aliases=['gigibit-per-second', 'gigibits-per-second'], invoke_without_command=True, description='units/data-tibps-gibps-desc')
    async def gibps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gibps

    @tibps.command(aliases=['terabit-per-second', 'terabits-per-second'], invoke_without_command=True, description='units/data-tibps-tbps-desc')
    async def tbps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbps

    @tibps.command(aliases=['terabyte-per-second', 'terabytes-per-second'], invoke_without_command=True, description='units/data-tibps-TBps-desc')
    async def TBps(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TBps


    @convert.group(aliases=[], invoke_without_command=True, description='units/storage-desc')
    @lone_group(True)
    async def storage(self, ctx):
        pass


    @storage.group(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-b-desc')
    @lone_group(True)
    async def b(self, ctx):
        pass


    @b.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-b-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @b.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-b-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @b.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-b-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @b.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-b-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @b.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-b-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @b.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-b-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @b.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-b-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @b.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-b-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @b.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-b-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @b.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-b-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @b.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-b-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @b.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-b-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @b.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-b-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @b.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-b-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @b.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-b-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @b.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-b-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @b.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-b-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @b.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-b-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @b.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-b-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @b.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-b-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @b.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-b-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-kb-desc')
    @lone_group(True)
    async def kb(self, ctx):
        pass


    @kb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-kb-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @kb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-kb-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @kb.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-kb-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @kb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-kb-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @kb.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-kb-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @kb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-kb-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @kb.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-kb-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @kb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-kb-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @kb.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-kb-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @kb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-kb-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @kb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-kb-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @kb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-kb-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @kb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-kb-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @kb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-kb-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @kb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-kb-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @kb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-kb-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @kb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-kb-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @kb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-kb-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @kb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-kb-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @kb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-kb-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @kb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-kb-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-kib-desc')
    @lone_group(True)
    async def kib(self, ctx):
        pass


    @kib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-kib-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @kib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-kib-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @kib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-kib-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @kib.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-kib-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @kib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-kib-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @kib.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-kib-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @kib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-kib-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @kib.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-kib-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @kib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-kib-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @kib.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-kib-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @kib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-kib-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @kib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-kib-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @kib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-kib-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @kib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-kib-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @kib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-kib-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @kib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-kib-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @kib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-kib-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @kib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-kib-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @kib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-kib-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @kib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-kib-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @kib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-kib-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1024 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-mb-desc')
    @lone_group(True)
    async def mb(self, ctx):
        pass


    @mb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-mb-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @mb.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-mb-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @mb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-mb-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @mb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-mb-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @mb.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-mb-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @mb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-mb-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @mb.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-mb-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @mb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-mb-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @mb.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-mb-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @mb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-mb-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @mb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-mb-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @mb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-mb-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @mb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-mb-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @mb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-mb-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @mb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-mb-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @mb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-mb-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @mb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-mb-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @mb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-mb-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @mb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-mb-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @mb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-mb-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @mb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-mb-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-mib-desc')
    @lone_group(True)
    async def mib(self, ctx):
        pass


    @mib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-mib-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @mib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-mib-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @mib.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-mib-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @mib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-mib-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @mib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-mib-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @mib.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-mib-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @mib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-mib-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @mib.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-mib-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @mib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-mib-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @mib.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-mib-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @mib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-mib-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @mib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-mib-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @mib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-mib-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @mib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-mib-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @mib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-mib-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @mib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-mib-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @mib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-mib-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @mib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-mib-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @mib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-mib-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @mib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-mib-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @mib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-mib-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**2) / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-gb-desc')
    @lone_group(True)
    async def gb(self, ctx):
        pass


    @gb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-gb-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @gb.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-gb-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @gb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-gb-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @gb.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-gb-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @gb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-gb-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @gb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-gb-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @gb.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-gb-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @gb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-gb-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @gb.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-gb-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @gb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-gb-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @gb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-gb-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @gb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-gb-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @gb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-gb-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @gb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-gb-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @gb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-gb-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @gb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-gb-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @gb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-gb-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @gb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-gb-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @gb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-gb-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @gb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-gb-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @gb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-gb-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-gib-desc')
    @lone_group(True)
    async def gib(self, ctx):
        pass


    @gib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-gib-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @gib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-gib-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @gib.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-gib-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @gib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-gib-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @gib.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-gib-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @gib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-gib-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @gib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-gib-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @gib.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-gib-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @gib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-gib-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @gib.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-gib-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @gib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-gib-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @gib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-gib-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @gib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-gib-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @gib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-gib-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @gib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-gib-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @gib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-gib-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @gib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-gib-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @gib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-gib-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @gib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-gib-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @gib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-gib-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @gib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-gib-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**3) / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-tb-desc')
    @lone_group(True)
    async def tb(self, ctx):
        pass


    @tb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-tb-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @tb.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-tb-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @tb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-tb-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @tb.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-tb-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @tb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-tb-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @tb.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-tb-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @tb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-tb-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @tb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-tb-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @tb.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-tb-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @tb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-tb-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @tb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-tb-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @tb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-tb-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @tb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-tb-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @tb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-tb-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @tb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-tb-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @tb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-tb-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @tb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-tb-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @tb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-tb-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @tb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-tb-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @tb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-tb-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @tb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-tb-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e12 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-tib-desc')
    @lone_group(True)
    async def tib(self, ctx):
        pass


    @tib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-tib-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @tib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-tib-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @tib.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-tib-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @tib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-tib-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @tib.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-tib-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @tib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-tib-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @tib.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-tib-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @tib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-tib-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @tib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-tib-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @tib.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-tib-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @tib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-tib-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @tib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-tib-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @tib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-tib-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @tib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-tib-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @tib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-tib-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @tib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-tib-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @tib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-tib-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @tib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-tib-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @tib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-tib-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @tib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-tib-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @tib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-tib-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**4) / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-pb-desc')
    @lone_group(True)
    async def pb(self, ctx):
        pass


    @pb.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-pb-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @pb.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-pb-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @pb.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-pb-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @pb.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-pb-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @pb.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-pb-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @pb.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-pb-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @pb.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-pb-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @pb.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-pb-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @pb.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-pb-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @pb.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-pb-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @pb.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-pb-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @pb.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-pb-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @pb.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-pb-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @pb.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-pb-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @pb.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-pb-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @pb.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-pb-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @pb.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-pb-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @pb.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-pb-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @pb.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-pb-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @pb.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-pb-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @pb.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-pb-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 1e15 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-pib-desc')
    @lone_group(True)
    async def pib(self, ctx):
        pass


    @pib.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-pib-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @pib.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-pib-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @pib.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-pib-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @pib.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-pib-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @pib.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-pib-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @pib.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-pib-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @pib.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-pib-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @pib.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-pib-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @pib.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-pib-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @pib.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-pib-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @pib.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-pib-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @pib.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-pib-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @pib.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-pib-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @pib.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-pib-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @pib.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-pib-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @pib.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-pib-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @pib.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-pib-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @pib.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-pib-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @pib.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-pib-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @pib.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-pib-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @pib.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-pib-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * (1024**5) / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-B-desc')
    @lone_group(True)
    async def B(self, ctx):
        pass


    @B.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-B-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @B.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-B-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @B.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-B-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @B.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-B-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @B.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-B-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @B.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-B-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @B.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-B-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @B.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-B-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @B.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-B-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @B.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-B-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @B.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-B-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @B.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-B-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @B.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-B-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @B.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-B-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @B.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-B-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @B.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-B-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @B.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-B-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @B.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-B-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @B.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-B-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @B.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-B-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @B.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-B-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-KB-desc')
    @lone_group(True)
    async def KB(self, ctx):
        pass


    @KB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-KB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @KB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-KB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @KB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-KB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @KB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-KB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @KB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-KB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @KB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-KB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @KB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-KB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @KB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-KB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @KB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-KB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @KB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-KB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @KB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-KB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @KB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-KB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @KB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-KB-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @KB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-KB-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @KB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-KB-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @KB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-KB-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @KB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-KB-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @KB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-KB-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @KB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-KB-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @KB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-KB-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @KB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-KB-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e3 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-KiB-desc')
    @lone_group(True)
    async def KiB(self, ctx):
        pass


    @KiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-KiB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @KiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-KiB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @KiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-KiB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @KiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-KiB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @KiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-KiB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @KiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-KiB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @KiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-KiB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @KiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-KiB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @KiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-KiB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @KiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-KiB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @KiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-KiB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @KiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-KiB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @KiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-KiB-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @KiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-KiB-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @KiB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-KiB-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @KiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-KiB-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @KiB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-KiB-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @KiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-KiB-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @KiB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-KiB-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @KiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-KiB-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @KiB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-KiB-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024) / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-MB-desc')
    @lone_group(True)
    async def MB(self, ctx):
        pass


    @MB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-MB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @MB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-MB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @MB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-MB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @MB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-MB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @MB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-MB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @MB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-MB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @MB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-MB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @MB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-MB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @MB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-MB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @MB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-MB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @MB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-MB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @MB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-MB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @MB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-MB-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @MB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-MB-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @MB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-MB-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @MB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-MB-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @MB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-MB-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @MB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-MB-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @MB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-MB-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @MB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-MB-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @MB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-MB-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e6 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-MiB-desc')
    @lone_group(True)
    async def MiB(self, ctx):
        pass


    @MiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-MiB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @MiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-MiB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @MiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-MiB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @MiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-MiB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @MiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-MiB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @MiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-MiB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @MiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-MiB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @MiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-MiB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @MiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-MiB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @MiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-MiB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @MiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-MiB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @MiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-MiB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @MiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-MiB-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @MiB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-MiB-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @MiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-MiB-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @MiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-MiB-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @MiB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-MiB-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @MiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-MiB-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @MiB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-MiB-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @MiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-MiB-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @MiB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-MiB-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 2) / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-GB-desc')
    @lone_group(True)
    async def GB(self, ctx):
        pass


    @GB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-GB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @GB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-GB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @GB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-GB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @GB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-GB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @GB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-GB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @GB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-GB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @GB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-GB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @GB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-GB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @GB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-GB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @GB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-GB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @GB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-GB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @GB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-GB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @GB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-GB-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @GB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-GB-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @GB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-GB-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @GB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-GB-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @GB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-GB-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @GB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-GB-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @GB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-GB-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @GB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-GB-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @GB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-GB-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e9 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-GiB-desc')
    @lone_group(True)
    async def GiB(self, ctx):
        pass


    @GiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-GiB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @GiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-GiB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @GiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-GiB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @GiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-GiB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @GiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-GiB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @GiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-GiB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @GiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-GiB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @GiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-GiB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @GiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-GiB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @GiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-GiB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @GiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-GiB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @GiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-GiB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @GiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-GiB-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @GiB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-GiB-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @GiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-GiB-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @GiB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-GiB-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @GiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-GiB-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @GiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-GiB-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @GiB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-GiB-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @GiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-GiB-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @GiB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-GiB-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 3) / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-TB-desc')
    @lone_group(True)
    async def TB(self, ctx):
        pass


    @TB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-TB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @TB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-TB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @TB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-TB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @TB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-TB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @TB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-TB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @TB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-TB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @TB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-TB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @TB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-TB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @TB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-TB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @TB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-TB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @TB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-TB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @TB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-TB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @TB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-TB-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @TB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-TB-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @TB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-TB-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @TB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-TB-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @TB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-TB-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @TB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-TB-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @TB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-TB-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @TB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-TB-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @TB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-TB-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e12 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-TiB-desc')
    @lone_group(True)
    async def TiB(self, ctx):
        pass


    @TiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-TiB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @TiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-TiB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @TiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-TiB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @TiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-TiB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @TiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-TiB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @TiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-TiB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @TiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-TiB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @TiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-TiB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @TiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-TiB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @TiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-TiB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @TiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-TiB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @TiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-TiB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @TiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-TiB-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @TiB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-TiB-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @TiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-TiB-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @TiB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-TiB-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @TiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-TiB-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @TiB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-TiB-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @TiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-TiB-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @TiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-TiB-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB

    @TiB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-TiB-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 4) / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-PB-desc')
    @lone_group(True)
    async def PB(self, ctx):
        pass


    @PB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-PB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @PB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-PB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @PB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-PB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @PB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-PB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @PB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-PB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @PB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-PB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @PB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-PB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @PB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-PB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @PB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-PB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @PB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-PB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @PB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-PB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @PB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-PB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @PB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-PB-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @PB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-PB-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @PB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-PB-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @PB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-PB-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @PB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-PB-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @PB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-PB-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @PB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-PB-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @PB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-PB-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @PB.command(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-PB-PiB-desc')
    async def PiB(ctx, amount: float):
        try:
            await ctx.send(amount * 8e15 / (8 * 1024 ** 5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PiB

    @storage.group(aliases=['pebibyte', 'pebibytes'], invoke_without_command=True, description='units/storage-PiB-desc')
    @lone_group(True)
    async def PiB(self, ctx):
        pass


    @PiB.command(aliases=['bit', 'bits'], invoke_without_command=True, description='units/storage-PiB-b-desc')
    async def b(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del b

    @PiB.command(aliases=['kilobit', 'kilobits'], invoke_without_command=True, description='units/storage-PiB-kb-desc')
    async def kb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kb

    @PiB.command(aliases=['kibibit', 'kibibits'], invoke_without_command=True, description='units/storage-PiB-kib-desc')
    async def kib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 1024)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kib

    @PiB.command(aliases=['megabit', 'megabits'], invoke_without_command=True, description='units/storage-PiB-mb-desc')
    async def mb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mb

    @PiB.command(aliases=['mebibit', 'mebibits'], invoke_without_command=True, description='units/storage-PiB-mib-desc')
    async def mib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / (1024**2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mib

    @PiB.command(aliases=['gigabit', 'gigabits'], invoke_without_command=True, description='units/storage-PiB-gb-desc')
    async def gb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gb

    @PiB.command(aliases=['gibibit', 'gibibits'], invoke_without_command=True, description='units/storage-PiB-gib-desc')
    async def gib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / (1024**3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gib

    @PiB.command(aliases=['terabit', 'terabits'], invoke_without_command=True, description='units/storage-PiB-tb-desc')
    async def tb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 1e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tb

    @PiB.command(aliases=['tebibit', 'tebibits'], invoke_without_command=True, description='units/storage-PiB-tib-desc')
    async def tib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / (1024**4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tib

    @PiB.command(aliases=['petabit', 'petabits'], invoke_without_command=True, description='units/storage-PiB-pb-desc')
    async def pb(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 1e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pb

    @PiB.command(aliases=['pebibit', 'pebibits'], invoke_without_command=True, description='units/storage-PiB-pib-desc')
    async def pib(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / (1024**5))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pib

    @PiB.command(aliases=['byte', 'bytes'], invoke_without_command=True, description='units/storage-PiB-B-desc')
    async def B(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del B

    @PiB.command(aliases=['kilobyte', 'kilobytes'], invoke_without_command=True, description='units/storage-PiB-KB-desc')
    async def KB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 8e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KB

    @PiB.command(aliases=['kibibyte', 'kibibytes'], invoke_without_command=True, description='units/storage-PiB-KiB-desc')
    async def KiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del KiB

    @PiB.command(aliases=['megabyte', 'megabytes'], invoke_without_command=True, description='units/storage-PiB-MB-desc')
    async def MB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 8e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MB

    @PiB.command(aliases=['mebibyte', 'mebibytes'], invoke_without_command=True, description='units/storage-PiB-MiB-desc')
    async def MiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024 ** 2))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del MiB

    @PiB.command(aliases=['gigabyte', 'gigabytes'], invoke_without_command=True, description='units/storage-PiB-GB-desc')
    async def GB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 8e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GB

    @PiB.command(aliases=['gibibyte', 'gibibytes'], invoke_without_command=True, description='units/storage-PiB-GiB-desc')
    async def GiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024 ** 3))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del GiB

    @PiB.command(aliases=['terabyte', 'terabytes'], invoke_without_command=True, description='units/storage-PiB-TB-desc')
    async def TB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 8e12)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TB

    @PiB.command(aliases=['tebibyte', 'tebibytes'], invoke_without_command=True, description='units/storage-PiB-TiB-desc')
    async def TiB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / (8 * 1024 ** 4))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del TiB

    @PiB.command(aliases=['petabyte', 'petabytes'], invoke_without_command=True, description='units/storage-PiB-PB-desc')
    async def PB(ctx, amount: float):
        try:
            await ctx.send(amount * (8 * 1024 ** 5) / 8e15)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del PB


    @convert.group(aliases=[], invoke_without_command=True, description='units/energy-desc')
    @lone_group(True)
    async def energy(self, ctx):
        pass


    @energy.group(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-J-desc')
    @lone_group(True)
    async def J(self, ctx):
        pass


    @J.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-J-kJ-desc')
    async def kJ(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kJ

    @J.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-J-cal-desc')
    async def cal(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 4.184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cal

    @J.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-J-kcal-desc')
    async def kcal(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 4184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kcal

    @J.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-J-Wh-desc')
    async def Wh(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Wh

    @J.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-J-kWh-desc')
    async def kWh(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 3.6e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kWh

    @J.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-J-eV-desc')
    async def eV(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/6.242e18))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del eV

    @J.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-J-btu-desc')
    async def btu(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1055.06)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del btu

    @J.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-J-ust-desc')
    async def ust(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1.05506e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ust

    @J.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-J-ftlb-desc')
    async def ftlb(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1.35582)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ftlb

    @energy.group(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-kJ-desc')
    @lone_group(True)
    async def kJ(self, ctx):
        pass


    @kJ.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-kJ-J-desc')
    async def J(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del J

    @kJ.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-kJ-cal-desc')
    async def cal(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 4.184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cal

    @kJ.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-kJ-kcal-desc')
    async def kcal(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 4184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kcal

    @kJ.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-kJ-Wh-desc')
    async def Wh(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Wh

    @kJ.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-kJ-kWh-desc')
    async def kWh(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 3.6e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kWh

    @kJ.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-kJ-eV-desc')
    async def eV(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / (1/6.242e18))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del eV

    @kJ.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-kJ-btu-desc')
    async def btu(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1055.06)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del btu

    @kJ.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-kJ-ust-desc')
    async def ust(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1.05506e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ust

    @kJ.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-kJ-ftlb-desc')
    async def ftlb(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1.35582)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ftlb

    @energy.group(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-cal-desc')
    @lone_group(True)
    async def cal(self, ctx):
        pass


    @cal.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-cal-J-desc')
    async def J(ctx, amount: float):
        try:
            await ctx.send(amount * 4.184 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del J

    @cal.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-cal-kJ-desc')
    async def kJ(ctx, amount: float):
        try:
            await ctx.send(amount * 4.184 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kJ

    @cal.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-cal-kcal-desc')
    async def kcal(ctx, amount: float):
        try:
            await ctx.send(amount * 4.184 / 4184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kcal

    @cal.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-cal-Wh-desc')
    async def Wh(ctx, amount: float):
        try:
            await ctx.send(amount * 4.184 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Wh

    @cal.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-cal-kWh-desc')
    async def kWh(ctx, amount: float):
        try:
            await ctx.send(amount * 4.184 / 3.6e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kWh

    @cal.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-cal-eV-desc')
    async def eV(ctx, amount: float):
        try:
            await ctx.send(amount * 4.184 / (1/6.242e18))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del eV

    @cal.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-cal-btu-desc')
    async def btu(ctx, amount: float):
        try:
            await ctx.send(amount * 4.184 / 1055.06)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del btu

    @cal.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-cal-ust-desc')
    async def ust(ctx, amount: float):
        try:
            await ctx.send(amount * 4.184 / 1.05506e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ust

    @cal.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-cal-ftlb-desc')
    async def ftlb(ctx, amount: float):
        try:
            await ctx.send(amount * 4.184 / 1.35582)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ftlb

    @energy.group(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-kcal-desc')
    @lone_group(True)
    async def kcal(self, ctx):
        pass


    @kcal.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-kcal-J-desc')
    async def J(ctx, amount: float):
        try:
            await ctx.send(amount * 4184 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del J

    @kcal.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-kcal-kJ-desc')
    async def kJ(ctx, amount: float):
        try:
            await ctx.send(amount * 4184 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kJ

    @kcal.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-kcal-cal-desc')
    async def cal(ctx, amount: float):
        try:
            await ctx.send(amount * 4184 / 4.184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cal

    @kcal.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-kcal-Wh-desc')
    async def Wh(ctx, amount: float):
        try:
            await ctx.send(amount * 4184 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Wh

    @kcal.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-kcal-kWh-desc')
    async def kWh(ctx, amount: float):
        try:
            await ctx.send(amount * 4184 / 3.6e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kWh

    @kcal.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-kcal-eV-desc')
    async def eV(ctx, amount: float):
        try:
            await ctx.send(amount * 4184 / (1/6.242e18))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del eV

    @kcal.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-kcal-btu-desc')
    async def btu(ctx, amount: float):
        try:
            await ctx.send(amount * 4184 / 1055.06)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del btu

    @kcal.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-kcal-ust-desc')
    async def ust(ctx, amount: float):
        try:
            await ctx.send(amount * 4184 / 1.05506e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ust

    @kcal.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-kcal-ftlb-desc')
    async def ftlb(ctx, amount: float):
        try:
            await ctx.send(amount * 4184 / 1.35582)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ftlb

    @energy.group(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-Wh-desc')
    @lone_group(True)
    async def Wh(self, ctx):
        pass


    @Wh.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-Wh-J-desc')
    async def J(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del J

    @Wh.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-Wh-kJ-desc')
    async def kJ(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kJ

    @Wh.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-Wh-cal-desc')
    async def cal(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 4.184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cal

    @Wh.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-Wh-kcal-desc')
    async def kcal(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 4184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kcal

    @Wh.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-Wh-kWh-desc')
    async def kWh(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 3.6e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kWh

    @Wh.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-Wh-eV-desc')
    async def eV(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / (1/6.242e18))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del eV

    @Wh.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-Wh-btu-desc')
    async def btu(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 1055.06)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del btu

    @Wh.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-Wh-ust-desc')
    async def ust(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 1.05506e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ust

    @Wh.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-Wh-ftlb-desc')
    async def ftlb(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 1.35582)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ftlb

    @energy.group(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-kWh-desc')
    @lone_group(True)
    async def kWh(self, ctx):
        pass


    @kWh.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-kWh-J-desc')
    async def J(ctx, amount: float):
        try:
            await ctx.send(amount * 3.6e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del J

    @kWh.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-kWh-kJ-desc')
    async def kJ(ctx, amount: float):
        try:
            await ctx.send(amount * 3.6e6 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kJ

    @kWh.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-kWh-cal-desc')
    async def cal(ctx, amount: float):
        try:
            await ctx.send(amount * 3.6e6 / 4.184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cal

    @kWh.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-kWh-kcal-desc')
    async def kcal(ctx, amount: float):
        try:
            await ctx.send(amount * 3.6e6 / 4184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kcal

    @kWh.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-kWh-Wh-desc')
    async def Wh(ctx, amount: float):
        try:
            await ctx.send(amount * 3.6e6 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Wh

    @kWh.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-kWh-eV-desc')
    async def eV(ctx, amount: float):
        try:
            await ctx.send(amount * 3.6e6 / (1/6.242e18))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del eV

    @kWh.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-kWh-btu-desc')
    async def btu(ctx, amount: float):
        try:
            await ctx.send(amount * 3.6e6 / 1055.06)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del btu

    @kWh.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-kWh-ust-desc')
    async def ust(ctx, amount: float):
        try:
            await ctx.send(amount * 3.6e6 / 1.05506e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ust

    @kWh.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-kWh-ftlb-desc')
    async def ftlb(ctx, amount: float):
        try:
            await ctx.send(amount * 3.6e6 / 1.35582)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ftlb

    @energy.group(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-eV-desc')
    @lone_group(True)
    async def eV(self, ctx):
        pass


    @eV.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-eV-J-desc')
    async def J(ctx, amount: float):
        try:
            await ctx.send(amount * (1/6.242e18) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del J

    @eV.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-eV-kJ-desc')
    async def kJ(ctx, amount: float):
        try:
            await ctx.send(amount * (1/6.242e18) / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kJ

    @eV.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-eV-cal-desc')
    async def cal(ctx, amount: float):
        try:
            await ctx.send(amount * (1/6.242e18) / 4.184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cal

    @eV.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-eV-kcal-desc')
    async def kcal(ctx, amount: float):
        try:
            await ctx.send(amount * (1/6.242e18) / 4184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kcal

    @eV.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-eV-Wh-desc')
    async def Wh(ctx, amount: float):
        try:
            await ctx.send(amount * (1/6.242e18) / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Wh

    @eV.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-eV-kWh-desc')
    async def kWh(ctx, amount: float):
        try:
            await ctx.send(amount * (1/6.242e18) / 3.6e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kWh

    @eV.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-eV-btu-desc')
    async def btu(ctx, amount: float):
        try:
            await ctx.send(amount * (1/6.242e18) / 1055.06)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del btu

    @eV.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-eV-ust-desc')
    async def ust(ctx, amount: float):
        try:
            await ctx.send(amount * (1/6.242e18) / 1.05506e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ust

    @eV.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-eV-ftlb-desc')
    async def ftlb(ctx, amount: float):
        try:
            await ctx.send(amount * (1/6.242e18) / 1.35582)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ftlb

    @energy.group(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-btu-desc')
    @lone_group(True)
    async def btu(self, ctx):
        pass


    @btu.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-btu-J-desc')
    async def J(ctx, amount: float):
        try:
            await ctx.send(amount * 1055.06 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del J

    @btu.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-btu-kJ-desc')
    async def kJ(ctx, amount: float):
        try:
            await ctx.send(amount * 1055.06 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kJ

    @btu.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-btu-cal-desc')
    async def cal(ctx, amount: float):
        try:
            await ctx.send(amount * 1055.06 / 4.184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cal

    @btu.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-btu-kcal-desc')
    async def kcal(ctx, amount: float):
        try:
            await ctx.send(amount * 1055.06 / 4184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kcal

    @btu.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-btu-Wh-desc')
    async def Wh(ctx, amount: float):
        try:
            await ctx.send(amount * 1055.06 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Wh

    @btu.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-btu-kWh-desc')
    async def kWh(ctx, amount: float):
        try:
            await ctx.send(amount * 1055.06 / 3.6e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kWh

    @btu.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-btu-eV-desc')
    async def eV(ctx, amount: float):
        try:
            await ctx.send(amount * 1055.06 / (1/6.242e18))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del eV

    @btu.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-btu-ust-desc')
    async def ust(ctx, amount: float):
        try:
            await ctx.send(amount * 1055.06 / 1.05506e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ust

    @btu.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-btu-ftlb-desc')
    async def ftlb(ctx, amount: float):
        try:
            await ctx.send(amount * 1055.06 / 1.35582)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ftlb

    @energy.group(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-ust-desc')
    @lone_group(True)
    async def ust(self, ctx):
        pass


    @ust.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-ust-J-desc')
    async def J(ctx, amount: float):
        try:
            await ctx.send(amount * 1.05506e8 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del J

    @ust.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-ust-kJ-desc')
    async def kJ(ctx, amount: float):
        try:
            await ctx.send(amount * 1.05506e8 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kJ

    @ust.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-ust-cal-desc')
    async def cal(ctx, amount: float):
        try:
            await ctx.send(amount * 1.05506e8 / 4.184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cal

    @ust.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-ust-kcal-desc')
    async def kcal(ctx, amount: float):
        try:
            await ctx.send(amount * 1.05506e8 / 4184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kcal

    @ust.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-ust-Wh-desc')
    async def Wh(ctx, amount: float):
        try:
            await ctx.send(amount * 1.05506e8 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Wh

    @ust.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-ust-kWh-desc')
    async def kWh(ctx, amount: float):
        try:
            await ctx.send(amount * 1.05506e8 / 3.6e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kWh

    @ust.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-ust-eV-desc')
    async def eV(ctx, amount: float):
        try:
            await ctx.send(amount * 1.05506e8 / (1/6.242e18))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del eV

    @ust.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-ust-btu-desc')
    async def btu(ctx, amount: float):
        try:
            await ctx.send(amount * 1.05506e8 / 1055.06)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del btu

    @ust.command(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-ust-ftlb-desc')
    async def ftlb(ctx, amount: float):
        try:
            await ctx.send(amount * 1.05506e8 / 1.35582)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ftlb

    @energy.group(aliases=['foot-pound', 'foot-pounds'], invoke_without_command=True, description='units/energy-ftlb-desc')
    @lone_group(True)
    async def ftlb(self, ctx):
        pass


    @ftlb.command(aliases=['joule', 'joules'], invoke_without_command=True, description='units/energy-ftlb-J-desc')
    async def J(ctx, amount: float):
        try:
            await ctx.send(amount * 1.35582 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del J

    @ftlb.command(aliases=['kilojoule', 'kilojoules'], invoke_without_command=True, description='units/energy-ftlb-kJ-desc')
    async def kJ(ctx, amount: float):
        try:
            await ctx.send(amount * 1.35582 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kJ

    @ftlb.command(aliases=['calorie', 'calories'], invoke_without_command=True, description='units/energy-ftlb-cal-desc')
    async def cal(ctx, amount: float):
        try:
            await ctx.send(amount * 1.35582 / 4.184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cal

    @ftlb.command(aliases=['kilocalorie', 'kilocalories'], invoke_without_command=True, description='units/energy-ftlb-kcal-desc')
    async def kcal(ctx, amount: float):
        try:
            await ctx.send(amount * 1.35582 / 4184)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kcal

    @ftlb.command(aliases=['watt-hour', 'watt-hours'], invoke_without_command=True, description='units/energy-ftlb-Wh-desc')
    async def Wh(ctx, amount: float):
        try:
            await ctx.send(amount * 1.35582 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Wh

    @ftlb.command(aliases=['kilowatt-hour', 'kilowatt-hours'], invoke_without_command=True, description='units/energy-ftlb-kWh-desc')
    async def kWh(ctx, amount: float):
        try:
            await ctx.send(amount * 1.35582 / 3.6e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kWh

    @ftlb.command(aliases=['electronvolt', 'electronvolts'], invoke_without_command=True, description='units/energy-ftlb-eV-desc')
    async def eV(ctx, amount: float):
        try:
            await ctx.send(amount * 1.35582 / (1/6.242e18))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del eV

    @ftlb.command(aliases=['british-thermal-unit', 'british-thermal-units'], invoke_without_command=True, description='units/energy-ftlb-btu-desc')
    async def btu(ctx, amount: float):
        try:
            await ctx.send(amount * 1.35582 / 1055.06)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del btu

    @ftlb.command(aliases=['us-therm', 'us-therms'], invoke_without_command=True, description='units/energy-ftlb-ust-desc')
    async def ust(ctx, amount: float):
        try:
            await ctx.send(amount * 1.35582 / 1.05506e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ust


    @convert.group(aliases=['freq'], invoke_without_command=True, description='units/frequency-desc')
    @lone_group(True)
    async def frequency(self, ctx):
        pass


    @frequency.group(aliases=['hertz'], invoke_without_command=True, description='units/frequency-Hz-desc')
    @lone_group(True)
    async def Hz(self, ctx):
        pass


    @Hz.command(aliases=['kilohertz'], invoke_without_command=True, description='units/frequency-Hz-kHz-desc')
    async def kHz(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kHz

    @Hz.command(aliases=['megahertz'], invoke_without_command=True, description='units/frequency-Hz-mHz-desc')
    async def mHz(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mHz

    @Hz.command(aliases=['gigahertz'], invoke_without_command=True, description='units/frequency-Hz-gHz-desc')
    async def gHz(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gHz

    @frequency.group(aliases=['kilohertz'], invoke_without_command=True, description='units/frequency-kHz-desc')
    @lone_group(True)
    async def kHz(self, ctx):
        pass


    @kHz.command(aliases=['hertz'], invoke_without_command=True, description='units/frequency-kHz-Hz-desc')
    async def Hz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Hz

    @kHz.command(aliases=['megahertz'], invoke_without_command=True, description='units/frequency-kHz-mHz-desc')
    async def mHz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mHz

    @kHz.command(aliases=['gigahertz'], invoke_without_command=True, description='units/frequency-kHz-gHz-desc')
    async def gHz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gHz

    @frequency.group(aliases=['megahertz'], invoke_without_command=True, description='units/frequency-mHz-desc')
    @lone_group(True)
    async def mHz(self, ctx):
        pass


    @mHz.command(aliases=['hertz'], invoke_without_command=True, description='units/frequency-mHz-Hz-desc')
    async def Hz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Hz

    @mHz.command(aliases=['kilohertz'], invoke_without_command=True, description='units/frequency-mHz-kHz-desc')
    async def kHz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kHz

    @mHz.command(aliases=['gigahertz'], invoke_without_command=True, description='units/frequency-mHz-gHz-desc')
    async def gHz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gHz

    @frequency.group(aliases=['gigahertz'], invoke_without_command=True, description='units/frequency-gHz-desc')
    @lone_group(True)
    async def gHz(self, ctx):
        pass


    @gHz.command(aliases=['hertz'], invoke_without_command=True, description='units/frequency-gHz-Hz-desc')
    async def Hz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Hz

    @gHz.command(aliases=['kilohertz'], invoke_without_command=True, description='units/frequency-gHz-kHz-desc')
    async def kHz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kHz

    @gHz.command(aliases=['megahertz'], invoke_without_command=True, description='units/frequency-gHz-mHz-desc')
    async def mHz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e9 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mHz


    @convert.group(aliases=[], invoke_without_command=True, description='units/fuel-desc')
    @lone_group(True)
    async def fuel(self, ctx):
        pass


    @fuel.group(aliases=['us-miles-per-gallon', 'us-mile-per-gallon'], invoke_without_command=True, description='units/fuel-umpg-desc')
    @lone_group(True)
    async def umpg(self, ctx):
        pass


    @umpg.command(aliases=['imperial-miles-per-gallon', 'imperial-mile-per-gallon', 'mile-per-gallon', 'miles-per-gallon'], invoke_without_command=True, description='units/fuel-umpg-impg-desc')
    async def impg(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.352) / (1/2.825))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del impg

    @umpg.command(aliases=['kilometer-per-liter', 'kilometers-per-liter', 'kilometre-per-litre', 'kilometres-per-litre'], invoke_without_command=True, description='units/fuel-umpg-kmpL-desc')
    async def kmpL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.352) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kmpL

    @umpg.command(aliases=['liters-per-hundred-kilometers', 'liter-per-hundred-kilometers', 'litres-per-hundred-kilometres', 'litre-per-hundred-kilometres'], invoke_without_command=True, description='units/fuel-umpg-Lphkm-desc')
    async def Lphkm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.352) / 1 * 100 / (amount * amount))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Lphkm

    @fuel.group(aliases=['imperial-miles-per-gallon', 'imperial-mile-per-gallon', 'mile-per-gallon', 'miles-per-gallon'], invoke_without_command=True, description='units/fuel-impg-desc')
    @lone_group(True)
    async def impg(self, ctx):
        pass


    @impg.command(aliases=['us-miles-per-gallon', 'us-mile-per-gallon'], invoke_without_command=True, description='units/fuel-impg-umpg-desc')
    async def umpg(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.825) / (1/2.352))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del umpg

    @impg.command(aliases=['kilometer-per-liter', 'kilometers-per-liter', 'kilometre-per-litre', 'kilometres-per-litre'], invoke_without_command=True, description='units/fuel-impg-kmpL-desc')
    async def kmpL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.825) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kmpL

    @impg.command(aliases=['liters-per-hundred-kilometers', 'liter-per-hundred-kilometers', 'litres-per-hundred-kilometres', 'litre-per-hundred-kilometres'], invoke_without_command=True, description='units/fuel-impg-Lphkm-desc')
    async def Lphkm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.825) / 1 * 100 / (amount * amount))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Lphkm

    @fuel.group(aliases=['kilometer-per-liter', 'kilometers-per-liter', 'kilometre-per-litre', 'kilometres-per-litre'], invoke_without_command=True, description='units/fuel-kmpL-desc')
    @lone_group(True)
    async def kmpL(self, ctx):
        pass


    @kmpL.command(aliases=['us-miles-per-gallon', 'us-mile-per-gallon'], invoke_without_command=True, description='units/fuel-kmpL-umpg-desc')
    async def umpg(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/2.352))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del umpg

    @kmpL.command(aliases=['imperial-miles-per-gallon', 'imperial-mile-per-gallon', 'mile-per-gallon', 'miles-per-gallon'], invoke_without_command=True, description='units/fuel-kmpL-impg-desc')
    async def impg(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/2.825))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del impg

    @kmpL.command(aliases=['liters-per-hundred-kilometers', 'liter-per-hundred-kilometers', 'litres-per-hundred-kilometres', 'litre-per-hundred-kilometres'], invoke_without_command=True, description='units/fuel-kmpL-Lphkm-desc')
    async def Lphkm(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1 * 100 / (amount * amount))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Lphkm

    @fuel.group(aliases=['liters-per-hundred-kilometers', 'liter-per-hundred-kilometers', 'litres-per-hundred-kilometres', 'litre-per-hundred-kilometres'], invoke_without_command=True, description='units/fuel-Lphkm-desc')
    @lone_group(True)
    async def Lphkm(self, ctx):
        pass


    @Lphkm.command(aliases=['us-miles-per-gallon', 'us-mile-per-gallon'], invoke_without_command=True, description='units/fuel-Lphkm-umpg-desc')
    async def umpg(ctx, amount: float):
        try:
            await ctx.send(amount * 1 * 100 / (amount * amount) / (1/2.352))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del umpg

    @Lphkm.command(aliases=['imperial-miles-per-gallon', 'imperial-mile-per-gallon', 'mile-per-gallon', 'miles-per-gallon'], invoke_without_command=True, description='units/fuel-Lphkm-impg-desc')
    async def impg(ctx, amount: float):
        try:
            await ctx.send(amount * 1 * 100 / (amount * amount) / (1/2.825))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del impg

    @Lphkm.command(aliases=['kilometer-per-liter', 'kilometers-per-liter', 'kilometre-per-litre', 'kilometres-per-litre'], invoke_without_command=True, description='units/fuel-Lphkm-kmpL-desc')
    async def kmpL(ctx, amount: float):
        try:
            await ctx.send(amount * 1 * 100 / (amount * amount) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kmpL


    @convert.group(aliases=[], invoke_without_command=True, description='units/length-desc')
    @lone_group(True)
    async def length(self, ctx):
        pass


    @length.group(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-km-desc')
    @lone_group(True)
    async def km(self, ctx):
        pass


    @km.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-km-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @km.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-km-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @km.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-km-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @km.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-km-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @km.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-km-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @km.command(aliases=['miles'], invoke_without_command=True, description='units/length-km-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @km.command(aliases=['yards'], invoke_without_command=True, description='units/length-km-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @km.command(aliases=['feet'], invoke_without_command=True, description='units/length-km-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @km.command(aliases=['inches'], invoke_without_command=True, description='units/length-km-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch

    @km.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-km-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * 1000 / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-m-desc')
    @lone_group(True)
    async def m(self, ctx):
        pass


    @m.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-m-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @m.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-m-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @m.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-m-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @m.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-m-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @m.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-m-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @m.command(aliases=['miles'], invoke_without_command=True, description='units/length-m-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @m.command(aliases=['yards'], invoke_without_command=True, description='units/length-m-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @m.command(aliases=['feet'], invoke_without_command=True, description='units/length-m-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @m.command(aliases=['inches'], invoke_without_command=True, description='units/length-m-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch

    @m.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-m-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-cm-desc')
    @lone_group(True)
    async def cm(self, ctx):
        pass


    @cm.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-cm-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @cm.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-cm-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @cm.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-cm-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @cm.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-cm-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @cm.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-cm-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @cm.command(aliases=['miles'], invoke_without_command=True, description='units/length-cm-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @cm.command(aliases=['yards'], invoke_without_command=True, description='units/length-cm-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @cm.command(aliases=['feet'], invoke_without_command=True, description='units/length-cm-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @cm.command(aliases=['inches'], invoke_without_command=True, description='units/length-cm-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch

    @cm.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-cm-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-2 / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-mm-desc')
    @lone_group(True)
    async def mm(self, ctx):
        pass


    @mm.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-mm-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @mm.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-mm-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @mm.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-mm-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @mm.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-mm-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @mm.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-mm-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @mm.command(aliases=['miles'], invoke_without_command=True, description='units/length-mm-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @mm.command(aliases=['yards'], invoke_without_command=True, description='units/length-mm-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @mm.command(aliases=['feet'], invoke_without_command=True, description='units/length-mm-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @mm.command(aliases=['inches'], invoke_without_command=True, description='units/length-mm-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch

    @mm.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-mm-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-micron-desc')
    @lone_group(True)
    async def micron(self, ctx):
        pass


    @micron.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-micron-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @micron.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-micron-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @micron.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-micron-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @micron.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-micron-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @micron.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-micron-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @micron.command(aliases=['miles'], invoke_without_command=True, description='units/length-micron-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @micron.command(aliases=['yards'], invoke_without_command=True, description='units/length-micron-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @micron.command(aliases=['feet'], invoke_without_command=True, description='units/length-micron-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @micron.command(aliases=['inches'], invoke_without_command=True, description='units/length-micron-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch

    @micron.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-micron-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-nm-desc')
    @lone_group(True)
    async def nm(self, ctx):
        pass


    @nm.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-nm-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @nm.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-nm-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @nm.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-nm-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @nm.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-nm-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @nm.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-nm-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @nm.command(aliases=['miles'], invoke_without_command=True, description='units/length-nm-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @nm.command(aliases=['yards'], invoke_without_command=True, description='units/length-nm-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @nm.command(aliases=['feet'], invoke_without_command=True, description='units/length-nm-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @nm.command(aliases=['inches'], invoke_without_command=True, description='units/length-nm-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch

    @nm.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-nm-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['miles'], invoke_without_command=True, description='units/length-mile-desc')
    @lone_group(True)
    async def mile(self, ctx):
        pass


    @mile.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-mile-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @mile.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-mile-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @mile.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-mile-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @mile.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-mile-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @mile.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-mile-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @mile.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-mile-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @mile.command(aliases=['yards'], invoke_without_command=True, description='units/length-mile-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @mile.command(aliases=['feet'], invoke_without_command=True, description='units/length-mile-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @mile.command(aliases=['inches'], invoke_without_command=True, description='units/length-mile-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch

    @mile.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-mile-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * 1609.344 / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['yards'], invoke_without_command=True, description='units/length-yard-desc')
    @lone_group(True)
    async def yard(self, ctx):
        pass


    @yard.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-yard-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @yard.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-yard-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @yard.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-yard-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @yard.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-yard-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @yard.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-yard-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @yard.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-yard-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @yard.command(aliases=['miles'], invoke_without_command=True, description='units/length-yard-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @yard.command(aliases=['feet'], invoke_without_command=True, description='units/length-yard-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @yard.command(aliases=['inches'], invoke_without_command=True, description='units/length-yard-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch

    @yard.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-yard-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.094) / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['feet'], invoke_without_command=True, description='units/length-foot-desc')
    @lone_group(True)
    async def foot(self, ctx):
        pass


    @foot.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-foot-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @foot.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-foot-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @foot.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-foot-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @foot.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-foot-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @foot.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-foot-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @foot.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-foot-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @foot.command(aliases=['miles'], invoke_without_command=True, description='units/length-foot-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @foot.command(aliases=['yards'], invoke_without_command=True, description='units/length-foot-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @foot.command(aliases=['inches'], invoke_without_command=True, description='units/length-foot-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch

    @foot.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-foot-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['inches'], invoke_without_command=True, description='units/length-inch-desc')
    @lone_group(True)
    async def inch(self, ctx):
        pass


    @inch.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-inch-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @inch.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-inch-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @inch.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-inch-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @inch.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-inch-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @inch.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-inch-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @inch.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-inch-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @inch.command(aliases=['miles'], invoke_without_command=True, description='units/length-inch-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @inch.command(aliases=['yards'], invoke_without_command=True, description='units/length-inch-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @inch.command(aliases=['feet'], invoke_without_command=True, description='units/length-inch-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @inch.command(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-inch-nautmil-desc')
    async def nautmil(ctx, amount: float):
        try:
            await ctx.send(amount * 2.54e-2 / 1852)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nautmil

    @length.group(aliases=['nautical-mile', 'nautical-miles'], invoke_without_command=True, description='units/length-nautmil-desc')
    @lone_group(True)
    async def nautmil(self, ctx):
        pass


    @nautmil.command(aliases=['kilometer', 'kilometers', 'kilometre', 'kilometres'], invoke_without_command=True, description='units/length-nautmil-km-desc')
    async def km(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / 1000)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del km

    @nautmil.command(aliases=['meter', 'meters', 'metre', 'metres'], invoke_without_command=True, description='units/length-nautmil-m-desc')
    async def m(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m

    @nautmil.command(aliases=['centimeter', 'centimeters', 'centimetre', 'centimetres'], invoke_without_command=True, description='units/length-nautmil-cm-desc')
    async def cm(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / 1e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cm

    @nautmil.command(aliases=['millimeter', 'millimeters', 'millimetre', 'millimetres'], invoke_without_command=True, description='units/length-nautmil-mm-desc')
    async def mm(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mm

    @nautmil.command(aliases=['micrometer', 'micrometers', 'micrometre', 'micrometres'], invoke_without_command=True, description='units/length-nautmil-micron-desc')
    async def micron(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micron

    @nautmil.command(aliases=['nanometer', 'nanometers', 'nanometre', 'nanometres'], invoke_without_command=True, description='units/length-nautmil-nm-desc')
    async def nm(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del nm

    @nautmil.command(aliases=['miles'], invoke_without_command=True, description='units/length-nautmil-mile-desc')
    async def mile(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / 1609.344)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mile

    @nautmil.command(aliases=['yards'], invoke_without_command=True, description='units/length-nautmil-yard-desc')
    async def yard(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / (1/1.094))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del yard

    @nautmil.command(aliases=['feet'], invoke_without_command=True, description='units/length-nautmil-foot-desc')
    async def foot(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del foot

    @nautmil.command(aliases=['inches'], invoke_without_command=True, description='units/length-nautmil-inch-desc')
    async def inch(ctx, amount: float):
        try:
            await ctx.send(amount * 1852 / 2.54e-2)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del inch


    @convert.group(aliases=[], invoke_without_command=True, description='units/mass-desc')
    @lone_group(True)
    async def mass(self, ctx):
        pass


    @mass.group(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-t-desc')
    @lone_group(True)
    async def t(self, ctx):
        pass


    @t.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-t-kg-desc')
    async def kg(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kg

    @t.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-t-g-desc')
    async def g(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del g

    @t.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-t-mg-desc')
    async def mg(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mg

    @t.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-t-microg-desc')
    async def microg(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del microg

    @t.command(aliases=[], invoke_without_command=True, description='units/mass-t-ton-desc')
    async def ton(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 1.016e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ton

    @t.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-t-uston-desc')
    async def uston(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 907184.74)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uston

    @t.command(aliases=[], invoke_without_command=True, description='units/mass-t-stone-desc')
    async def stone(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 6350.293)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del stone

    @t.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-t-lb-desc')
    async def lb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 453.592)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lb

    @t.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-t-oz-desc')
    async def oz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e6 / 28.3495)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del oz

    @mass.group(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-kg-desc')
    @lone_group(True)
    async def kg(self, ctx):
        pass


    @kg.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-kg-t-desc')
    async def t(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del t

    @kg.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-kg-g-desc')
    async def g(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del g

    @kg.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-kg-mg-desc')
    async def mg(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mg

    @kg.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-kg-microg-desc')
    async def microg(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del microg

    @kg.command(aliases=[], invoke_without_command=True, description='units/mass-kg-ton-desc')
    async def ton(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1.016e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ton

    @kg.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-kg-uston-desc')
    async def uston(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 907184.74)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uston

    @kg.command(aliases=[], invoke_without_command=True, description='units/mass-kg-stone-desc')
    async def stone(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 6350.293)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del stone

    @kg.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-kg-lb-desc')
    async def lb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 453.592)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lb

    @kg.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-kg-oz-desc')
    async def oz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 28.3495)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del oz

    @mass.group(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-g-desc')
    @lone_group(True)
    async def g(self, ctx):
        pass


    @g.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-g-t-desc')
    async def t(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del t

    @g.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-g-kg-desc')
    async def kg(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kg

    @g.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-g-mg-desc')
    async def mg(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mg

    @g.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-g-microg-desc')
    async def microg(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del microg

    @g.command(aliases=[], invoke_without_command=True, description='units/mass-g-ton-desc')
    async def ton(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1.016e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ton

    @g.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-g-uston-desc')
    async def uston(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 907184.74)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uston

    @g.command(aliases=[], invoke_without_command=True, description='units/mass-g-stone-desc')
    async def stone(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 6350.293)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del stone

    @g.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-g-lb-desc')
    async def lb(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 453.592)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lb

    @g.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-g-oz-desc')
    async def oz(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 28.3495)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del oz

    @mass.group(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-mg-desc')
    @lone_group(True)
    async def mg(self, ctx):
        pass


    @mg.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-mg-t-desc')
    async def t(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del t

    @mg.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-mg-kg-desc')
    async def kg(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kg

    @mg.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-mg-g-desc')
    async def g(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del g

    @mg.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-mg-microg-desc')
    async def microg(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del microg

    @mg.command(aliases=[], invoke_without_command=True, description='units/mass-mg-ton-desc')
    async def ton(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1.016e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ton

    @mg.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-mg-uston-desc')
    async def uston(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 907184.74)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uston

    @mg.command(aliases=[], invoke_without_command=True, description='units/mass-mg-stone-desc')
    async def stone(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 6350.293)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del stone

    @mg.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-mg-lb-desc')
    async def lb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 453.592)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lb

    @mg.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-mg-oz-desc')
    async def oz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 28.3495)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del oz

    @mass.group(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-microg-desc')
    @lone_group(True)
    async def microg(self, ctx):
        pass


    @microg.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-microg-t-desc')
    async def t(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del t

    @microg.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-microg-kg-desc')
    async def kg(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kg

    @microg.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-microg-g-desc')
    async def g(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del g

    @microg.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-microg-mg-desc')
    async def mg(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mg

    @microg.command(aliases=[], invoke_without_command=True, description='units/mass-microg-ton-desc')
    async def ton(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1.016e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ton

    @microg.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-microg-uston-desc')
    async def uston(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 907184.74)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uston

    @microg.command(aliases=[], invoke_without_command=True, description='units/mass-microg-stone-desc')
    async def stone(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 6350.293)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del stone

    @microg.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-microg-lb-desc')
    async def lb(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 453.592)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lb

    @microg.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-microg-oz-desc')
    async def oz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 28.3495)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del oz

    @mass.group(aliases=[], invoke_without_command=True, description='units/mass-ton-desc')
    @lone_group(True)
    async def ton(self, ctx):
        pass


    @ton.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-ton-t-desc')
    async def t(ctx, amount: float):
        try:
            await ctx.send(amount * 1.016e6 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del t

    @ton.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-ton-kg-desc')
    async def kg(ctx, amount: float):
        try:
            await ctx.send(amount * 1.016e6 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kg

    @ton.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-ton-g-desc')
    async def g(ctx, amount: float):
        try:
            await ctx.send(amount * 1.016e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del g

    @ton.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-ton-mg-desc')
    async def mg(ctx, amount: float):
        try:
            await ctx.send(amount * 1.016e6 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mg

    @ton.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-ton-microg-desc')
    async def microg(ctx, amount: float):
        try:
            await ctx.send(amount * 1.016e6 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del microg

    @ton.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-ton-uston-desc')
    async def uston(ctx, amount: float):
        try:
            await ctx.send(amount * 1.016e6 / 907184.74)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uston

    @ton.command(aliases=[], invoke_without_command=True, description='units/mass-ton-stone-desc')
    async def stone(ctx, amount: float):
        try:
            await ctx.send(amount * 1.016e6 / 6350.293)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del stone

    @ton.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-ton-lb-desc')
    async def lb(ctx, amount: float):
        try:
            await ctx.send(amount * 1.016e6 / 453.592)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lb

    @ton.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-ton-oz-desc')
    async def oz(ctx, amount: float):
        try:
            await ctx.send(amount * 1.016e6 / 28.3495)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del oz

    @mass.group(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-uston-desc')
    @lone_group(True)
    async def uston(self, ctx):
        pass


    @uston.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-uston-t-desc')
    async def t(ctx, amount: float):
        try:
            await ctx.send(amount * 907184.74 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del t

    @uston.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-uston-kg-desc')
    async def kg(ctx, amount: float):
        try:
            await ctx.send(amount * 907184.74 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kg

    @uston.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-uston-g-desc')
    async def g(ctx, amount: float):
        try:
            await ctx.send(amount * 907184.74 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del g

    @uston.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-uston-mg-desc')
    async def mg(ctx, amount: float):
        try:
            await ctx.send(amount * 907184.74 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mg

    @uston.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-uston-microg-desc')
    async def microg(ctx, amount: float):
        try:
            await ctx.send(amount * 907184.74 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del microg

    @uston.command(aliases=[], invoke_without_command=True, description='units/mass-uston-ton-desc')
    async def ton(ctx, amount: float):
        try:
            await ctx.send(amount * 907184.74 / 1.016e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ton

    @uston.command(aliases=[], invoke_without_command=True, description='units/mass-uston-stone-desc')
    async def stone(ctx, amount: float):
        try:
            await ctx.send(amount * 907184.74 / 6350.293)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del stone

    @uston.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-uston-lb-desc')
    async def lb(ctx, amount: float):
        try:
            await ctx.send(amount * 907184.74 / 453.592)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lb

    @uston.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-uston-oz-desc')
    async def oz(ctx, amount: float):
        try:
            await ctx.send(amount * 907184.74 / 28.3495)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del oz

    @mass.group(aliases=[], invoke_without_command=True, description='units/mass-stone-desc')
    @lone_group(True)
    async def stone(self, ctx):
        pass


    @stone.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-stone-t-desc')
    async def t(ctx, amount: float):
        try:
            await ctx.send(amount * 6350.293 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del t

    @stone.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-stone-kg-desc')
    async def kg(ctx, amount: float):
        try:
            await ctx.send(amount * 6350.293 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kg

    @stone.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-stone-g-desc')
    async def g(ctx, amount: float):
        try:
            await ctx.send(amount * 6350.293 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del g

    @stone.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-stone-mg-desc')
    async def mg(ctx, amount: float):
        try:
            await ctx.send(amount * 6350.293 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mg

    @stone.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-stone-microg-desc')
    async def microg(ctx, amount: float):
        try:
            await ctx.send(amount * 6350.293 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del microg

    @stone.command(aliases=[], invoke_without_command=True, description='units/mass-stone-ton-desc')
    async def ton(ctx, amount: float):
        try:
            await ctx.send(amount * 6350.293 / 1.016e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ton

    @stone.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-stone-uston-desc')
    async def uston(ctx, amount: float):
        try:
            await ctx.send(amount * 6350.293 / 907184.74)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uston

    @stone.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-stone-lb-desc')
    async def lb(ctx, amount: float):
        try:
            await ctx.send(amount * 6350.293 / 453.592)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lb

    @stone.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-stone-oz-desc')
    async def oz(ctx, amount: float):
        try:
            await ctx.send(amount * 6350.293 / 28.3495)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del oz

    @mass.group(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-lb-desc')
    @lone_group(True)
    async def lb(self, ctx):
        pass


    @lb.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-lb-t-desc')
    async def t(ctx, amount: float):
        try:
            await ctx.send(amount * 453.592 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del t

    @lb.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-lb-kg-desc')
    async def kg(ctx, amount: float):
        try:
            await ctx.send(amount * 453.592 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kg

    @lb.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-lb-g-desc')
    async def g(ctx, amount: float):
        try:
            await ctx.send(amount * 453.592 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del g

    @lb.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-lb-mg-desc')
    async def mg(ctx, amount: float):
        try:
            await ctx.send(amount * 453.592 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mg

    @lb.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-lb-microg-desc')
    async def microg(ctx, amount: float):
        try:
            await ctx.send(amount * 453.592 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del microg

    @lb.command(aliases=[], invoke_without_command=True, description='units/mass-lb-ton-desc')
    async def ton(ctx, amount: float):
        try:
            await ctx.send(amount * 453.592 / 1.016e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ton

    @lb.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-lb-uston-desc')
    async def uston(ctx, amount: float):
        try:
            await ctx.send(amount * 453.592 / 907184.74)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uston

    @lb.command(aliases=[], invoke_without_command=True, description='units/mass-lb-stone-desc')
    async def stone(ctx, amount: float):
        try:
            await ctx.send(amount * 453.592 / 6350.293)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del stone

    @lb.command(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-lb-oz-desc')
    async def oz(ctx, amount: float):
        try:
            await ctx.send(amount * 453.592 / 28.3495)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del oz

    @mass.group(aliases=['ounce', 'ounces'], invoke_without_command=True, description='units/mass-oz-desc')
    @lone_group(True)
    async def oz(self, ctx):
        pass


    @oz.command(aliases=['Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], invoke_without_command=True, description='units/mass-oz-t-desc')
    async def t(ctx, amount: float):
        try:
            await ctx.send(amount * 28.3495 / 1e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del t

    @oz.command(aliases=['kilogram', 'kilograms'], invoke_without_command=True, description='units/mass-oz-kg-desc')
    async def kg(ctx, amount: float):
        try:
            await ctx.send(amount * 28.3495 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kg

    @oz.command(aliases=['gram', 'grams'], invoke_without_command=True, description='units/mass-oz-g-desc')
    async def g(ctx, amount: float):
        try:
            await ctx.send(amount * 28.3495 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del g

    @oz.command(aliases=['milligram', 'milligrams'], invoke_without_command=True, description='units/mass-oz-mg-desc')
    async def mg(ctx, amount: float):
        try:
            await ctx.send(amount * 28.3495 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mg

    @oz.command(aliases=['microgram', 'micrograms'], invoke_without_command=True, description='units/mass-oz-microg-desc')
    async def microg(ctx, amount: float):
        try:
            await ctx.send(amount * 28.3495 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del microg

    @oz.command(aliases=[], invoke_without_command=True, description='units/mass-oz-ton-desc')
    async def ton(ctx, amount: float):
        try:
            await ctx.send(amount * 28.3495 / 1.016e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ton

    @oz.command(aliases=['us-ton', 'us-tons'], invoke_without_command=True, description='units/mass-oz-uston-desc')
    async def uston(ctx, amount: float):
        try:
            await ctx.send(amount * 28.3495 / 907184.74)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uston

    @oz.command(aliases=[], invoke_without_command=True, description='units/mass-oz-stone-desc')
    async def stone(ctx, amount: float):
        try:
            await ctx.send(amount * 28.3495 / 6350.293)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del stone

    @oz.command(aliases=['pound', 'pounds'], invoke_without_command=True, description='units/mass-oz-lb-desc')
    async def lb(ctx, amount: float):
        try:
            await ctx.send(amount * 28.3495 / 453.592)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lb


    @convert.group(aliases=[], invoke_without_command=True, description='units/angle-desc')
    @lone_group(True)
    async def angle(self, ctx):
        pass


    @angle.group(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-deg-desc')
    @lone_group(True)
    async def deg(self, ctx):
        pass


    @deg.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-deg-grad-desc')
    async def grad(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 0.9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del grad

    @deg.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-deg-mrad-desc')
    async def mrad(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (180/(1000 * pi)))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mrad

    @deg.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-deg-arcmin-desc')
    async def arcmin(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/60))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcmin

    @deg.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-deg-rad-desc')
    async def rad(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (180/pi))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del rad

    @deg.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-deg-arcsec-desc')
    async def arcsec(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/3600))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcsec

    @angle.group(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-grad-desc')
    @lone_group(True)
    async def grad(self, ctx):
        pass


    @grad.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-grad-deg-desc')
    async def deg(ctx, amount: float):
        try:
            await ctx.send(amount * 0.9 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del deg

    @grad.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-grad-mrad-desc')
    async def mrad(ctx, amount: float):
        try:
            await ctx.send(amount * 0.9 / (180/(1000 * pi)))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mrad

    @grad.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-grad-arcmin-desc')
    async def arcmin(ctx, amount: float):
        try:
            await ctx.send(amount * 0.9 / (1/60))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcmin

    @grad.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-grad-rad-desc')
    async def rad(ctx, amount: float):
        try:
            await ctx.send(amount * 0.9 / (180/pi))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del rad

    @grad.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-grad-arcsec-desc')
    async def arcsec(ctx, amount: float):
        try:
            await ctx.send(amount * 0.9 / (1/3600))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcsec

    @angle.group(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-mrad-desc')
    @lone_group(True)
    async def mrad(self, ctx):
        pass


    @mrad.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-mrad-deg-desc')
    async def deg(ctx, amount: float):
        try:
            await ctx.send(amount * (180/(1000 * pi)) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del deg

    @mrad.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-mrad-grad-desc')
    async def grad(ctx, amount: float):
        try:
            await ctx.send(amount * (180/(1000 * pi)) / 0.9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del grad

    @mrad.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-mrad-arcmin-desc')
    async def arcmin(ctx, amount: float):
        try:
            await ctx.send(amount * (180/(1000 * pi)) / (1/60))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcmin

    @mrad.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-mrad-rad-desc')
    async def rad(ctx, amount: float):
        try:
            await ctx.send(amount * (180/(1000 * pi)) / (180/pi))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del rad

    @mrad.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-mrad-arcsec-desc')
    async def arcsec(ctx, amount: float):
        try:
            await ctx.send(amount * (180/(1000 * pi)) / (1/3600))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcsec

    @angle.group(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-arcmin-desc')
    @lone_group(True)
    async def arcmin(self, ctx):
        pass


    @arcmin.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-arcmin-deg-desc')
    async def deg(ctx, amount: float):
        try:
            await ctx.send(amount * (1/60) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del deg

    @arcmin.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-arcmin-grad-desc')
    async def grad(ctx, amount: float):
        try:
            await ctx.send(amount * (1/60) / 0.9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del grad

    @arcmin.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-arcmin-mrad-desc')
    async def mrad(ctx, amount: float):
        try:
            await ctx.send(amount * (1/60) / (180/(1000 * pi)))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mrad

    @arcmin.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-arcmin-rad-desc')
    async def rad(ctx, amount: float):
        try:
            await ctx.send(amount * (1/60) / (180/pi))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del rad

    @arcmin.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-arcmin-arcsec-desc')
    async def arcsec(ctx, amount: float):
        try:
            await ctx.send(amount * (1/60) / (1/3600))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcsec

    @angle.group(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-rad-desc')
    @lone_group(True)
    async def rad(self, ctx):
        pass


    @rad.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-rad-deg-desc')
    async def deg(ctx, amount: float):
        try:
            await ctx.send(amount * (180/pi) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del deg

    @rad.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-rad-grad-desc')
    async def grad(ctx, amount: float):
        try:
            await ctx.send(amount * (180/pi) / 0.9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del grad

    @rad.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-rad-mrad-desc')
    async def mrad(ctx, amount: float):
        try:
            await ctx.send(amount * (180/pi) / (180/(1000 * pi)))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mrad

    @rad.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-rad-arcmin-desc')
    async def arcmin(ctx, amount: float):
        try:
            await ctx.send(amount * (180/pi) / (1/60))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcmin

    @rad.command(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-rad-arcsec-desc')
    async def arcsec(ctx, amount: float):
        try:
            await ctx.send(amount * (180/pi) / (1/3600))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcsec

    @angle.group(aliases=['arc-second', 'arc-seconds'], invoke_without_command=True, description='units/angle-arcsec-desc')
    @lone_group(True)
    async def arcsec(self, ctx):
        pass


    @arcsec.command(aliases=['degree', 'degrees'], invoke_without_command=True, description='units/angle-arcsec-deg-desc')
    async def deg(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3600) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del deg

    @arcsec.command(aliases=['gradian', 'gradians'], invoke_without_command=True, description='units/angle-arcsec-grad-desc')
    async def grad(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3600) / 0.9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del grad

    @arcsec.command(aliases=['milliradian', 'milliradians'], invoke_without_command=True, description='units/angle-arcsec-mrad-desc')
    async def mrad(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3600) / (180/(1000 * pi)))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mrad

    @arcsec.command(aliases=['arc-minute', 'arc-minutes'], invoke_without_command=True, description='units/angle-arcsec-arcmin-desc')
    async def arcmin(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3600) / (1/60))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del arcmin

    @arcsec.command(aliases=['radian', 'radians'], invoke_without_command=True, description='units/angle-arcsec-rad-desc')
    async def rad(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3600) / (180/pi))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del rad


    @convert.group(aliases=[], invoke_without_command=True, description='units/pressure-desc')
    @lone_group(True)
    async def pressure(self, ctx):
        pass


    @pressure.group(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-atm-desc')
    @lone_group(True)
    async def atm(self, ctx):
        pass


    @atm.command(aliases=[], invoke_without_command=True, description='units/pressure-atm-bar-desc')
    async def bar(ctx, amount: float):
        try:
            await ctx.send(amount * 101325 / 1e5)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bar

    @atm.command(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-atm-Pa-desc')
    async def Pa(ctx, amount: float):
        try:
            await ctx.send(amount * 101325 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Pa

    @atm.command(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-atm-psi-desc')
    async def psi(ctx, amount: float):
        try:
            await ctx.send(amount * 101325 / 6894.757)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del psi

    @atm.command(aliases=[], invoke_without_command=True, description='units/pressure-atm-torr-desc')
    async def torr(ctx, amount: float):
        try:
            await ctx.send(amount * 101325 / 133.322)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del torr

    @pressure.group(aliases=[], invoke_without_command=True, description='units/pressure-bar-desc')
    @lone_group(True)
    async def bar(self, ctx):
        pass


    @bar.command(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-bar-atm-desc')
    async def atm(ctx, amount: float):
        try:
            await ctx.send(amount * 1e5 / 101325)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del atm

    @bar.command(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-bar-Pa-desc')
    async def Pa(ctx, amount: float):
        try:
            await ctx.send(amount * 1e5 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Pa

    @bar.command(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-bar-psi-desc')
    async def psi(ctx, amount: float):
        try:
            await ctx.send(amount * 1e5 / 6894.757)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del psi

    @bar.command(aliases=[], invoke_without_command=True, description='units/pressure-bar-torr-desc')
    async def torr(ctx, amount: float):
        try:
            await ctx.send(amount * 1e5 / 133.322)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del torr

    @pressure.group(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-Pa-desc')
    @lone_group(True)
    async def Pa(self, ctx):
        pass


    @Pa.command(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-Pa-atm-desc')
    async def atm(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 101325)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del atm

    @Pa.command(aliases=[], invoke_without_command=True, description='units/pressure-Pa-bar-desc')
    async def bar(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e5)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bar

    @Pa.command(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-Pa-psi-desc')
    async def psi(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 6894.757)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del psi

    @Pa.command(aliases=[], invoke_without_command=True, description='units/pressure-Pa-torr-desc')
    async def torr(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 133.322)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del torr

    @pressure.group(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-psi-desc')
    @lone_group(True)
    async def psi(self, ctx):
        pass


    @psi.command(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-psi-atm-desc')
    async def atm(ctx, amount: float):
        try:
            await ctx.send(amount * 6894.757 / 101325)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del atm

    @psi.command(aliases=[], invoke_without_command=True, description='units/pressure-psi-bar-desc')
    async def bar(ctx, amount: float):
        try:
            await ctx.send(amount * 6894.757 / 1e5)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bar

    @psi.command(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-psi-Pa-desc')
    async def Pa(ctx, amount: float):
        try:
            await ctx.send(amount * 6894.757 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Pa

    @psi.command(aliases=[], invoke_without_command=True, description='units/pressure-psi-torr-desc')
    async def torr(ctx, amount: float):
        try:
            await ctx.send(amount * 6894.757 / 133.322)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del torr

    @pressure.group(aliases=[], invoke_without_command=True, description='units/pressure-torr-desc')
    @lone_group(True)
    async def torr(self, ctx):
        pass


    @torr.command(aliases=['atmosphere', 'atmospheres'], invoke_without_command=True, description='units/pressure-torr-atm-desc')
    async def atm(ctx, amount: float):
        try:
            await ctx.send(amount * 133.322 / 101325)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del atm

    @torr.command(aliases=[], invoke_without_command=True, description='units/pressure-torr-bar-desc')
    async def bar(ctx, amount: float):
        try:
            await ctx.send(amount * 133.322 / 1e5)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del bar

    @torr.command(aliases=['pascal', 'pascals'], invoke_without_command=True, description='units/pressure-torr-Pa-desc')
    async def Pa(ctx, amount: float):
        try:
            await ctx.send(amount * 133.322 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del Pa

    @torr.command(aliases=['pound-per-square-inch', 'pounds-per-square-inch'], invoke_without_command=True, description='units/pressure-torr-psi-desc')
    async def psi(ctx, amount: float):
        try:
            await ctx.send(amount * 133.322 / 6894.757)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del psi


    @convert.group(aliases=[], invoke_without_command=True, description='units/speed-desc')
    @lone_group(True)
    async def speed(self, ctx):
        pass


    @speed.group(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-mph-desc')
    @lone_group(True)
    async def mph(self, ctx):
        pass


    @mph.command(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-mph-fps-desc')
    async def fps(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.237) / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del fps

    @mph.command(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-mph-mps-desc')
    async def mps(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.237) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mps

    @mph.command(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-mph-kmph-desc')
    async def kmph(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.237) / (1/3.6))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kmph

    @mph.command(aliases=['knots'], invoke_without_command=True, description='units/speed-mph-knot-desc')
    async def knot(ctx, amount: float):
        try:
            await ctx.send(amount * (1/2.237) / (1/1.944))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del knot

    @speed.group(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-fps-desc')
    @lone_group(True)
    async def fps(self, ctx):
        pass


    @fps.command(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-fps-mph-desc')
    async def mph(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / (1/2.237))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mph

    @fps.command(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-fps-mps-desc')
    async def mps(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mps

    @fps.command(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-fps-kmph-desc')
    async def kmph(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / (1/3.6))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kmph

    @fps.command(aliases=['knots'], invoke_without_command=True, description='units/speed-fps-knot-desc')
    async def knot(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.281) / (1/1.944))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del knot

    @speed.group(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-mps-desc')
    @lone_group(True)
    async def mps(self, ctx):
        pass


    @mps.command(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-mps-mph-desc')
    async def mph(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/2.237))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mph

    @mps.command(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-mps-fps-desc')
    async def fps(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del fps

    @mps.command(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-mps-kmph-desc')
    async def kmph(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/3.6))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kmph

    @mps.command(aliases=['knots'], invoke_without_command=True, description='units/speed-mps-knot-desc')
    async def knot(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/1.944))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del knot

    @speed.group(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-kmph-desc')
    @lone_group(True)
    async def kmph(self, ctx):
        pass


    @kmph.command(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-kmph-mph-desc')
    async def mph(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.6) / (1/2.237))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mph

    @kmph.command(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-kmph-fps-desc')
    async def fps(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.6) / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del fps

    @kmph.command(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-kmph-mps-desc')
    async def mps(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.6) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mps

    @kmph.command(aliases=['knots'], invoke_without_command=True, description='units/speed-kmph-knot-desc')
    async def knot(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.6) / (1/1.944))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del knot

    @speed.group(aliases=['knots'], invoke_without_command=True, description='units/speed-knot-desc')
    @lone_group(True)
    async def knot(self, ctx):
        pass


    @knot.command(aliases=['mile-per-hour', 'miles-per-hour'], invoke_without_command=True, description='units/speed-knot-mph-desc')
    async def mph(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.944) / (1/2.237))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mph

    @knot.command(aliases=['foot-per-second', 'feet-per-second'], invoke_without_command=True, description='units/speed-knot-fps-desc')
    async def fps(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.944) / (1/3.281))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del fps

    @knot.command(aliases=['meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], invoke_without_command=True, description='units/speed-knot-mps-desc')
    async def mps(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.944) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mps

    @knot.command(aliases=['kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], invoke_without_command=True, description='units/speed-knot-kmph-desc')
    async def kmph(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.944) / (1/3.6))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del kmph


    @convert.group(aliases=['temp'], invoke_without_command=True, description='units/temperature-desc')
    @lone_group(True)
    async def temperature(self, ctx):
        pass


    @temperature.group(aliases=['Celsius'], invoke_without_command=True, description='units/temperature-C-desc')
    @lone_group(True)
    async def C(self, ctx):
        pass


    @C.command(aliases=['Farenheit'], invoke_without_command=True, description='units/temperature-C-F-desc')
    async def F(ctx, amount: float):
        await ctx.send(amount * 9 / 5 + 32)

    del F

    @C.command(aliases=['Kelvin'], invoke_without_command=True, description='units/temperature-C-K-desc')
    async def K(ctx, amount: float):
        await ctx.send(amount + 273.15)

    del K

    @temperature.group(aliases=['Farenheit'], invoke_without_command=True, description='units/temperature-F-desc')
    @lone_group(True)
    async def F(self, ctx):
        pass


    @F.command(aliases=['Celsius'], invoke_without_command=True, description='units/temperature-F-C-desc')
    async def C(ctx, amount: float):
        await ctx.send((amount - 32) * 5 / 9)

    del C

    @F.command(aliases=['Kelvin'], invoke_without_command=True, description='units/temperature-F-K-desc')
    async def K(ctx, amount: float):
        await ctx.send((amount - 32) * 5 / 9 + 273.15)

    del K

    @temperature.group(aliases=['Kelvin'], invoke_without_command=True, description='units/temperature-K-desc')
    @lone_group(True)
    async def K(self, ctx):
        pass


    @K.command(aliases=['Celsius'], invoke_without_command=True, description='units/temperature-K-C-desc')
    async def C(ctx, amount: float):
        await ctx.send((amount - 273.15))

    del C

    @K.command(aliases=['Farenheit'], invoke_without_command=True, description='units/temperature-K-F-desc')
    async def F(ctx, amount: float):
        await ctx.send((amount - 273.15) * 9 / 5 + 32)

    del F


    @convert.group(aliases=[], invoke_without_command=True, description='units/time-desc')
    @lone_group(True)
    async def time(self, ctx):
        pass


    @time.group(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-ns-desc')
    @lone_group(True)
    async def ns(self, ctx):
        pass


    @ns.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-ns-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @ns.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-ns-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @ns.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-ns-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @ns.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-ns-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @ns.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-ns-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @ns.command(aliases=['days'], invoke_without_command=True, description='units/time-ns-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @ns.command(aliases=['weeks'], invoke_without_command=True, description='units/time-ns-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @ns.command(aliases=['months'], invoke_without_command=True, description='units/time-ns-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @ns.command(aliases=['years'], invoke_without_command=True, description='units/time-ns-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @ns.command(aliases=['decades'], invoke_without_command=True, description='units/time-ns-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @ns.command(aliases=['centuries'], invoke_without_command=True, description='units/time-ns-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-9 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-micros-desc')
    @lone_group(True)
    async def micros(self, ctx):
        pass


    @micros.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-micros-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @micros.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-micros-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @micros.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-micros-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @micros.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-micros-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @micros.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-micros-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @micros.command(aliases=['days'], invoke_without_command=True, description='units/time-micros-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @micros.command(aliases=['weeks'], invoke_without_command=True, description='units/time-micros-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @micros.command(aliases=['months'], invoke_without_command=True, description='units/time-micros-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @micros.command(aliases=['years'], invoke_without_command=True, description='units/time-micros-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @micros.command(aliases=['decades'], invoke_without_command=True, description='units/time-micros-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @micros.command(aliases=['centuries'], invoke_without_command=True, description='units/time-micros-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-6 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-ms-desc')
    @lone_group(True)
    async def ms(self, ctx):
        pass


    @ms.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-ms-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @ms.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-ms-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @ms.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-ms-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @ms.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-ms-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @ms.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-ms-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @ms.command(aliases=['days'], invoke_without_command=True, description='units/time-ms-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @ms.command(aliases=['weeks'], invoke_without_command=True, description='units/time-ms-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @ms.command(aliases=['months'], invoke_without_command=True, description='units/time-ms-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @ms.command(aliases=['years'], invoke_without_command=True, description='units/time-ms-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @ms.command(aliases=['decades'], invoke_without_command=True, description='units/time-ms-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @ms.command(aliases=['centuries'], invoke_without_command=True, description='units/time-ms-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-s-desc')
    @lone_group(True)
    async def s(self, ctx):
        pass


    @s.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-s-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @s.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-s-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @s.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-s-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @s.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-s-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @s.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-s-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @s.command(aliases=['days'], invoke_without_command=True, description='units/time-s-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @s.command(aliases=['weeks'], invoke_without_command=True, description='units/time-s-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @s.command(aliases=['months'], invoke_without_command=True, description='units/time-s-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @s.command(aliases=['years'], invoke_without_command=True, description='units/time-s-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @s.command(aliases=['decades'], invoke_without_command=True, description='units/time-s-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @s.command(aliases=['centuries'], invoke_without_command=True, description='units/time-s-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-min-desc')
    @lone_group(True)
    async def min(self, ctx):
        pass


    @min.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-min-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @min.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-min-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @min.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-min-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @min.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-min-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @min.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-min-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @min.command(aliases=['days'], invoke_without_command=True, description='units/time-min-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @min.command(aliases=['weeks'], invoke_without_command=True, description='units/time-min-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @min.command(aliases=['months'], invoke_without_command=True, description='units/time-min-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @min.command(aliases=['years'], invoke_without_command=True, description='units/time-min-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @min.command(aliases=['decades'], invoke_without_command=True, description='units/time-min-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @min.command(aliases=['centuries'], invoke_without_command=True, description='units/time-min-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 60 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-h-desc')
    @lone_group(True)
    async def h(self, ctx):
        pass


    @h.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-h-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @h.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-h-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @h.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-h-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @h.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-h-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @h.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-h-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @h.command(aliases=['days'], invoke_without_command=True, description='units/time-h-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @h.command(aliases=['weeks'], invoke_without_command=True, description='units/time-h-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @h.command(aliases=['months'], invoke_without_command=True, description='units/time-h-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @h.command(aliases=['years'], invoke_without_command=True, description='units/time-h-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @h.command(aliases=['decades'], invoke_without_command=True, description='units/time-h-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @h.command(aliases=['centuries'], invoke_without_command=True, description='units/time-h-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 3600 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['days'], invoke_without_command=True, description='units/time-day-desc')
    @lone_group(True)
    async def day(self, ctx):
        pass


    @day.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-day-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @day.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-day-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @day.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-day-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @day.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-day-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @day.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-day-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @day.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-day-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @day.command(aliases=['weeks'], invoke_without_command=True, description='units/time-day-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @day.command(aliases=['months'], invoke_without_command=True, description='units/time-day-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @day.command(aliases=['years'], invoke_without_command=True, description='units/time-day-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @day.command(aliases=['decades'], invoke_without_command=True, description='units/time-day-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @day.command(aliases=['centuries'], invoke_without_command=True, description='units/time-day-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 86400 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['weeks'], invoke_without_command=True, description='units/time-week-desc')
    @lone_group(True)
    async def week(self, ctx):
        pass


    @week.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-week-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @week.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-week-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @week.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-week-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @week.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-week-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @week.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-week-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @week.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-week-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @week.command(aliases=['days'], invoke_without_command=True, description='units/time-week-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @week.command(aliases=['months'], invoke_without_command=True, description='units/time-week-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @week.command(aliases=['years'], invoke_without_command=True, description='units/time-week-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @week.command(aliases=['decades'], invoke_without_command=True, description='units/time-week-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @week.command(aliases=['centuries'], invoke_without_command=True, description='units/time-week-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 604800 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['months'], invoke_without_command=True, description='units/time-month-desc')
    @lone_group(True)
    async def month(self, ctx):
        pass


    @month.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-month-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @month.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-month-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @month.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-month-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @month.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-month-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @month.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-month-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @month.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-month-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @month.command(aliases=['days'], invoke_without_command=True, description='units/time-month-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @month.command(aliases=['weeks'], invoke_without_command=True, description='units/time-month-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @month.command(aliases=['years'], invoke_without_command=True, description='units/time-month-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @month.command(aliases=['decades'], invoke_without_command=True, description='units/time-month-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @month.command(aliases=['centuries'], invoke_without_command=True, description='units/time-month-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 2.628e6 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['years'], invoke_without_command=True, description='units/time-year-desc')
    @lone_group(True)
    async def year(self, ctx):
        pass


    @year.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-year-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @year.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-year-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @year.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-year-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @year.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-year-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @year.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-year-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @year.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-year-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @year.command(aliases=['days'], invoke_without_command=True, description='units/time-year-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @year.command(aliases=['weeks'], invoke_without_command=True, description='units/time-year-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @year.command(aliases=['months'], invoke_without_command=True, description='units/time-year-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @year.command(aliases=['decades'], invoke_without_command=True, description='units/time-year-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade

    @year.command(aliases=['centuries'], invoke_without_command=True, description='units/time-year-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e7 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['decades'], invoke_without_command=True, description='units/time-decade-desc')
    @lone_group(True)
    async def decade(self, ctx):
        pass


    @decade.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-decade-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @decade.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-decade-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @decade.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-decade-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @decade.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-decade-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @decade.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-decade-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @decade.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-decade-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @decade.command(aliases=['days'], invoke_without_command=True, description='units/time-decade-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @decade.command(aliases=['weeks'], invoke_without_command=True, description='units/time-decade-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @decade.command(aliases=['months'], invoke_without_command=True, description='units/time-decade-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @decade.command(aliases=['years'], invoke_without_command=True, description='units/time-decade-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @decade.command(aliases=['centuries'], invoke_without_command=True, description='units/time-decade-century-desc')
    async def century(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e8 / 3.154e9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del century

    @time.group(aliases=['centuries'], invoke_without_command=True, description='units/time-century-desc')
    @lone_group(True)
    async def century(self, ctx):
        pass


    @century.command(aliases=['nanosecond', 'nanoseconds'], invoke_without_command=True, description='units/time-century-ns-desc')
    async def ns(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 1e-9)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ns

    @century.command(aliases=['microsecond', 'microseconds'], invoke_without_command=True, description='units/time-century-micros-desc')
    async def micros(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 1e-6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del micros

    @century.command(aliases=['millisecond', 'milliseconds'], invoke_without_command=True, description='units/time-century-ms-desc')
    async def ms(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ms

    @century.command(aliases=['second', 'seconds'], invoke_without_command=True, description='units/time-century-s-desc')
    async def s(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del s

    @century.command(aliases=['minute', 'minutes'], invoke_without_command=True, description='units/time-century-min-desc')
    async def min(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 60)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del min

    @century.command(aliases=['hour', 'hours'], invoke_without_command=True, description='units/time-century-h-desc')
    async def h(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 3600)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del h

    @century.command(aliases=['days'], invoke_without_command=True, description='units/time-century-day-desc')
    async def day(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 86400)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del day

    @century.command(aliases=['weeks'], invoke_without_command=True, description='units/time-century-week-desc')
    async def week(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 604800)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del week

    @century.command(aliases=['months'], invoke_without_command=True, description='units/time-century-month-desc')
    async def month(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 2.628e6)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del month

    @century.command(aliases=['years'], invoke_without_command=True, description='units/time-century-year-desc')
    async def year(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 3.154e7)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del year

    @century.command(aliases=['decades'], invoke_without_command=True, description='units/time-century-decade-desc')
    async def decade(ctx, amount: float):
        try:
            await ctx.send(amount * 3.154e9 / 3.154e8)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del decade


    @convert.group(aliases=[], invoke_without_command=True, description='units/volume-desc')
    @lone_group(True)
    async def volume(self, ctx):
        pass


    @volume.group(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-lgallon-desc')
    @lone_group(True)
    async def lgallon(self, ctx):
        pass


    @lgallon.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-lgallon-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @lgallon.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-lgallon-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @lgallon.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-lgallon-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @lgallon.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-lgallon-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @lgallon.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-lgallon-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @lgallon.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-lgallon-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @lgallon.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-lgallon-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @lgallon.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-lgallon-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @lgallon.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-lgallon-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @lgallon.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-lgallon-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @lgallon.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-lgallon-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @lgallon.command(aliases=['pints'], invoke_without_command=True, description='units/volume-lgallon-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @lgallon.command(aliases=['cups'], invoke_without_command=True, description='units/volume-lgallon-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @lgallon.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-lgallon-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @lgallon.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-lgallon-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @lgallon.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-lgallon-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @lgallon.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-lgallon-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @lgallon.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-lgallon-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * 3.78541 / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-lquart-desc')
    @lone_group(True)
    async def lquart(self, ctx):
        pass


    @lquart.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-lquart-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @lquart.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-lquart-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @lquart.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-lquart-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @lquart.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-lquart-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @lquart.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-lquart-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @lquart.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-lquart-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @lquart.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-lquart-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @lquart.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-lquart-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @lquart.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-lquart-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @lquart.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-lquart-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @lquart.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-lquart-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @lquart.command(aliases=['pints'], invoke_without_command=True, description='units/volume-lquart-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @lquart.command(aliases=['cups'], invoke_without_command=True, description='units/volume-lquart-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @lquart.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-lquart-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @lquart.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-lquart-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @lquart.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-lquart-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @lquart.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-lquart-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @lquart.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-lquart-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.057) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-lpint-desc')
    @lone_group(True)
    async def lpint(self, ctx):
        pass


    @lpint.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-lpint-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @lpint.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-lpint-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @lpint.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-lpint-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @lpint.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-lpint-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @lpint.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-lpint-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @lpint.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-lpint-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @lpint.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-lpint-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @lpint.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-lpint-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @lpint.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-lpint-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @lpint.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-lpint-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @lpint.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-lpint-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @lpint.command(aliases=['pints'], invoke_without_command=True, description='units/volume-lpint-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @lpint.command(aliases=['cups'], invoke_without_command=True, description='units/volume-lpint-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @lpint.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-lpint-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @lpint.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-lpint-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @lpint.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-lpint-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @lpint.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-lpint-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @lpint.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-lpint-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-uscup-desc')
    @lone_group(True)
    async def uscup(self, ctx):
        pass


    @uscup.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-uscup-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @uscup.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-uscup-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @uscup.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-uscup-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @uscup.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-uscup-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @uscup.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-uscup-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @uscup.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-uscup-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @uscup.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-uscup-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @uscup.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-uscup-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @uscup.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-uscup-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @uscup.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-uscup-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @uscup.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-uscup-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @uscup.command(aliases=['pints'], invoke_without_command=True, description='units/volume-uscup-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @uscup.command(aliases=['cups'], invoke_without_command=True, description='units/volume-uscup-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @uscup.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-uscup-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @uscup.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-uscup-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @uscup.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-uscup-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @uscup.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-uscup-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @uscup.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-uscup-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/4.167) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-usfloz-desc')
    @lone_group(True)
    async def usfloz(self, ctx):
        pass


    @usfloz.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-usfloz-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @usfloz.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-usfloz-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @usfloz.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-usfloz-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @usfloz.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-usfloz-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @usfloz.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-usfloz-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @usfloz.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-usfloz-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @usfloz.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-usfloz-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @usfloz.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-usfloz-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @usfloz.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-usfloz-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @usfloz.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-usfloz-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @usfloz.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-usfloz-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @usfloz.command(aliases=['pints'], invoke_without_command=True, description='units/volume-usfloz-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @usfloz.command(aliases=['cups'], invoke_without_command=True, description='units/volume-usfloz-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @usfloz.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-usfloz-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @usfloz.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-usfloz-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @usfloz.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-usfloz-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @usfloz.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-usfloz-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @usfloz.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-usfloz-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/33.814) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-ustbsp-desc')
    @lone_group(True)
    async def ustbsp(self, ctx):
        pass


    @ustbsp.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-ustbsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @ustbsp.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-ustbsp-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @ustbsp.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-ustbsp-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @ustbsp.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-ustbsp-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @ustbsp.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-ustbsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @ustbsp.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-ustbsp-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @ustbsp.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-ustbsp-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @ustbsp.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-ustbsp-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @ustbsp.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-ustbsp-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @ustbsp.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-ustbsp-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @ustbsp.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-ustbsp-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @ustbsp.command(aliases=['pints'], invoke_without_command=True, description='units/volume-ustbsp-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @ustbsp.command(aliases=['cups'], invoke_without_command=True, description='units/volume-ustbsp-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @ustbsp.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-ustbsp-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @ustbsp.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-ustbsp-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @ustbsp.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-ustbsp-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @ustbsp.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-ustbsp-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @ustbsp.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-ustbsp-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/67.628) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-ustsp-desc')
    @lone_group(True)
    async def ustsp(self, ctx):
        pass


    @ustsp.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-ustsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @ustsp.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-ustsp-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @ustsp.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-ustsp-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @ustsp.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-ustsp-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @ustsp.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-ustsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @ustsp.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-ustsp-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @ustsp.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-ustsp-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @ustsp.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-ustsp-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @ustsp.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-ustsp-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @ustsp.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-ustsp-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @ustsp.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-ustsp-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @ustsp.command(aliases=['pints'], invoke_without_command=True, description='units/volume-ustsp-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @ustsp.command(aliases=['cups'], invoke_without_command=True, description='units/volume-ustsp-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @ustsp.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-ustsp-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @ustsp.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-ustsp-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @ustsp.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-ustsp-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @ustsp.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-ustsp-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @ustsp.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-ustsp-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/202.884) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-m3-desc')
    @lone_group(True)
    async def m3(self, ctx):
        pass


    @m3.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-m3-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @m3.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-m3-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @m3.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-m3-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @m3.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-m3-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @m3.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-m3-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @m3.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-m3-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @m3.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-m3-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @m3.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-m3-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @m3.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-m3-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @m3.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-m3-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @m3.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-m3-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @m3.command(aliases=['pints'], invoke_without_command=True, description='units/volume-m3-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @m3.command(aliases=['cups'], invoke_without_command=True, description='units/volume-m3-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @m3.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-m3-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @m3.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-m3-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @m3.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-m3-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @m3.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-m3-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @m3.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-m3-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * 1e3 / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-L-desc')
    @lone_group(True)
    async def L(self, ctx):
        pass


    @L.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-L-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @L.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-L-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @L.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-L-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @L.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-L-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @L.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-L-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @L.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-L-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @L.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-L-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @L.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-L-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @L.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-L-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @L.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-L-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @L.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-L-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @L.command(aliases=['pints'], invoke_without_command=True, description='units/volume-L-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @L.command(aliases=['cups'], invoke_without_command=True, description='units/volume-L-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @L.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-L-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @L.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-L-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @L.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-L-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @L.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-L-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @L.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-L-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * 1 / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-mL-desc')
    @lone_group(True)
    async def mL(self, ctx):
        pass


    @mL.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-mL-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @mL.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-mL-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @mL.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-mL-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @mL.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-mL-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @mL.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-mL-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @mL.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-mL-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @mL.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-mL-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @mL.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-mL-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @mL.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-mL-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @mL.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-mL-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @mL.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-mL-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @mL.command(aliases=['pints'], invoke_without_command=True, description='units/volume-mL-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @mL.command(aliases=['cups'], invoke_without_command=True, description='units/volume-mL-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @mL.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-mL-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @mL.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-mL-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @mL.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-mL-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @mL.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-mL-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @mL.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-mL-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * 1e-3 / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['gallons'], invoke_without_command=True, description='units/volume-gallon-desc')
    @lone_group(True)
    async def gallon(self, ctx):
        pass


    @gallon.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-gallon-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @gallon.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-gallon-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @gallon.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-gallon-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @gallon.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-gallon-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @gallon.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-gallon-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @gallon.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-gallon-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @gallon.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-gallon-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @gallon.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-gallon-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @gallon.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-gallon-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @gallon.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-gallon-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @gallon.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-gallon-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @gallon.command(aliases=['pints'], invoke_without_command=True, description='units/volume-gallon-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @gallon.command(aliases=['cups'], invoke_without_command=True, description='units/volume-gallon-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @gallon.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-gallon-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @gallon.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-gallon-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @gallon.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-gallon-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @gallon.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-gallon-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @gallon.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-gallon-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * 4.546 / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['quarts'], invoke_without_command=True, description='units/volume-quart-desc')
    @lone_group(True)
    async def quart(self, ctx):
        pass


    @quart.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-quart-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @quart.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-quart-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @quart.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-quart-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @quart.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-quart-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @quart.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-quart-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @quart.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-quart-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @quart.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-quart-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @quart.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-quart-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @quart.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-quart-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @quart.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-quart-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @quart.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-quart-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @quart.command(aliases=['pints'], invoke_without_command=True, description='units/volume-quart-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @quart.command(aliases=['cups'], invoke_without_command=True, description='units/volume-quart-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @quart.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-quart-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @quart.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-quart-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @quart.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-quart-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @quart.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-quart-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @quart.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-quart-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * 1.3652 / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['pints'], invoke_without_command=True, description='units/volume-pint-desc')
    @lone_group(True)
    async def pint(self, ctx):
        pass


    @pint.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-pint-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @pint.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-pint-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @pint.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-pint-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @pint.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-pint-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @pint.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-pint-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @pint.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-pint-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @pint.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-pint-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @pint.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-pint-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @pint.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-pint-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @pint.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-pint-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @pint.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-pint-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @pint.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-pint-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @pint.command(aliases=['cups'], invoke_without_command=True, description='units/volume-pint-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @pint.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-pint-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @pint.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-pint-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @pint.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-pint-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @pint.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-pint-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @pint.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-pint-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/1.76) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['cups'], invoke_without_command=True, description='units/volume-cup-desc')
    @lone_group(True)
    async def cup(self, ctx):
        pass


    @cup.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-cup-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @cup.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-cup-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @cup.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-cup-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @cup.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-cup-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @cup.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-cup-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @cup.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-cup-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @cup.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-cup-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @cup.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-cup-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @cup.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-cup-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @cup.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-cup-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @cup.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-cup-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @cup.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-cup-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @cup.command(aliases=['pints'], invoke_without_command=True, description='units/volume-cup-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @cup.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-cup-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @cup.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-cup-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @cup.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-cup-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @cup.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-cup-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @cup.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-cup-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/3.52) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-floz-desc')
    @lone_group(True)
    async def floz(self, ctx):
        pass


    @floz.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-floz-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @floz.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-floz-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @floz.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-floz-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @floz.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-floz-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @floz.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-floz-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @floz.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-floz-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @floz.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-floz-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @floz.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-floz-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @floz.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-floz-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @floz.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-floz-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @floz.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-floz-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @floz.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-floz-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @floz.command(aliases=['pints'], invoke_without_command=True, description='units/volume-floz-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @floz.command(aliases=['cups'], invoke_without_command=True, description='units/volume-floz-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @floz.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-floz-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @floz.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-floz-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @floz.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-floz-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @floz.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-floz-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/35.195) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-tbsp-desc')
    @lone_group(True)
    async def tbsp(self, ctx):
        pass


    @tbsp.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-tbsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @tbsp.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-tbsp-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @tbsp.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-tbsp-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @tbsp.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-tbsp-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @tbsp.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-tbsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @tbsp.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-tbsp-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @tbsp.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-tbsp-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @tbsp.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-tbsp-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @tbsp.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-tbsp-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @tbsp.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-tbsp-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @tbsp.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-tbsp-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @tbsp.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-tbsp-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @tbsp.command(aliases=['pints'], invoke_without_command=True, description='units/volume-tbsp-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @tbsp.command(aliases=['cups'], invoke_without_command=True, description='units/volume-tbsp-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @tbsp.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-tbsp-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @tbsp.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-tbsp-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @tbsp.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-tbsp-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @tbsp.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-tbsp-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/56.312) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-tsp-desc')
    @lone_group(True)
    async def tsp(self, ctx):
        pass


    @tsp.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-tsp-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @tsp.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-tsp-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @tsp.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-tsp-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @tsp.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-tsp-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @tsp.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-tsp-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @tsp.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-tsp-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @tsp.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-tsp-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @tsp.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-tsp-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @tsp.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-tsp-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @tsp.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-tsp-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @tsp.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-tsp-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @tsp.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-tsp-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @tsp.command(aliases=['pints'], invoke_without_command=True, description='units/volume-tsp-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @tsp.command(aliases=['cups'], invoke_without_command=True, description='units/volume-tsp-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @tsp.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-tsp-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @tsp.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-tsp-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @tsp.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-tsp-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

    @tsp.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-tsp-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/168.936) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-ft3-desc')
    @lone_group(True)
    async def ft3(self, ctx):
        pass


    @ft3.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-ft3-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @ft3.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-ft3-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @ft3.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-ft3-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @ft3.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-ft3-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @ft3.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-ft3-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @ft3.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-ft3-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @ft3.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-ft3-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @ft3.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-ft3-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @ft3.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-ft3-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @ft3.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-ft3-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @ft3.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-ft3-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @ft3.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-ft3-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @ft3.command(aliases=['pints'], invoke_without_command=True, description='units/volume-ft3-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @ft3.command(aliases=['cups'], invoke_without_command=True, description='units/volume-ft3-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @ft3.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-ft3-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @ft3.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-ft3-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @ft3.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-ft3-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @ft3.command(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-ft3-in3-desc')
    async def in3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/28.317) / (1/61.024))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del in3

    @volume.group(aliases=['cubic-inch', 'cubic-inches'], invoke_without_command=True, description='units/volume-in3-desc')
    @lone_group(True)
    async def in3(self, ctx):
        pass


    @in3.command(aliases=['us-liquid-gallon', 'us-liquid-gallons'], invoke_without_command=True, description='units/volume-in3-lgallon-desc')
    async def lgallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / 3.78541)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lgallon

    @in3.command(aliases=['us-liquid-quart', 'us-liquid-quarts'], invoke_without_command=True, description='units/volume-in3-lquart-desc')
    async def lquart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/1.057))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lquart

    @in3.command(aliases=['us-liquid-pint', 'us-liquid-pints'], invoke_without_command=True, description='units/volume-in3-lpint-desc')
    async def lpint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del lpint

    @in3.command(aliases=['us-legal-cup', 'us-legal-cups'], invoke_without_command=True, description='units/volume-in3-uscup-desc')
    async def uscup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/4.167))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del uscup

    @in3.command(aliases=['us-fluid-ounce', 'us-fluid-ounces'], invoke_without_command=True, description='units/volume-in3-usfloz-desc')
    async def usfloz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/33.814))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del usfloz

    @in3.command(aliases=['us-tablespoon', 'us-tablespoons'], invoke_without_command=True, description='units/volume-in3-ustbsp-desc')
    async def ustbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/67.628))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustbsp

    @in3.command(aliases=['us-teaspoon', 'us-teaspoons'], invoke_without_command=True, description='units/volume-in3-ustsp-desc')
    async def ustsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/202.884))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ustsp

    @in3.command(aliases=['cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], invoke_without_command=True, description='units/volume-in3-m3-desc')
    async def m3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / 1e3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del m3

    @in3.command(aliases=['liter', 'liters', 'litre', 'litres'], invoke_without_command=True, description='units/volume-in3-L-desc')
    async def L(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / 1)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del L

    @in3.command(aliases=['milliliter', 'milliliters', 'millilitre', 'millilitres'], invoke_without_command=True, description='units/volume-in3-mL-desc')
    async def mL(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / 1e-3)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del mL

    @in3.command(aliases=['gallons'], invoke_without_command=True, description='units/volume-in3-gallon-desc')
    async def gallon(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / 4.546)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del gallon

    @in3.command(aliases=['quarts'], invoke_without_command=True, description='units/volume-in3-quart-desc')
    async def quart(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / 1.3652)
        except ZeroDivisionError:
            await ctx.send('NaN')

    del quart

    @in3.command(aliases=['pints'], invoke_without_command=True, description='units/volume-in3-pint-desc')
    async def pint(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/1.76))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del pint

    @in3.command(aliases=['cups'], invoke_without_command=True, description='units/volume-in3-cup-desc')
    async def cup(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/3.52))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del cup

    @in3.command(aliases=['fluid-ounce', 'fluid-ounces'], invoke_without_command=True, description='units/volume-in3-floz-desc')
    async def floz(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/35.195))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del floz

    @in3.command(aliases=['tablespoon', 'tablespoons'], invoke_without_command=True, description='units/volume-in3-tbsp-desc')
    async def tbsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/56.312))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tbsp

    @in3.command(aliases=['teaspoon', 'teaspoons'], invoke_without_command=True, description='units/volume-in3-tsp-desc')
    async def tsp(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/168.936))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del tsp

    @in3.command(aliases=['cubic-foot', 'cubic-feet'], invoke_without_command=True, description='units/volume-in3-ft3-desc')
    async def ft3(ctx, amount: float):
        try:
            await ctx.send(amount * (1/61.024) / (1/28.317))
        except ZeroDivisionError:
            await ctx.send('NaN')

    del ft3

