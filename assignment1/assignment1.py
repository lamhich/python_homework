# Write your code here.
# Task1: Hello
def hello():
    return "Hello!"

# Task2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

# Task3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b if b != 0 else "You can't divide by 0!"
            case "modulo":
                return a % b
            case "int_divide":
                return a // b if b != 0 else "You can't divide by 0!"
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
    except Exception as e:
        if "divide by zero" in str(e):
            return "You can't divide by 0!"
        return f"You can't multiply those values!"

# Task4: Data Type Conversion
def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        elif data_type == "int":
            return int(value)
        else:
            return f"Invalid data type: {data_type}"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

# Task5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

# Task6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

# Task7: Student Scores, Using **kwargs
def student_scores(status, **kwargs):
    if status == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    elif status == "mean":
        avg_score = sum(kwargs.values()) / len(kwargs)
        return avg_score
    else:
        return "Invalid status"

# Task8: Titleize, with String and List Operations
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    return " ".join(words)

# Task9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# Task10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    def convert_word(word):
        if word[0] in "aeiou":
            return word + "ay"
        elif word[:2] == "qu":
            return word[2:] + "quay"
        else:
            for i in range(len(word)):
                if word[i] in "aeiou":
                    return word[i:] + word[:i] + "ay"
            return word + "ay"

    words = sentence.split()
    return " ".join(convert_word(word) for word in words)

