import cv2
from os import listdir
import glob

img_names = glob.glob("*.jpg")

print(img_names)
for images in img_names:
    img=cv2.imread(images,0)
    resized_image=cv2.resize(img,(100,100))
    cv2.imshow("01",resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+images,resized_image)

print(type(img))
print(img.shape)
print(img.ndim)
print(img_names)