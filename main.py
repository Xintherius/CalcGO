# main.py
# Entry point for CalcGO!
from calculations import calculate_needed_score
from models import Course
from utils import format_percentage

def main():
    close = 1
    print("Welcome to CalcGO! The calculator for students!\nDeveloped by: XinMedia")
    while (close == 1):
        #Menu
        menu = int(input("Menu:\n1. What can this app do?\n0. Exit\n"))
        
        #What does the app do?
        if (menu == 1):
            print("CalcGO! is a basically a grade calculator for students.\nYou may be facing a situation like 'What grade do I need to get x grade as my final'\nWe, at XinMedia have been in that situation too and would like to help you make school a little less stresfful!")

        elif (menu == 0):
            print("Goodbye!")
            close = 0
        else:
            print("Invalid option, please choose a number from the menu.")

if __name__ == "__main__":
    main()