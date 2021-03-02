from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n+k) only works when the range of potential items in the input is known ahead of time
    TODO: Memory usage: O(n+k) If the rnage of potential values is big, then counting sort requires a lot of space"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    max_value = int(max(numbers))
    min_value = int(min(numbers))
    # Created a count array to store count of individual elements and initialize
    # array as 0
    counter = []
    
    for _ in range(max_value - min_value + 1):
        counter.append(0)
    
    outer = [] 
    for _ in range(len(numbers)):
        outer.append(0)
    # Store count of each character
    for i in range(0, len(numbers)):
        counter[numbers[i]- min_value] += 1
    # Build output character array
    for i in range(len(numbers)-1, -1, -1):
        outer[counter[numbers[i] - min_value] - 1] = numbers
        counter[numbers[i] - min_value] -= 1

    # Copy output array to arr, so that arr now contains sorted characters
    for i in range(0, len(numbers)):
        numbers[i] = outer[i]

    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time:
    Best: O(n*k) You only need to traverse the original array once,
    and the new array or bucket k times, where k is the number of buckets that isn't empty
    Worst: O(n^2), There would be the same number of full buckets ast ehre are items in the original array, or else the array balues are so unevenly distributed that the sorting and arranging of the sub-arrays in the buckets takes more time
    Memory usage:O(n) memory usage will be linear as the algorithm only needs to create one extra data structure. Python uses dynamic arrays which allow for more flexibility"""
    arr =  []

    # Create empty buckets
    for i in range(num_buckets):
        arr.append([])

    # isnert each elements from numbers into each bucket
    for num in numbers:
        index = int(num/max(numbers)* (num_buckets + 1))
        bucket = arr[index]
        bucket.append(num)

    # Then sort each element using insertion sort
    for bucket in arr:
        insertion_sort(bucket)

    # get sorted elements
    index = 0
    for i in range(num_buckets):
        for value in arr[i]:
            numbers[index] = value
            index += 1

    # return sorted numbers array
    return numbers