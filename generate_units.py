import sys

units = (
    (['area'], (
        (['sqkm', 'square-kilometers', 'square-kilometres', 'square-kilometer', 'square-kilometre'], '1e6'),
        (['sqm', 'square-meters', 'square-metres', 'square-meter', 'square-metre'], '1'),
        (['sqmil', 'square-miles', 'square-mile'], '2.59e6'),
        (['sqyard', 'square-yards', 'square-yard'], '(1/1.196)'),
        (['sqft', 'square-feet', 'square-foot'], '(1/10.764)'),
        (['sqin', 'square-inches', 'square-inch'], '(1/1550.003)'),
        (['hectare', 'hectares'], '10000'),
        (['acre', 'acres'], '4046.856')
    )),
    (['data'], (
        (['bps', 'bit-per-second', 'bits-per-second'], '1'),
        (['kbps', 'kilobit-per-second', 'kilobits-per-second'], '1e3'),
        (['KBps', 'kilobyte-per-second', 'kilobytes-per-second'], '8e3'),
        (['kibps', 'kibibit-per-second', 'kibibits-per-second'], '1024'),
        (['mbps', 'megabit-per-second', 'megabits-per-second'], '1e6'),
        (['MBps', 'megabyte-per-second', 'megabytes-per-second'], '8e6'),
        (['mibps', 'mebibit-per-second', 'mebibits-per-second'], '(1024**2)'),
        (['gbps', 'gigabit-per-second', 'gigabits-per-second'], '1e9'),
        (['GBps', 'gigabyte-per-second', 'gigabytes-per-second'], '8e9'),
        (['gibps', 'gigibit-per-second', 'gigibits-per-second'], '(1024**3)'),
        (['tbps', 'terabit-per-second', 'terabits-per-second'], '1e12'),
        (['TBps', 'terabyte-per-second', 'terabytes-per-second'], '8e12'),
        (['tibps', 'tebibit-per-second', 'tebibits-per-second'], '(1024**4)'),
    )),
    (['storage'], (
        (['b', 'bit', 'bits'], '1'),
        (['kb', 'kilobit', 'kilobits'], '1e3'),
        (['kib', 'kibibit', 'kibibits'], '1024'),
        (['mb', 'megabit', 'megabits'], '1e6'),
        (['mib', 'mebibit', 'mebibits'], '(1024**2)'),
        (['gb', 'gigabit', 'gigabits'], '1e9'),
        (['gib', 'gibibit', 'gibibits'], '(1024**3)'),
        (['tb', 'terabit', 'terabits'], '1e12'),
        (['tib', 'tebibit', 'tebibits'], '(1024**4)'),
        (['pb', 'petabit', 'petabits'], '1e15'),
        (['pib', 'pebibit', 'pebibits'], '(1024**5)'),
        (['B', 'byte', 'bytes'], '8'),
        (['KB', 'kilobyte', 'kilobytes'], '8e3'),
        (['KiB', 'kibibyte', 'kibibytes'], '(8 * 1024)'),
        (['MB', 'megabyte', 'megabytes'], '8e6'),
        (['MiB', 'mebibyte', 'mebibytes'], '(8 * 1024 ** 2)'),
        (['GB', 'gigabyte', 'gigabytes'], '8e9'),
        (['GiB', 'gibibyte', 'gibibytes'], '(8 * 1024 ** 3)'),
        (['TB', 'terabyte', 'terabytes'], '8e12'),
        (['TiB', 'tebibyte', 'tebibytes'], '(8 * 1024 ** 4)'),
        (['PB', 'petabyte', 'petabytes'], '8e15'),
        (['PiB', 'pebibyte', 'pebibytes'], '(8 * 1024 ** 5)')
    )),
    (['energy'], (
        (['J', 'joule', 'joules'], '1'),
        (['kJ', 'kilojoule', 'kilojoules'], '1000'),
        (['cal', 'calorie', 'calories'], '4.184'),
        (['kcal', 'kilocalorie', 'kilocalories'], '4184'),
        (['Wh', 'watt-hour', 'watt-hours'], '3600'),
        (['kWh', 'kilowatt-hour', 'kilowatt-hours'], '3.6e6'),
        (['eV', 'electronvolt', 'electronvolts'], '(1/6.242e18)'),
        (['btu', 'british-thermal-unit', 'british-thermal-units'], '1055.06'),
        (['ust', 'us-therm', 'us-therms'], '1.05506e8'),
        (['ftlb', 'foot-pound', 'foot-pounds'], '1.35582')
    )),
    (['frequency', 'freq'], (
        (['Hz', 'hertz'], '1'),
        (['kHz', 'kilohertz'], '1e3'),
        (['mHz', 'megahertz'], '1e6'),
        (['gHz', 'gigahertz'], '1e9')
    )),
    (['fuel'], (
        (['umpg', 'us-miles-per-gallon', 'us-mile-per-gallon'], '(1/2.352)'),
        (['impg', 'imperial-miles-per-gallon', 'imperial-mile-per-gallon', 'mile-per-gallon', 'miles-per-gallon'], '(1/2.825)'),
        (['kmpL', 'kilometer-per-liter', 'kilometers-per-liter', 'kilometre-per-litre', 'kilometres-per-litre'], '1'),
        # 100 / kmpL = Lphkm. This conversion works out to be
        # amount * 1 * 100 / (amount * amount) / 1 for Lphkm to kmpL
        # and amount * 1 / 1 * 100 / (amount * amount) for kmpL to Lphkm
        (['Lphkm', 'liters-per-hundred-kilometers', 'liter-per-hundred-kilometers', 'litres-per-hundred-kilometres', 'litre-per-hundred-kilometres'], '1 * 100 / (amount * amount)')
    )),
    (['length'], (
        (['km', 'kilometer', 'kilometers', 'kilometre', 'kilometres'], '1000'),
        (['m', 'meter', 'meters', 'metre', 'metres'], '1'),
        (['cm', 'centimeter', 'centimeters', 'centimetre', 'centimetres'], '1e-2'),
        (['mm', 'millimeter', 'millimeters', 'millimetre', 'millimetres'], '1e-3'),
        (['micron', 'micrometer', 'micrometers', 'micrometre', 'micrometres'], '1e-6'),
        (['nm', 'nanometer', 'nanometers', 'nanometre', 'nanometres'], '1e-9'),
        (['mile', 'miles'], '1609.344'),
        (['yard', 'yards'], '(1/1.094)'),
        (['foot', 'feet'], '(1/3.281)'),
        (['inch', 'inches'], '2.54e-2'),
        (['nautmil', 'nautical-mile', 'nautical-miles'], '1852')
    )),
    (['mass'], (
        (['t', 'Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], '1e6'),
        (['kg', 'kilogram', 'kilograms'], '1e3'),
        (['g', 'gram', 'grams'], '1'),
        (['mg', 'milligram', 'milligrams'], '1e-3'),
        (['microg', 'microgram', 'micrograms'], '1e-6'),
        (['ton'], '1.016e6'),
        (['uston', 'us-ton', 'us-tons'], '907184.74'),
        (['stone'], '6350.293'),
        (['lb', 'pound', 'pounds'], '453.592'),
        (['oz', 'ounce', 'ounces'], '28.3495')
    )),
    (['angle'], (
        (['deg', 'degree', 'degrees'], '1'),
        (['grad', 'gradian', 'gradians'], '0.9'),
        (['mrad', 'milliradian', 'milliradians'], '(180/(1000 * pi))'),
        (['arcmin', 'arc-minute', 'arc-minutes'], '(1/60)'),
        (['rad', 'radian', 'radians'], '(180/pi)'),
        (['arcsec', 'arc-second', 'arc-seconds'], '(1/3600)')
    )),
    (['pressure'], (
        (['atm', 'atmosphere', 'atmospheres'], '101325'),
        (['bar'], '1e5'),
        (['Pa', 'pascal', 'pascals'], '1'),
        (['psi', 'pound-per-square-inch', 'pounds-per-square-inch'], '6894.757'),
        (['torr'], '133.322')
    )),
    (['speed'], (
        (['mph', 'mile-per-hour', 'miles-per-hour'], '(1/2.237)'),
        (['fps', 'foot-per-second', 'feet-per-second'], '(1/3.281)'),
        (['mps', 'meter-per-second', 'meters-per-second', 'metre-per-second', 'metres-per-second'], '1'),
        (['kmph', 'kilometer-per-hour', 'kilometers-per-hour', 'kilometre-per-hour', 'kilometres-per-hour'], '(1/3.6)'),
        (['knot', 'knots'], '(1/1.944)')
    )),
    (['temperature', 'temp'], (
        (['C', 'Celsius'], '#TODO: CHANGE CELSIUS'),
        (['F', 'Farenheit'], '#TODO: CHANGE FAHRENHEIT'),
        (['K', 'Kelvin'], '#TODO: CHANGE KELVIN'),
        (['R', 'Rankine'], '#TODO: CHANGE RANKINE'),
    )),
    (['time'], (
        (['ns', 'nanosecond', 'nanoseconds'], '1e-9'),
        (['micros', 'microsecond', 'microseconds'], '1e-6'),
        (['ms', 'millisecond', 'milliseconds'], '1e-3'),
        (['s', 'second', 'seconds'], '1'),
        (['min', 'minute', 'minutes'], '60'),
        (['h', 'hour', 'hours'], '3600'),
        (['day', 'days'], '86400'),
        (['week', 'weeks'], '604800'),
        (['month', 'months'], '2.628e6'),
        (['year', 'years'], '3.154e7'),
        (['decade', 'decades'], '3.154e8'),
        (['century', 'centuries'], '3.154e9')
    )),
    (['volume'], (
        (['lgallon', 'us-liquid-gallon', 'us-liquid-gallons'], '3.78541'),
        (['lquart', 'us-liquid-quart', 'us-liquid-quarts'], '(1/1.057)'),
        (['lpint', 'us-liquid-pint', 'us-liquid-pints'], '(1/4.167)'),
        (['uscup', 'us-legal-cup', 'us-legal-cups'], '(1/4.167)'),
        (['usfloz', 'us-fluid-ounce', 'us-fluid-ounces'], '(1/33.814)'),
        (['ustbsp', 'us-tablespoon', 'us-tablespoons'], '(1/67.628)'),
        (['ustsp', 'us-teaspoon', 'us-teaspoons'], '(1/202.884)'),
        (['m3', 'cubic-meter', 'cubic-meters', 'cubic-metre', 'cubic-metres'], '1e3'),
        (['L', 'liter', 'liters', 'litre', 'litres'], '1'),
        (['mL', 'milliliter', 'milliliters', 'millilitre', 'millilitres'], '1e-3'),
        (['gallon', 'gallons'], '4.546'),
        (['quart', 'quarts'], '1.3652'),
        (['pint', 'pints'], '(1/1.76)'),
        (['cup', 'cups'], '(1/3.52)'),
        (['floz', 'fluid-ounce', 'fluid-ounces'], '(1/35.195)'),
        (['tbsp', 'tablespoon', 'tablespoons'], '(1/56.312)'),
        (['tsp', 'teaspoon', 'teaspoons'], '(1/168.936)'),
        (['ft3', 'cubic-foot', 'cubic-feet'], '(1/28.317)'),
        (['in3', 'cubic-inch', 'cubic-inches'], '(1/61.024)')
    ))
)

sys.stdout = open('kenny2automate/units.py', 'w')

print("""from math import pi
from discord.ext.commands import group, Cog
from .utils import lone_group

class Units(Cog):
    \"\"\"units/cog-desc\"\"\"

    @group(invoke_without_command=True, description='units/convert-desc')
    @lone_group(True)
    async def convert(self, ctx):
        pass
""")
for kind, pairs in units:
    kind, *aliases = kind
    print(f"""
    @convert.group(aliases={aliases!r}, invoke_without_command=True, description='units/{kind}-desc')
    @lone_group(True)
    async def {kind}(self, ctx):
        pass

""")
    for unit1, factor1 in iter(pairs):
        unit1, *aliases = unit1
        print(f"""    @{kind}.group(aliases={aliases!r}, invoke_without_command=True, description='units/{kind}-{unit1}-desc')
    @lone_group(True)
    async def {unit1}(self, ctx):
        pass

""")
        for unit2, factor2 in iter(pairs):
            unit2, *aliases = unit2
            if unit1 == unit2:
                continue
            if kind == 'temperature':
                if unit1 == 'C':
                    if unit2 == 'F':
                        factor = 'amount * 1.8 + 32'
                    elif unit2 == 'K':
                        factor = 'amount + 273.15'
                    elif unit2 == 'R':
                        factor = 'amount * 1.8 + 491.67'
                elif unit1 == 'F':
                    if unit2 == 'R':
                        factor = 'amount + 459.67'
                    elif unit2 == 'C':
                        factor = '(amount - 32) / 1.8'
                    elif unit2 == 'K':
                        factor = '(amount - 32) / 1.8 + 273.15'
                elif unit1 == 'K':
                    if unit2 == 'R':
                        factor = 'amount * 1.8'
                    elif unit2 == 'C':
                        factor = '(amount - 273.15)'
                    elif unit2 == 'F':
                        factor = '(amount - 273.15) * 1.8 + 32'
                elif unit1 == 'R':
                    if unit2 == 'K':
                        factor = 'amount / 1.8'
                    elif unit2 == 'C':
                        factor = '(amount - 491.67) / 1.8'
                    elif unit2 == 'F':
                        factor = 'amount - 459.67'
                print(f"""    @{unit1}.command(aliases={aliases!r}, invoke_without_command=True, description='units/{kind}-{unit1}-{unit2}-desc')
    async def {unit2}(ctx, amount: float):
        await ctx.send({factor})

    del {unit2}
""")
            else:
                print(f"""    @{unit1}.command(aliases={aliases!r}, invoke_without_command=True, description='units/{kind}-{unit1}-{unit2}-desc')
    async def {unit2}(ctx, amount: float):
        try:
            await ctx.send(amount * {factor1} / {factor2})
        except ZeroDivisionError:
            await ctx.send('NaN')

    del {unit2}
""")

sys.stdout.close()
sys.stdout = sys.__stdout__
