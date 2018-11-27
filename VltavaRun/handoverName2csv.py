import json

with open('exportedLegs.json', 'r', encoding='utf8') as f:
    route = json.load(f)
    with open('legs.csv', 'w') as fOut:
        for i in range(37):
            # leg = route['legs'][i]
            legString = str.format(route['handovers'][i]['name'])
            fOut.write(legString)
            fOut.write('\n')
