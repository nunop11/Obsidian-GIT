## v1 - ING
### 2. Methodology
#### 2.1 Line detection algorithm
In this work we used a mobile robot with a 2D LiDAR parallel to the groud. It measures 2D point clouds, showing the robot's surroundings in each frame. After extensive testing, we concluded that walls appear in the point clouds as linear point clusters.

**Clustering**
Using this information, our algorithm starts by dividing the point cloud into clusters. Clusters are divided according to the distance between two consecutive points: if this distance is above a certain threshold, one of the points is significantly closer to the robot and they belong to different clusters.

The threshold used is based on the angular divergence of two consective LiDAR beams. If the LiDAR has an angular resolution of $\delta$, two consecutive beams will diverge by a distance of $d\tan(\delta)$, after propagating a distance $d$. In order for this threshold to work with noisy data, a sensibility parameter $\tau$ was introduced:
$$\text{Cluster Threshold} = d\tan(\delta)\cdot\tau$$
When defining the clusters, two consecutive data points $i,i+1$ are in the same cluster if the mean of their distances to the LiDAR is below the threshold. A minimum number of points in each cluster is also enforced.

**Cluster linearity**
After dividing the data cloud into clusters, the 2D covariance matrix of each cluster is calculated. Using its eigenvalues, the linearity of the cluster is determined \(FONTE):
$$\text{Linearity} = \frac{\lambda_{1}-\lambda_{2}}{\lambda_{1}}$$
Where $\lambda_{1}$ is the highest eigenvalue of the covariance matrix. This criterium was chosen, because it has shown high consistency and resistance to noise. Clusters whose linearity is above a threshold $\varepsilon$ are considered valid lines and saved.

**Non validated clusters**
Various reasons can cause a cluster to have linearity below the linearity threshold $\varepsilon$. The data might have a lot of noise, it might contain two interseting lines (with a corner) or it simply doesn't represent any linear section. In the context of the Robot@Factory competition, corners are unlikely to be detected, so the most likely scenario is that the cluster contains a wall with noise behind it, but close enough to be put into the same cluster.

In order to precisely localize de robot, it is imperative that all walls visible are utilized. So, next, our algorithm calculates the local linearity in each point of the cluster, using $2n$ neighobring points, where $n$ is a parameter that controls the local linearity sensibility. To determine the local linearity, the covariance matrix of the neighbhood is determined and the linearity calculated with its eigenvalues.

In various tests, we observed that the point with minimum local linearity consistently marks a corner or the point where a linear section of the cluster ends and a noisy section begins. The cluster is dividedd in two along the minimum linearity point and each subcluster is analysed as detailed above. If a subcluster has a linearity above $\varepsilon$ it is considered a valid line and saved, otherwise it is rejected. Subclusters are never subdivided again.

**Saving lines**
Clusters that are validated as lines are saved for the localization algorithm. Each valid cluster is fitted using 2D PCA and the cluster's starting and ending points are projected onto the principal component direction. Using this projected points, the length, center and orientation of the fitted line are calculated. It should be noted that this orientation is the line's orientation relatively to the robot's heading, not its global orientation.

#### 2.2 Localization algorithm
In order to find the robot's pose, each wall detected is matched to a reference wall from the Robot@Factory track. This macthing could be performed by minimizing a certain cost criterion (FONTE). However, taking advantages in the track's specific geometry as noted in SECCAO PISTA allows us to create matches with lower computational effort and higher precision. Below, we will explore the algorithm developed.

##### 2.2.1 Matching
**Length Filtering**
Firstly, we reject all walls whose length isn't the same as a machine's or a warehouse's length. To make this comparison, a dynamic distance tolerance was defined after carefully studying the LiDAR's behavior:
$$\text{Length Tolerance}(L,d) = A \frac{L^{2}}{d} + B \tan(\delta)\sqrt{d^{2}+ \tfrac14L^{2}}$$
where $L$ is the reference wall's length, $d$ the distance from the LiDAR to the center of the detected line and $A,B$ are sensibility control parameters. The first term introduces higher tolerance near the detected wall, where the LiDAR might not be detecting the entire wall. The second term introduces higher tolerance further away from the wall, where the angular resolution makes it impossible to precisely detect the wall's extremes. A line detected with length $L_{d}$ is considered the same length as a reference wall with length $L_{r}$ if $|L_{d}-L_{r}|<\text{Length Threshold}(L_{r},d)$.

Each wall is atributed a type according to its length: machine, warehouse or invalid. Only "machine" and "warehouse" walls will be considered from this point.

**Relative comparisons**
Upon inspecting the Robot@Factory track, it becomes evident that at least one machine  are always detected whitou noise in close to them (while objects may be outside the track, just behind a warehouse), making them more trustworthy. It was also possible to confirm that at least one machine should always be visible, independently of the robot's position. 

For these reasons, we start by comparing each "machine" line detected $i$ with the all other lines $j$. This process is repeated until we find a pair that meets 4 simultaneous criterions: distance between line centers, coherent types, cross and dot product. Comparing the lengths of the lines was proven redundant, as their types consistently carry this information.

If two walls $i,j$ are the same type, they have to be machines. Therefore they must be parallel and the distance between their center must be a specific value, according to the competition track. If two walls are different types, they must be perpendicular and the distance between their centers can only have two values, as observed in the FIGURA DA PISTA COM LEGENDAS ???? . 

When a pair $i,j$ is found, the robot's heading estimated by odometry is used to determine each wall's position relative to the robot. That is, we determine if each wall is to the Right or to the Left of the robot. For example, we can see if $i$ is more to the right of the robot than $j$. This allows us to eliminate the 180º simmetry and correctly match each line to a reference wall. The indexes $i,j$ are stored in an array with 4 valued, each one corresponding to one of the 4 reference walls.

Afterwards, we check which of the walls $i$ or $j$ is closest to the robot. The closest wall is then compared to all the $k$ detected lines, not yet evaluated. The same relative comparison process as above is applied to find any new wall that follows all the crieterions above and allows us to fill another place in the matches array.

**Extended Kalman Filter (EKF)**
Using the matched lines we use a EKF to determine the robot's pose. This method allows us to use anywhere between 2 and 4 walls matched as measurements. This filter uses the odometry inputs to predict the robot's pose. Then, each detected wall is introduced in the innovation as a LiDAR measurement $(\rho,\alpha)$ of the line's center, which is compared to the expected measurement of the corresponding reference wall.




