 Inspirações para escrever estes códigos: L2, L4 e D2 do ficheiro da Introdução

## Vars
```
FUNCTION Vars():
    Inputs: Cluster (array of 2D points of a cluster)
    Outputs: centroid (centroid of Cluster), Sxx, Sxy, Syy (covariances of Cluster)
    
    xm <- 0, ym <- 0, Sxx <- 0, Sxy <- 0, Syy <- 0
    IF length of Cluster <= 1 THEN
        centroid <- (xm, ym)
        RETURN centroid, Sxx, Sxy, Syy
    END
    Calculate xm: average of Cluster points' X coordinate
    Calculate ym: average of Cluster points' Y coordinate
    centroid <- (xm, ym)
    Calculate Sxx and Syy: variance of Cluster points X and Y coordinates (using xm and ym)
    Calculate Sxy: crossed covariance (using xm and ym)
    RETURN centroid, Sxx, Sxy, Syy 
END
```

## Linearity
$$\lambda_{\pm}=\frac{S_{xx}+S_{yy} \pm \sqrt{(S_{xx}-S_{yy})^{2}+4S_{xy}^{2}}}{2}$$

```
FUNCTION calcLin():
    Inputs: Sxx, Sxy, Syy (Elements of the covariance matrix)
    Outputs: linearity
    
    LMax <- 0.5 * (Sxx + Syy + sqrt( (Sxx-Syy)^2 + 4Sxy^2 ) )
    LMin <- 0.5 * (Sxx + Syy - sqrt( (Sxx-Syy)^2 + 4Sxy^2 ) )
    linearity <- (LMax - Lmin) / LMax
    RETURN linearity
END
```

