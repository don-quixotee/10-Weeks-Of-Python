def linear_search(n,k):
    for index,value in enumerate(n):
        if value == k:
            return True,index
            
    else:
        return False

nums = [10,20,30,40,50,60]
key = 50
print(linear_search(nums,key))