

try:
    note = input("Enter a short note/message: ")

    # Save to file using "w" mode
    with open("notes.txt", "w") as file:
        file.write(note)

    print("\n✔ Message saved to notes.txt")

except Exception as e:
    print("Error:", e)



try:
    with open("notes.txt", "r") as file:
        content = file.read()

    print("\n Content of the file:")
    print(content)

except FileNotFoundError:
    print(" File not found.")



try:
    new_note = input("\nEnter another note: ")

    
    with open("notes.txt", "a") as file:
        file.write("\n" + new_note)

    
    with open("notes.txt", "r") as file:
        updated_content = file.read()

    print("\n Updated content:")
    print(updated_content)

except Exception as e:
    print("Error:", e)
