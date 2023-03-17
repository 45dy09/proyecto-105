import os
import cv2

path="Images"
images=[]
for file in os.listdir(path):
    name,ext=os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name=path+"/"+ file
       # print (file_name)
        images.append(file_name)
count=len(images)
#print (count)
frame=cv2.imread(images[0])
h,w,chanels=frame.shape
size=(w,h)
#print(size)
out=cv2.VideoWriter("proyecto105.mp4",cv2.VideoWriter_fourcc(*"DIVX"),1,size)
for i in range(0,count):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()