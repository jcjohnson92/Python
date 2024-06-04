# MEOWS = 3 # a CONSTANT

# for _ in range(MEOWS):
#     print("meow")

class Cat():
    MEOWS = 3
    """Meow 3 times"""
    def meow(self, n: int) -> str:
        return "meow\n" * n



cat = Cat()
number: int = int(input("Number: "))
meows: str= cat.meow(number)
print(meows)

# def meow(n: int) -> str:
#    return "meow\n" * n


# number: int = int(input("Number: ")) 
# meows: str = meow(number) 
# print(meows, end="")

