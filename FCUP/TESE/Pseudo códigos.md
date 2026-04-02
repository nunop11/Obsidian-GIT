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

## Find Lines
Temos a fórmula do ângulo com invariante de Hu:
$$\begin{align*}
\Theta&= \frac{1}{2}\arctan \left(\frac{2\mu_{11}'}{\mu_{20}'-\mu_{02}'} \right)= \frac{1}{2}\arctan \left(\frac{2S_{xy}}{S_{xx}-S_{yy}} \right)
\end{align*}$$


```
Inputs: LidarData (2D points measured by LiDAR, ordered by angle), TolClusters (tolerance factor for clusters, EX:5), MinPoints (minimum points per line, EX:5), NNeighbors (number of neighbors for local linearity calculation, EX:2), LinearityThreshold (threshold to consider a valid line, EX:0.9)
Outputs: Centroids, Lengths, Orientations (of the lines detected)

FOR each Point in LidarData:
    d <- distance from Point to Origin
    threshold <- d * tan(1º) * TolClusters
    IF distance to next Point < threshold:
        Point added to the Cluster
    ELSE IF number of points in Cluster > MinPoints:
        Terminate and Save the current Cluster in startEndIdx
    END
END

FOR each Cluster saved in startEndIdx:
    centroid, Sxx, Sxy, Syy <- Vars(Cluster)
    linearity <- calcLin(Sxx, Sxy, Syy)
    IF linearity > 0.9 THEN
        length: distance between first and last point of Cluster
        angle: orientation of the line, using Hu's invariant formula
        Save centroid, length and angle to arrays Centroids, Lengths and Orientations    
    ELSE:
        localLinearities <- empty array
        FOR Point in Cluster:
            subCluster <- array of Point and NNeighbors points before and after it
            centroid, Sxx, Sxy, Syy <- Vars(subCluster)
            linearity <- calcLin(Sxx, Sxy, Syy)
            Save linearity in localLinearities
        END
        Find minimum linearity and its index in localLinearities
        IF minimum linearity > 0.9 THEN:
            CONTINUE 
        ELSE:
            subCluster <- division of Cluster along minimum linearity point with the most points
            centroid, Sxx, Sxy, Syy <- Vars(subCluster)
            linearity <- calcLin(Sxx, Sxy, Syy)
            IF linearity > 0.9 THEN
                Calculate length: distance between first and last point of subCluster
                Calculate angle: orientation of the line, using Hu's invariant formula
                Save centroid, length and angle to arrays Centroids, Lengths and Orientations
            END
        END
    END
END
RETURN Centroids, Lengths, Orientations
```

## Find Pose
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

```
Inputs: PoseIni (initial pose estimation), ref (referance walls information), Lines (structure containing Centroids, Lengths and Orientations of the lines detected)
Outputs: PoseEst (pose estimation calculated)

IF number of lines in Lines = 0 THEN
    PoseEst = PoseIni
END

validWalls <- empty array
FOR line in Lines
    
     
END
```

- Lógica do pose v2:
    1. Definimos um custo: $C=w_{\theta}\Delta \theta + w_{r}\Delta r$  que calculamos para todos os "matchs" possíveis
    2. Excluir paredes com centros muito fora da pista (|y| > 600, etc)
    3. Repetir passos abaixo, comparando a parede `i` a cada parede de referência `j`
        1. Interromper a comparação se as orientações forem muito diferentes
        2. Interromper a comparação se os comprimentos forem muito diferentes
        3. Calcular distância entre centros ($\Delta r$) e diferença entre orientações ($\Delta \theta$)
        4. Ver se a parede de referência `j` foi a referência que melhor encaixa com `i`
    4. Ver se o melhor match da parede `i` teve o menor custo até agora. Se sim, guardamos numa lista `[i, j_match]`
    5. No final de ver as paredes todas, usar o match com menor custo para fazer a correção
