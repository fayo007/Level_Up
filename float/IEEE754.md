# IEEE 754 is a standard for representing floating-point numbers (i.e. numbers that can have a fractional part and emulate real numbers).

# Its use is currently ubiquitous in both software (programming languages implementations) and hardware (Floating Point Units (FPU) chips embedded in processors).

# The 2 most widely used IEEE 754 formats are called the single precision (SP, encoded on 32 bits) and double precision (DP, encoded on 64 bits) formats.

# In C/C++, these correspond respectively to the types float and double, in virtually every implementation that supports floating-point numbers
# The default Python implementation, CPython, is written in C and represents Python floats internally as C doubles, and thus as IEEE 754 DP
# In JavaScript, all Numbers are IEEE 754 DP values.
# In Rust, these correspond respectively to the types f32 and f64.
# In Java, these correspond respectively to the types float and double.
# Before Lua 5.3, all numbers were IEEE 754 DP. Since Lua 5.3, numbers can be either IEEE 754 DP or 2's complement integers.
# The Haskell 2010 Language Report defines the Float and Double types for single/double precision floating point numbers. Most, if not all, implementations of Haskell (including GHC) represent Float/Double internally in IEEE 754 SP/DP format.
# As you can see on the images below, IEEE 754 numbers are divided into 3 fields :

# a sign bit;
# an exponent encoded on 8 (SP) or 11 (DP) bits;
# a mantissa (also called significand) encoded on 23 (SP) or 52 (DP) bits.
# The IEEE 754 single-precision encoding schemeThe IEEE 754 double-precision encoding scheme
# Your task is to write a function that takes as input a floating point number, and returns the binary IEEE 754 encoding of this number as a string, with fields separated by spaces for readability. If your programming language supports both SP and DP, you will have 2 functions to write, one for each type.

# Example
# Single Precision
# input:
# 15.875
# output:
# "0 10000010 11111100000000000000000"
# Double Precision
# input:
# 15.875
# output:
# "0 10000000010 1111110000000000000000000000000000000000000000000000"
# Note
# If you find yourself writing overly complex code, you are probably on the wrong path. Your solution should only be concerned with the bit-pattern of the number, without dealing with its value.

Insight :

This problem helped me understand the Float data type much more deeply. I learned more about binary numbers and how float values are stored in binary — specifically how they are represented with a sign bit, exponent, and fraction part using 0s and 1s.

Through this, I also discovered Python’s special formatting technique, which is really useful when converting numbers into binary strings. One of the most important things I learned was about the struct module in Python — this module is used to convert float numbers into their binary representation. I learned how to correctly use the .pack() and .unpack() methods and give them the right format parameters.

As for the algorithm of the problem: I first converted the float number into bytes using struct.pack(). Then I turned those bytes into an integer using struct.unpack(), and from there, I formatted the integer into its binary form using Python string formatting. To solve the problem properly, I also needed to understand how a float is stored in memory. That’s where I learned about the concepts of sign, exponent, and fraction, and how they are used in the IEEE 754 format.

Overall, this problem helped me improve my understanding of programming at a deeper level.