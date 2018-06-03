

# noinspection PyUnusedLocal
# skus = unicode string
#

def checkout(skus):

  if type(skus) != type(""):
    return -1

  valids = ["A", "B", "C", "D"]
  aAmount, bAmount, cAmount, dAmount = 0, 0, 0, 0

  count = {}

  for char in skus:
      if char in valids and char in count:
        count[char] += 1
      elif char in valids:
    	count[char] = 1


  if "A" in count.keys() and count["A"] >= 3:
    i = count["A"]
    aCounter = 0
    while i >= 3:
      i = count["A"] % 3  
      aCounter += 1

      aAmount = aCounter*130 + i*50
  elif "A" in count.keys():
  	aAmount = count["A"] * 50


  if "B" in count.keys() and count["B"] >= 2:
    j = count["B"]
    bCounter = 0
    while j >= 2:
      j = count["B"] % 2  
      bCounter += 1

      bAmount = bCounter*45 + j*30
  elif "B" in count.keys():
  	bAmount = count["B"] * 30


  if "C" in count.keys():
    cAmount = count["C"] * 20


  if "D" in count.keys():  
    dAmount = count["D"] * 15

  result = aAmount + bAmount + cAmount + dAmount

  return result

# Exact tests are passing locally, but failing when being sent to the server.