import cv2

image = cv2.imread("dragon.jpg", 0);

print(type(image));#prints the type of the image that is an numpy array 
print(image);
print(image.shape);#prints the dimension of the image

# Learning how to show images with the opencv 

image = cv2.resize(image,(int(image.shape[0]/2),int(image.shape[0]/2)));
cv2.imshow("Dragon", image);
cv2.imwrite("Dragon_resized.jpeg",image);
cv2.waitKey(0);
cv2.destroyAllWindows();