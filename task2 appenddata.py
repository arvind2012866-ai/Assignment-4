text1 = input("Enter some text: ")

file = open("output.txt", "w")
file.write(text1 + "\n")
file.close()

text2 = input("Enter more text to add: ")

file = open("output.txt", "a")
file.write(text2 + "\n")
file.close()

file = open("output.txt", "r")
print("\nHere is the content of the file:")
print(file.read())
file.close()
