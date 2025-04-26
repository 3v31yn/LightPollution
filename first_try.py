import os
from PIL import Image


f=open("data/sky_data_real_mean_data_try3.txt", "w")

def calc_mean(image_path):
    img=Image.open(image_path).convert("L")
    pixels=list(img.getdata())
    mean_value=sum(pixels)/len(pixels)
    return mean_value

results={}
folder_path="C:/!uni things/light_pollution_research/sky_data_try3"

for filename in os.listdir(folder_path):
    if filename.lower().endswith('jpg'):
        image_path = os.path.join(folder_path, filename)
        mean_value=calc_mean(image_path)
        results[filename]=mean_value

for img_name, mean_val in results.items():
  #  print(f"{img_name}: mean value = {mean_val:2f}")
     f.write(str(mean_val))
     f.write("\n")

f.close()

#arrhenius curve

