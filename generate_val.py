import os

image_files = []
i = 0
os.chdir(os.path.join("data", "validation/snake"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("/content/pytorch-YOLOv4/data/validation/snake" + filename)
        i+=1
print('Total Val JPG file = ',i)  
i = 0           
os.chdir("..")
with open("val.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
        i+=1
    outfile.close()
    print('Total Val Txt file = ',i) 
os.chdir("..")
