import os

image_files = []
i = 0
os.chdir(os.path.join("data", "train/snake"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("/content/pytorch-YOLOv4/data/train/snake" + filename) 
        i+=1
print('Total Train JPG file = ',i) 
i = 0 
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
        i+=1
    outfile.close()
    print('Total Train Txt file = ',i)
os.chdir("..")