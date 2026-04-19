
# 1. Create a Python Program
try:
    note = input("Enter a short note/message: ")

    # Save to file using "w" mode
    with open("notes.txt", "w") as file:
        file.write(note)

    print("\n✔ Message saved to notes.txt")

except Exception as e:
    print("Error:", e)


# 2. Read File
try:
    with open("notes.txt", "r") as file:
        content = file.read()

    print("\n📄 Content of the file:")
    print(content)

except FileNotFoundError:
    print("❌ File not found.")


# 3. Append new data
try:
    new_note = input("\nEnter another note: ")

    # Append using "a" mode
    with open("notes.txt", "a") as file:
        file.write("\n" + new_note)

    # Display updated content
    with open("notes.txt", "r") as file:
        updated_content = file.read()

    print("\n📄 Updated content:")
    print(updated_content)

except Exception as e:
    print("Error:", e)