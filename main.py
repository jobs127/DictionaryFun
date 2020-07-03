words = []

file = open ('dictionary.txt', 'r')

for line in file:
  words.append (line.strip ('\n').split (','))

file.close
print(len(words))
