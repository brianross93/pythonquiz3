def adding(num_input):
    # create variable to store number iterated over
    add_tracker=0
    for i in num_input:
        #add the current number to previous number
        add_tracker+=i
    return add_tracker
# 4 + 5 + 2 +-3 = 8
print(adding([4,5,2,-3]))