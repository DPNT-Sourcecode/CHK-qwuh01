

# noinspection PyUnusedLocal
# skus = unicode string
#

def checkout(skus):

  if type(skus) != type(""):
    return -1

  aAmount, bAmount, cAmount, dAmount = 0, 0, 0, 0

  count = {'A': skus.count('A'), 'B': skus.count('B'), 'C': skus.count('C'), 'D': skus.count('D')}

  if "A" in count.keys() and count["A"] >= 3:
      i = count["A"] % 3  
      aCounter = count["A"] / 3 
      aAmount = aCounter*130 + i*50
  elif "A" in count.keys():
  	aAmount = count["A"] * 50


  if "B" in count.keys() and count["B"] >= 2:
      j = count["B"] % 2  
      bCounter = count["B"] / 2
      bAmount = bCounter*45 + j*30
  elif "B" in count.keys():
  	bAmount = count["B"] * 30


  if "C" in count.keys():
    cAmount = count["C"] * 20


  if "D" in count.keys():  
    dAmount = count["D"] * 15

  return aAmount + bAmount + cAmount + dAmount