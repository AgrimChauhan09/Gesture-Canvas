# Gesture-Controlled Air Canvas using OpenCV and MediaPipe

## Overview
This project is a **Gesture-Controlled Air Canvas** that allows users to draw on a virtual canvas using hand gestures. The project utilizes **OpenCV** for computer vision tasks and **MediaPipe** for hand tracking, enabling the detection of hand landmarks and drawing gestures in real-time.

---

## Features
- **Real-Time Hand Tracking**: Uses MediaPipe to detect and track hand movements.
- **Gesture-Based Drawing**: Control the canvas using your index finger as a virtual pen.
- **Color Selection**: Choose between different colors (Blue, Green, Red, Yellow) for drawing.
- **Clear Canvas Functionality**: Erase the entire canvas with a simple hand gesture.

---

## How It Works
1. **Hand Detection**: The webcam captures frames, which are processed using MediaPipe to detect hand landmarks.
2. **Gesture Recognition**: The index finger and thumb are tracked to identify drawing gestures.
3. **Drawing on Canvas**: Based on the position of the index finger, points are drawn on a virtual canvas.
4. **Color and Clear Options**: Different rectangles on the screen allow users to change the drawing color or clear the canvas.

---

## Project Structure
```
Gesture-Canvas/
├── main.py           # Main Python file containing the project code
├── requirements.txt  # Dependencies for the project
└── README.md         # Project documentation
```

---

## Installation
### Prerequisites
- Python 3.x
- OpenCV
- MediaPipe
- NumPy

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gesture-canva.git
   cd gesture-canva
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   python main.py
   ```

---

## Usage
- **Start the application**: Run the `main.py` file.
- **Use your index finger**: The application will detect your hand gestures.
- **Change colors**: Hover your finger over the color buttons at the top of the screen.
- **Clear the canvas**: Hover over the "CLEAR" button.

---

## Hand Gesture Controls
| Gesture       | Action                |
|---------------|-----------------------|
| Index Finger  | Draw on the canvas     |
| Thumb + Index | Switch color           |
| Clear Button  | Clear the canvas       |

---

## Code Explanation
The project is structured as follows:
- **Hand Detection**: Utilizes MediaPipe's `Hands` module to track hand landmarks.
- **Drawing Logic**: Stores points in separate arrays for each color and draws lines based on hand gestures.
- **Canvas Setup**: Creates a virtual canvas with color buttons and a clear button.

### Key Libraries Used:
- `cv2` (OpenCV): For image processing and GUI handling.
- `mediapipe`: For hand tracking.
- `numpy`: For array manipulations.

---

## Algorithm Workflow
1. **Initialize Webcam**
2. **Set Up Canvas and Color Buttons**
3. **Hand Landmark Detection**
4. **Identify Drawing Gestures**
5. **Draw on the Canvas**
6. **Change Colors or Clear Canvas**

---

## Future Improvements
- **Add More Colors**
- **Save the Drawing as an Image**
- **Gesture-Based Shape Drawing (e.g., circles, rectangles)**
- **Multi-Hand Support**

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgements
- **OpenCV**: https://opencv.org/
- **MediaPipe**: https://mediapipe.dev/

Feel free to fork, contribute, or report issues to make this project better!
