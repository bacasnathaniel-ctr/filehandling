def main():
    try:

        x = input("Enter username: ").strip()
        if not x:
            raise ValueError("Username cannot be empty.")

        age_input = input("Enter age: ").strip()

        age = int(age_input)

        if age <= 0:
            raise ValueError("Age must be a positive number.")

        with open("users.txt", "a") as file:
            file.write(f"{x} - {age}\n")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
    
        try:
            print("\nSaved Users:")
            with open("users.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No users found yet.")

        print("System complete.")

main()