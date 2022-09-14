a = input("Letter here: ")
key = int(input("How many key: "))

def shift(letter):
    asci = ord(letter)
    cypherShift = 97 + (asci + key -97) % 26
    return chr(cypherShift)

letterList = []
shiftList = []
combineList = {}

def convert(e):
  return combineList[data]

for i in range(65,91):
  letterList.append(chr(i))

for x in range(len(letterList)):
  shiftList.append(shift(letterList[x]).upper())

for z in range(len(letterList)):
  combineList.update({shiftList[z].upper(): letterList[z].upper()})
  combineList.update({shiftList[z].lower(): letterList[z].lower()})
combineList.update({" ": " "})

result = ""
for w in range(len(a)):
  data = a[w]
  result = result + convert(data)

print(result)
