def calculate_average_score(file_name):
    with open(file_name, 'r') as file:
        scores = [int(line.split()[1]) for line in file]
    average = sum(scores) / len(scores)
    print(f"The average score is: {round(average, 2)}")

calculate_average_score("students.txt")