## Find Lines v2
Temos a fórmula do ângulo com invariante de Hu:
$$\begin{align*}
\Theta&= \frac{1}{2}\arctan \left(\frac{2\mu_{11}'}{\mu_{20}'-\mu_{02}'} \right)= \frac{1}{2}\arctan \left(\frac{2S_{xy}}{S_{xx}-S_{yy}} \right)
\end{align*}$$

Fórmula da tolerância ao fazer clusters:
$$\text{Threshold} = d \cdot\tan(1º) \cdot\text{TolClusters}$$

```
Inputs: LidarData (2D points measured by LiDAR, ordered by angle), TolClusters (tolerance factor for clusters, EX:5), MinPoints (minimum points per line, EX:5), NNeighbors (number of neighbors for local linearity calculation, EX:2), LinearityThreshold (threshold to consider a valid line, EX:0.9)
Outputs: Centroids, Lengths, Orientations (of the lines detected)

FOR each Point in LidarData:
    Calculate d: distance from Point to Robot
    Use d to calculate the accepted threshold
    Calculate dist_pair: distance from Point to following point
    IF dist_pair > threshold THEN
        Terminate current cluster if it has MinPoints points
    ELSE 
        Add Point to the cluster
    END
END

FOR each Cluster saved in startEndIdx:
    centroid, Sxx, Sxy, Syy <- Vars(Cluster)
    linearity <- calcLin(Sxx, Sxy, Syy)
    IF linearity > LinearityThreshold THEN
        length: distance between first and last point of Cluster
        angle: orientation of the line, using Hu's invariant formula
        Save centroid, length and angle to arrays Centroids, Lengths and Orientations
    ELSE:
        Find point of the Cluster with minimum linearity and its index
        IF minimum linearity > LinearityThreshold THEN:
            CONTINUE 
        ELSE:
            subCluster <- division of Cluster along minimum linearity point with the most points
            centroid, Sxx, Sxy, Syy <- Vars(subCluster)
            linearity <- calcLin(Sxx, Sxy, Syy)
            IF linearity > LinearityThreshold THEN
                Calculate length: distance between first and last point of subCluster
                Calculate angle: orientation of the line, using Hu's invariant formula
                Save centroid, length and angle to arrays Centroids, Lengths and Orientations
            END
        END
    END
END
RETURN Centroids, Lengths, Orientations
```

## Find Pose v3
A tolerância de erro no comprimento de uma parede detetada é dada por:
$$\text{Tol} = 0.15 \frac{L^{2}}{d} + 4\tan(1º)\sqrt{d^{2}+ \tfrac14L^{2}}$$

```
FUNCTION wallLengthToll()
    Inputs: L (reference wall length), d (distance from robot to line centroid)
    Outputs: tolerance
    
    tolerance <- 0.15 * L^2/d + 4 * tan(1º) * sqrt(d^2 + 0.25 * L^2)
    RETURN tolerance
END 
```
Lógica do algoritmo:
1. Filtrar paredes por comprimento
2. Pegar em cada _máquina_ e comprar a cada **parede válida**. Comparar até algum par cumprir 4 critérios:
    - mesmo tipo ou não
    - distância entre os centros
    - produto escalar 
    - produto vetorial
3. Se for encontrado um par que cumpre tudo, determinar a posição de cada centro relativa ao robot. Usando isso, perceber a que par de referência corresponde
4. Usar as fórmulas para obter a orientação usando a máquina (é indiferente)
5. Determinar a posição:
    1. Se tivermos 2 máquina, usar a fórmula com a mais próxima 
    2. Se tivermos 1 máquina e 1 armazém, determinar X com a máquina e Y com o armazém

$$\begin{align*}
\delta &= \theta_\text{ref} - \theta_{i}\\
P &= P_\text{ref} - R_{\delta}(P_{i}^\text{local})\\
&= P_{\text{ref}} - \begin{pmatrix}\cos\delta & -\sin\delta\\
\sin\delta & \cos\delta\end{pmatrix} \begin{pmatrix}C_{xi}\\
C_{yi}\end{pmatrix}\\
&= \begin{pmatrix}C_{x}^{\text{ref}}- \cos\delta C_{x}^{i} + \sin\delta C_{y}^{i}\\
C_{y}^{\text{ref}}- \sin\delta C_{x}^{i} - \cos\delta C_{y}^{i} \end{pmatrix}
\end{align*}$$

### Versão detalhada
```
Inputs: lidarWalls (centroids, lengths and orientantions of detected walls), refWalls (centers, lengths and orientations of the reference map walls), thetaOdo (orientation given by odometry), thresholds for distance, vector product and angle comparations, expected distances for the walls (center distances, cross and dot produtct)
Output: pose estimation (x,y,theta)

FOR each Wall in lidarWalls:
    IF Wall's length is within threshold of Machine length THEN
        type = machine
    ELSE IF Wall's length is within threshold of Warehouse length THEN
        type = warehouse
    ELSE
        type = invalid
    END
END

FOR each Wall i in lidarWalls:
    IF type == machine THEN
        FOR each Wall j != i in lidarWalls:
            IF type != invalid THEN
                Calculate d_ij: distance between the walls' centers
                Calculate same_type: flag indicating if they are the same type
                Calculate cross: cross product magnitude of the walls' unit vectors
                Calculate dot: dot product of the walls' unit vectors
                
                IF d_ij, same_type, cross, dot ALL meet the requirements THEN
                    Calculate each wall's relative position to the robot, using thetaOdo
                    Using these positions, determine the matching pair of reference walls
                    Terminate the search for a pair
                END
            END
        END
    END
END

IF a valid pair is found THEN
    Use cross and dot products to normalize the angles so the walls have the correct orientations
    Calculate orientation with the formula
    Normalize orientation so it is coherent with thetaOdo
    IF the pair is a machine + machine pair THEN
        Calculate position with the formula, using the nearest wall
    ELSE
        Calculate X position with the formula and the machine
        Calculate Y position with the formula and the warehouse
    END
END
```

### Versão resumida
```
Inputs: lidarWalls (centroids, lengths and orientantions of detected walls), refWalls (centers, lengths and orientations of the reference map walls), thetaOdo (orientation given by odometry), thresholds for distance, vector product and angle comparations, expected distances for the walls (center distances, cross and dot produtct)
Output: pose estimation (x,y,theta)

Atribute a type to each wall, considering its length

FOR each Wall i with type "machine"
    FOR each valid Wall j != i
        Calculate d_ij: distance between the walls' centers
        Calculate same_type: flag indicating if they are the same type
        Calculate cross: cross product magnitude of the walls' unit vectors
        Calculate dot: dot product of the walls' unit vectors
        IF d_ij, same_type, cross, dot ALL meet the requirements THEN
            Calculate each wall's relative position to the robot, using thetaOdo
            Using these positions, determine the matching pair of reference walls
            Terminate the search for a pair
        END
    END 
END

IF a valid pair is found THEN
    Use cross and dot products to normalize the angles so the walls have the correct orientations
    Calculate orientation with the formula
    Normalize orientation so it is coherent with thetaOdo
    IF the pair is a machine + machine pair THEN
        Calculate position with the formula, using the nearest wall
    ELSE
        Calculate X position with the formula and the machine
        Calculate Y position with the formula and the warehouse
    END
END
```