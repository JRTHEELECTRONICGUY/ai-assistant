# File management utilities for input/output
def save_input(input_data):
    with open('user_inputs.txt', 'a') as file:
        file.write(input_data + '\n')
