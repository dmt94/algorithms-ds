
def max(arr, count=0):
    # print("RECURSION")
    count += 1

    if len(arr) == 1:
        print("Base Case reached =>", arr[0])
        return arr[0]
    
    max_of_remainder = max(arr[1:], count)

    # comparison of first number against max of remainder variable
    if arr[0] > max_of_remainder:
        print("Count is:", count)
        print("New max found ", arr[0])
        return arr[0]
    else:
        print("Count is:", count)
        print("Max of remainder for this round is: ", max_of_remainder)
        return max_of_remainder
    

max([4,3,8,7,12,22,9,15])