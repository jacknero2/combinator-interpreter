import types

class CombinatorExpression():
    argument_count = {'S': 3, 'K':2, 'I':1}
    
    def __init__(self, input_string) -> None:
        self.expression = self.convert_to_list(input_string)
    
    def convert_to_list(self, input_string: str):
        stack = [[]]
        for char in input_string:
            if char == "K" or char == "S" or char == "I":
                stack[-1].append(char)
            elif char == "(":
                stack.append([])
            elif char == ")":
                subparenthesis_expression = stack.pop()
                stack[-1].append(subparenthesis_expression)
            else:
                raise ValueError(f"We did not recognize a character in your expression: character is '{char}'")
        
        return stack[0]
    
    def __str__(self) -> str:
        return str(self.expression)
    
    def apply_I(self, expression):
        return expression
    
    def apply_S(self, expression):
        a, b, c = expression[0], expression[1], expression[2]
        return [a, c, [b, c]] + expression[3:]
    def apply_K(self, expression):
        a = expression[0]
        return [a] + expression[2:]
    
    def apply_combinator(self, combinator, tail) -> list:
        if combinator == 'I':
                    return self.apply_I(tail)
        if combinator == 'K':
            return self.apply_K(tail)
        if combinator == 'S':
            return self.apply_S(tail)
        else:
            return []
        
        
    def reduce(self, expression): #returns whether there was a change
        #recursive DFS searching for changes
        # 
        # 1. check the current first element if you can reduce it return 
        # 2. reduce each of the children from left to right
        
        if not isinstance(expression, list):
            return False
        while (isinstance(expression[0], list)):
            expression[:] = expression[0] + expression[1:] #edit the original expression
        
        if isinstance(expression[0], str) and expression[0]  in self.argument_count and self.argument_count[expression[0]] <= len(expression[1:]):
            expression[:] = self.apply_combinator(expression[0], expression[1:])
            return True
        else:
            for child in expression:
                if (self.reduce(child)):
                    return True
    
    def fully_reduce(self):
        while (self.reduce(self.expression)):
            pass

        return self.expression
        
def main():
    pass

if __name__ == "__main__":
    main()