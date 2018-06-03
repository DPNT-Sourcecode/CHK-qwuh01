

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
      i = count["A"] % 3  
      aCounter = count["A"] / 3 
      aAmount = aCounter*130 + i*50
  elif "A" in count.keys():
  	aAmount = count["A"] * 50


  if "B" in count.keys() and count["B"] >= 2:
      j = count["B"] % 2  
      bCounter = count["B"] % 2
      bAmount = bCounter*45 + j*30
  elif "B" in count.keys():
  	bAmount = count["B"] * 30


  if "C" in count.keys():
    cAmount = count["C"] * 20


  if "D" in count.keys():  
    dAmount = count["D"] * 15

  return aAmount + bAmount + cAmount + dAmount

print checkout('AAABBBBB')
print 130+90+30