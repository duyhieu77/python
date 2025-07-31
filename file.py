data = [
    "Aptech"
    "Aptech"
    "Aptech"
    "Aptech"
    "Aptech"
]

with open("data.txt", "w") as file:
    for line in data:
        file.write(line + "\n")

with open("data.txt", "r") as file:
    for line in file:
        if "Aptech" in line:
            print(line.strip())