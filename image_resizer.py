# Image Resizer

import cv2

def img_to_resize(source, destination, scale_percent):
    src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

    #cv2.imshow("title", src)

    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    output = cv2.resize(src, (new_width, new_height))

    cv2.imwrite(destination, output)
    #cv2.waitKey(0)


if __name__ == "__main__":
    source = "bird.png"
    destination = "newpic.png"
    scale_percent = 10 # Percent by which the image is resize
    img_to_resize(source, destination, scale_percent)
