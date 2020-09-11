# AUTOMATED-TRAFFIC-MANAGEMENT-SYSTEM

<img src ='https://images.squarespace-cdn.com/content/v1/53f78d0be4b06aa2bfc2d8da/1450204066544-CURD8Q4Y9J5FNGHCMCBP/ke17ZwdGBToddI8pDm48kD8CuAIZkq9N8hb0i_3XLvYUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKc89AJUwEjX8DQLiIhOsVfkPWEpIqnx-skx3ZV02U_kD7o301BB-hY3eq-4LA4hOjV/TV_Web_2015_Home_placeholder4a.png?format=1500w'>

# REALTIME EFFICIENT TRAFFIC MONITORING

The fact is that, the population of city and numbers of vehicles on the road are increasing day by day. 
With increasing urban population and hence the number of vehicles, need of controlling streets, highways and roads is major issue.
The main reason behind today’s traffic problem is the techniques that are used for traffic management. 
Today’s traffic management system has no emphasis on live traffic scenario, which leads to inefficient traffic management systems.
This project has been implemented by using Deep Learning and it aims to prevent heavy traffic congestion.

The increasing number of vehicles on our road intersections has given rise to the problems like road accidents, congestions, conflicts and bottlenecks. 
These problems can now only be solved by providing an efficient traffic control at intersections and that can be achieved by provision of automated volume 
based traffic signal system at intersections for continuous and efficient movement of vehicles through the intersections .

Four videos captured live from a camera facing each lanes, are divided into certain time instance and parallel processed for vehicle detection and counting. 
This phase is done using multithreading and subclip function of Moviepy library.

# VEHICLE DETECTION
In that timestamp function call is made to Cvlib detect_common_objects() function that uses Yolov3-tiny model from COCO datasets to detect 80 common objects.
For our work we keep identification limited to vehicles such as - cars, motorcycles, trucks, buses. Confidence of detected objects is also given.
Detection of vehicles is the process of identifying a vehicle from a video image / frame with bounding boxes showing its location.
A redundant collection of overlapping bounding boxes within the image / frame is suggested as potentially useful areas for the region's proposal network.
YOLO is special, as it looks at a certain part of an object only once, like other classifiers. As an object detector, this technique is much quicker with comparable precision.

<img src='https://i.ytimg.com/vi/zIZeGewfKBg/maxresdefault.jpg'>

Step I: The input video file is given to the module. 

Step II: Frames are extracted from the videos. 

Step III: Extracted frames are given to the Deep Neural Network.

Step IV: Yolo V3 weight file is also given to the Deep Neural Network (YOLO v3). 

Step V: Object (car) is detected here with the help of the YOLO v3 module. 

# VEHICLE TRACKING
The detected object is a car with different probabilities and continuously monitored with a bounding box of green color.
The various probabilities indicate that the detected object is a car with a probability 0-1 indicates the likelihood of being a car. 

# VEHICLE COUNTING
It gives the number of cars according to the number of bounding boxes detected around the cars.
Appending each count to subsequent lane numbers.
A text in the top of the window shows number of detected vehicles at that instant .

# LANE ADDITION
At first iteration(timestamp) all 4 lanes are taken into consideration and the lane with maximum number of cars is given green signal. 
From 2nd iteration 3 leftover lanes are considered that were in red signal, the number of cars for next timestamp gets added. 
If lane gets green signal its reset to 0 again.

# DEADLOCK PREVENTION
Always considering maximum could lead to deadlock i.e, a lane with least number of cars could be waiting for infinite time.
To prevent this situation we maintain a counter array with most output occurrences and when it exceeds 2 , 
for that iteration we give output to lane which hasn’t been a chance before.

# PREDICTION
Comparison of Four counts(lanes) is then done and lane with maximum number of vehicles is given green signal for that timestamp. Process continues for next timestamp.

Green signal to lane number 4	      //prediction

{1: 33, 2: 12, 3: 15, 4: 42}	      //lane numbers and no. of car count in a dictionary

Green signal to lane number 1

{1: 117, 2: 28, 3: 32}

Green signal to lane number 3

{2: 40, 3: 49, 4: 45}

Green signal to lane number 2

{1: 46, 2: 55, 4: 86}

Green signal to lane number 1

{1: 114, 3: 22, 4: 75}

# FUTURE SCOPE
1.Criminal tracking for rules violation and subsequent signal forwarding to nearest police station.

2.Collision detection & prediction.

3.Number plate detection.

4.Emergency vehicle detection like ambulance,fire brigade,police van, etc.



