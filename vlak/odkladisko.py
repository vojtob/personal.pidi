import json












def float_range(start, end, step):
    while start <= end:
        yield start
        start += step
'''
with open("vlak.csv", 'w') as f:
    f.write('{:>12s}; {:>12s}; {:>12s}; {:>12s}\n'.format('startVelocity', 'endVelocity', 'doba', 'dlzka'))
    for startVelocity in range(20, 100, 10):
        for endVelocity in range(startVelocity, startVelocity+10, 2) :
            for doba in float_range(0.6,1.4,0.1):
                dlzka = ((startVelocity+endVelocity) / (2*3.6)) * doba
                f.write('{:12d}; {:12d}; {:12.2f}; {:12.4f}\n'.format(startVelocity, endVelocity,doba, dlzka))
                #print(startVelocity, endVelocity, '{:5.2f}'.format(doba), '{:8.4f}'.format(dlzka), sep=';')
'''

with open("vlak.json", 'w') as f:
    for startVelocity in range(20, 100, 10):
        for endVelocity in range(startVelocity, startVelocity+10, 2) :
            for doba in float_range(0.6,1.4,0.1):
                dlzka = ((startVelocity+endVelocity) / (2*3.6)) * doba
                rec = {'startVelocity':startVelocity, 'endVelocity':endVelocity, 'doba':doba, 'dlzka':dlzka}
                f.write(json.dumps(rec))
                f.write('\n')

with open("vlak.json", 'r') as f:
    for line in f:
        t = json.loads(line)
        print(t)
        print(t['startVelocity']+2)
