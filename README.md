### Introduction
This project aims to develop a system capable of detecting and tracking a specific object based on its color, applicable to both still images and videos using watershed algorithm. Watershed is a computer vision and image segmentation technique used for segmenting objects or regions of interest in an image. It is particularly useful when you have an image with objects that touch or overlap each other, and you want to separate them into distinct segments.

### Objectives
- **Color Detection**: Isolate a specific object (like a tomato) in an image using its color.
- **Object Tracking**: Track this object in a video sequence.
- **Object Identification**: Under certain conditions, specify the nature of the detected object.

## Output

![Alt Beispiel](https://github.com/ange-nguetsop/ImageSegmentation001/blob/master/Beispiel.gif)

### Challenges and Solutions
1. **Calibration of HSV Values**
   The first challenge was to find the optimal HSV values to isolate the desired color under various lighting conditions. For this, a function for manual adjustment of HSV values was used, testing on multiple photos taken under varied conditions. After numerous trials, the ideal values were determined.

2. **Use of the watershed method**
   After the calibration step, all that remained was to use the watershed method, and the job was done

### Results
The developed system successfully identified and clearly encircled tomatoes in various images and could even count the number of tomatoes detected by the system. The system is adaptable and can be modified to isolate other fruits or vegetables, such as avocados or oranges.


### Possibilities for Improvement
- **Automation of HSV Value Determination**: Development of an algorithm to automatically adjust HSV values based on the object (fruit or vegetable) to be detected and isolated.
- **Advanced Object Identification**: Improvement of the system to identify the object based on parameters such as shape, color, and area, under certain conditions.

### Conclusion
This project demonstrates the effectiveness of image processing and computer vision techniques in detecting and tracking specific objects. Although the current system is focused on tomato detection, its flexibility and potential for extension make it a powerful tool for various industrial, commercial, and educational applications.
