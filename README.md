# Gesture-Controlled Air Canvas using OpenCV and MediaPipe

## Project Overview
The **Gesture-Controlled Air Canvas** is an innovative computer vision project that allows users to draw on a virtual canvas using hand gestures. This project utilizes OpenCV, MediaPipe, and Flask to create a web-based application that tracks hand landmarks and translates finger movements into drawing actions on a canvas. The system offers different color options, real-time drawing feedback, and an intuitive split-screen interface.

## Tech Stack
- **Programming Language:** Python
- **Web Framework:** Flask
- **Libraries:**
  - OpenCV (for image processing and camera feed)
  - MediaPipe (for hand landmark detection)
  - NumPy (for array operations)
  - Flask (for web application framework)
  - Collections (for deque data structures)
- **Frontend:** HTML5, CSS3, JavaScript
- **UI Features:** Responsive design, gradient backgrounds, modern styling

## Project Features

### 1. Web-Based Interface
- Clean, modern web interface with split-screen layout
- Real-time camera feed on the left side
- Drawing canvas display on the right side
- Responsive design that works on desktop and mobile devices

### 2. Hand Gesture Detection
- Uses MediaPipe to detect hand landmarks and track finger movements
- Real-time hand tracking with visual feedback
- Accurate finger position detection for precise drawing

### 3. Air Canvas Drawing
- Draw on a virtual canvas by moving your index finger in the air
- Smooth line drawing with customizable thickness
- Pen lift functionality using thumb-index finger proximity

### 4. Color Selection
- Four color options available: Blue, Green, Red, and Yellow
- Visual color palette displayed on the camera feed
- Real-time color switching by pointing at colored rectangles
- Current selected color indicator

### 5. Clear Functionality
- Reset the canvas with gesture (point at "C" rectangle)
- Clear button available in the web interface
- Instant canvas clearing without interrupting the drawing session

### 6. Real-time Streaming
- Live video feed streaming using Flask
- Separate canvas feed for clean drawing output
- Multi-threaded application for smooth performance

## Algorithm Explanation

### 1. Hand Detection
- MediaPipe's Hand module detects hand landmarks and provides real-time coordinates
- Tracks 21 key hand landmarks with high accuracy
- Focuses on index finger (landmark 8) and thumb (landmark 4) for drawing control

### 2. Canvas Setup
- White canvas created using NumPy (640x480 pixels)
- Separate drawing surface from camera feed
- Real-time canvas updates streamed to web interface

### 3. Gesture Recognition
- **Drawing Mode:** When thumb and index finger are apart (distance > 30 pixels)
- **Pen Lift Mode:** When thumb and index finger are close together (distance < 30 pixels)
- **Color Selection:** When finger points at colored rectangles in the top area
- **Clear Canvas:** When finger points at the clear rectangle

### 4. Color Selection & Clear Functionality
- Color rectangles positioned at the top of the camera feed
- Cooldown mechanism prevents rapid color switching
- Clear function resets all drawing points and canvas

### 5. Drawing Process
- Finger position tracked and stored in color-specific deques
- Lines drawn using OpenCV's line function
- Simultaneous drawing on both camera feed and canvas
- Different colors stored in separate point arrays

## User Interface Details

### Web Interface Components
- **Header:** Gradient background with project title
- **Split Screen Layout:**
  - **Left Side:** Live camera feed with hand tracking and color palette
  - **Right Side:** Clean drawing canvas output
- **Instructions Panel:** Floating overlay with usage instructions
- **Control Buttons:** Bottom bar with color selection and clear functionality
- **Responsive Design:** Adapts to different screen sizes

### Interactive Elements
- **Color Palette:** Visual rectangles for Blue, Green, Red, Yellow, and Clear
- **Hand Tracking Visualization:** Real-time hand landmark drawing
- **Current Color Indicator:** Shows selected color on camera feed
- **Drawing Feedback:** Green dot follows index finger position

## Code Architecture

### Flask Application Structure
```
├── app.py (Main Flask application)
├── templates/
│   └── index.html (Web interface)
├── static/ (CSS and JS files)
└── README.md
```

### Key Components

#### 1. Flask Routes
- `/` - Main application page
- `/video_feed` - Camera feed streaming
- `/canvas_feed` - Drawing canvas streaming
- `/color/<color>` - Color selection API
- `/clear` - Clear canvas API

#### 2. Core Functions
- `generate_frames()` - Main camera processing loop
- `draw_color_palette()` - Renders color selection interface
- `check_color_selection()` - Handles color switching logic
- `clear_canvas()` - Resets drawing canvas

#### 3. Drawing Logic
- Color-specific point arrays using deque data structures
- Real-time line drawing on both feeds
- Pen state management based on finger proximity

## Installation & Setup

### Prerequisites
```bash
pip install flask opencv-python mediapipe numpy
```

### Running the Application
```bash
python app.py
```

### Access the Application
Open your web browser and navigate to: `http://localhost:5000`

## Usage Instructions

1. **Start Drawing:** Keep your thumb and index finger apart while moving your hand
2. **Lift Pen:** Bring your thumb and index finger close together
3. **Change Colors:** Point your index finger at the colored rectangles at the top of the video feed
4. **Clear Canvas:** Point at the white "C" rectangle or click the Clear button
5. **View Results:** Your drawing appears in real-time on the right side canvas

## Technical Specifications

- **Camera Resolution:** 640x480 pixels
- **Canvas Size:** 640x480 pixels
- **Hand Detection:** Single hand tracking with 70% confidence threshold
- **Drawing Thickness:** 3 pixels for better visibility
- **Color Format:** BGR for OpenCV compatibility
- **Streaming:** MJPEG format for web compatibility

## Future Enhancements

- **Brush Size Control:** Variable line thickness based on hand gestures
- **Save Functionality:** Export drawings as image files
- **Multiple Hands:** Support for two-handed drawing
- **Shape Recognition:** Automatic shape detection and completion
- **Undo/Redo:** Drawing history management
- **Custom Colors:** RGB color picker interface

## Contributing
Feel free to fork this project and submit pull requests for improvements or bug fixes. Please ensure your code follows the existing style and includes appropriate documentation.

## License
This project is open-source and available under the MIT License.