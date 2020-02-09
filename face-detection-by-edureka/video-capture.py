import cv2, time

# video capture using the webcam 
video = cv2.VideoCapture(0)

a = 1 

while True:
	a = a + 1

	# check is a Boolean and check whether it is captured okay
	check, frame = video.read()
	print(frame)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('Capturing', gray)

	key = cv2.waitKey(1)

	if key == ord('q'):
		break



print(a)
video.release()
cv2.destroyAllWindows()

