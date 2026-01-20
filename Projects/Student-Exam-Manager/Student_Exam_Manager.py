def get_valid_int(prompt, min=1, max=6):
    """
    Prompt the user to enter an integer within a specified range.

    Args:
        prompt (str): Message shown to the user.
        min (int): Minimum allowed value.
        max (int): Maximum allowed value.

    Returns:
        int: A valid integer between min and max (inclusive).
    """
    try:
        choice = int(input(prompt))
        if choice < min or choice > max:
            raise ValueError("Number out of range!")
        return choice
    except ValueError as e:
        print(f"[ERROR] {e}")
        return get_valid_int(prompt, min, max)


def calculate_averages(student_data):
    """
    Calculate average score for each student.

    Args:
        student_data (dict): Dictionary containing student info.

    Returns:
        dict: Dictionary with student names as keys and averages as values.
    """
    student_averages = {}

    for name, data in student_data.items():
        total = 0
        for i in range(3):
            total += data[1][i]

        avg = total / 3
        student_averages[name] = avg

    return student_averages


def save_to_file(student_data):
    """
    Save student data to a text file.

    Args:
        student_data (dict): Dictionary containing student information.
    """
    with open("students.txt", "w") as f:
        for name, (age, scores) in student_data.items():
            scores_str = ", ".join(map(str, scores))
            f.write(f"Name: {name} | Age: {age} | Scores: {scores_str}\n")

    print("[INFO] Data saved successfully")


def read_from_file():
    """
    Read student data from a text file.

    Returns:
        dict: Dictionary containing loaded student information.
    """
    student_data = {}

    try:
        with open("students.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(" | ")
                name = parts[0].split(": ")[1]
                age = int(parts[1].split(": ")[1])
                scores = list(map(float, parts[2].split(": ")[1].split(", ")))

                student_data[name] = (age, scores)

        print("[INFO] Data loaded successfully")

    except FileNotFoundError:
        print("[ERROR] File not found!")

    return student_data


def main():
    """
    Main program loop that displays menu and handles user choices.
    """
    student_data = {}

    while True:
        print("\n" + "=" * 40)
        print(" Student Management System ")
        print("=" * 40)
        print("1. Add student")
        print("2. Show averages")
        print("3. List students above average")
        print("4. Save to file")
        print("5. Read from file")
        print("6. Exit")
        print("=" * 40)

        choice = get_valid_int("Enter choice: ", 1, 6)

        if choice == 1:
            try:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))

                if age <= 0:
                    raise ValueError("Age must be positive")

                scores = []
                for i in range(3):
                    score = float(input(f"Enter score for subject {i + 1}: "))
                    if score < 0 or score > 100:
                        raise ValueError("Scores must be between 0 and 100")
                    scores.append(score)

                student_data[name] = (age, scores)
                print("[SUCCESS] Student added successfully ✅")

            except ValueError as e:
                print(f"[ERROR] {e}")

        elif choice == 2:
            averages = calculate_averages(student_data)
            print("\n--- Student Averages ---")
            for name, avg in averages.items():
                print(f"{name}: {avg:.2f}")

        elif choice == 3:
            averages = calculate_averages(student_data)
            try:
                threshold = int(input("Enter average threshold: "))
            except ValueError as e:
                print(f"[ERROR] {e}")
                continue

            print("\n--- Students Above Average ---")
            for name, avg in averages.items():
                if avg > threshold:
                    print(f"{name}: {avg:.2f}")

        elif choice == 4:
            save_to_file(student_data)

        elif choice == 5:
            student_data = read_from_file()

        elif choice == 6:
            print("\nGoodbye")
            break


if __name__ == "__main__":
    main()
