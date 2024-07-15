import cv2

#video capture instance
cap = cv2.VideoCapture('videos_30fps.mp4')

#total no. of frame in video
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

#frame per second of video
fps = cap.get(cv2.CAP_PROP_FPS)

#height and width 
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#initalizing the output writer for the video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('reversed2.avi', fourcc, fps, (int(width*0.5), int(height*0.5)))

print("No. of frames are: {}".format(frames))
print("FPs is :{}".format(fps))

#we have to get index of last frame of video
frame_index = frames-1
#checking if video instance is ready
if(cap.isOpened()):
    #reading till the end of the video
    while(frame_index != 0):
        #we get the current frame position to the last frame 
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()

        #resize the frame
        frame = cv2.resize(frame,(int(width*0.5), int(height*0.5)))

        #optional to show the reverse video
        cv2.imshow('winname', frame)

        #writing the reeversed video
        out.write(frame)
        #decremantin frame index at each step
        frame_index = frame_index-1

        #printng the progress
        if(frame_index%100 == 0):
            print(frame_index)
        if(cv2.waitKey(2)==ord('q')):
            break

out.release()
cap.release()
cv2.destroyAllWindows()
