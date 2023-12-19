import random

lapok = "AQKJ"
randomLapok = ""

for i in range(1):
    randomLapok = random.choice(lapok)

lapocskak = random.sample(range(1, 10), 4)
print(lapocskak)
osszlap = []
for i in lapocskak:
    osszlap.append(i)
osszlap.append(randomLapok)

print(osszlap)