class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts

    def __str__(self) -> str:
        return f"Galleons:{self.galleons}, Sickles:{self.sickles}, Knuts:{self.knuts}"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.galleons + other.galleons
        knuts = self.knuts + other.knuts
        return Vault(galleons,sickles, knuts)

potter = Vault(100,50,20)
print(potter)

weasley = Vault(20,50,100)
print(weasley)

total = potter + weasley
print(total)