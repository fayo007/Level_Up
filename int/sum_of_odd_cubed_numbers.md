# Find the sum of the odd numbers within an array, after cubing the initial integers. 
# The function should return undefined/None/nil/NULL if any of the values aren't numbers.
# Note: Booleans should not be considered as numbers.


This function takes a list as input and returns the sum of the odd numbers after cubing them — only if all elements are valid integers. If there is even one non-integer (like a string, None, or bool), the function returns None.

What I learned from this problem

Working on this problem helped me understand the int data type much better in Python. Here's what I gained:

I learned to use the isinstance() function to check the type of each value in the list. This is useful when you want to be sure you're only working with integers.

I also practiced using logical operators like and and not to combine conditions. For example, I used not isinstance(i, bool) because in Python, bool is a subclass of int, and I didn’t want True and False to be counted as integers.

I used the is operator to compare values to None. I read that using is is the preferred way to check for None instead of ==, and this helped me write cleaner code.

To check if a cubed number is odd, I used the modulus operator % to see if the number leaves a remainder when divided by 2.

Overall, this challenge made me more confident with data type checks and writing condition-based logic. It also showed me how to carefully handle edge cases like bool or other non-integer values.

