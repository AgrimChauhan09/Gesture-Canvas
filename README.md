# Gesture-Controlled Air Canvas using OpenCV and MediaPipe

##  **Project Overview**
The **Gesture-Controlled Air Canvas** is an innovative computer vision project that allows users to draw on a virtual canvas using hand gestures. This project utilizes OpenCV and MediaPipe to track hand landmarks and translate the motion into drawing actions on a canvas. The system offers different color options and a clear button to reset the canvas.

---

##  **Tech Stack**
- **Programming Language:** Python
- **Libraries:**
  - OpenCV (for image processing)
  - MediaPipe (for hand landmark detection)
  - NumPy (for array operations)

---

##  **Project Features**
1. **Hand Gesture Detection:**
   - Uses MediaPipe to detect hand landmarks and track finger movements.
2. **Air Canvas Drawing:**
   - Draw on a virtual canvas by moving your index finger in the air.
3. **Color Selection:**
   - Four color options available: Blue, Green, Red, and Yellow.
4. **Clear Button:**
   - Reset the canvas with a single gesture.

---

##  **Algorithm Explanation**
1. **Hand Detection:**
   - MediaPipe's Hand module detects hand landmarks and provides real-time coordinates.
2. **Canvas Setup:**
   - A white canvas is created using NumPy to display the drawing.
3. **Gesture Recognition:**
   - The position of the index finger (landmark 8) and thumb (landmark 4) are tracked to detect drawing gestures.
4. **Color Selection & Clear Functionality:**
   - Hand movement near the color boxes selects different colors, while movement near the clear box resets the canvas.
5. **Drawing Process:**
   - The finger's position is used to draw lines on the canvas in the selected color.

---

##  **User Interface Details**
The canvas interface includes:
- **CLEAR Button**
- **BLUE, GREEN, RED, and YELLOW Color Buttons**
- Real-time webcam feed for hand tracking



## 📚 **Code Walkthrough**
1. **Initialization:**
   - Import necessary libraries: OpenCV, NumPy, MediaPipe
   - Define deque arrays for color points
   - Set up the drawing canvas and color buttons
2. **Webcam Setup:**
   - Initialize the webcam feed using OpenCV's `VideoCapture()`
3. **Hand Tracking:**
   - Use MediaPipe to detect hand landmarks
   - Track the index finger and thumb positions
4. **Drawing Logic:**
   - Draw on the canvas based on finger movement
   - Change colors or clear the canvas based on finger position near buttons

---
