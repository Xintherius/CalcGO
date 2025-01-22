# main.py
# Entry point for CalcGO!
from calculations import calculate_needed_score


def main():
    #Keeps the menu/program running
    close = 1
    print("Welcome to CalcGO! The calculator for students!\nDeveloped by: XinMedia")
    while (close == 1):
        #Menu
        menu = int(input("Menu:\n1. What can this app do?\n2. Calculate\n0. Exit\n"))
        
        
        #Gives info on the program
        if (menu == 1):
            print("\n\nCalcGO! is a basically a grade calculator for students.\nYou may be facing a situation like 'What grade do I need to get x grade as my final'\nWe, at XinMedia have been in that situation too and would like to help you make school a little less stresfful!\nThis is a beta so you can only calculater what you need in your final\n\n")

        #Gets the input from the user
        elif ( menu == 2):
            #Get the course information
            while True:
                try:
                    course_name = input("Enter the name of the course: ")
                    per_attendance = float(input("Enter the percentage of attendance: "))
                    per_homework = float(input("Enter the percentage of homework: "))
                    per_assing = float(input("Enter the porcentage of all assingments: "))
                    per_project = float(input("Enter the percentage of project/s: "))
                    per_exam = float(input("Enter the percentage of all the exams: "))
                    total_per = per_attendance + per_homework + per_project + per_exam + per_assing
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    continue

            #Check if the total percentage is 100%
            if (total_per != 100):
                print("The total percentage is not 100%. Please try again.")
                continue

            #Input grades attendace,
            while True:
                try:
                    grade_attendance = float(input("Enter your attendance grade: "))
                    print("Moving to the next category")
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    continue
           
           #input hw grades
            i_hw = 0
            while True:
                try:
                    
                    hw_in = float(input("Enter your homework grades individually, when you're done "))
                    if (hw_in == 101):
                        print("Moving to the next category")
                        break
                    grade_homework = grade_homework + hw_in
                    i_hw = i_hw + 1
                    print(i_hw)
                

                except ValueError:
                    continue


            #Desired grade
            desired_grade = float(input("Enter the desired grade: "))

        #Closes the program
        elif (menu == 0):
            print("Goodbye!")
            close = 0
        else:
            print("\n\nPlease enter a valid number\n\n")
            continue

if __name__ == "__main__":
    main()