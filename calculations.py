# calculations.py
# Contains grade calculation logic
def calculate_needed_score(current_score, weight, desired_grade):
    """
    Calculate the score needed on a weighted assignment to achieve a desired grade.

    :param current_score: Current grade as a percentage (e.g., 85 for 85%)
    :param weight: Weight of the assignment (e.g., 0.4 for 40%)
    :param desired_grade: Desired final grade as a percentage
    :return: Required score on the assignment
    """
    return (desired_grade - current_score * (1 - weight)) / weight