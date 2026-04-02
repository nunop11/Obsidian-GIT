## Find Lines v2
Temos a fórmula do ângulo com invariante de Hu:
$$\begin{align*}
\Theta&= \frac{1}{2}\arctan \left(\frac{2\mu_{11}'}{\mu_{20}'-\mu_{02}'} \right)= \frac{1}{2}\arctan \left(\frac{2S_{xy}}{S_{xx}-S_{yy}} \right)
\end{align*}$$

Fórmula da tolerância ao fazer clusters:
$$\text{Threshold} = d \cdot\tan(1º) \cdot\text{TolClusters}$$

```
Inputs: LidarData (2D points measured by LiDAR, ordered by angle), TolClusters (tolerance factor for clusters), MinPoints (minimum points per line), LinearityThreshold (threshold to consider a valid line), CornerThreshold (threshold to consider a minimum local linearity point a corner)
Outputs: Centroids, Lengths, Orientations (of the lines detected)

FOR each Point in LidarData:
    Calculate d: mean of the distances from the Points to the robot
    Use d to calculate the clustering threshold
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
            Subcluster1: part of the cluster before the minimum linearity point
            Subcluster2: part of the cluster after the minimum linearity point
            Apply Vars and calcLin to each subcluster
            IF each subcluster has linearity > LinearityThreshold THEN
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
Inputs: lidarWalls (centroids, lengths and orientantions of detected walls), refWalls (centers, lengths and orientations of the reference map walls), thetaOdo (orientation given by odometry), thresholds for distance, vector product and angle comparations, expected distances for the walls (center distances, cross and dot produtct)
Output: pose estimation (x,y,theta)

Atribute a type to each wall, considering its length

// Comparar e encontrar paredes validas
// Usar todas no filtro de Kalman
```