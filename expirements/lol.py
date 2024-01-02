with open('expirements/smooth.py', 'r') as file:
    lines = file.readlines()

# Create an empty dictionary to store the tuples
tuples_dict = {}

# Modify lines 3 to 985
for i in range(2, 985):
    # Parse the numbers from the line
    nums = [int(num) for num in lines[i].replace('(', '').replace(')', '').replace(',', '').split()]
    
    # Add the tuple to the dictionary
    tuples_dict[nums[0]] = nums[1]
    tuples_dict[nums[2]] = nums[3]

# Now 'tuples_dict' is a dictionary with the tuples
import json

with open('expirements/smooth.py', 'w') as file:
    file.write(json.dumps(tuples_dict, indent=4))