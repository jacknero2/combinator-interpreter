Author: Jack Nero


Purpose of the Application

    A Python program to interpret combinator expressions written as text strings and recognizing only S, K, or I as functions (i.e. stop if any character other than S, K, or I shows up as the leftmost function, but can be left as argument). 

Usage Information

    usage: main.py [-h] (-e EXPRESSION | -p PATH | -i)

    options:
    -h, --help            show this help message and exit
    -e, --expression EXPRESSION
                            Evaluate the reduction of a particular expression: make sure to input as "expression"
    -p, --path PATH       Evaluate the reduction of a text file line by line as expressions
    -i, --input           Evaluate on inputs in an interactive mode.

Note:
    
    This application may only work on valid inputs within a certain margin of error. I did not rigorously account for difficulties such as placing a variable in the wrong place, etc. This application and source code may be utilized by others freely.