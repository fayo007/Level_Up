# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

def double_char(s):
    new_str = ""
    for letter in s:
        new_str+=(letter*2)
    return new_str

my_str = "Lalala"
print(double_char(my_str))