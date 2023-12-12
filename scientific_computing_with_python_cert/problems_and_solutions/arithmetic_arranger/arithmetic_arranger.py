def arithmetic_arranger(problems, show_answers=False):
    # Check if the number of problems is within the limit
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    top_line = ""
    bottom_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        # Split the problem into operands and operator
        operand1, operator, operand2 = problem.split()

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands contain only digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if operands are within the limit of four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the maximum width for the current problem
        max_width = max(len(operand1), len(operand2)) + 2  # Add 2 for the operator and space

        # Build the lines for the current problem
        top_line += operand1.rjust(max_width) + "    "
        bottom_line += operator + operand2.rjust(max_width - 1) + "    "
        dash_line += '-' * max_width + "    "

        # Calculate the answer if required
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answer_line += answer.rjust(max_width) + "    "

    # Remove trailing spaces and add newlines
    arranged_problems += top_line.rstrip() + "\n"
    arranged_problems += bottom_line.rstrip() + "\n"
    arranged_problems += dash_line.rstrip() + "\n"
    if show_answers:
        arranged_problems += answer_line.rstrip() + "\n"

    return arranged_problems.rstrip()
