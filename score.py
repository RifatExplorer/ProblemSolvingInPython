"""
Problem Statement:
You are organizing a coding competition. Write a program that takes a list of participants,
where each participant is represented by a dictionary with keys "name" and "score".
Calculate the average score and print a congratulatory message for participants who scored above the average.
"""

# Initialize an empty dictionary to store participant names and their scores
result_dic = {}

# Ask the user to input the number of participants
p = int(input("Enter the number of participants: "))

# Collect participant names and their scores
for i in range(1, (p + 1)):  # Loop for the given number of participants
    name = input(f"Enter the name of participant {i}: ")  # Input participant's name
    score = int(input(f"Enter the score of {name}: "))  # Input participant's score
    result_dic[name] = score  # Add the name and score to the dictionary

# Calculate the average score
sum = 0  # Variable to store the total score
x = len(result_dic)  # Get the total number of participants
for value in result_dic.values():  # Iterate through the scores
    sum += value  # Add each score to the total sum
avg = sum / x  # Calculate the average score

# Print congratulatory messages for participants who scored above the average
print("Congratulations to the participants who scored above the average:")
for key, value in result_dic.items():  # Iterate through the dictionary
    if value > avg:  # Check if the score is above the average
        print(f"Congratulations {key}! Your score of {value} is above the average.")
