name = input("Enter file: ")
handle = open(name)

with open(name) as file:
    cheeses = []
    for line in file:
        for cheese in line.split():
            cheeses.append(cheese)
    cheeses.sort()

    print(cheeses)
