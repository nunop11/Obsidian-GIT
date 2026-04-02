## line detection algorithm
**Accuracy**
The first part of this work to be developed and tested was the line dection algorithm, the essential basis of the work. To measure the algorithm's accuracy, we registered the position where the robot detected a wall at known distances, where a hundred attempts were registered. 

GRAFICO

We can see that the error stays relatively stable and under 1 centimeter. When the wall is 69-75 centimeters way from the robot, we can see an abrupt peak in the error. This happened due to the fucntioning of the LiDAR used, not due to the agorithm used. This LiDAR has two regimens, with different biases and precisions. The cut happens because, even after calibrating the sensor, a cut happens in the measurements and the walls are often not detected. 

**Optimization**
The execution time of the line detection algorithm was also tested. The robot was put to detect walls in different configurations, geometries and distances. The robot used has only a Raspberry Pi Pico W RP2040 as computational

GRAFICO

It is evident that there is a linear correlation between the execution time and the number of points detected in a LiDAR scan. This is the case because the algorithm has to examine each point in the clustering step. However, there does not appear to be any correlation between the number of lines detected and the execution time. The execution time consistently stays under 10 milliseconds.

## localization algorithm

**Optimization**
The robot was placed in various positions and orientations within the Robot@Factory track. Then, the execution time of the localization algorithm was registered. 

GRAFICO 

There isn't any evident correlation between the execution time of this algorithm and the amount of points or lines detected. More importantly, it consistently lays below 3 milliseconds.

**Lost mode**
Another test performed was placing the robot in five different places of the track. The robot was given a poor first estimate of its real locaiton, with the goal of evaluating the "Lost" mode. Then, the robot was left for some time estimating its pose, to evaluate the stability of the algorithm.

GRAFICO

It is evident that the algorithm seems to do its objective, localizing the robot. Special attention should be given to the upper right and lower left regions, where a machine and a warehouse are most clearly visible. In these areas, the estimates were more precise. In the center of the track the precision was also great, as in this zone all walls can be seen. Opposite this, close to the warehouses the precision is the worst, because there is less quality in the observations.

Note that errors in placing the robot in this positions could cause extra bias.

To better evaluate the functioning of the localization algorithm, we decided to better analyze the estimates from one of these points. 

GRAFICO do --

It is clear that the algorithm was able to converge to a stable pose estimation. It is also evident that the uncertainties (the values in the main diagonal of the covariance matrix) increase in sintony, which means XXX???. When walls are detected and matched to reference walls, the uncertainties fall close to zero, showing that the EKF is working properly.  

**Motion**
The last test performed consists of having the robot describe a rectangle on the track. This test was performed in the official track, as well as simulated computationally. In the real life test, the localization algorithm was given the same inputs as the odometry, but the estimated poses were not used in odometry control.

GRAFICOS LADO A LADO

The plot with the robot's estimates unfortunately does not represent correctly the trajectory taken. While odometry's error accumulation could affect the motion and the robot certainly did not follow the planned trajectory exactly, the error shown above is too much. This happens because, when the robot is in motion, often no line is detected. Because of the motion during the LiDAR measurements, lines are detected with distorcion and no longer detected. This makes the algorithm accumulate error and the estimate accumulates error. 

However, when the robot stops in a corner of the trajectory and rotates in place slowly, the algorithm can somewhat estimate the position.

In the simulated results, we can see that the algorithm has the potential to estimate the robot's pose in every point of the trajectory. However, due to measurement noise, odometry erros and XXX, this could not be replicated in real life.

## Discussion
