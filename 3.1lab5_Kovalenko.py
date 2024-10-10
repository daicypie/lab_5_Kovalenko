#Багатовимірні списки. Генератор списків

#1

# Взяла код з методички
temps = [[0.0 for h in range(24)] for d in range(31)]

# Взяла рандомні значення температур
import random

for d in range(31):
    for h in range(24):
        temps[d][h] = round(random.uniform(-10.0, 35.0), 1)

for day in temps:
   print(day)

#2

# Взяла код з методички
temps = [[0.0 for h in range(24)] for d in range(31)]
# Калькулятор середньомісячної полуденної температури
total = 0.0
for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)