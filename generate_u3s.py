"""Generate kenny2automate units i18n.

Procedure:
1. Internationalize i18n/units-meta/en.json into your language. For example,
   Japanese i18n goes in i18n/units-meta/ja.json - note to only translate the
   JSON values, not keys.
2. Run `python3 generate_u3s.py <language code, e.g. 'ja' for Japanese>`

"""

import sys
import json

LANG = sys.argv[1]

with open(f'i18n/units-meta/{LANG}.json') as f:
    units = json.load(f)

sys.stdout = open(f'i18n/units/{LANG}.json', 'w')

print('{')
print(f'  "cog-desc": {json.dumps(units["*"]["cog-desc"])},')
print(f'  "convert-desc": {json.dumps(units["*"]["convert-desc"])},')
kinded = False
for kind, data in units.items():
    if kind == '*':
        continue
    k2n = data['name']
    pairs = data['units'].items()
    if kinded:
        print(',')
    else:
        kinded = True
    string = json.dumps(units['*']['kind-desc'])
    string1 = json.dumps(units['*']['kind-unit1-desc'])
    string12 = json.dumps(units['*']['kind-unit1-unit2-desc'])
    for unit1, u2n1 in iter(pairs):
        for unit2, u2n2 in iter(pairs):
            if unit1 == unit2:
                continue
            string123 = string12.format(
                k2n, u2n1, u2n2
            )
            print(f'  "{kind}-{unit1}-{unit2}-desc": {string123},')
        string123 = string1.format(k2n, u2n1)
        print(f'  "{kind}-{unit1}-desc": {string123},')
    string123 = string.format(k2n)
    print(f'  "{kind}-desc": {string123}', end='')
print('\n}')

sys.stdout.close()
sys.stdout = sys.__stdout__
