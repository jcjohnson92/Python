
class Car:
    def __init__(self, make:str,model:str,year:int,color:str,for_sale:bool) -> None:
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):
        print(f"{self.make} drives")

    def stop(self):
        print(f"{self.make} stops")

    def describte(self):
        print(f"{self.year} {self.make} {self.model}")