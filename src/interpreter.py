import math

class CombinatorExpression():
    argument_count = {'S': 3, 'K':2, 'I':1}
    
    def __init__(self, input_string, show_steps=False) -> None:
        self.expression = self.convert_to_list(input_string)
        self.show_steps = show_steps
    
    def convert_to_list(self, input_string: str):
        stack = [[]]
        for char in input_string:
            if char == "(":
                stack.append([])
            elif char == ")":
                subparenthesis_expression = stack.pop()
                stack[-1].append(subparenthesis_expression)
            else :
                stack[-1].append(char)
        
        return stack[0]
    
    def __str__(self) -> str:
        result = str(self.expression).strip(', ')
        for character in "', ":
            result = result.replace(character, '')
        result = result.replace('[', "(").replace(']', ")")
        return result[1:-1]
    
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
        i = 1
        while (self.reduce(self.expression)):
            if self.show_steps:
                print(f"{i}. {str(self)}")
            i+=1

        return self.expression
    
    def find_in_sublist(self, expression, variable):
        for subexpression in expression:
            if subexpression == variable:
                return True
            elif isinstance(subexpression,list) and self.find_in_sublist(subexpression, variable):
                return True
        return False
    
    def bracket_abstract(self, subexpression, variable):
        if not self.find_in_sublist(subexpression, variable):
            return ['K', subexpression]
        elif len(subexpression) == 1 and subexpression[0] == variable:
            return 'I'
        elif len(subexpression) == 1:
            return self.bracket_abstract(subexpression[0], variable)
        else:
            return ['S',self.bracket_abstract(subexpression[0:-1], variable),self.bracket_abstract(subexpression[-1], variable)]
        
    def find_nonstd_combinator(self, expression, result_list):
        if result_list is None:
            result_list = []
        for subexpression in expression:
            if isinstance(subexpression,list):
                self.find_nonstd_combinator(subexpression, result_list)
            elif subexpression.islower() and subexpression not in result_list: #check if we have already added it
                result_list.append(subexpression)
        return result_list
        
    def reduce_bracket_abstract(self) ->None:
        result_list = self.find_nonstd_combinator(self.expression, result_list=[])
        
        for variable in reversed(result_list):
            self.expression = self.bracket_abstract(self.expression,variable=variable)
            
    def flatten_rec(self, expression):
        #flatten the list as far as maxes sense ( [x] ought to go to x for example and [[x,y] z] ought to go to x, y, z)
        
        if not isinstance(expression, list):
            return expression

        expression = [self.flatten_rec(subexpression) for subexpression in expression]
        
        while expression and isinstance(expression[0], list): #this covers the 
            expression = expression[0] + expression[1:]
        
        if len(expression) == 1: #this covers the case that it is [x] goes to x 
            return expression[0]
        
        return expression
    
    def flatten(self):
        self.expression = self.flatten_rec(self.expression)
        
def main():
    pass

if __name__ == "__main__":
    main()