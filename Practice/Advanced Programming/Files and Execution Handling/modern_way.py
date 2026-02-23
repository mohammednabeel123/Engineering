with open("modern_way.txt","w") as f:
        f.write("This is the modern way to handle files in Python.\n")
# with open("modern_way.txt","r") as f:
#         print(f.readline())
#         print(f.readline())

with open("modern_way.txt","a") as f:
    f.write("This line is appended to the file.\n")
with open("modern_way.txt","r") as f:
      for line in f:
            print(line.strip())

