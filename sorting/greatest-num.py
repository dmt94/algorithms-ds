
def greatest_number(arr):
    for i in arr:
        # assume first element is greatest
        isValGreatest = True

        for j in arr:
            # if we find another val that is greater than i,
            # means i is not the greatest 
            if j > i:
                isValGreatest = False
        
        if isValGreatest:
            return i
        

# rewrite the above so it becomes a speedy O(N)
# find the greatest single number within an array

def the_greatest_num(arr):
    greatest_num = arr[0]

    for num in arr:
        if num > greatest_num:
            greatest_num = num
    return greatest_num


print(the_greatest_num([4,23,100,2,22]))