units = (
    ('area', 'areas', (
        ('sqkm', 'square kilometers'),
        ('sqm', 'square meters'),
        ('sqmil', 'square miles'),
        ('sqyard', 'square yards'),
        ('sqft', 'square feet'),
        ('sqin', 'square inches'),
        ('hectare', 'hectares'),
        ('acre', 'acres')
    )),
    ('data', 'data transfer rates', (
        ('bps', 'bits per second'),
        ('kbps', 'kilobits per second'),
        ('KBps', 'kilobytes per second'),
        ('kibps', 'kibibits per second'),
        ('mbps', 'megabits per second'),
        ('MBps', 'megabytes per second'),
        ('mibps', 'mebibits per second'),
        ('gbps', 'gigabits per second'),
        ('GBps', 'gigabytes per second'),
        ('gibps', 'gibibits per second'),
        ('tbps', 'terabits per second'),
        ('TBps', 'terabytes per second'),
        ('tibps', 'tebibits per second')
    )),
    ('storage', 'digital storage units', (
        ('b', 'bits'),
        ('kb', 'kilobits'),
        ('kib', 'kibibits'),
        ('mb', 'megabits'),
        ('mib', 'mebibits'),
        ('gb', 'gigabits'),
        ('gib', 'gibibits'),
        ('tb', 'terabits'),
        ('tib', 'tebibits'),
        ('pb', 'petabits'),
        ('pib', 'pebibits'),
        ('B', 'bytes'),
        ('KB', 'kilobytes'),
        ('KiB', 'kibibytes'),
        ('MB', 'megabytes'),
        ('MiB', 'mebibytes'),
        ('GB', 'gigabytes'),
        ('GiB', 'gibibytes'),
        ('TB', 'terabytes'),
        ('TiB', 'tebibytes'),
        ('PB', 'petabytes'),
        ('PiB', 'pebibytes')
    )),
    ('energy', 'energy units', (
        ('joule', 'Joules'),
        ('kilojoule', 'kilojoules'),
        ('calorie', 'gram calories'),
        ('kcal', 'kilocalories'),
        ('watthour', 'watt hours'),
        ('kwh', 'kilowatt hours'),
        ('ev', 'electronvolts'),
        ('btu', 'British thermal units'),
        ('ust', 'US therms'),
        ('ftlb', 'foot-pounds')
    )),
    ('frequency', 'frequencies', (
        ('hz', 'Hertz'),
        ('khz', 'kilohertz'),
        ('mhz', 'megahertz'),
        ('ghz', 'gigahertz')
    )),
    ('fuel', 'fuel economy units', (
        ('umpg', 'US miles per gallon'),
        ('impg', 'Imperial miles per gallon'),
        ('kmpl', 'kilometers per liter'),
        ('lphkm', 'liters per 100 kilometers')
    )),
    ('length', 'lengths', (
        ('km', 'kilometers'),
        ('m', 'meters'),
        ('cm', 'centimeters'),
        ('mm', 'milimeters'),
        ('micron', 'micrometers'),
        ('nm', 'nanometers'),
        ('mile', 'miles'),
        ('yard', 'yards'),
        ('foot', 'feet'),
        ('inch', 'inches'),
        ('nautmil', 'nautical miles')
    )),
    ('mass', 'masses', (
        ('tonne', 'tonnes'),
        ('kg', 'kilograms'),
        ('g', 'grams'),
        ('mg', 'milligrams'),
        ('microg', 'micrograms'),
        ('ton', 'Imperial tons'),
        ('uston', 'US tons'),
        ('stone', 'stone'),
        ('lb', 'pounds'),
        ('oz', 'ounces')
    )),
    ('angle', 'plane angles', (
        ('deg', 'degrees'),
        ('grad', 'gradians'),
        ('mrad', 'milliradians'),
        ('arcmin', 'minutes of arc'),
        ('rad', 'radians'),
        ('arcsec', 'seconds of arc')
    )),
    ('pressure', 'pressures', (
        ('atm', 'atmospheres'),
        ('bar', 'bars'),
        ('pa', 'Pascals'),
        ('psi', 'pound-force per square inch'),
        ('torr', 'torrs')
    )),
    ('speed', 'speeds', (
        ('mph', 'miles per hour'),
        ('fps', 'feet per second'),
        ('mps', 'meters per second'),
        ('kmph', 'kilometers per hour'),
        ('knot', 'knots')
    )),
    ('temperature', 'temperatures', (
        ('C', 'degrees Celsius'),
        ('F', 'degrees Fahrenheit'),
        ('K', 'degrees Kelvin')
    )),
    ('time', 'times', (
        ('ns', 'nanoseconds'),
        ('micros', 'microseconds'),
        ('ms', 'milliseconds'),
        ('s', 'seconds'),
        ('min', 'minutes'),
        ('h', 'hours'),
        ('day', 'days'),
        ('week', 'weeks'),
        ('month', 'months'),
        ('year', 'years'),
        ('decade', 'decades'),
        ('century', 'centuries')
    )),
    ('volume', 'volumes', (
        ('lgallon', 'US liquid gallons'),
        ('lquart', 'US liquid quarts'),
        ('lpint', 'US liquid pints'),
        ('uscup', 'US legal cups'),
        ('usfloz', 'US fluid ounces'),
        ('ustbsp', 'US tablespoons'),
        ('ustsp', 'US teaspoons'),
        ('m3', 'cubic meters'),
        ('l', 'liters (cubic decimeters)'),
        ('ml', 'milliliters (cubic centimeters)'),
        ('gallon', 'Imperial gallons'),
        ('quart', 'Imperial quarts'),
        ('pint', 'Imperial pints'),
        ('cup', 'Imperial cups'),
        ('floz', 'Imperial fluid ounces'),
        ('tbsp', 'Imperial tablespoons'),
        ('tsp', 'Imperial teaspoons'),
        ('ft3', 'cubic feet'),
        ('in3', 'cubic inches')
    ))
)

print('{')
print('  "cog-desc": "Convert units between each other.\nRun `{0}help Units` to see unit types.\nRun `{0}help <type>` to see units available.\nRun `{0}<type> <unit1> <unit2> <amount>` to convert from `unit1` to `unit2`.",')
for kind, k2n, pairs in units:
    print(f'  "{kind}-desc": "Convert {k2n}",')
    for unit1, u2n1 in iter(pairs):
        print(f'  "{kind}-{unit1}-desc": "Convert {k2n} from {u2n1}",')
        for unit2, u2n2 in iter(pairs):
            if unit1 == unit2:
                continue
            print(f'  "{kind}-{unit1}-{unit2}-desc": "Convert {k2n} from {u2n1} to {u2n2}",')
print('}')
print('// REMEMBER TO REMOVE LAST COMMA')
