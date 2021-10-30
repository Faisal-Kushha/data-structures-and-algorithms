from stack_and_queue.stack_queue import Stack


def validate_brackets(string):
    """
    A function called validate brackets representing whether or not the brackets in the string are balanced
    Arguments: string
    Return: boolean
    """

    stack = Stack()
    for i in string:

        if i == "(" or i == "[" or i == "{":
            stack.push(i)
        else:

            if not stack.top:
                return True
            else:
                top = stack.top.value
                if (
                    i == ")"
                    and top == "("
                    or i == "]"
                    and top == "["
                    or i == "}"
                    and top == "{"
                ):
                    stack.pop()
    if not stack.top:
        return True
    else:
        return False


if __name__ == "__main__":
    print(validate_brackets("{}"))
