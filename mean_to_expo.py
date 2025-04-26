import math

a = 3.56759065977771e5
b = 35.780570888204
c = -275.11845478299
d = 0.00030040268570601
e = 9717.9322229303

# Define your function
def transform(y):
    return (1 / c) * math.log((a - (y + e) * b) / (y + e)) - d

# File paths
input_file = 'data/sky_data_real_mean_data_try3.txt'
output_file = 'data/sky_data_real_eet_data_try3.txt'

# Read, transform, and write
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        try:
            number = float(line.strip())
            result = transform(number)
            # Debugging: print the input and the result
            print(f"Input: {number}, Result: {result}")
            outfile.write(f"{result}\n")
        except ValueError:
            # Handle the case where a line is not a valid float
            continue
