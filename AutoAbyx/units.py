from decimal import Decimal as D, InvalidOperation
from typing import Iterable
import discord
from discord.ext import commands
from .chars import ZWNJ
from .i18n import Embed, Msg

UNITS: dict[str, tuple[tuple[list[str], D], ...]] = {
    'area': (
        (['sqkm', 'square-kilometers', 'square-kilometres',
         'square-kilometer', 'square-kilometre'], D('1e6')),
        (['sqm', 'square-meters', 'square-metres',
         'square-meter', 'square-metre'], D('1')),
        (['sqmil', 'square-miles', 'square-mile'], D('2.59e6')),
        (['sqyard', 'square-yards', 'square-yard'], 1 / D('1.196')),
        (['sqft', 'square-feet', 'square-foot'], D('10.764')),
        (['sqin', 'square-inches', 'square-inch'], D('1550.003')),
        (['hectare', 'hectares'], D('10000')),
        (['acre', 'acres'], D('4046.856'))
    ),
    'data': (
        (['bps', 'bit-per-second',
          'bits-per-second', 'b-per-second'], D('1')),
        (['kbps', 'kilobit-per-second',
          'kilobits-per-second', 'kb-per-second'], D('1e3')),
        (['KBps', 'kilobyte-per-second',
          'kilobytes-per-second', 'KB-per-second'], D('8e3')),
        (['kibps', 'kibibit-per-second',
          'kibibits-per-second', 'kib-per-second'], D('1024')),
        (['mbps', 'megabit-per-second',
          'megabits-per-second', 'mb-per-second'], D('1e6')),
        (['MBps', 'megabyte-per-second',
          'megabytes-per-second', 'MB-per-second'], D('8e6')),
        (['mibps', 'mebibit-per-second',
          'mebibits-per-second', 'mib-per-second'], D('1048576')),
        (['gbps', 'gigabit-per-second',
          'gigabits-per-second', 'gb-per-second'], D('1e9')),
        (['GBps', 'gigabyte-per-second',
          'gigabytes-per-second', 'GB-per-second'], D('8e9')),
        (['gibps', 'gigibit-per-second',
          'gigibits-per-second', 'gib-per-second'], D('1073741824')),
        (['tbps', 'terabit-per-second',
          'terabits-per-second', 'tb-per-second'], D('1e12')),
        (['TBps', 'terabyte-per-second',
          'terabytes-per-second', 'TB-per-second'], D('8e12')),
        (['tibps', 'tebibit-per-second',
          'tebibits-per-second', 'tib-per-second'], D('1099511627776')),
    ),
    'storage': (
        (['b', 'bit', 'bits'], D('1')),
        (['kb', 'kilobit', 'kilobits'], D('1e3')),
        (['kib', 'kibibit', 'kibibits'], D('1024')),
        (['mb', 'megabit', 'megabits'], D('1e6')),
        (['mib', 'mebibit', 'mebibits'], D('1048576')),
        (['gb', 'gigabit', 'gigabits'], D('1e9')),
        (['gib', 'gibibit', 'gibibits'], D('1073741824')),
        (['tb', 'terabit', 'terabits'], D('1e12')),
        (['tib', 'tebibit', 'tebibits'], D('1099511627776')),
        (['pb', 'petabit', 'petabits'], D('1e15')),
        (['pib', 'pebibit', 'pebibits'], D('1125899906842624')),
        (['B', 'byte', 'bytes'], D('8')),
        (['KB', 'kilobyte', 'kilobytes'], D('8e3')),
        (['KiB', 'kibibyte', 'kibibytes'], D('8192')),
        (['MB', 'megabyte', 'megabytes'], D('8e6')),
        (['MiB', 'mebibyte', 'mebibytes'], D('8388608')),
        (['GB', 'gigabyte', 'gigabytes'], D('8e9')),
        (['GiB', 'gibibyte', 'gibibytes'], D('8589934592')),
        (['TB', 'terabyte', 'terabytes'], D('8e12')),
        (['TiB', 'tebibyte', 'tebibytes'], D('8796093022208')),
        (['PB', 'petabyte', 'petabytes'], D('8e15')),
        (['PiB', 'pebibyte', 'pebibytes'], D('9007199254740992'))
    ),
    'energy': (
        (['J', 'joule', 'joules'], D('1')),
        (['kJ', 'kilojoule', 'kilojoules'], D('1000')),
        (['cal', 'calorie', 'calories'], D('4.184')),
        (['kcal', 'kilocalorie', 'kilocalories'], D('4184')),
        (['Wh', 'watt-hour', 'watt-hours'], D('3600')),
        (['kWh', 'kilowatt-hour', 'kilowatt-hours'], D('3.6e6')),
        (['eV', 'electronvolt', 'electronvolts'], 1 / D('6.242e18')),
        (['btu', 'british-thermal-unit', 'british-thermal-units'], D('1055.06')),
        (['ust', 'us-therm', 'us-therms'], D('1.05506e8')),
        (['ftlb', 'foot-pound', 'foot-pounds'], D('1.35582'))
    ),
    'frequency': (
        (['Hz', 'hertz', 'cycle', 'cycles', 'c', 'C'], D('1')),
        (['kHz', 'kilohertz', 'KHz', 'kilocycle',
          'kilocycles', 'kc', 'Kc', 'kC', 'KC'], D('1e3')),
        (['MHz', 'megahertz', 'mHz', 'megacycle',
          'megacycles', 'mc', 'Mc', 'mC', 'MC'], D('1e6')),
        (['GHz', 'gigahertz', 'gHz', 'gigacycle',
          'gigacycles', 'gc', 'Gc', 'gC', 'GC'], D('1e9'))
    ),
    'fuel': (
        (['umpg', 'us-miles-per-gallon', 'us-mile-per-gallon'], 1 / D('2.352')),
        (['impg', 'imperial-miles-per-gallon', 'imperial-mile-per-gallon',
         'mile-per-gallon', 'miles-per-gallon'], 1 / D('2.825')),
        (['kmpL', 'kilometer-per-liter', 'kilometers-per-liter',
         'kilometre-per-litre', 'kilometres-per-litre'], D('1'))
    ),
    'length': (
        (['km', 'kilometer', 'kilometers', 'kilometre', 'kilometres'], D('1000')),
        (['m', 'meter', 'meters', 'metre', 'metres'], D('1')),
        (['cm', 'centimeter', 'centimeters', 'centimetre', 'centimetres'], D('1e-2')),
        (['mm', 'millimeter', 'millimeters', 'millimetre', 'millimetres'], D('1e-3')),
        (['micron', 'micrometer', 'micrometers', 'micrometre', 'micrometres'], D('1e-6')),
        (['nm', 'nanometer', 'nanometers', 'nanometre', 'nanometres'], D('1e-9')),
        (['mile', 'miles'], D('1609.344')),
        (['yard', 'yards'], 1 / D('1.094')),
        (['foot', 'feet'], 1 / D('3.281')),
        (['inch', 'inches'], D('2.54e-2')),
        (['nautmil', 'nautical-mile', 'nautical-miles'], D('1852'))
    ),
    'mass': (
        (['t', 'Mg', 'tonne', 'tonnes', 'megagram', 'megagrams'], D('1e6')),
        (['kg', 'kilogram', 'kilograms'], D('1e3')),
        (['g', 'gram', 'grams'], D('1')),
        (['mg', 'milligram', 'milligrams'], D('1e-3')),
        (['microg', 'microgram', 'micrograms'], D('1e-6')),
        (['ton'], D('1.016e6')),
        (['uston', 'us-ton', 'us-tons'], D('907184.74')),
        (['stone'], D('6350.293')),
        (['lb', 'pound', 'pounds'], D('453.592')),
        (['oz', 'ounce', 'ounces'], D('28.3495'))
    ),
    'angle': (
        (['deg', 'degree', 'degrees'], D('1')),
        (['grad', 'gradian', 'gradians'], D('0.9')),
        (['mrad', 'milliradian', 'milliradians'],
         # 180 / (1000 * pi)
         D('0.05729577951308232087679815482')),
        (['arcmin', 'arc-minute', 'arc-minutes'], 1 / D('60')),
        (['rad', 'radian', 'radians'],
         # 180 / pi
         D('57.29577951308232087679815482')),
        (['arcsec', 'arc-second', 'arc-seconds'], 1 / D('3600'))
    ),
    'pressure': (
        (['atm', 'atmosphere', 'atmospheres'], D('101325')),
        (['bar'], D('1e5')),
        (['Pa', 'pascal', 'pascals'], D('1')),
        (['psi', 'pound-per-square-inch', 'pounds-per-square-inch'], D('6894.757')),
        (['torr'], D('133.322'))
    ),
    'speed': (
        (['mph', 'mile-per-hour', 'miles-per-hour'], 1 / D('2.237')),
        (['fps', 'foot-per-second', 'feet-per-second'], 1 / D('3.281')),
        (['mps', 'meter-per-second', 'meters-per-second',
         'metre-per-second', 'metres-per-second'], D('1')),
        (['kmph', 'kilometer-per-hour', 'kilometers-per-hour',
         'kilometre-per-hour', 'kilometres-per-hour'], 1 / D('3.6')),
        (['knot', 'knots'], 1 / D('1.944'))
    ),
    'temperature': (
        (['C', 'Celsius', 'c'], 'C'),
        (['F', 'Farenheit', 'f'], 'F'),
        (['K', 'Kelvin', 'k'], 'K'),
        (['R', 'Rankine', 'r'], 'R'),
    ),
    'time': (
        (['ns', 'nanosecond', 'nanoseconds'], D('1e-9')),
        (['micros', 'microsecond', 'microseconds'], D('1e-6')),
        (['ms', 'millisecond', 'milliseconds'], D('1e-3')),
        (['s', 'second', 'seconds'], D('1')),
        (['min', 'minute', 'minutes'], D('60')),
        (['h', 'hour', 'hours'], D('3600')),
        (['day', 'days'], D('86400')),
        (['week', 'weeks'], D('604800')),
        (['month', 'months'], D('2.628e6')),
        (['year', 'years'], D('3.154e7')),
        (['decade', 'decades'], D('3.154e8')),
        (['century', 'centuries'], D('3.154e9'))
    ),
    'volume': (
        (['gallon', 'gallons', 'liquid-gallon', 'liquid-gallons'], D('3.78541')),
        (['quart', 'quarts', 'liquid-quart', 'liquid-quarts'], 1 / D('1.057')),
        (['pint', 'pints', 'liquid-pint', 'liquid-pints'], 1 / D('4.167')),
        (['cup', 'cups', 'us-legal-cup', 'us-legal-cups'], 1 / D('4.167')),
        (['floz', 'fluid-ounce', 'fluid-ounces'], 1 / D('33.814')),
        (['tbsp', 'tablespoon', 'tablespoons'], 1 / D('67.628')),
        (['tsp', 'teaspoon', 'teaspoons'], 1 / D('202.884')),
        (['m3', 'cubic-meter', 'cubic-meters', 'cubic-metre',
          'cubic-metres', 'cubic-m', 'm-cubed'], D('1e3')),
        (['L', 'liter', 'liters', 'litre', 'litres'], D('1')),
        (['mL', 'milliliter', 'milliliters', 'millilitre', 'millilitres'], D('1e-3')),
        (['cm3', 'cubic-centimeter', 'cubic-centimeters', 'cubic-centimetre',
          'cubic-centimetres', 'cubic-cm', 'cm-cubed'], D('1e-3')),
        (['dm3', 'cubic-decimeter', 'cubic-decimeters', 'cubic-decimetre',
          'cubic-decimetres', 'cubic-dm', 'dm-cubed'], D('1')),
        (['ukgallon', 'ukgallons', 'imperial-gallon', 'imperial-gallons'], D('4.546')),
        (['ukquart', 'ukquarts', 'imperial-quart', 'imperial-quarts'], D('1.3652')),
        (['ukpint', 'ukpints', 'imperial-pint', 'imperial-pints'], 1 / D('1.76')),
        (['ukcup', 'ukcups', 'imperial-cup', 'imperial-cups'], 1 / D('3.52')),
        (['ukfloz', 'imperial-fluid-ounce', 'imperial-fluid-ounces'], 1 / D('35.195')),
        (['uktbsp', 'imperial-tablespoon', 'imperial-tablespoons'], 1 / D('56.312')),
        (['uktsp', 'imperial-teaspoon', 'imperial-teaspoons'], 1 / D('168.936')),
        (['ft3', 'cubic-foot', 'cubic-feet'], 1 / D('28.317')),
        (['in3', 'cubic-inch', 'cubic-inches'], 1 / D('61.024'))
    )
}

