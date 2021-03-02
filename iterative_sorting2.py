#funtion returns weather items are sorted or not boolean
#creating the function and passing in items
def is_sorted(items):
    # setting variable copy to equal items
    copy = items[:]
    #calling sort method on copy
    copy.sort()
    # if copy is equal to items it returns true 
    return copy == items

def bubble_sort(items):
    #set is sorted to true
    is_sorted = True
    # set a counter to 0
    counter = 0
    # while items_is_sorted we want to then change is sorted to false
    while(is_sorted):
        #set is sorted to false 
        is_sorted = False
        # this is the for loop to loop trhough the items
        for i in range(len(items) - counter - 1):
            #if the item we are looking at is larger thane the item to its right we want to swap them 
            if items[i] > items[i+1]:
                # swap the items positioins
                items[i], items[i+1] = items[i+1], items[i]
                # is sorted now becomes troue
                is_sorted = True
                # incremantation of the counter to move though the array
        counter += 1

def selection_sort(items):
    #finding the  minimum item and swaping it with the first unsorted item and repeating until all items are in soreted order
    #for loop to loop throught the items
    items_length = range(0, len(items)-1)
    for i in items_length:
        #set min value to i
        min_value = i
#nested for loop to set  j value
        for j in range(i+1, len(items)):
            if items[j] < items[min_value]:
                min_value = j
        
        items[min_value], items[i] = items[i], items[min_value]
    return items


def insertion_sort(items):
    item_length = range(1, len(items))
    for i in item_length:
          #element to be compared
        unsorted_value = items[i]

            #comparing the current element with the sorted portion and swapping

        while items[i-1] > unsorted_value and i > 0:
            items[i], items[i-1] = items[i-1], items[i]
            i -= 1
            #returning items 
    return items