'''Procedure:-

Isolate the last digit, say d from the number using % operator. If d is 0 make d’s value 1 else the digit remains as it is. 
Use the formula ans = tmp*d+ ans  to form the number. 
Divide the original integer by 10 to discard the last digit.
Multiply tmp with 10.
Repeat step 1-4  till input integer > 0. '''
def replaceZerosWithOnes(num):
    if(num == 0):
        return 1
    ans =0
    decimal =1
    while(num > 0):
        d = num %10
        if(d == 0):
            d =1
        ans = d * decimal + ans
        num = int(num/10)
        decimal = decimal * 10
    return ans

print("Replace Zero with 1",replaceZerosWithOnes(130204))