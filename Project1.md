# Fundamental Booster

## ▶ Demo Video

<a href="https://your-video-link.com/replace-with-real-link" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/%E2%96%B6-Watch%20Demo%20Video-e63946?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch demo video" />
</a>

<sub>Video link: <a href="https://your-video-link.com/replace-with-real-link">https://your-video-link.com/replace-with-real-link</a></sub>

## Objective

Create an Interactive Personal Data Collector application in Python that captures, processes, and displays personal information from the user using fundamental Python functions and concepts. The project demonstrates print() and input(), data types, variables, operators, type casting, and built-in functions like id() and type().

## Requirements

### Detailed Use of print() and input() Functions
- Use input() to gather personal information: name, age, height, favourite number.
- Use print() to display formatted information and guide the user through each step.

### Data Types, Variables & Operators
- Store each piece of collected information in a variable with an appropriate data type.
- Demonstrate arithmetic operators (+, -, *, /) e.g. calculating birth year from age.
- Use string concatenation / f-strings to build user-friendly output messages.

### Type Casting Constructors
- Cast input() text to int (age, favourite number) and float (height).
- Convert between types as needed and explain the conversion in the output.

### id() and type() Functions
- Display the data type and memory address of each variable using type() and id().
- Output a summary of each variable: name, value, data type, memory location.


## Program Flow

1. **Welcome and Instructions**
   - Display a welcome message and a brief description of what the program does.
2. **Collect Information**
   - Prompt the user for name (string), age (int), height (float), favourite number (int).
3. **Data Processing**
   - Perform calculations with user-provided data, e.g. determine birth year from age.
   - Print each variable's value, data type, and memory address via type() and id().
4. **Display Results**
   - Print a user-friendly summary of the collected information.
   - Show messages explaining how data types were converted where applicable.
5. **Exit Message**
   - End with a thank-you message and encourage the user to explore Python further.



## Example Console Interaction

```
Welcome to the Interactive Personal Data Collector!

Please enter your name: Alice
Please enter your age: 25
Please enter your height in meters: 1.68
Please enter your favourite number: 7

Thank you! Here is the information we collected:

Name: Alice (Type: <class 'str'>, Memory Address: 140703847239568)
Age: 25 (Type: <class 'int'>, Memory Address: 9793456)
Height: 1.68 (Type: <class 'float'>, Memory Address: 140703847253232)
Favourite Number: 7 (Type: <class 'int'>, Memory Address: 9793312)

Your birth year is approximately: 1998 (based on your age of 25)

Thank you for using the Personal Data Collector. Goodbye!
```

## Python Source Code

Full source: [`personal_data_collector.py`](./personal_data_collector.py)

```python
"""
Fundamental Booster
--------------------
Interactive Personal Data Collector

Captures, processes, and displays personal information from the user
using fundamental Python concepts: print()/input(), variables,
data types, operators, type casting, and the built-in id() / type()
functions.
"""

from datetime import datetime


def welcome():
    """Display a welcome message and a brief description of the program."""
    print("Welcome to the Interactive Personal Data Collector!")
    print("This program will ask you a few quick questions, store your")
    print("answers in different Python data types, show you how Python")
    print("represents and converts that data, and then summarise it all")
    print("for you.\n")


def collect_information():
    """Prompt the user for name, age, height, and favourite number."""
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    height = float(input("Please enter your height in meters: "))
    favourite_number = int(input("Please enter your favourite number: "))
    return name, age, height, favourite_number


def show_variable_details(name, age, height, favourite_number):
    """Print each variable's value, data type, and memory address."""
    print("\nThank you! Here is the information we collected:\n")

    print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
    print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
    print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
    print(
        f"Favourite Number: {favourite_number} "
        f"(Type: {type(favourite_number)}, Memory Address: {id(favourite_number)})"
    )


def process_data(age, height, favourite_number):
    """Perform calculations and demonstrate type casting / operators."""
    current_year = datetime.now().year
    birth_year = current_year - age  # arithmetic operator: subtraction
    print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

    # Type casting: float -> int
    rounded_height = int(height)
    print(
        f"Type casting demo: your height {height} (float) converted to an "
        f"integer becomes {rounded_height}."
    )

    # Type casting: int -> float
    favourite_number_as_float = float(favourite_number)
    print(
        f"Type casting demo: your favourite number {favourite_number} (int) "
        f"converted to a float becomes {favourite_number_as_float}."
    )

    # Simple arithmetic operators demo
    doubled_favourite = favourite_number * 2
    half_height = height / 2
    print(
        f"Just for fun: double your favourite number is {doubled_favourite}, "
        f"and half your height is {half_height:.2f} meters."
    )


def display_summary(name, age, height, favourite_number):
    """Print a user-friendly summary using string formatting/concatenation."""
    summary = (
        "\nSummary -> Name: " + name +
        " | Age: " + str(age) +
        " | Height: " + str(height) + "m" +
        " | Favourite Number: " + str(favourite_number)
    )
    print(summary)


def goodbye():
    """End with a thank-you message and encourage further exploration."""
    print("\nThank you for using the Personal Data Collector. Goodbye!")
    print("Keep exploring Python - there's always more to discover!")


def main():
    welcome()
    name, age, height, favourite_number = collect_information()
    show_variable_details(name, age, height, favourite_number)
    process_data(age, height, favourite_number)
    display_summary(name, age, height, favourite_number)
    goodbye()


if __name__ == "__main__":
    main()

```

---
*This README, the flowchart, and the video button above were all generated
programmatically by `generate_readme.py` -- edit the lists/dicts at the top
of that file and rerun it to regenerate everything.*
