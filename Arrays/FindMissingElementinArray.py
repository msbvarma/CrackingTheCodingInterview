class ArraysProblemSolving:
    #O(n)
    @staticmethod
    def findMissingElementinArray(input):
        array_len = len(input)+1
        print('array_len=',array_len)
        expected_sum = (array_len * (array_len+1))/2 #O(1)
        print('expected_sum=',expected_sum)
        actual_sum = 0
        for element in input: #O(n)
            actual_sum += element
        print('actual_sum=',actual_sum)
        print('Missing Number=',int(expected_sum)-actual_sum)
        #Problem is risk of overflow while calcualting sum of n numbers
    @staticmethod
    def missingNumerBinarySearch(ar):
        # A binary search based program to find
        # the only missing number in a sorted
        # in a sorted array of distinct elements
        # within limited range
        size = len(ar)
        a ,b,mid = 0 ,size - 1, 0
        while b > a + 1:
            mid = (a + b) // 2
            if (ar[a] - a) != (ar[mid] - mid):
                b = mid
            elif (ar[b] - b) != (ar[mid] - mid):
                a = mid
        print("Missing=",ar[a] + 1)

# This code is contributed
# by Mohit Kumar

class Array:
    problemSolving = ArraysProblemSolving()
    
    #Missing Element in an array
    input1= [1,2,3,4,5,7,8,9,10]
    problemSolving.findMissingElementinArray(input1)
    problemSolving.missingNumerBinarySearch(input1)
    #We can use XOR operation based sum, which will result in O(n)