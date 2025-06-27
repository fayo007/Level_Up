# Output
# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).


In this challenge, I learned how to deal with slightly more complex conditions in a loop. The code works by taking one element from the list at a time using a for loop. Then it uses the count function to check how many times that number appears in the list.To find the odd-occurring number, I used the modulo % operator, which is a well-known method to detect if a number is odd. If the count is not divisible by 2, that means it appears an odd number of times, and I return it.The code is not too complicated, but I still find it very useful. It helped me better understand how to mix loops, conditions, and built-in methods to solve problems.