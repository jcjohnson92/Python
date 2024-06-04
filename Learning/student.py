class Student:
    def __init__(self, name, house):    
        self.name = name
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} in {self.house}"


    @property
    def name(self):
         return self._name
    
    @name.setter
    def name(self,name):
         if not name:
              raise ValueError("Empty Name")
         self._name = name

    # Getter 
    @property
    def house(self):
         return self._house
    
    # Setter
    @house.setter
    def house(self, house):
         if house not in ["Gryffindor", "Hufflepuff","Ravenclaw","Slytherin"]:
              raise ValueError ("Invalid House")
         self._house = house

def get_student():    
        name = input("Name: ")
        house = input("House: ")
        return Student(name,house)
    
    
def main():
    student = get_student ()
    print(student)


if __name__ == "__main__":
    main()