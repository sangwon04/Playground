# findUniqueNums.py
# Finds unique entries within file containing random, 6-digit integers

f = open('randomNumbers', 'r')
nums = f.read().splitlines()
unique = set(nums)
print '\n'.join(list(unique))
f.close()
print "\nTotal: %d" % len(unique)
