with open("numbers.txt","w") as f:
    for num in range(1,101):
        f.write(f"{num}\n")
with open("numbers.txt","r") as f:
    for line in f:
        print(line.strip())
