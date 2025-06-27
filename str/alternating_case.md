# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
# As usual, your function/method should be pure, i.e. it should not mutate the original string.


What I learned from this challenge
While solving this problem, I discovered and practiced the use of

isupper() — a method to check if a character is uppercase.

lower() and upper() — to convert a character’s case.

This challenge helped me better understand how strings work in Python and how to conditionally modify each character while iterating through them. It also made me more confident using string methods inside loops.

Solution

def to_alternating_case(string):
    new_string = ""
    for letter in string:
        if letter.isupper():
            new_string += letter.lower()
        else:
            new_string += letter.upper()
    return new_string