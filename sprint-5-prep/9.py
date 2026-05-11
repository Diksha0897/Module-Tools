from typing import List


class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names: List[str] = []

    def change_last_name(self, last_name: str) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        if self.previous_last_names:
            return f"{self.first_name} {self.last_name} (née {self.previous_last_names[0]})"
        return self.get_name()


# --- Demo ---

person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())
print(person1.get_full_name())

person1.change_last_name("Tyurina")
print(person1.get_name())
print(person1.get_full_name())


person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())