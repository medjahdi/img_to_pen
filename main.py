import os

try:
    import cv2
except:
    os.system("pip install opencv-python")
    os.system("pip install opencv-contrib-python")
    os.system("pip install cv2")
    import cv2

img_path = "pic1.jpg"  

output_folder = "results"
output_filename = "sketch_image.png"

# Make sure the output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_path = os.path.join(output_folder, output_filename)

image = cv2.imread(img_path)

if image is None:
    print("Error: Unable to load image. Please check the file path.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray_image
    blur = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = 255 - blur
    sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)
    cv2.imwrite(output_path, sketch)
    print(f"Sketch image saved to {output_path}")
    cv2.imshow("Sketch Image", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
