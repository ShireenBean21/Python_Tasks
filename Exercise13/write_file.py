f = open("pelican.txt", "w")
f.write("A wonderful bird is the Pelican,\n ")
f.append("His bill holds more than his pelican,\n ")
lines = ["He can take in his beak,\n", "Enough food for a week,\n" "But I'm damned if I see how the pelican.\n"]
f.writelines(lines)
print(f)
