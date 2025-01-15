# main.py
# Entry point for CalcGO!
from calculations import calculate_needed_score
from models import Course
from utils import format_percentage

def main():
    print("Welcome to CalcGO! Your grade tracking companion.")
    # Example: Call a function from calculations
    score = calculate_needed_score(85, 0.4, 90)
    print(f"You need to score at least {format_percentage(score)} on your final exam.")

if __name__ == "__main__":
    main()