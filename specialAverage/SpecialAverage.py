#This program is built on Python 3.7
list1 = [1, 2, 3, 4, 100]
list2 = [1, 1, 5, 5, 10, 8, 7]
list3 = [-10, -4, -2, -4, -2, 0]
list4 = [100, 200]

def SpecialAverage(list):
    # Check if the length is the required
    if (len(list) < 3):
        raise Exception("The list should contain at least three elements")
    else:
        # Sort the list to have it ordered
        list.sort()
        # print("list sorted is ", list)
        # Remove the first element
        list.pop(0)
        # Count the length and remove the last elemet
        lastItemPos  = len(list) - 1
        list.pop(lastItemPos)
        # print("Removing first and last element, list is ", list)
        # Sum all the elements and count the list length
        # Do the int division after, assign it to the average
        listSum = sum(list)
        listLen = len(list)

        average = listSum // listLen
        print("Special Average of list is", average)
        return average;

SpecialAverage(list1)
# SpecialAverage(list2)
# SpecialAverage(list3)
# SpecialAverage(list4)
