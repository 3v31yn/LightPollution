import math

a = -122.24363
b = -0.53079
c = 0.012779
d = -257.32059


def transform(y):
    return (1 / c) * math.log((a / (y + d)) - b)


input_file = 'late_night_mean_data.txt'
output_file = 'late_night_lux_data.txt'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        try:
            number = float(line.strip())
            result = transform(number)
        except ValueError:
            continue
