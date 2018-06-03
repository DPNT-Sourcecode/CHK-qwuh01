

# noinspection PyUnusedLocal
# skus = unicode string
#

def firstAOffer(value):
    i = value % 3  
    aCounter = value / 3 
    aAmount = aCounter*130 + i*50

    return aAmount

def checkout(skus):

  #if not isinstance(skus, unicode):
    #return -1

  aAmount, bAmount, cAmount, dAmount, eAmount, fAmount = 0, 0, 0, 0, 0, 0

  noOfferPrices = {'C': 20, 'D': 15, 'G':20, 'I':35, 'J':60, 'L':90, 'M':15, 'O':10, 'S':30, 'T':20, 'W':20, 'X':90, 'Y':10, 'Z':50}

  count = {'A': skus.count('A'), 'B': skus.count('B'), 'C': skus.count('C'), 'D': skus.count('D'), 'E': skus.count('E'), 'F': skus.count('F'),
  'G': skus.count('G'), 'H': skus.count('H'), 'I': skus.count('I'), 'J': skus.count('J'), 'K': skus.count('K'), 'L': skus.count('L'), 'M': skus.count('M'),
  'N': skus.count('N'), 'O': skus.count('O'), 'P': skus.count('P'), 'Q': skus.count('Q'), 'R': skus.count('R'), 'S': skus.count('S'), 'T': skus.count('T'),
  'U': skus.count('U'), 'V': skus.count('V'), 'W': skus.count('W'), 'X': skus.count('X'), 'Y': skus.count('Y'), 'Z': skus.count('Z')}

  items = count.keys()

  noOfferItemsValue = 0

  for char in items:
  	if char in noOfferPrices.keys():
  		noOfferItemsValue += count[char] * noOfferPrices[char]


  for i in skus:
  	if i not in items:
  	  return -1


  if "A" in items and count["A"] >= 3 and count["A"] < 5:
    i = count["A"] % 3  
    aCounter = count["A"] / 3 
    aAmount = aCounter*130 + i*50
  elif "A" in items and count["A"] >= 5:
  	i = count["A"] % 5  
    	aCounter = count["A"] / 5
    	if i >= 3:
      		otherAmount = firstAOffer(i)
      		aAmount = aCounter*200 + otherAmount
    	else:
      		aAmount = aCounter*200 + i*50
  elif "A" in items:
  	aAmount = count["A"] * 50


  if "E" in items and count["E"] >= 2:
  	eCounter = count["E"] / 2
  	count["B"] -= eCounter
  	eAmount = count["E"]*40
  elif "E" in items:
  	eAmount = count["E"]*40


  if "B" in items and count["B"] >= 2:
    j = count["B"] % 2  
    bCounter = count["B"] / 2
    bAmount = bCounter*45 + j*30
  elif "B" in items:
  	if count["B"] < 0:
  		count["B"] = 0
  	bAmount = count["B"] * 30


  #if "C" in items:
    #cAmount = count["C"] * 20


  #if "D" in items:  
    #dAmount = count["D"] * 15

  if "F" in items and count["F"] == 3:
      fCounter = count["F"] / 2
      count["F"] -= fCounter
      fAmount = count["F"] * 10
  if "F" in items and count["F"] > 3:
  	  	count["F"] -= 2
  		fCounter = count["F"] / 2
		count["F"] -= fCounter
		fAmount = count["F"] * 10 + 20
  else: 
    fAmount = count["F"] * 10

  if count["H"] > 5 and count["H"] < 10:
  	i = count["H"] % 5  
    hCounter = count["H"] / 5 
    hAmount = hCounter*130 + i*10

  return aAmount + bAmount + eAmount + fAmount + noOfferItemsValue

print checkout('CD')