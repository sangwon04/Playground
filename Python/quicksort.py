'''
Practicing quicksort algorithms
'''

# Taking raw input and creating a list out of it
myList = raw_input("Enter a sequence of numbers separated by a space: ")
myList = myList.split()
myList = [int(x) for x in myList[0:]]
print "Unsorted: %r\n" % myList

# quicksort magic
def quickSort(unsortedList):
    if len(unsortedList) < 2:
        return unsortedList
    lesser = quickSort([x for x in unsortedList[1:] if x <= unsortedList[0]])
    bigger = quickSort([x for x in unsortedList[1:] if x > unsortedList[0]])
    print lesser, bigger, unsortedList, sum([lesser, [unsortedList[0]], bigger], [])
    return sum([lesser, [unsortedList[0]], bigger], [])

#print "Sorted: %r" % quickSort(myList)
print "\nSorted: %r" % quickSort(myList)
