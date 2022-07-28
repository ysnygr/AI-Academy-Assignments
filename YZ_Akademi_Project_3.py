import cv2
import pafy


tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW','MOSSE', 'CSRT']
tracker_type = tracker_types[6]

if tracker_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create() 
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create() 
if tracker_type == 'TLD':
    tracker = cv2.legacy.TrackerTLD_create() 
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow_create() 
if tracker_type == 'MOSSE':
    tracker = cv2.legacy.TrackerMOSSE_create()
if tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()
    

# Get the video file and read it
url = "https://www.youtube.com/watch?v=c-D5dkySZnI"
video_url = pafy.new(url)

best  = video_url.getbest(preftype="mp4")

video = cv2.VideoCapture(best.url)
 
ret, frame = video.read()

frame_height, frame_width = frame.shape[:2]

# Resize the video for a more convinient view
frame = cv2.resize(frame, [frame_width//2, frame_height//2])

# Initialize video writer to save the results
output = cv2.VideoWriter(f'{tracker_type}.avi', 
                         cv2.VideoWriter_fourcc(*'XVID'), 60.0, 
                         (frame_width//2, frame_height//2), True)

Frame_ID = 1
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
f = open("frameids.txt", "a")
f.truncate(0) #Comment this line to avoid deleting old pixel values from "frameids.txt"

if not ret:
    print('cannot read the video')

# Select the bounding box in the first frame
bbox = cv2.selectROI(frame, False)
ret = tracker.init(frame, bbox)

# Start tracking
while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, [frame_width//2, frame_height//2])
    if not ret:
        print('something went wrong')
        break
    timer = cv2.getTickCount()
    ret, bbox = tracker.update(frame)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    if ret:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        #print("x is:", bbox[0])
        #print("y is:",bbox[1])
        #print("Width is:", bbox[2])
        #print("Heights is:", bbox[3])
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        
        
        f = open("frameids.txt", "a")        
        f.write("FRAME {} =".format(Frame_ID) + str(bbox[0]) +"," + str(bbox[1]) + "," + str(bbox[2]) + "," + str(bbox[3]) + "\n")
        Frame_ID = Frame_ID + 1


    else:
        cv2.putText(frame, "Tracking failure detected", (100,80),
            
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        bbox = cv2.selectROI(frame, False)
        ret = tracker.init(frame, bbox)


    cv2.putText(frame, tracker_type + " Tracker", (200,20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
    
    cv2.putText(frame, " x is " +str(bbox[0])  , (0,20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,255,255),2)
    cv2.putText(frame, " y is " +str(bbox[1])  , (0,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,255,255),2)
    cv2.putText(frame, " width is " +str(bbox[2])  , (0,60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,255,255),2)
    cv2.putText(frame, " height is " +str(bbox[3])  , (0,80), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,255,255),2)
    
    cv2.putText(frame, "FPS : " + str(int(fps)), (200,50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
    cv2.imshow("Tracking", frame)
    output.write(frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break
        
video.release()
output.release()
cv2.destroyAllWindows() 
