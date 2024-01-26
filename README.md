### Introduction
This project aims to develop a system capable of detecting and tracking a specific object based on its color, applicable to both still images and videos. Such technology finds its utility in various fields, particularly in the industry, where precise object recognition can be crucial.

### Objectives
- **Color Detection**: Isolate a specific object (like a tomato) in an image using its color.
- **Object Tracking**: Track this object in a video sequence.
- **Object Identification**: Under certain conditions, specify the nature of the detected object.

## Output

![Alt Beispiel](https://github.com/ange-nguetsop/ImageSegmentation001/blob/master/Beispiel.gif)

### Challenges and Solutions
1. **Calibration of HSV Values**
   The first challenge was to find the optimal HSV values to isolate the desired color under various lighting conditions. For this, a function for manual adjustment of HSV values was used, testing on multiple photos taken under varied conditions. After numerous trials, the ideal values were determined.

2. **Detection of Closed Contours**
   A major issue encountered was forcing the algorithm to detect only closed contours. Various image processing techniques such as erosion, dilation, and thresholding were applied to achieve closed contours, a crucial step for the system's accuracy.

3. **Filtering of Contours**
   After obtaining closed contours, it was necessary to filter the internal contours to keep only the most external ones. This step effectively isolated the object of interest.

### Results
The developed system successfully identified and clearly encircled tomatoes in various images and could even count the number of tomatoes detected by the system. The system is adaptable and can be modified to isolate other fruits or vegetables, such as avocados or oranges.

### Application Areas and Utility
#### Food Industry
- **Sorting and Quality**: Used for automatic sorting of fruits and vegetables based on their color, which often indicates their ripeness or quality.
- **Process Automation**: Integration into production lines for the automation of harvesting, packaging, and quality control.

#### Surveillance and Security
- **Detection of Specific Objects**: Identification and tracking of objects or clothing of a specific color in monitored areas for security reasons.

#### Commerce and Marketing
- **Interactive Display**: Used in interactive applications where users can select objects by color to receive information or special offers.

#### Research and Education
- **Educational Tool**: Used as a teaching tool to demonstrate the principles of computer vision and image processing.

### Possibilities for Improvement
- **Automation of HSV Value Determination**: Development of an algorithm to automatically adjust HSV values based on the object (fruit or vegetable) to be detected and isolated.
- **Advanced Object Identification**: Improvement of the system to identify the object based on parameters such as shape, color, and area, under certain conditions.

### Conclusion
This project demonstrates the effectiveness of image processing and computer vision techniques in detecting and tracking specific objects. Although the current system is focused on tomato detection, its flexibility and potential for extension make it a powerful tool for various industrial, commercial, and educational applications.
