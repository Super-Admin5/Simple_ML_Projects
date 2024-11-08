import cv2 as cv

# Function to rescale an image or video frame to a given size
def rescale(frame, scale=0.75):
    """
    Rescales the given frame to the specified scale.
    
    Parameters:
        frame (numpy.ndarray): The input image or frame.
        scale (float): Scale factor to resize the frame. Default is 0.75.
    
    Returns:
        numpy.ndarray: The resized frame.
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Read and display an image with rescaling
image_path = '../Resources/Photos/cat_large.jpg'
img = cv.imread(image_path)

if img is not None:
    resized_img = rescale(img, scale=0.2)
    cv.imshow('Resized Image - Cat', resized_img)
    cv.waitKey(0)
else:
    print(f"Error: Could not load image from path '{image_path}'")

# Capture and display video from the default camera with rescaling
video_capture = cv.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not access the camera.")
else:
    while True:
        is_true, frame = video_capture.read()
        
        # Check if the frame was captured successfully
        if not is_true:
            print("Error: Could not read frame.")
            break
        
        # Resize the captured frame
        resized_frame = rescale(frame, scale=0.25)
        
        # Display the original and resized video frames
        cv.imshow('Original Video', frame)
        cv.imshow('Resized Video', resized_frame)
        
        # Exit loop if 'd' key is pressed
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

# Release resources
video_capture.release()
cv.destroyAllWindows()
