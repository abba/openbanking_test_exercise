from openbanking_test_exercise.client.rest_client import RestClient

rest_client = RestClient()

# 1. The animals list includes Giraffe, Lion, and Mouse
def test_1():
    subset_of_animals = ['Giraffe', 'Lion', 'Mouse']
    animals = rest_client.get_animals()
    is_sub_set_of = set(subset_of_animals).issubset(set(animals))
    assert is_sub_set_of

# 2. The people list contains no names longer than ten characters
def test_2():
    people = rest_client.get_people()
    more_than_10characters = list(filter(lambda x: len(x) >= 10, people))
    assert len(more_than_10characters) == 0

# 3. There exists a person whose name is the same as the name of an animal
def test_3():
    animals = rest_client.get_animals()
    people = rest_client.get_people()
    common_name = set(animals) - (set(animals) - set(people))
    assert list(common_name)[0] == 'Wolf'


