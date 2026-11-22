# Author: Jack Nero
# File name: main.py
# Purpose: reduce combinator expressions
import argparse
from pathlib import Path

from interpreter import CombinatorExpression

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--expression", help="Evaluate the reduction of a particular expression: make sure to input as \"expression\"")
    group.add_argument("-p", "--path", help="Evaluate the reduction of a text file line by line as expressions")
    group.add_argument("-i", "--input", action="store_true", help="Evaluate on inputs in an interactive mode.")
    args = parser.parse_args()
    
    if args.expression:
        expression = CombinatorExpression(str(args.expression))
        print(expression.fully_reduce())
    elif args.input:
        while True:
            try:
                expression = CombinatorExpression(input("> ").strip().upper())
                print(expression.fully_reduce())
            except ValueError:
                print("Try again. We didn't understand you input.")
            except (KeyboardInterrupt, EOFError):
                print("\rThank you for you using the combinator interpreter by Jack Nero.")
                return
    elif args.path:
        input_path = Path(args.path)
        if input_path.exists():
            print("Path exists.")
        
        print()
        
        if input_path.suffix.lower() == ".txt":
            print("Valid input file type")
        else:
            raise ValueError(f"Expected a file of the form .txt but received {input_path}")
        
        print("Converting to expression objects of class CombinatorExpression and reducing")
        
        print()
        with open(input_path, "r") as file:
            i = 1
            for line in file:
                print(f"{i}.")
                print()
                line = line.strip()
                expression = CombinatorExpression(line)
                expression.fully_reduce()
                print(expression)
                print()
                i+=1
if __name__ == "__main__":
    main()