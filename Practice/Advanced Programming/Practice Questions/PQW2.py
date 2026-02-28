#Question1
with open("numbers.txt","w") as f:
    for num in range(1,101):
        f.write(f"{num}\n")


#Question2
with open("numbers.txt","r") as f:
    total = 0
    for line in f:
        # print(type(line))
        lines = int(line.strip())
        total +=lines

with open("numbers.txt","a") as f:
        f.write(f"\nThe sum of these numbers are:{str(total)}\n")