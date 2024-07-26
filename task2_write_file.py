data = [
    "this is first line",
    "this is second line",
    "this is third line"
]


with open("textFile.txt", "w") as file:
    for line in data:
        file.write(line + "\n")

print("lines add successfully")