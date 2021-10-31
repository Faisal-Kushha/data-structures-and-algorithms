from stack_and_queue.stack_queue_pseudo import Node, Stack, PseudoQueue
import pytest


def test_enqueue_happy_path(testqueue):
    # Actual
    actual = testqueue.__str__()
    # Expected
    expected = "{ 5 } -> { 10 } -> { 15 } -> { 20 }"
    # Assert
    assert actual == expected


def test_enqueue_expected_failure(testqueue):
    # Actual
    actual = testqueue.__str__()
    # Expected
    expected = "{ 5 } -> { 10 } -> { 20 }"
    # Assert
    assert actual != expected


def test_enqueue_edge_case(testqueue):
    # Actual
    actual = testqueue.__str__()
    # Expected
    expected = "{ 5 } -> { 10 } -> { 20 }"
    # Assert
    assert actual != expected


@pytest.fixture
def testqueue():
    queue = PseudoQueue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    return queue
