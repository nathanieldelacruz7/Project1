import random
def headsOrTails():
    hORt = ("H", "T")
    results = []
    for i in range(100):
        results.append(random.choice(hORt))
    return results

def streakOfSix(ht):
    initial = ht[0]
    currentStreak = 0
    for i in range(1,99):
        if ht[i] == ht[i-1]:
            currentStreak +=1
        else:
            currentStreak = 0
        if currentStreak == 6:
            return 1
    return 0

totalStreaks = 0
for i in range(10000):
    totalStreaks += streakOfSix(headsOrTails())

print('Chance of streak: {}%'.format(round(((totalStreaks/10000 )*100),2)))
