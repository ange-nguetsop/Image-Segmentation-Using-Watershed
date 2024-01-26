import cv2
import numpy as np
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Beispiel.mp4', fourcc, 25, (width, height))

while True:
    #image = cv2.imread('Tomate_google.jpg')
    ret,image = cap.read()
    result = image.copy()
    image = cv2.GaussianBlur(image,(11,11),0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([0,77,42])
    upper = np.array([18,255,255])
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(result,result, mask= mask)
    output = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(output,30,255,cv2.THRESH_BINARY)

        # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    # Ignorer le fond et les bords, donc compter les labels uniques supérieurs à 1
    n_objects = len(np.unique(markers)) - 2  # Soustraire 2 pour ignorer le fond et les bords

    text = "Tomates: " + str(n_objects)

    markers = cv2.watershed(result,markers)
    result[markers == -1] = [255,0,0]
    cv2.putText(img = result, text = text , org = (0,50), fontFace =cv2.FONT_HERSHEY_SIMPLEX , fontScale = 2, color  = (0,0,255), thickness = 2, lineType = cv2.LINE_AA)
    out.write(result)
    cv2.imshow('result',result)

    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
