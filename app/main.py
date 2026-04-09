class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

        # Second pass: link spouses
    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
            # Automatically link back
            if not hasattr(person.wife, "husband"):
                person.wife.husband = person

        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]
            # Automatically link back
            if not hasattr(person.husband, "wife"):
                person.husband.wife = person

    return list(Person.people.values())
