# Find the sum of the odd numbers within an array, after cubing the initial integers. 
# The function should return undefined/None/nil/NULL if any of the values aren't numbers.
# Note: Booleans should not be considered as numbers.

def cub_odd(arr):
    total = None
    
    for i in arr:
        if  isinstance(i, int) and not isinstance(i, bool):
            cube = i ** 3
            if cube % 2 != 0:
                if total is None:
                    total = cube
                else:
                    total += cube 
        else:
            return None
        
    return total

my_list = [1,4,True,False,None,"FD",4,4,6,43,234,46,5,2,34,5,6,7]
my_list_2 = [3,3,4,5]
print(cub_odd(my_list_2))