def greet(name):
    match name:
        case "Shijon":
            print("Hi, Shijon!")
        case _:
            print("Howdy, stranger!")

greet("Shijon")