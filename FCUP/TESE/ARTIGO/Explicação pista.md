## 1.2 Pista Robot@Factory 4.0
### v0 - PT
--- IMAGEM OFICIAL
Na figura XXX podemos ver o traçado da pista da competição (FONTE). As paredes verticais representam máquinas, que recebem items à esquerda e retornam items processados à direita. As paredes horizontais são armazéns, o de cima fornece materiais, o de baixo recebe materiais finais. Notemos que existem 2 pares de paredes paralelas e com o mesmo comprimento. Além disso, é evidente que a pista tem uma simetria de 180º.

A competição consiste em 3 fases, em que diferentes produtos são processados pelo robot, podendo passar por nenhuma, uma ou ambas as máquinas. Desta forma, um desafio fundamental para executar esta competição com sucesso é localizar o robot. O nosso algoritmo permite localizar o robot dentro desta pista com poucos recursos computacionais, utilizando as paredes detetadas com dados LiDAR 2D.

### v1 - ING
------- OFFICIAL IMAGE
Figure XXX displays the official track of the Robot@Factory 4.0 competition (FONTE). The vertical walls represent machines, which receive materials from the right and return processed products on the right. The horizontal walls are warehouses; the top one contain the starting materials, the bottom one receives the final products. In practice, this is done by simulation: a box is moved into a compartment on the left side of a machine and a different box is picked up on the right side.

The competition conssists of 3 phases, where robots must transport boxes between warehouses and machines. Therefore, in order to beat the competition, a fundamental problem to solve is localization. In this article we propose an algorithm that can determine the robot's pose within this track with small computational effort. Before explaining the algorithm, special attention should be given to the geometrical properties of the track: it has a 180 degree simmetry of the track and the machines/warehouses consist of 2 pairs of parallel walls with the same length, in simmetrical positions. 

### v2 - ING (melhorado)
------- OFFICIAL IMAGE
Figure XXX displays the official track of the Robot@Factory 4.0 competition (FONTE). The vertical walls represent machines, which receive raw materials on their right side and return processed products on the left. The horizontal walls are warehouses: the upper warehouse contains the initial raw materials, while the lower warehouse receives the final products. In practice, the machine's prcessing is simulated by moving a box into a compartment on the left side of a machine and then retrieving a different box from the right side.

The competition consists of three phases, where robots must transport boxes between warehouses and machines. Therefore, in order to complete the competition, a fundamental problem to adress is localization. In this work, we propose an algorithm capable of estimating the robot's pose within this track with low computational effort. 

Before explaining the algorithm, special attention should be given to the geometrical properties of the track. The layout has a 180 degree symmetry and the machines and warehouses consist of 2 pairs of parallel walls with the same length, placed in symmetric positions. These characteristics play a central role in the localization algorithm proposed.