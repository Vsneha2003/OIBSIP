def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using the formula: BMI = weight / (height ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI and provide a corresponding category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    while True:
        # Get user input for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Interpret BMI and display the result
        interpretation = interpret_bmi(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {interpretation}")

        # Ask the user if they want to calculate again
        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
