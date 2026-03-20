# Project: Checking Alphabets using Python operators

ch = input("Enter a character: ")

if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print(ch, "is an alphabet.")
else:
    print(ch, "is NOT an alphabet.")