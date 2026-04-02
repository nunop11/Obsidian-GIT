## v2 - ING (melhorado) 
### 2. Methodology
#### 2.1 Line detection algorithm
In this work we used a mobile robot with a 2D LiDAR sensor parallel to the groud. It measures 2D point clouds, showing the robot's surroundings at each frame. We observed that walls appear in the point clouds as clusters of points arranged approximately in straight lines.

**Clustering**
Based on this observation, the proposed algorithm starts by dividing the point cloud into clusters. Clusters are formed according to the distance between two consecutive points: if this distance is above a certain threshold, one of the points is significantly closer to the robot and they are assigned to different clusters.

This threshold is defined based on the angular divergence between two consecutive LiDAR beams. If the LiDAR has an angular resolution of $\delta$, two consecutive beams will diverge by a distance of $d\tan(\delta)$ after propagating a distance $d$. To ensure robustness with noisy data, a sensibility parameter $\tau$ was introduced:
$$\text{Cluster Threshold} = d\tan(\delta)\cdot\tau$$
When defining the clusters, two consecutive data points $i,i+1$ are assigned to the same cluster if the mean of their distances to the LiDAR is below the threshold. Additionally, a minimum number of points in each cluster is enforced.

**Cluster linearity**
After dividing the point cloud into clusters, the 2D covariance matrix of each cluster is computed. Using its eigenvalues, the linearity of the cluster is determined (FONTE):
$$\text{Linearity} = \frac{\lambda_{1}-\lambda_{2}}{\lambda_{1}} ~~~~,~~~~ \begin{cases} \lambda_{1}=\frac{S_{xx}+S_{yy} + \sqrt{(S_{xx}-S_{yy})^{2}+4S_{xy}^{2}}}{2} \\
\lambda_{2}=\frac{S_{xx}+S_{yy} 2 \sqrt{(S_{xx}-S_{yy})^{2}+4S_{xy}^{2}}}{2} \\
\end{cases}$$
Where $\lambda_{1}$ is the largest eigenvalue of the covariance matrix. This criterion was chosen due to its high consistency and robustness to noise. Clusters whose linearity is above a threshold $\varepsilon$ are considered valid lines and stored for the localization algorithm.

**Non validated clusters**
Various factors may cause a cluster to have linearity below the linearity threshold $\varepsilon$. The data may be strongly affected by noise, it may contain two interseting lines (and a corner) or it may simply not represent a linear structure. In the context of the Robot@Factory competition, corners are unlikely to be detected; so the most likely scenario is that the cluster contains a wall with noise behind it, close enough to be grouped into the same cluster.

In order to accurately localize de robot, it is imperative that all walls visible are utilized. For this reason, the algorithm calculates the local linearity in each point of the cluster using $2n$ neighobring points, where $n$ is a parameter that controls the sensbility of local linearity analysis. To determine the local linearity, the covariance matrix of the neighbhood is determined and the linearity calculated with its eigenvalues.

Various testes have shown that the point with minimum local linearity consistently marks a corner or the transition between a linear section and a noisy section of the cluster. The cluster is divided into two subclusters, along the minimum linearity point. Each subcluster is analyzed as explained above. If a subcluster has a linearity above $\varepsilon$ it is considered a valid wall and stored, otherwise it is rejected.

**Storing walls**
Clusters that are validated as walls are saved for the localization algorithm. Each valid cluster is fitted using 2D PCA and the starting and ending points of the cluster are projected onto the principal component direction. Using these projected points, the length, center and orientation of the fitted line are calculated. It should be noted that this orientation is the walls's orientation relatively to the robot's heading, not its global orientation.

#### 2.2 Localization algorithm
To estimate the robot's pose, each detected wall is matched to a reference wall from the Robot@Factory track map. The discrepancies between detected and reference walls are used to estimate the robot's pose. Therefore, the algorithm starts by doing this matching. 

Two matching modes were implemented: "Localized" and "Lost". Both versions start by performing a length filtering step.

**Length Filtering**
All detected walls whose lengths are incompatible with those of either machines or warehouses are rejected. To make this comparison, a dynamic length tolerance was defined after carefully studying the LiDAR's measurement characteristics:
$$\text{Length Tolerance}(L,d) = A \frac{L^{2}}{d} + B \tan(\delta)\sqrt{d^{2}+ \tfrac14L^{2}}$$
where $L$ is the reference wall's length, $d$ the distance from the LiDAR to the center of the detected wall and $A,B$ are sensitivity control parameters. 

The first term introduces a higher tolerance near the detected wall, where the LiDAR may not detect the entire wall. The second term introduces a higher tolerance far away from the wall, where the LiDAR's angular resolution limits the accurate detection of the wall's extremities. A detected wall with length $L_{d}$ is considered the same length as a reference wall of length $L_{r}$ if $|L_{d}-L_{r}|<\text{Length Threshold}(L_{r},d)$.

