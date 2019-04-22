units = (
    (['area'], (
        ('sqkm', '1e6'),
        ('sqm', '1'),
        ('sqmil', '2.59e6'),
        ('sqyard', '(1/1.196)'),
        ('sqft', '(1/10.764)'),
        ('sqin', '(1/1550.003)'),
        ('hectare', '10000'),
        ('acre', '4046.856')
    )),
    (['data'], (
        ('bps', '1'),
        ('kbps', '1e3'),
        ('KBps', '8e3'),
        ('kibps', '1024'),
        ('mbps', '1e6'),
        ('MBps', '8e6'),
        ('mibps', '(1024**2)'),
        ('gbps', '1e9'),
        ('GBps', '8e9'),
        ('gibps', '(1024**3)'),
        ('tbps', '1e12'),
        ('TBps', '8e12'),
        ('tibps', '(1024**4)'),
    )),
    (['storage'], (
        ('b', '1'),
        ('kb', '1e3'),
        ('kib', '1024'),
        ('mb', '1e6'),
        ('mib', '(1024**2)'),
        ('gb', '1e9'),
        ('gib', '(1024**3)'),
        ('tb', '1e12'),
        ('tib', '(1024**4)'),
        ('pb', '1e15'),
        ('pib', '(1024**5)'),
        ('B', '8'),
        ('KB', '8e3'),
        ('KiB', '(8 * 1024)'),
        ('MB', '8e6'),
        ('MiB', '(8 * 1024 ** 2)'),
        ('GB', '8e9'),
        ('GiB', '(8 * 1024 ** 3)'),
        ('TB', '8e12'),
        ('TiB', '(8 * 1024 ** 4)'),
        ('PB', '8e15'),
        ('PiB', '(8 * 1024 ** 5)')
    )),
    (['energy'], (
        ('joule', '1'),
        ('kilojoule', '1000'),
        ('calorie', '4.184'),
        ('kcal', '4184'),
        ('watthour', '3600'),
        ('kwh', '3.6e6'),
        ('ev', '(1/6.242e18)'),
        ('btu', '1055.06'),
        ('ust', '1.05506e8'),
        ('ftlb', '1.35582')
    )),
    (['frequency', 'freq'], (
        ('hz', '1'),
        ('khz', '1e3'),
        ('mhz', '1e6'),
        ('ghz', '1e9')
    )),
    (['fuel'], (
        ('umpg', '(1/2.352)'),
        ('impg', '(1/2.825)'),
        ('kmpl', '1'),
        ('lphkm', '100')
    )),
    (['length'], (
        ('km', '1000'),
        ('m', '1'),
        ('cm', '1e-2'),
        ('mm', '1e-3'),
        ('micron', '1e-6'),
        ('nm', '1e-9'),
        ('mile', '1609.344'),
        ('yard', '(1/1.094)'),
        ('foot', '(1/3.281)'),
        ('inch', '2.54e-2'),
        ('nautmil', '1852')
    )),
    (['mass'], (
        ('tonne', '1e6'),
        ('kg', '1e3'),
        ('g', '1'),
        ('mg', '1e-3'),
        ('microg', '1e-6'),
        ('ton', '1.016e6'),
        ('uston', '907184.74'),
        ('stone', '6350.293'),
        ('lb', '453.592'),
        ('oz', '28.3495')
    )),
    (['angle'], (
        ('deg', '1'),
        ('grad', '0.9'),
        ('mrad', '(180/(1000 * math.pi))'),
        ('arcmin', '(1/60)'),
        ('rad', '(180/math.pi)'),
        ('arcsec', '(1/3600)')
    )),
    (['pressure'], (
        ('atm', '101325'),
        ('bar', '1e5'),
        ('pa', '1'),
        ('psi', '6894.757'),
        ('torr', '133.322')
    )),
    (['speed'], (
        ('mph', '(1/2.237)'),
        ('fps', '(1/3.281)'),
        ('mps', '1'),
        ('kmph', '(1/3.6)'),
        ('knot', '(1/1.944)')
    )),
    (['temperature', 'temp'], (
        ('C', '#TODO: CHANGE CELSIUS'),
        ('F', '#TODO: CHANGE FAHRENHEIT'),
        ('K', '#TODO: CHANGE KELVIN')
    )),
    (['time'], (
        ('ns', '1e-9'),
        ('micros', '1e-6'),
        ('ms', '1e-3'),
        ('s', '1'),
        ('min', '60'),
        ('h', '3600'),
        ('day', '86400'),
        ('week', '604800'),
        ('month', '2.628e6'),
        ('year', '3.154e7'),
        ('decade', '3.154e8'),
        ('century', '3.154e9')
    )),
    (['volume'], (
        ('lgallon', '3.78541'),
        ('lquart', '(1/1.057)'),
        ('lpint', '(1/4.167)'),
        ('uscup', '(1/4.167)'),
        ('usfloz', '(1/33.814)'),
        ('ustbsp', '(1/67.628)'),
        ('ustsp', '(1/202.884)'),
        ('m3', '1e3'),
        ('l', '1'),
        ('ml', '1e-3'),
        ('gallon', '4.546'),
        ('quart', '1.3652'),
        ('pint', '(1/1.76)'),
        ('cup', '(1/3.52)'),
        ('floz', '(1/35.195)'),
        ('tbsp', '(1/56.312)'),
        ('tsp', '(1/168.936)'),
        ('ft3', '(1/28.317)'),
        ('in3', '(1/61.024)')
    ))
)

print("""from discord.ext.commands import group, Cog
from .i18n import i18n

class Units(Cog):
    \"\"\"units/cog-desc\"\"\"

    @group(invoke_without_command=True, description='units/convert-desc')
    async def convert(self, ctx):
        pass
""")
for kind, pairs in units:
    print(f"""
    @convert.group(aliases={kind[1:]}, invoke_without_command=True, description='units/{kind[0]}-desc')
    async def {kind[0]}(self, ctx):
        pass

""")
    if kind[0] == 'temperature':
        print("""    @group(aliases=['temp'], invoke_without_command=True, description='units/temperature-desc')
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

""")
        continue
    for unit1, factor1 in iter(pairs):
        print(f"""    @{kind[0]}.group(invoke_without_command=True, description='units/{kind[0]}-{unit1}-desc')
    async def {unit1}(ctx):
        pass

""")
        for unit2, factor2 in iter(pairs):
            if unit1 == unit2:
                continue
            print(f"""    @{unit1}.command(invoke_without_command=True, description='units/{kind[0]}-{unit1}-{unit2}-desc')
    async def {unit2}(ctx, amount: float):
        await ctx.send(amount * {factor1} / {factor2})
""")
