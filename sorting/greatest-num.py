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