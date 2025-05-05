import math

#this algorithm uses the function i found that creates a connection between mean value and exposure time
#EET=(1/c)*ln[(a-(MEAN+e)*b)/(MEAN+e)]-d

#parameters for the function
a = 3.56759065977771e5
b = 35.780570888204
c = -275.11845478299
d = 0.00030040268570601
e = 9717.9322229303

# fit function f(mean_value)=(equivalent_exposure_time)
def transform(y):
    return (1 / c) * math.log((a - (y + e) * b) / (y + e)) - d

# File paths
input_file = 'data/sky_data_real_mean_data_try3.txt' #text file containing mean pixel value data
output_file = 'data/sky_data_real_eet_data_try3.txt' #text file where the equivalent exposure time values will be saved

#opens file and uses the defined function
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        try:
            number = float(line.strip())
            result = transform(number)
            #use the next line for debugging (it shows directly the mean values and eet-s next to eachother)
            #print(f"Input: {number}, Result: {result}")
            outfile.write(f"{result}\n")
        except ValueError:
            #skips line if the float is not valid
            continue
