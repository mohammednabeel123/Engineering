words_arrays = []

def compare_string(first_string, second_string):

    for i in range(min(len(first_string), len(second_string))):
        if first_string[i] == second_string[i]:
            words_arrays.append(first_string[i])

    if first_string == second_string:
        return "The strings are exactly the same."
    else:
        return "The strings are different."


first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

result = compare_string(first_string, second_string)

print("Matching characters:", words_arrays)
print(result)