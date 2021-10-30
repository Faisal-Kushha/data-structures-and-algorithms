from stack_queue_pseudo.stack_queue_pseudo import Node, Stack, PseudoQueue


def test_enqueue_happy_path():
    queue = PseudoQueue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    # Actual
    actual = queue.__str__()
    # Expected
    expected = "{ 5 } -> { 10 } -> { 15 } -> { 20 }"
    # Assert
    assert actual == expected


def test_enqueue_expected_failure():
    queue = PseudoQueue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    # Actual
    actual = queue.__str__()
    # Expected
    expected = "{ 5 } -> { 10 } -> { 20 }"
    # Assert
    assert actual != expected


def test_enqueue_edge_case():
    queue = PseudoQueue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    # Actual
    actual = queue.__str__()
    # Expected
    expected = "{ 5 } -> { 10 } -> { 20 }"
    # Assert
    assert actual != expected
