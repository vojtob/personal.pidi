import re

def createStrings(fileName):
    with open(fileName, 'r', encoding='utf8') as f:
        temp = f.readlines()
        text = []
        for l in temp:
            text.append(l.rstrip())
        rows = len(text)
        cols = len(text[0])
        print("rows: {0}  cols: {1}  pismen: {2}".format(rows, cols, rows*cols))

        directions = []

        # po riadkoch
        dir = []
        for r in range(rows):
            dir.append(text[r])
        directions.append(dir)

        # po riadkoch opacne
        dir = []
        for r in range(rows):
            s = ''
            for c in range(cols):
                s += text[r][cols-c-1]
            dir.append(s)
        directions.append(dir)

        # po stlpcoch
        dir = []
        for c in range(cols):
            s = ''
            for r in range(rows):
                s += text[r][c]
            dir.append(s.rstrip())
        directions.append(dir)

        # po stlpcoch opacne
        dir = []
        for c in range(cols):
            s = ''
            for r in range(rows):
                s += text[rows - 1- r][c]
            dir.append(s.rstrip())
        directions.append(dir)

        # JZ - SV
        dir = []
        for sum in range(rows+cols-1):
            s = ''
            for c in range(sum+1):
                r = sum-c
                if(c < cols) and (r<rows):
                    s += text[r][c]
            dir.append(s)
        directions.append(dir)

        # SV - JZ
        dir = []
        for sum in range(rows+cols-1):
            s = ''
            for c in range(sum+1):
                r = sum-c
                if(c < cols) and (r<rows):
                    s = text[r][c] + s
            dir.append(s)
        directions.append(dir)

        # SZ - JV
        dir = []
        for sum in range(rows+cols-1):
            s = ''
            for c in range(sum+1):
                r = sum-c
                if (r<cols) and (c<rows):
                    s += text[rows - 1 - c][r]
            dir.append(s)
        directions.append(dir)

        # JV - SZ
        dir = []
        for sum in range(rows+cols-1):
            s = ''
            for c in range(sum+1):
                r = sum-c
                if (r<cols) and (c<rows):
                    s = text[rows - 1 - c][r] + s
            dir.append(s)
        directions.append(dir)

    return directions

popisSmerov = ["Z-V", "V-Z", "S-J", "J-S", "JZ-SV", "SV-JZ", "JV-SZ", "SZ-JV"]
def findPattern(pattern, strings):
    for d in range(8):
        dir = strings[d]
        for s in dir:
            if re.search(pattern, s, re.IGNORECASE) is not None:
                res = re.search(pattern, s, re.IGNORECASE)
                print(popisSmerov[d], s[:res.start()] + '*'+s[res.start():res.end()] + '*' + s[res.end():])

def findWord(word, strings):
    for i in range(len(word)):
        findPattern(word[:i] + '.' + word[i+1:], strings)

def findWord2(word, strings):
    for i in range(len(word)-1):
        for j in range (i+1, len(word)):
            findPattern(word[:i] + '.' + word[i+1:j] + '.' + word[j+1:], strings)

strings = createStrings('T8.txt')
findWord('ORLI', strings)
# findWord2('NEKOV', strings)