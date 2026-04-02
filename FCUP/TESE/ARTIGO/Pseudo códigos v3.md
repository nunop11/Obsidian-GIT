## Find Lines v3
```
Inputs: LidarData (2D points measured by LiDAR, ordered by angle), TolClusters (tolerance factor for clusters), MinPoints (minimum points per cluster), LinearityThreshold (threshold to consider a valid line), CornerThreshold (threshold to consider a minimum local linearity point a corner)
Outputs: Centroids, Lengths, Orientations (of the lines detected)

FOR each Point i and Point i+1 in LidarData:
    d: mean of the distances from the two Points to the robot
    Use d to calculate the cluster threshold
    dist_pair: distance from Point i to Point i+1
    IF dist_pair > cluster threshold THEN
        Terminate current cluster if it has MinPoints points
    ELSE 
        Add Point to the cluster or start new cluster
    END
END

FOR each Cluster saved in startEndIdx:
    Compute Centroid, Sxx, Syy, Sxy of the Cluster
    Compute linearity using Sxx, Syy and Sxy
    IF linearity > LinearityThreshold THEN
        Project the first and last points of the cluster in the 2D PCA principal direction
        Compute center, length and orientation using the projected points
    ELSE:
        Find point of the Cluster with minimum local linearity and its index
        IF minimum linearity > CornerThreshold THEN:
            CONTINUE 
        ELSE:
            Subcluster1: part of the Cluster before the minimum local linearity point
            Subcluster2: part of the Cluster after the minimum local linearity point
            Compute Centroid, Sxx, Syy, Sxy of the Cluster
            Compute linearity using Sxx, Syy and Sxy
            IF each subcluster has linearity > LinearityThreshold THEN
                Project the first and last points of the cluster in the 2D PCA principal direction
                Compute center, length and orientation using the projected points   
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

Lógica do algoritmo:
1. Filtrar paredes por comprimento
2. Pegar em cada _máquina_ e comprar a cada **parede válida**. Comparar até algum par cumprir 4 critérios:
    - mesmo tipo ou não
    - distância entre os centros
    - produto escalar 
    - produto vetorial
3. Se for encontrado um par que cumpre tudo, determinar a posição de cada centro relativa ao robot. Usando isso, perceber a que par de referência corresponde
4. Determinar a parede mais próxima do robot, entre i e j
5. Continuar a procurar paredes que cumpram os 4 criterios, ao comparar com a mais próxima
6. KALMAN

### Versão resumida
```
Inputs: lidarWalls (centers, lengths and orientantions of detected walls), refWalls (centers, lengths and orientations of reference walls), thetaOdo (orientation given by odometry), thresholds for distance, vector product and angle comparations, expected distances for the walls (center distances, cross and dot produtct)
Output: pose estimation (x,y,theta)


```