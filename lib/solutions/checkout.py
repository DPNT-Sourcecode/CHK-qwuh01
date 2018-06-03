

# noinspection PyUnusedLocal
# skus = unicode string
#

def checkout(skus):

  if type(skus) != type(''):
    return -1

  valids = ['A', 'B', 'C', 'D']
  aAmount, bAmount, cAmount, dAmount = 0, 0, 0, 0

  count = {}

  for char in skus:
      if char in valids and char in count:
        count[char] += 1
      elif char in valids:
    	count[char] = 1


    if count['A'] >= 3:
    	i = count['A']
    	aCounter = 0
    	while i >= 3:
    		i = count['A'] % 3  
    		aCounter += 1

    	aAmount = aCounter*130 + i*50

    if count['B'] >= 2:
    	j = count['B']
    	bCounter = 0
    	while j >= 2:
    		j = count['B'] % 2  
    		bCounter += 1

    	bAmount = bCounter*45 + 30

    cAmount = count['C'] * 20
    dAmount = count['D'] * 15

    return aAmount + bAmount + cAmount + dAmount

print checkout('ABCD')

