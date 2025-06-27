# Count the Digit   
# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

# Square all numbers k (0 <= k <= n) between 0 and n.

# Count the numbers of digits d used in the writing of all the k**2.



<!-- Insight -->

This task helped me get more confident with the int data type and how to work with numbers in Python. I practiced using the for loop together with the range() function, and also reviewed how the count() method works on strings.

In this solution, I started by creating an empty string called p = ''. Then inside the loop, I used range(n + 1) to go through all numbers from 0 up to and including n. I used n + 1 here because the task specifically said that n itself should be included.

For each number i, I squared it with i**2 and converted the result to a string, then added it to the p string. After building this long string of all squared numbers, I used p.count(str(d)) to count how many times the digit d appears.

This was a good practice to understand how loops and counting work in Python, and it helped me improve my overall logic.