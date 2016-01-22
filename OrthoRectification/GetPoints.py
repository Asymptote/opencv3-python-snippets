import cv2
import imutils
import numpy as np

pts_one = []
pts_two = []

getPointsOne = True
getPointsTwo = False

totalPointsRequired = 8

def get_points(event, x, y, flags, param):
	global getPointsOne
	global getPointsTwo
	global pts_one
	global pts_two
	global totalPointsRequired

	if(event == cv2.EVENT_LBUTTONDOWN):
		if(getPointsOne):
			print("Getting points on 1")
			pts_one.append((x, y))
			if(len(pts_one) == totalPointsRequired):
				getPointsOne = False
				getPointsTwo = True
			return

		if(getPointsTwo):
			print("Getting points on 2")
			pts_two.append((x, y))
			if(len(pts_two) == totalPointsRequired):
				getPointsOne = False
				getPointsTwo = False
			return



image1 = cv2.imread("Camera/cam1.png")
image1 = imutils.resize(image1, width=800)
image2 = cv2.imread("Google/cam1-1.png")
image2 = imutils.resize(image2, width=800)

cv2.namedWindow("Input window1")
cv2.setMouseCallback("Input window1", get_points)


while True:
	if(getPointsOne):
		cv2.imshow("Input window1", image1)
		c = cv2.waitKey(1)
		if(c==1):
			break
	elif(getPointsTwo):
		cv2.imshow("Input window1", image2)
		c = cv2.waitKey(1)
		if(c==1):
			break
	else:
		break

cv2.destroyAllWindows()


fromPts = np.array(pts_one)
toPts = np.array(pts_two)

H, matches = cv2.findHomography(fromPts,toPts, cv2.RANSAC)
result = cv2.warpPerspective(image1, H,(1000, 1000))
cv2.imshow("Result", result)
cv2.waitKey(0)

