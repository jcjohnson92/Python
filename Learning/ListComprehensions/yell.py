def main():
    yell("this", "is", "CS50")


def yell(*words,**kwargs):
    # uppercase = map(str.upper, words) # mapping
    uppercase = [word.upper() for word in words] # list comphresion
    print(*uppercase)

if __name__ == "__main__":
    main()