import cv2
import numpy as np
import os
import time
import sys

# ASCII characters ordered by density
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def rgb_to_ansi(r, g, b):
    """Convert RGB values to ANSI color code"""
    return f"\033[38;2;{r};{g};{b}m"

def reset_color():
    """Reset terminal color"""
    return "\033[0m"

def pixel_to_ascii(pixel_value):
    """Convert a pixel value (0-255) to an ASCII character"""
    # Ensure pixel_value is within valid range and convert to int
    pixel_value = int(pixel_value)
    pixel_value = max(0, min(255, pixel_value))  # Clamp to 0-255 range
    
    # Calculate index safely
    index = (pixel_value * len(ASCII_CHARS)) // 256
    
    # Ensure index is within bounds
    index = min(index, len(ASCII_CHARS) - 1)
    
    return ASCII_CHARS[index]

def frame_to_ascii(frame, width=80):
    """Convert a video frame to ASCII art"""
    # Get frame dimensions
    height, original_width = frame.shape[:2]
    
    # Calculate new height to maintain aspect ratio
    aspect_ratio = height / original_width
    new_height = int(aspect_ratio * width * 0.5)  # 0.5 to account for character height
    
    # Resize frame
    resized_frame = cv2.resize(frame, (width, new_height))
    
    # Convert to grayscale if not already
    if len(resized_frame.shape) == 3:
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    else:
        gray_frame = resized_frame
    
    # Convert pixels to ASCII
    ascii_str = ""
    for row in gray_frame:
        for pixel in row:
            ascii_str += pixel_to_ascii(pixel)
        ascii_str += '\n'
    
    return ascii_str

def frame_to_colored_ascii(frame, width=80):
    """Convert a video frame to colored ASCII art"""
    height, original_width = frame.shape[:2]
    aspect_ratio = height / original_width
    new_height = int(aspect_ratio * width * 0.5)
    
    # Resize frame
    resized_frame = cv2.resize(frame, (width, new_height))
    
    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    
    # Build ASCII string with colors
    ascii_str = ""
    for y in range(new_height):
        for x in range(width):
            # Get pixel values
            gray_pixel = gray_frame[y, x]
            r, g, b = rgb_frame[y, x]
            
            # Get ASCII character
            ascii_char = pixel_to_ascii(gray_pixel)
            
            # Add color
            colored_char = f"{rgb_to_ansi(int(r), int(g), int(b))}{ascii_char}{reset_color()}"
            ascii_str += colored_char
        
        ascii_str += '\n'
    
    return ascii_str

def main():
    """Main function to capture webcam and display ASCII art"""
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    # Set webcam properties for better performance
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    print("ASCII Webcam started! Press 'q' to quit.")
    print("Press any key to start...")
    input()
    
    try:
        while True:
            # Capture frame
            ret, frame = cap.read()
            
            if not ret:
                print("Error: Could not read frame.")
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Convert frame to ASCII
            ascii_art = frame_to_ascii(frame, width=120)
            
            # Clear screen and display ASCII art
            clear_screen()
            print(ascii_art)
            
            # Small delay to control frame rate
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nExiting...")
    
    finally:
        # Release resources
        cap.release()
        cv2.destroyAllWindows()

def main_colored():
    """Main function with color support"""
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    # Set webcam properties
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    print("Colored ASCII Webcam started! Press Ctrl+C to quit.")
    print("Make sure your terminal supports ANSI colors.")
    print("Press any key to start...")
    input()
    
    try:
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("Error: Could not read frame.")
                break
            
            # Flip frame for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Convert to colored ASCII
            ascii_art = frame_to_colored_ascii(frame, width=100)
            
            # Display
            clear_screen()
            print(ascii_art)
            
            # Control frame rate
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nExiting...")
    
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Choose version:")
    print("1. Basic ASCII (Black & White)")
    print("2. Colored ASCII")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "2":
        main_colored()
    else:
        main()
