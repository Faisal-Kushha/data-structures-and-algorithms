from stack_and_queue.stack_queue import Stack


def validate_brackets(string):
    stack = Stack()
    opening_brackets = ["(", "{", "["]
    closing_brackets = [")", "}", "]"]

    for i in string:
        if i == "(" or i == "{" or i == "[":
            stack.push(i)
        elif i == ")" or i == "}" or i == "]":
            if stack.is_empty:
                return False
            elif i in opening_brackets and stack.top.value in opening_brackets:
                stack.pop()
            elif i in closing_brackets and stack.top.value in closing_brackets:
                stack.pop()
            else:
                return False
    if stack.is_empty:
        return True
    else:
        return False


if __name__ == "__main__":
    print(validate_brackets("{}"))
