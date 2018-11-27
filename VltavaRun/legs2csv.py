import json

separator = '\t'
with open('exportedLegs.json', 'r', encoding='utf8') as f:
    route = json.load(f)
    with open('legs.csv', 'w') as fOut:
        for i in range(36):
            leg = route['legs'][i]
            legString = str.format("{}{}{}{}{}{}{}{}{}{}{}{}{}",
                                   i+1, separator,
                                   route['handovers'][i]['name'], separator,
                                   route['handovers'][i+1]['name'], separator,
                                   leg['length'], separator,
                                   leg['difficulty'], separator,
                                   leg['upHill'], separator,
                                   leg['downHill'])
            fOut.write(legString)
            fOut.write('\n')