def similarity(a: str, b: str) -> float:
    """Calculate the Levenshtein ratio of similarity between a and b.

    Adapted from:
    https://www.datacamp.com/community/tutorials/fuzzy-string-python
    """
    rows = len(a) + 1
    cols = len(b) + 1
    distance = [[0] * cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            distance[i][0] = i
            distance[0][j] = j

    for col in range(1, cols):
        for row in range(1, rows):
            if a[row-1] == b[col-1]:
                cost = 0
            elif a[row-1].casefold() == b[col-1].casefold():
                cost = 1 # don't penalize capitalization changes as much
            else:
                cost = 2
            distance[row][col] = min(
                distance[row-1][col] + 1,
                distance[row][col-1] + 1,
                distance[row-1][col-1] + cost
            )

    return 1 - distance[row][col] / (len(a) + len(b))

class Units(commands.Cog):
    """units/cog-desc"""

    @commands.command(brief='units/convert-desc')
    async def convert(
        self,
        ctx: commands.Context,
        category: str,
        source: str,
        dest: str,
        value: str = None,
    ):
        """units/convert-help"""
        try:
            if value is None:
                value = D(dest)
                dest = source
                source = category
                category = None
            else:
                value = D(value)
        except InvalidOperation:
            raise commands.BadArgument(
                f'bad number: {value or dest}') from None
        assumptions = []
        if category is None:
            key = max(UNITS, key=lambda k: max(max(
                similarity(name, source)
                for name in unit[0]) for unit in UNITS[k]))
            assumptions.append((str(Msg(ctx, 'units/category')), key))
        else:
            key = self.best(UNITS, category)
            if category != key:
                assumptions.append((repr(category), key))
        src = self.category_best(key, source)
        srckey = self.best(src[0], source)
        if source != srckey:
            assumptions.append((repr(source), srckey))
        src = src[1]
        dst = self.category_best(key, dest)
        dstkey = self.best(dst[0], dest)
        if dest != dstkey:
            assumptions.append((repr(dest), dstkey))
        dst = dst[1]
        if src == dst:
            await ctx.send(embed=Embed(
                ctx, Msg('error'), Msg(
                    'units/same-unit',
                    self.assumptions(ctx, assumptions)
                ), color=0xff0000))
            return
        if key != 'temperature':
            try:
                await self.send_amount(ctx, assumptions, value * src / dst)
            except ZeroDivisionError:
                await self.send_amount(ctx, assumptions, D('NaN'))
        else:
            m = D('1.8')
            f = D('32')
            r = D('491.67')
            k = D('273.15')
            if src == 'C':
                if dst == 'F':
                    amount = value * m + f
                elif dst == 'K':
                    amount = value + k
                elif dst == 'R':
                    amount = value * m + r
            elif src == 'F':
                if dst == 'R':
                    amount = value + r
                elif dst == 'C':
                    amount = (value - f) / m
                elif dst == 'K':
                    amount = (value - f) / m + k
            elif src == 'K':
                if dst == 'R':
                    amount = value * m
                elif dst == 'C':
                    amount = value - k
                elif dst == 'F':
                    amount = (value - k) * m + f
            elif src == 'R':
                if dst == 'K':
                    amount = value / m
                elif dst == 'C':
                    amount = (value - r) / m
                elif dst == 'F':
                    amount = value - r
            await self.send_amount(ctx, assumptions, amount)

    @staticmethod
    def assumptions(ctx: commands.Context, inp: list[tuple[str, str]]) -> str:
        return str(Msg(ctx, ',')).join(
            str(Msg(ctx, 'units/assumption', source, dest))
            for source, dest in inp
        ) or str(Msg(ctx, 'units/nothing'))

    async def send_amount(self, ctx: commands.Context,
                          assumptions: list[tuple[str, str]], amount: D):
        """Send the final amount, stating assumptions of input."""
        assumptions = self.assumptions(ctx, assumptions)
        await ctx.send(Msg(ctx, 'units/assumptions',
                           assumptions, float(amount)))

    @staticmethod
    def best(iterable: Iterable[str], key: str) -> str:
        """Get the best match of key inside iterable."""
        return max(iterable, key=lambda name: similarity(name, key))

    @staticmethod
    def category_best(cat: str, key: str) -> tuple[list[str], str]:
        """Get the best match of key inside cat."""
        return max(UNITS[cat], key=lambda unit: max(
            similarity(name, key) for name in unit[0]))

    @commands.command(brief='units/units-desc')
    async def units(self, ctx: commands.Context, category: str = None):
        """units/units-help"""
        if category is None:
            await ctx.send(embed=Embed(
                ctx,
                description=Msg('units/category-list', ctx.prefix),
                fields=((ZWNJ, key, True) for key in UNITS),
                color=discord.Color.blue()
            ))
        else:
            key = self.best(UNITS, category)
            await ctx.send(embed=Embed(
                ctx,
                description=(
                    Msg('units/unit-list', key)
                    if key == category
                    else Msg('units/fuzzy-list', category, key)),
                fields=(
                    (name[0], Msg(
                        'units/aka',
                        str(Msg(ctx, ',')).join(name[1:])
                        or str(Msg(ctx, 'units/no-aka'))
                    ), True)
                    for name, _ in UNITS[key]
                ),
                color=discord.Color.blue()
            ))

def setup(bot: commands.Bot):
    bot.add_cog(Units())
