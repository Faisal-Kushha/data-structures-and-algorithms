from stack_and_queue.stack_queue import Node, Stack, Queue
# import pytest


# Stack Tests

def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push("car")
    # Actual
    actual = stack.top.value
    # Expected
    expected = "car"
    # Assert
    assert actual == expected


def test_multiple_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push("car")
    stack.push(5)
    stack.push(6)
    # Actual
    actual = stack.top.value
    # Expected
    expected = 6
    # Assert
    assert actual == expected


def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push("car")
    # Actual
    actual = stack.pop()
    # Expected
    expected = "car"
    # Assert
    assert actual == expected


def test_multiple_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    # Actual
    actual = stack.top
    # Expected
    expected = None
    # Assert
    assert actual == expected


def test_peek_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push("car")
    # Actual
    actual = stack.peek()
    # Expected
    expected = "car"
    # Assert
    assert actual == expected


def test_instantiate_stack():
    stack = Stack()
    # Actual
    actual = stack.top
    # Expected
    expected = None
    # Assert
    assert actual == expected


def test_is_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True


#-----------------------------------------------------------------------------#
# Queue Tests


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    # Actual
    actual = queue.rear.value
    # Expected
    expected = 3
    # Assert
    assert actual == expected


def test_multiple_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(5)
    # Actual
    actual = queue.rear.value
    # Expected
    expected = 5
    # Assert
    assert actual == expected


def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    # Actual
    actual = queue.front.value
    # Expected
    expected = 2
    # Assert
    assert actual == expected


def test_multiple_dequeue():
    queue = Queue()
    queue.enqueue("Morning")
    queue.enqueue("Evening")
    queue.enqueue("Night")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    # Actual
    actual = queue.front
    # Expected
    expected = None
    # Assert
    assert actual == expected


def test_instantiate_queue():
    queue = Queue()
    # Actual
    actual = queue.front
    # Expected
    expected = None
    # Assert
    assert actual == expected


def test_peek_queue():
    queue = Queue()
    queue.enqueue("BMW")
    queue.enqueue("KIA")
    # Actual
    actual = queue.peek()
    # Expected
    expected = "BMW"
    # Assert
    assert actual == expected


def test_is_empty():
    queue = Queue()
    # Assert
    assert queue.is_empty() == True


#-------------------------------------------------------------------------------#
# Decorator(Fixture):
# @pytest.fixture
# def stack():
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     stack.push("car")
#     return stack
