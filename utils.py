# utils.py
# Contains utility functions
def format_percentage(value):
    """
    Format a numeric value as a percentage.

    :param value: Numeric value to format (e.g., 0.85 for 85%)
    :return: String formatted as a percentage (e.g., "85.00%")
    """
    return f"{value:.2f}%"