

# noinspection PyUnusedLocal
# skus = unicode string
#

def firstAOffer(value):
    i = value % 3  
    aCounter = value / 3 
    aAmount = aCounter*130 + i*50

    return aAmount

def checkout(skus):

  if not isinstance(skus, unicode):
    return -1

  aAmount, bAmount, cAmount, dAmount, eAmount = 0, 0, 0, 0, 0

  count = {'A': skus.count('A'), 'B': skus.count('B'), 'C': skus.count('C'), 'D': skus.count('D'), 'E': skus.count('E')}

  items = count.keys()

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


  if "E" in items and count["E"] >=:
  	eCounter = count["E"] / 2
  	count["B"] -= eCounter
  	eAmount = count["E"]*40


  if "B" in items and count["B"] >= 2:
      j = count["B"] % 2  
      bCounter = count["B"] / 2
      bAmount = bCounter*45 + j*30
  elif "B" in items:
  	bAmount = count["B"] * 30


  if "C" in items:
    cAmount = count["C"] * 20


  if "D" in items:  
    dAmount = count["D"] * 15

  return aAmount + bAmount + cAmount + dAmount + eAmount
