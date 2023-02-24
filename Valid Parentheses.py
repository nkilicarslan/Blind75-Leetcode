class Solution:
    def isValid(self, s: str) -> bool:
        # create stack to keep track of the paranthesis
        stack_list = []
        # iterate over the string
        for i in s:
            # if char one of them ('(' or '{' or '[') push to the stack
            if i == '(' or i == '{' or i == '[':
                stack_list.append(i)
            # if char one of them (')' or '}' or ']')
            else:
                # check the stack is empty or not
                if len(stack_list) == 0:
                    return False
                # pop the last value of the stack
                popped_element = stack_list.pop()
                # if these two char are matched, continue
                if (popped_element == '(' and i == ')') or (popped_element == '{' and i == '}') or (popped_element == '[' and i == ']'):
                    continue
                # if these two char are not matched return false
                else:
                    return False
        # if the stack is empty return true
        if len(stack_list) == 0:
            return True
        # otherwise return false
        else:
            return False