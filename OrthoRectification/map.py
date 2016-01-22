import cv2
import imutils

refPt = []

def click_and_crop(event, x, y, flags, param):
	global refPt
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt.append((x, y))
		print(refPt)


image = cv2.imread("cam1.png")
image = imutils.resize(image, width=800)
#clone = image.copy()
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("image", click_and_crop)

cv2.imshow("image", image)
cv2.waitKey(0)
print(refPt)

# rc 1 rc 2 lc 3
# lcup1 lcup2 rcup3

#o1 (501, 504), (463, 477), (411, 451), (452, 213), (480, 182), (505, 288)]
#np.array([[501, 504], [463, 477], [411, 451], [452, 213], [480, 182], [505, 288]]
#cam1 [(371, 418), (345, 352), (304, 299), (544, 198), (593, 194), (566, 245)]
#np.array([[371, 418], [345, 352], [304, 299], [544, 198], [593, 194], [566, 245]])

# keep looping until the 'q' key is pressed
'''while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
 
	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break
 
# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imshow("ROI", roi)
	cv2.waitKey(0)
 
# close all open windows
cv2.destroyAllWindows()
'''
