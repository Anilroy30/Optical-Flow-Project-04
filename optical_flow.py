import cv2
import numpy as np

# Use webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Parameters for ShiTomasi corner detection
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# Parameters for Lucas-Kanade optical flow
lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Take first frame and find corners
ret, old_frame = cap.read()
if not ret:
    print("Failed to access webcam")
    exit()

old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# Create mask for drawing
mask = np.zeros_like(old_frame)

print("Webcam opened. Move your hand or an object in front of the camera.")
print("Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Select good points
    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # Draw motion tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), 
                          color=(0, 255, 0), thickness=2)
            frame = cv2.circle(frame, (int(a), int(b)), 5, 
                             color=(0, 0, 255), thickness=-1)

        img = cv2.add(frame, mask)
    else:
        img = frame

    cv2.imshow('Optical Flow - Webcam', img)

    # Press ESC to exit
    key = cv2.waitKey(30)
    if key == 27:  # ESC key
        break

    # Update for next frame
    old_gray = frame_gray.copy()
    if p1 is not None:
        p0 = good_new.reshape(-1, 1, 2)

cap.release()
cv2.destroyAllWindows()
print("Program ended.")
