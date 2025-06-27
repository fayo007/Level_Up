Problem: Jaden Smith Capitalization
Task:
We are given a sentence (string), and we need to return it with each word capitalized — the way Jaden Smith writes on Twitter.

Example:
"How can mirrors be real if our eyes aren't real" →
"How Can Mirrors Be Real If Our Eyes Aren't Real"

My Thought Process:
This task is mainly about string manipulation, and more specifically, capitalizing each word.

To solve this, I needed to:

Split the sentence into individual words,

Capitalize the first letter of each word,

Then join the words back together into a single string.

At first, I did this using a loop and it worked — and that felt great!
But then I discovered a more elegant and readable approach using list comprehension.

Why List Comprehension?
List comprehension allows us to create a new list by applying a transformation to each item in an existing list — all in a single line.

In this problem, we used it like this:

python
Copy
Edit
" ".join([word.capitalize() for word in my_str.split()])
my_str.split() turns the string into a list of words.

word.capitalize() capitalizes each word.

join() merges the list back into a string with spaces.

My Solution:
python
Copy
Edit
def to_jaden_case(my_str):
    return " ".join([word.capitalize() for word in my_str.split()])
What I Learned:
Python strings work well with lists — they can be split and re-joined easily.

The combination of split(), capitalize(), and join() makes string formatting very clean.

List comprehension makes the code shorter, more readable, and feels more "Pythonic".

This task showed me that even simple-looking problems can teach important ideas like how to transform data step by step.