from flask import Flask, render_template, Response, request
import cv2
import numpy as np
import mediapipe as mp
from collections import deque
import time

app = Flask(__name__)

# Initialize drawing points for each color
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]

# Initialize indices for each color
blue_index = green_index = red_index = yellow_index = 0

# Create kernel for morphological operations
kernel = np.ones((5,5), np.uint8)

# Define colors (BGR format for OpenCV)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0

# Create paint window with white background
paintWindow = np.ones((480, 640, 3), dtype=np.uint8) * 255

# Initialize MediaPipe hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mpDraw = mp.solutions.drawing_utils

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def draw_color_palette(frame):
    """Draw color selection palette on the frame"""
    # Define color rectangles positions (top of the screen)
    color_rects = [
        (10, 10, 60, 60),    # Blue
        (70, 10, 120, 60),   # Green  
        (130, 10, 180, 60),  # Red
        (190, 10, 240, 60),  # Yellow
        (250, 10, 300, 60)   # Clear (white)
    ]
    
    # Draw color rectangles with their respective colors
    cv2.rectangle(frame, (color_rects[0][0], color_rects[0][1]), 
                 (color_rects[0][2], color_rects[0][3]), (255, 0, 0), -1)  # Blue
    cv2.rectangle(frame, (color_rects[1][0], color_rects[1][1]), 
                 (color_rects[1][2], color_rects[1][3]), (0, 255, 0), -1)  # Green
    cv2.rectangle(frame, (color_rects[2][0], color_rects[2][1]), 
                 (color_rects[2][2], color_rects[2][3]), (0, 0, 255), -1)  # Red
    cv2.rectangle(frame, (color_rects[3][0], color_rects[3][1]), 
                 (color_rects[3][2], color_rects[3][3]), (0, 255, 255), -1)  # Yellow
    cv2.rectangle(frame, (color_rects[4][0], color_rects[4][1]), 
                 (color_rects[4][2], color_rects[4][3]), (255, 255, 255), -1)  # Clear/White
    
    # Add borders to rectangles
    for rect in color_rects:
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 0, 0), 2)
    
    # Add text labels
    cv2.putText(frame, 'B', (25, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, 'G', (85, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(frame, 'R', (145, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, 'Y', (205, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(frame, 'C', (265, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    return color_rects

def check_color_selection(finger_pos, color_rects):
    """Check if finger is pointing at a color rectangle"""
    global colorIndex, bpoints, gpoints, rpoints, ypoints
    global blue_index, green_index, red_index, yellow_index, paintWindow
    
    x, y = finger_pos
    
    # Check each color rectangle
    for i, rect in enumerate(color_rects):
        if rect[0] <= x <= rect[2] and rect[1] <= y <= rect[3]:
            if i == 0:  # Blue
                colorIndex = 0
                return True
            elif i == 1:  # Green
                colorIndex = 1
                return True
            elif i == 2:  # Red
                colorIndex = 2
                return True
            elif i == 3:  # Yellow
                colorIndex = 3
                return True
            elif i == 4:  # Clear
                # Clear the canvas
                clear_canvas()
                return True
    
    return False

def clear_canvas():
    """Clear the drawing canvas"""
    global bpoints, gpoints, rpoints, ypoints
    global blue_index, green_index, red_index, yellow_index, paintWindow
    
    bpoints = [deque(maxlen=1024)]
    gpoints = [deque(maxlen=1024)]
    rpoints = [deque(maxlen=1024)]
    ypoints = [deque(maxlen=1024)]
    blue_index = green_index = red_index = yellow_index = 0
    paintWindow = np.ones((480, 640, 3), dtype=np.uint8) * 255

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/color/<color>')
def set_color(color):
    global colorIndex
    colors_map = {'blue': 0, 'green': 1, 'red': 2, 'yellow': 3}
    colorIndex = colors_map.get(color, 0)
    return '', 204

@app.route('/clear')
def clear():
    clear_canvas()
    return '', 204

def generate_frames():
    global blue_index, green_index, red_index, yellow_index
    color_selection_cooldown = 0  # To prevent rapid color switching
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Convert BGR to RGB for MediaPipe
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(framergb)

        # Draw color palette
        color_rects = draw_color_palette(frame)
        
        # Show current selected color
        color_names = ['Blue', 'Green', 'Red', 'Yellow']
        current_color_name = color_names[colorIndex]
        cv2.putText(frame, f'Current: {current_color_name}', (350, 35), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors[colorIndex], 2)

        if result.multi_hand_landmarks:
            landmarks = []
            for handlms in result.multi_hand_landmarks:
                for lm in handlms.landmark:
                    lmx = int(lm.x * 640)
                    lmy = int(lm.y * 480)
                    landmarks.append([lmx, lmy])
                
                # Draw hand landmarks
                mpDraw.draw_landmarks(frame, handlms, mpHands.HAND_CONNECTIONS)

            # Get important landmarks
            fore_finger = tuple(landmarks[8])  # Index finger tip
            thumb = tuple(landmarks[4])        # Thumb tip
            center = fore_finger
            
            # Draw a circle at finger tip
            cv2.circle(frame, center, 5, (0, 255, 0), -1)

            # Check if finger is in color selection area
            if color_selection_cooldown <= 0:
                if check_color_selection(center, color_rects):
                    color_selection_cooldown = 30  # Cooldown to prevent rapid switching
            else:
                color_selection_cooldown -= 1

            # Drawing logic (only if not in color selection area)
            if center[1] > 70:  # Only draw below the color palette area
                # Calculate distance between thumb and index finger
                distance = np.sqrt((thumb[0] - center[0])**2 + (thumb[1] - center[1])**2)
                
                if distance < 30:  # Fingers close together - lift pen
                    bpoints.append(deque(maxlen=512))
                    blue_index += 1
                    gpoints.append(deque(maxlen=512))
                    green_index += 1
                    rpoints.append(deque(maxlen=512))
                    red_index += 1
                    ypoints.append(deque(maxlen=512))
                    yellow_index += 1
                else:  # Fingers apart - draw
                    if colorIndex == 0:
                        bpoints[blue_index].appendleft(center)
                    elif colorIndex == 1:
                        gpoints[green_index].appendleft(center)
                    elif colorIndex == 2:
                        rpoints[red_index].appendleft(center)
                    elif colorIndex == 3:
                        ypoints[yellow_index].appendleft(center)
        else:
            # No hand detected - lift pen
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1
            rpoints.append(deque(maxlen=512))
            red_index += 1
            ypoints.append(deque(maxlen=512))
            yellow_index += 1

        # Draw lines on both frame and paint window
        points = [bpoints, gpoints, rpoints, ypoints]
        for i in range(len(points)):
            for j in range(len(points[i])):
                for k in range(1, len(points[i][j])):
                    if points[i][j][k - 1] is None or points[i][j][k] is None:
                        continue
                    cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 3)
                    cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 3)

        # Encode frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/canvas_feed')
def canvas_feed():
    """Stream the drawing canvas"""
    def generate_canvas():
        while True:
            # Create a copy of the paint window
            canvas = paintWindow.copy()
            
            # Add a subtle border
            cv2.rectangle(canvas, (0, 0), (639, 479), (200, 200, 200), 2)
            
            # Encode and yield the canvas
            _, buffer = cv2.imencode('.jpg', canvas)
            canvas_bytes = buffer.tobytes()
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + canvas_bytes + b'\r\n')
    
    return Response(generate_canvas(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)