char = input("~: enter some bruh ;;  ")
count = 0
vowels = set("aeiou")
for letter in char:
    if letter.lower() in vowels:
        count += 1
        print("Vowel")

print(f"Total: {count}")