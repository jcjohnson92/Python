def opposite(number):
  # your solution here
    if number >= 0: 
        print(type(-abs(number)))
    else:
        print(abs(number))


opposite(10)
opposite(-10)
opposite(5)
opposite(-5)

