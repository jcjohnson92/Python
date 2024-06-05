def main():
    n = int(input("N: "))

    for s in sheep(n+1):
        print(s)

def sheep(n):
    # flock = []
    for i in range(n):
        # flock.append("🐑" * i)
        yield "🐑" * i # return instantly instead of waiting to return all at once
    # return flock
   


if __name__ == "__main__":
   main()