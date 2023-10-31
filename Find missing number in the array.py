#Write a function to find the missing number in a given integer array 
def missing_number(arr,n):
    total = n*(n+1)//2
    print(total)
    sum_arr = sum(arr)
    missing =  total-sum_arr
    print(missing)
    return missing;

print(missing_number([1,3,4,5,6],6))