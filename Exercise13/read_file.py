with open('pelican.txt', 'r') as pelican:
    lines = pelican.read()
with open('pelican.txt', 'r') as pelican:
    llines = pelican.readlines()

print(lines)
print(len(llines))

print(''.join(llines))
