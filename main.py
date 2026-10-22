# My first program for learning Git and GitHub

def greet(name):
    return f"Hello, {name}! Welcome to Git and GitHub."

def main():
    name = input("What is your name? ")
    print(greet(name))

if __name__ == "__main__":
    main()