import os
from PIL import Image

#writes data inside a textfile
f=open("data/sky_data_real_mean_data_try3.txt", "w")

def calc_mean(image_path):
    #opens image and converts it to a black-white image
    img=Image.open(image_path).convert("L")
    #loads pixels (all pixel values)
    pixels=list(img.getdata())
    #calculates mean pixel value by calculating the average (the sum of pixel values / number of pixels)
    mean_value=sum(pixels)/len(pixels)
    return mean_value

results={}
#the folder that contains the photographs you want to work with
folder_path="C:/!uni things/light_pollution_research/sky_data_try3"

#goes through all the images in the folder and calculates the mean pixel values
for filename in os.listdir(folder_path):
    if filename.lower().endswith('jpg'):
        image_path = os.path.join(folder_path, filename)
        mean_value=calc_mean(image_path)
        results[filename]=mean_value

#loads data into text file
for img_name, mean_val in results.items():
  #  print(f"{img_name}: mean value = {mean_val:2f}")
     f.write(str(mean_val))
     f.write("\n")

f.close()

