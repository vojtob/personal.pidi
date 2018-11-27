import json

def processPage(pageNumber, pageLines, route):
    print(pageLines)
    leg = {}
    textRunner = ''
    textCar = ''
    modeRunner = True

    for lineNumber in range(len(pageLines)):
        lineText = pageLines[lineNumber]
        if lineText.startswith('Start'):
            route['handovers'].append(processHandover(lineText[len('Start'):]))
        elif lineText.startswith('Cíl'):
            if (pageNumber == 35):
                route['handovers'].append(processHandover(lineText[len('Cíl'):]))
        elif lineText.startswith('Trasa'):
            pass
        elif lineText.startswith('Délka'):
            leg = processLength(lineText, leg)
            if not textRunner:
                modeRunner = True
        elif 'Stoupání:' in lineText:
            leg = processUpHill(lineText, leg)
            if not textRunner:
                modeRunner = True
        elif 'Klesání:' in lineText:
            leg = processDownHill(lineText, leg)
            if not textRunner:
                modeRunner = True
        elif lineText.startswith('Povrch'):
            leg = processSurface(lineText, leg)
            if not textRunner:
                modeRunner = True
        elif lineText.startswith('bežce'):
            modeRunner = True
        elif lineText.startswith('auta'):
            modeRunner = False
        elif lineText[:2].isnumeric():
            # print("Ignore : ", lineText)
            if not textRunner:
                modeRunner = True
        else:
            if modeRunner:
                textRunner = textRunner + lineText
            else:
                textCar = textCar + lineText

    leg['runner'] = textRunner
    leg['car'] = textCar

    route['legs'].append(leg)
    return route

def processHandover(handoverText):
    handover = {}
    handoverText = handoverText[handoverText.find(' '):]
    # rozdel text po /, tam uz su suradnice
    tag = handoverText.find('/')
    handover['gps'] = handoverText[tag+2:].strip()
    handoverText = handoverText[:tag]
    # ak sa da rozdel na nazov a detail
    tag = handoverText.find(',')
    if(tag > -1):
        handover['name'] = handoverText[:tag].strip()
        handover['detail'] = handoverText[tag+2:].strip()
    else:
        handover['name'] = handoverText.strip()
    return handover

def processLength(lineText, leg):
    # print('Proces delka: {}', lineText)
    tag = lineText.find('km')
    leg['length'] = lineText[6:tag].strip()
    # spracuj obtiaznost
    lineText = lineText[tag + 2:]
    tag = lineText.find('Náro')
    leg['difficulty'] = lineText[tag+20:].strip()
    return leg

def processUpHill(lineText, leg):
    # print('Proces upHill: {}', lineText)
    tag = lineText.find('Stoupání:')
    lineText = lineText[tag+len('Stoupání:'):]
    tag = lineText.find('m')
    leg['upHill'] = lineText[:tag].strip()
    return leg

def processDownHill(lineText, leg):
    # print('Proces downHill: {}', lineText)
    tag = lineText.find('Klesání:')
    lineText = lineText[tag+len('Klesání:'):]
    tag = lineText.find('m')
    leg['downHill'] = lineText[:tag].strip()
    return leg

def processSurface(lineText, leg):
    # print('Proces surface: ', lineText)
    tag = lineText.find('Povrch')
    leg['surface'] = lineText[tag+len('Povrch'):].strip()
    return leg


route = { 'handovers' : [], 'legs' : []}

with open('sourceRoute.txt', 'r', encoding="utf8") as fInput:
    with open('exportedLegs.json', 'w', encoding='utf8') as f:
        # skip begin of file
        for i in range(17):
            fInput.readline();

        for pageNumber in range(36) :
            print("****** Start page {} ******".format(pageNumber))
            # skip until Propozice Vltava Run 2018
            while True:
                line = fInput.readline()
                if ('Propozice Vltava Run 2018' in line):
                    break
            # skip page number
            fInput.readline();

            pageLines = [];
            while True:
                line = fInput.readline()
                if('Propozice Vltava Run 2018' in line):
                    route = processPage(pageNumber, pageLines, route)
                    break
                else:
                    pageLines.append(line);
            #skip page number
            fInput.readline();

        f.write(json.dumps(route, ensure_ascii=False, indent=4))
# print(json.dumps(route, ensure_ascii=False, indent=4))
