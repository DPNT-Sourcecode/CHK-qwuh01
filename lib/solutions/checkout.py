

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	valids = ['A','B','C','D']

	count = {}

    for char in skus:
    	if char not in valids:
    		return -1
    	if char in count:
    		count[char] += 1
    	else:
    		count[char] = 1

    if  count['a'] >= 3:
    	i = count['a']
    	aCounter = 0
    	while i >= 3:
    		i = count['a'] % 3  
    		aCounter += 1

    	aAmount = aCounter*130 + i*50

    if count['b'] >= 2:
    	j = count['b']
    	bCounter = 0
    	while j >= 2:
    		j = count['b'] % 2  
    		bCounter += 1

    	bAmount = bCounter*45 + 30

    cAmount = count['c']*20
    dAmount = count['d']*15

    return aAmount + bAmount + cAmount + dAmount





