Problem: Accumulative String (a.k.a "Mumbling")
Task:
Given a string, return a new string where each character is repeated based on its index (starting from 1),
the first letter of each group is uppercase, and the rest are lowercase.
Groups are joined by hyphens (-).

Examples:

python
Copy
accum("abcd")     → "A-Bb-Ccc-Dddd"
accum("RqaEzty")  → "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")     → "C-Ww-Aaa-Tttt"
My Thought Process:
This task was a fun and interesting challenge for me because it helped me discover some powerful built-in Python tools.

Here’s how I approached it:

First, I used a for loop with enumerate() so I could get both the index and the character at the same time.
I learned that enumerate() is very useful when you want to keep track of the index while looping over an iterable.

For each character, I repeated it (index + 1) times using multiplication.
For example: "a" * 3 → "aaa".

Then I used the .capitalize() method to make the first character uppercase and the rest lowercase.
So "aaa".capitalize() → "Aaa".

After processing all characters, I used "separator".join(list) to combine them into a single string with - between them.