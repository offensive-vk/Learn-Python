def main():
    user_data = {}

    # Taking input from the user
    user_data['Name'] = input("Enter your name: ")
    user_data['Age'] = int(input("Enter your age: "))
    user_data['Salary'] = float(input("Enter your salary: "))
    user_data['Department'] = input("Enter your department: ")
    user_data['Section'] = input("Enter your section: ")

    display_option = input("Do you want to display the data? (yes/no): ")

    if display_option.lower() == 'yes':
        print("\nUser Data:")
        for key, value in user_data.items():
            print(f"{key}: {value}")
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
