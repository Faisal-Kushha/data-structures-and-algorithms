from stack_and_queue.animal_shelter import AnimalShelter


def test_happy_path():
    animalShelter = AnimalShelter()
    # Actual
    actual = animalShelter.enqueue("cat")
    # Expected
    expected = "cat"
    # Assert
    assert actual == expected


def test_expected_failure():
    animalShelter = AnimalShelter()
    # Actual
    actual = animalShelter.enqueue("dog")
    # Expected
    expected = "cat"
    # Assert
    assert actual != expected


def test_edge_case():
    animalShelter = AnimalShelter()
    # Actual
    actual = animalShelter.dequeue("hores")
    # Expected
    expected = None
    # Assert
    assert actual == expected
