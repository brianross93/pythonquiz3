number_list = [1,3,5,6,7]

def get_average(num_list):
    """this functions returns the average of the numbers in the input list"""

    num_Sum = 1
    for i in num_list:
        num_Sum += num_list[i]
        return sum(num_list) / len(num_list)



print(get_average(number_list))