Each detected wall is assigned a type according to its length: machine, warehouse or invalid. Only "machine" and "warehouse" walls will be considered from this point onward. Additionally, walls may later be assigned a fourth type: "matched", to avoid matching the same detected wall with multiple reference walls. 

Both matching modes operate on the detected walls using their types, determined in the filtering stage.

##### 2.2.1 Matching: "Localized" Mode
This matching mode is computationally efficient, but it relies heavily on the previous pose estimation. For this reason, this mode is applied when the estimation is working properly and the robot's pose estimate is considered reliable. 

This mode simply compares each reference wall $r$ to every detected wall $i$ of the same type, excluding invalid and already matched walls. Before computing the cost for each wall, the orientations of the reference and detected walls are compared using the cross product. Since matching walls should be parallel, if the cross product is above a certain threshold, then the orientations are too different and the match is rejected. 

The orientation check was done separately from the cost function due to the high importance of the robot's heading estimation. This criterion allows the robot to abandon the "localized" mode before it accumulates significant errors.

If the previous test is passed, the following cost function is computed:
$$\text{Cost} = w_{d}~d_{ir} + w_{a} \|\mathbf{t}_{r}\times \mathbf{t}_{i}\|C $$
Where $w_{d},w_{a}$ are the weights attributed to distances and angles in the cost function. $C$ is a scaling factor, used to bring the cross product to the same order of magnitude as the distance term. $d_{ir}$ is the distance between the reference wall's position and the estimated global position of the detected wall. The second term has the cross product of the tangent vector of the two walls, which are determined with their orientations. 

For each reference wall, the detected wall with minimum cost is selected. If that wall has a cost below a predetermined threshold, the match is validated. Wall's $i$ type becomes "matched".

However, if less than 2 matches are made after evaluating every wall, the "Localized" mode does not return any correspondences. If this happens, the robot is considered lost. In this case, the previous pose estimation is deemed unreliable and we switch to the "Lost" mode. 

##### 2.2.2 Matching: "Lost" Mode
This mode is computationally more expensive, but it is capable of estimating the robot's position using only the LiDAR measurements and the previous heading estimate. Experimental testing showed that this method reliably recovers the robot’s position as long as the heading error remains within a reasonable bound. 

This mode takes advantage of the track's specific geometry, as noted in SECCAO PISTA, which enables wall matching with less information. This mode is only applied when "Localized" mode fails. Note that the wall types assigned during the length filtering stage remain accessible.

**Relative comparisons**
The matching process begins by comparing each detected wall $i$ with all other detected walls $j$. This process continues until we find a pair that meets four criteria: distance between wall centers, compatibility of wall types, cross product and dot product of orientations. Comparing the lengths of the walls was found to be redundant, as the wall types consistently encode this information.

If two walls $i,j$ are of the same type, they must be parallel; otherwise they must be perpendicular. The distances between the walls centers can only take one of four possible values: machine-machine distance, warehouse-warehouse distance, machine-warehouse distance on the same side of the track and machine-warehouse distance on opposing sides of the track. Testing showed that this combination of criteria was enough to reliably perform correct matches. 

Once a valid pair $i,j$ is found, the robot's previous heading estimation is used to determine the relative position of each wall with respect to the robot. That is, it is determined if each wall is to the right or to the left of the robot. This resolves the 180º simmetry of the track and allows each detected wall to be correctly matched to a reference wall. The indexes $i,j$ are stored in an array with four elements, each corresponding to one of the four reference walls.

Next, the algorithm checks which of the walls $i$ or $j$ is closest to the robot. The closest wall is then compared to all the remaining detected walls $k$ that have not yet been evaluated. The same relative comparison process as above is applied to find any new wall that satisfies all the criteria and fills a spot in the matching array.

**Position estimation correction**
After matching the detected walls with reference walls in the map using only the robot's heading estimate, it is possible to apply corrections to the robot’s position estimate. Each detected wall introduces a directional constraint on the robot’s position: detecting a wall above (or below) implies that the robot must be below (or above) it. Similarly, detecting a wall to the left (or right) implies that the robot must lie to its right (or left). Using these constraints, we can refine the position estimation. 

However, this is not a complete position estimate. This process only places the previous estimation in a plausible region of the track. This will allow the Extended Kalman Filter to be initialized with a more reasonable state, which should avoid agressive corrections.

##### 2.2.3 Extended Kalman Filter
Once all the wall correspondences are established, an Extended Kalman Filter (EKF) is used to estimate the robot’s pose. This approach allows the use of between two and four matched walls as measurements. 

The filter uses odometry input measurements to predict the robot’s pose evolution. Then, each detected wall is incorporated into the update step as a LiDAR measurement $(\rho,\alpha)$ of the wall's center. These measurements are compared with the expected observations of the corresponding reference walls to estimate the robot's pose.

It should be noted that the walls were processed by the EKF sequentially, instead of simultaneously. This approach was chosen to reduce computational cost, as otherwise it could be necessary to invert a 8x8 matrix in the update step. 


