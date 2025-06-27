Task 

Given a string, return a string where every character is repeated once.

Examples
"String"      → "SSttrriinngg"
"Hello World" → "HHeelllloo  WWoorrlldd"
"1234!_ "     → "11223344!!__  "
My Thought Process:
This problem tests how well I can iterate through a string and manipulate its characters.

What I did

I created an empty string new_str.

Then I used a for loop to go through each character.

For every character, I duplicated it using letter * 2.

I added the duplicated character to the final result.

My Code

def double_char(s):
    new_str = ""
    for letter in s:
        new_str += (letter * 2)
    return new_str
What I Learned
How to iterate over strings

How to repeat a character using multiplication: "a" * 2 = "aa"

How to build a new string using += in a loop

Even though it's a simple problem, it helped me practice string operations, which is important for text-based tasks in Python