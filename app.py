# app.py

def calculate_score(marks):

    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'F'

if __name__ == "__main__":
    marks = int(input("Enter marks: "))
    print("Grade:", calculate_score(marks))
