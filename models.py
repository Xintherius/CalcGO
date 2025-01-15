# models.py
# Contains data models for structured information
class Course:
    def __init__(self, name, assignments, weight):
        """
        Initialize a course with its details.

        :param name: Name of the course (e.g., "Math 101")
        :param assignments: List of assignments and their scores
        :param weight: Weight of the course in the final grade calculation
        """
        self.name = name
        self.assignments = assignments
        self.weight = weight