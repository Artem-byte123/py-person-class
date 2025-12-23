class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        age = person_dict.get("age")
        name = person_dict.get("name")
        if isinstance(name, str) and isinstance(age, int):
            new_person = Person(name, age)
            person_list.append(new_person)

    for person_dict in people:
        current_name = person_dict.get("name")
        current_person_obj = Person.people.get(current_name)
        if current_person_obj is None:
            continue

        relation_key = None
        linked_name = None

        if "wife" in person_dict and person_dict["wife"] is not None:
            relation_key = "wife"
            linked_name = person_dict.get("wife")


        elif "husband" in person_dict and person_dict["husband"] is not None:
            relation_key = "husband"
            linked_name = person_dict.get("husband")
        else:
            continue

        if linked_name in Person.people:
            linked_person_obj = Person.people[linked_name]
            setattr(current_person_obj, relation_key, linked_person_obj)
    return person_list
