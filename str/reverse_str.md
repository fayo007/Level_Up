Reverse String

Task 
We are given a string, and we need to return it reversed.

Example 

"world" → "dlrow"  
"word" → "drow"

My Thought Process

This task looks simple because we have already seen this kind of string operation while learning the `str` data type.  
If I didn't know the slicing trick, maybe this task would take longer or feel confusing.  

But in Python, there is a very nice way to reverse a string using slicing:


s[::-1]
This is called slicing with step.

The format is [start:stop:step], and when we use [::-1], it means:
→ start from the end and go backwards.

My Solution

def solution(s):
    return s[::-1]

Why this works
Because strings in Python support slicing.

[::-1] is a special trick to reverse the order.

This way is short, clean, and fast — that's why it's called "Pythonic".

What I learned
Slicing is very powerful in Python.

Even a simple task can become easier when we really understand the data type.

If we know the tools, even hard problems can look easy.
