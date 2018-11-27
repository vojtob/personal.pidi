with open('ai_repeatWords.txt', 'w') as fTo:
    with open('ai_words.txt', 'r') as f:
        for line in f:
            lineSplit = line.split();
            print(lineSplit)
            for i in range(int(lineSplit[0])) :
                fTo.write(lineSplit[1])
                fTo.write("\n")
