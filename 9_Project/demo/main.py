from utils import create_greeting


if __name__ == "__main__":
    print("What is your name?")
    x = list(range(4))
    x.append(x)
    b = 0.
    a = x[3] / b
    name = input()
    print(create_greeting(name))
