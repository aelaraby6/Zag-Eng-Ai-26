def celsius_to_fahrenheit(c):
    """
    This function Converts a temperature in Celsius to Fahrenheit.
    """
    try:
        c = float(c)
        f = (c * (9 / 5)) + 32

        return f
    except ValueError:
        return "Input is not a number!"
    


def fahrenheit_to_celsius(f):
    """
    This function Converts a temperature in Fahrenheit to Celsius.
    """
    try:
        f = float(f)
        c = (f - 32) * (5 / 9)

        return c
    except ValueError:
        return "Input is not a number!"
    

def average_temperature(temp_list, scale):
    """
    This function Accepts a list of temperatures and a scale ('C' or 'F')
    returns the average temperature in that scale.
    """
    try:
        avg = sum(temp_list) / len(temp_list)
        if scale.upper() == 'F':
            avg = celsius_to_fahrenheit(avg)

        return avg
    except ZeroDivisionError:
        return "length of list must be > 0"


def highest_temperature(temp_list, scale):
    """
    This function Returns the highest temperature in the given scale.
    """
    try:
        max_element = float(max(temp_list))
        if scale.upper() == 'F':
            max_element = celsius_to_fahrenheit(max_element)
        
        return max_element
    except ValueError:
        return "Input is not a number!"


def main():
    user_input = input("Enter temperatures in Celsius, separated by commas: ")
    
    try:
        temp_list = [float(t.strip()) for t in user_input.split(",")]

        avg_c = average_temperature(temp_list, 'C')
        max_c = highest_temperature(temp_list, 'C')

        avg_f = average_temperature(temp_list, 'F')
        max_f = highest_temperature(temp_list, 'F')

        print(f"\nAverage Temperature: {avg_c:.2f}°C / {avg_f:.2f}°F")
        print(f"Highest Temperature: {max_c:.2f}°C / {max_f:.2f}°F")

    except ValueError:
        print("Error: Please enter valid numbers separated by commas.")


if __name__ == "__main__":
    main()
     