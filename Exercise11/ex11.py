
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print(Belgium)


print("-" * len(Belgium))

Belgium_list = Belgium.split(",")

print(Belgium_list)

Belgium = Belgium.replace(",", ":")

print(Belgium_list)

population = int(Belgium_list[1]) + int(Belgium_list[3])
print(population)


