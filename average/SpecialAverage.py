#This program is made on Python 3.7
list2 = [1, 2, 3, 4, 100]
#list2 = [1, 1, 5, 5, 10, 8, 7]
#list2 = [-10, -4, -2, -4, -2, 0]

print("Max value of list1 is ", max(list2), " and min value is ", min(list2))

print("list2 is ", list2)
list2.sort()
print("list2 sorted is ", list2)
list2.pop(0);
print("Removing first element, list2 is now", list2)
lastItemPos  = len(list2) - 1
print("Last item position is", lastItemPos)
list2.pop(lastItemPos)
print("Removing last element, list2 is now", list2)
sum = sum(list2)
len = len(list2)

print("Sum of list2 is ", sum, " and length of list2 is ", len)
average = sum//len
print("Special Average of list 2 is ", average)

def SpecialAverage(list):

    pass
