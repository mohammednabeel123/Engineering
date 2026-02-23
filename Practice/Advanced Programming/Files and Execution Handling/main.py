# print("Hello world")
# number_file = open("numbers_file.txt","w")
# for line in range(101):
#     number_file.write(str(line) + "\n")
# number_file.close()
# number_file = open("numbers_file.txt","r")
# for lines in number_file:
#     print(lines)
# number_file.close()

text_file = open("text_file.txt","w")
text_file.write("Hello, Thiis is my first .txt file\n")
text_file.close()

text_file = open("text_file.txt","w")
text_file.write("Hello, Thiis is my second.txt file\n")
text_file.close()

text_file = open("text_file.txt","r")
print(text_file.tell())
for lines in text_file:
    print(lines)
    
text_file.close()