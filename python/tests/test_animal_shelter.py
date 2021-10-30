from Animal_Shelter.animal_shelter import AnimalShelter


def test_happy_path():
    animalShelter = AnimalShelter()
    animalShelter.enqueue("cat")
    # Actual
    actual = animalShelter.cat.front.value
    # Expected
    expected = "cat"
    # Assert
    assert actual == expected


def test_expected_failure():
    animalShelter = AnimalShelter()
    animalShelter.enqueue("dog")
    # Actual
    actual = animalShelter.dog.front.value
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
