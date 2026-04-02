# Line Detection Algorithm

## Accuracy

The first component of this work to be developed and tested was the line detection algorithm, as it is the fundamental basis of the system. To evaluate the its accuracy, the robot was positioned at known distances from a wall, and the detected wall positions were recorded. For each distance, one hundred measurements were collected.

GRAFICO

As shown in the plot above, the error remains  stable and below 1 centimeter for most of the tested range. However, when the wall is at a distance between 69 and 75 centimeters from the robot, an abrupt peak in the error can be observed. This behavior is not caused by the algorithm itself but rather by the operating characteristics of the LiDAR sensor used. The LiDAR operates in two different measurement regimes, each with different biases and precision levels. Even after calibration, a discontinuity remains between these regimes, which causes a jump in the measured distances inside this interval. For this reason, wall detections become less reliable and there is increased error.

---

## Optimization

The execution time of the line detection algorithm was also evaluated. The robot was placed in different configurations, geometries, and distances to surrounding walls. The robot used in this work relies exclusively on a Raspberry Pi Pico W (RP2040) as its computational unit.

GRAFICO

The results show a clear linear correlation between the execution time and the number of points detected in a LiDAR scan. This occurs because the clustering stage of the algorithm examines every detected point.

In contrast, no clear correlation was observed between the number of detected lines and the execution time. This indicates that the computational cost is dominated by the point processing stage rather than by the subsequent 2D PCA line fitting.

Importantly, the execution time consistently remains below 10 milliseconds, which demonstrates that the algorithm is well suited for real-time operation on limited-capacity hardware.

---

# Localization Algorithm

## Optimization

To evaluate the computational performance of the localization algorithm, the robot was placed at different positions and orientations within the Robot@Factory track. The execution time required for each localization was then measured.

GRAFICO

No clear correlation was observed between the execution time and either the number of detected points or the number of detected lines. More importantly, the execution time consistently remained below 3 milliseconds, confirming that the localization algorithm is also suitable for real-time execution on a microcontroller.

---

## Lost Mode

Another test done consisted of placing the robot at five different locations in the track. In each, the robot was provided with a poor initial estimate of its position, with the goal of evaluating the performance of the "Lost" mode. The robot was then left running the localization algorithm repeatedly for an extended period to evaluate the convergence and stability of the algorithm. Note that, as mentioned above, the robot had to be provided a reasonable initial estimate of its heading, otherwise the algorithms would not work properly.

GRAFICO

The results show that the algorithm is generally capable of estimating the robot's pose. In particular, the upper-right and lower-left regions of the track show higher localization accuracy. These areas allow very clear views of a machine and a warehouse, which provide better geometric features for line detection. High accuracy was also observed in the central region of the track, where most surrounding walls are simultaneously visible, allowing multiple constraints to be used during localization.

However, the worst performances were observed in the areas near the warehouses, where fewer walls are visible to the LiDAR sensor. The reduced number of observations leads to weaker constraints and consequently worse precision and convergence. It should also be noted that small inaccuracies in the manual placement of the robot during these experiments may introduce additional bias in the measured errors.  

To further evaluate the behavior of the localization algorithm, we analyzed the pose estimates obtained from one of the test locations in more detail.

GRAFICO

The results clearly show that the algorithm converges toward a stable pose estimate over time. It is also evident that the uncertainties (which consiste of the values of the main diagonal of the covariance matrix) increase during periods without observations, reflecting the growing uncertainty in the robot's pose prediction.

Whenever walls are detected and matched to the reference map, the uncertainties decrease significantly, approaching zero. This behavior indicates that the Extended Kalman Filter is functioning correctly.

---

## Motion Experiment

The final experiment consisted of commanding the robot to follow a rectangular trajectory on the track. This experiment was conducted on the real Robot@Factory 4.0 track and in a computational simulation.

During the real-world experiment, the localization algorithm received the same inputs as the odometry system. However, the estimated poses produced by the localization algorithm were not used for motion control, which means that the robot's movement relied only on odometry.

GRAFICOS LADO A LADO

The plot showing the real-world's estimated poses unfortunately does not accurately represent the trajectory taken. Although odometry error accumulation can affect the robot's motion and therefore the robot likely did not follow the planned trajectory perfectly, the magnitude of the error observed in the estimates is significantly larger than desired.

This behavior occurs because, while the robot is in motion, the line detection algorithm often fails. During LiDAR scanning, the robot is in motion, which introduces distortions in the measured point cloud. As a result, lines may appear distorted and fail to be detected altogether.

However, when the robot stops at a corner of the trajectory and rotates slowly in place, the algorithm is again able to detect walls reliably and partially correct the accumulated error.

In contrast, the simulated results demonstrate that the algorithm is capable of estimating the robot's pose along the entire trajectory. In simulation, the measurements are not affected by motion distortion nor measurement noise. 

---
# Discussion

The results presented in this work demonstrate that the proposed line detection and localization algorithms are computationally efficient and suitable for execution on low-cost hardware. Both algorithms operate within strict real-time constraints, with execution times below 10 ms for line detection and below 3 ms for localization, when implemented on a RP2040 microcontroller.

The accuracy evaluation of the line detection algorithm shows that the system is capable of detecting walls with sub-centimeter precision under most conditions. 

The localization experiments show that the proposed algorithm is capable of recovering the robot's pose even when initialized with poor estimates, demonstrating the robustness of the "Lost" mode. The algorithm performs particularly well in areas where multiple walls are clearly visible, as these conditions allow strong constraints for the localization.

However, the motion experiments reveal an important limitation of the current system. When the robot moves while LiDAR measurements are being taken, the point cloud measured becomes distorted. This distortion reduces the amount and reliability of the detected lines. This then means the EKF has less observations to update the pose estimate. In this situations, the filter relies solely on the odometry, which tens to accumulate error. Over time, this can lead to elevated heading errors, which strongly affects the performance of the algorithms proposed.

These results suggest that improving motion compensation during LiDAR scanning or increasing the frequency of feature detection could significantly enhance the system's performance during motion. Despite these challenges, the simulation results indicate that the proposed localization approach is fundamentally capable of accurately estimating the robot's pose throughout the entire trajectory. Therefore, future work should focus on addressing the practical limitations introduced by real-world sensing conditions.

# Conclusao
This paper presented a lightweight LiDAR line-based localization approach designed for mobile robots operating on resource-limited, low-cost platforms.

Experimental results demonstrate that the proposed line detection algorithm achieves sub-centimeter accuracy while maintaining execution times below 10 ms on an RP2040 microcontroller. The EKF-based localization algorithm is even faster, with execution times below 3 ms.

The system is capable of reliably estimating the robot's pose and recovering from poor initial position estimates in a static scenario. However, experiments also revealed that motion during LiDAR measurement introduces distortions in the point clouds, that degrade line detection and localization results.

Despite these limitations, simulation results indicate that the proposed approach has the potential to provide accurate localization along the robot's trajectory. Future work should focus on mitigating motion-induced sensing errors and improving the robustness of line detection during robot movement.