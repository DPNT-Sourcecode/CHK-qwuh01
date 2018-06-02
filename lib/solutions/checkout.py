

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	valids = ['a','b','c']
	skus = skus.lower()
	
    for i in skus:
    	if i not in valids:
    		return -1
