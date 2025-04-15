**"Fabrication of Integrated Optical Devices in Fused Silica by Femtosecond Laser Direct Writing"**
## 3.2 - Categorização de dispositivos óticos integrados
### 3.2.1 - Medir perda de inserção (IL)
**Montagem**
![[montagem teste guias.png]]
- Usou-se um laser com 632.8nm de comprimento de onda para confirmar o coupling e um laser ajustável para testar na zona de 1550nm.
- A luz do lazer é levada por uma fibra até um 90/10 coupler (divide o sinal para 2 canais, um com 90% da potência e outro com 10%)
    - A fibra com os 90% vai par a amostra
    - A de 10% vai para o power meter
- Usamos index matching nas interfaces fibra-amostra para reduzir reflexões de Fresnel e obter maior precisão
- As fibras estão colocadas num sistema de posicionamento com movimento X,Y,Z. A amostra  é metida num sistema de precisão com movimento X,Y,yaw,pitch
- A luz transmitida é levada para o power meter. Aí, a saída de 10% do coupler serve de referência

**Perda**
- Medimos a potência do laser, ligando-o diretamente ao medidor: $P_{0}$
- Medimos a potência transmitida : $P_{1}$
- A perda de inserção em dB é:
$$IL=10\log_{10}\left(\frac{P_{1}}{P_{0}}\right)$$
- Foi medida a intensidade da saída de 90% e da de 10% do coupler. Observou-se que as potências variam de forma linear uma em relação à outra

### 3.2.2 - Medir perfil e perda de coupling (CL)
- Aqui a perda de coupling refere-se à perda de potência da fibra ótica para o dispositivo integrado.
- Fazemos index matching, portanto reflexões de Fresnel são desprezadas. Assim, a perda só pode ser causada pelo mismatch dos perfis modais.

**Mode diameter do guia**
- Precisamos de medir o diâmetro dos modos
- Temos esta montagem
![[montagem teste guias 2.png]]
invés de ter uma fibra na transmissão, temos uma câmara CCD. Temos ainda uma objetiva de microscópio de ampliação 20x.
- O diâmetro dos modos na fibra é de 10.4um para um comprimento de onda de 1550nm. Isto é dado pelo fabricante
- Removeu-se o ruído das imagens obtidas com a CCD ao subtrair imagens de referência. Os diâmetros são determinados com LaseView, em que se usou uma gaussiana para ajustar as direções X,Y
- A eficiência do coupling pode então ser determinada assim:
![[eficiencia guia.png]]
em que $$\Psi_{1}(X,Y)=A\exp (-(X^{2}+Y^{2})/a)~~~~,~~~~\Psi_{2}(X,Y)=B\exp(-(X^{2}/d_{X}^{2}+Y^{2}/d_{Y}^{2}))$$
- $a$ é o diâmetro do modo nas fibras. $d_{X},d_{Y}$ são os diâmetros dos modos medidos para a amostra nas direções xx e yy
- Podemos então escrever:
$$\eta=\frac{4a^{2}d_{X}d_{Y}}{(d_{X}^{2}+a^{2})(d_{Y}^{2}+a^{2})}$$
e temos a perda de coupling em dB:
$$CL=10\log_{10}(\eta)$$

### 3.2.3 - Perda de propagação (PL)
- Em guias há perdas de propagação devido a propagação de Rayleigh e absorção da luz.
- Podemos relacionar as perdas assim:
$$IL=2CL + PL \cdot L$$
($L$ é o comprimento do dispositivo/guia)
- Uma técnica é fazer um guia muito longo
    - Assim teremos $PL\simeq IL/L$. Assim, para a equação bater certo, é preciso que $PL\cdot L\gg 2CL$. Ou seja, teremos $IL\sim PL$
    - Ou seja, é preciso que $L$ seja maior quando tempos PL menor.
    - MAS na prática só iremos conseguir até ~10cm. Para guias com PL baixo e CL elevado, isto vai dar um erro considerável.
- Outra técnica baseia-se no comportamento linear de IL vs L. 
    - Assim, fazemos vários guias com comprimentos diferentes (mas todos os restantes parâmetros iguais) e medimos $IL(L)$
    - Do declive/ajuste podemos determinar as perdas. Teríamos PL quando $L=0$
    - MAS para os resultados serem de confiança precisamos de fazer muitos guias
- Temos então outra técnica: medição indireta. Determinamos IL,CL conforme explciado acima. Temos: $$PL=\frac{IL-2CL}{L}$$

### 3.2.4 - Caraterização de grating
![[montagem teste guias 3.png]]
- O setup de cima serve para determinar rapidamente o comprimento de onda de Bragg. O segundo serve para caraterizar os gratings de Bragg com mais resolução
    - Um grating de Bragg de fibra e um dispositivo que reflete comprimentos de onda muito específicos e deixa passar os outros
- O 1º setup consiste em medir o sinal refletido removido por um circulador
- O 2º setup permite variar a polarização. Temos ainda a fibra a ser rodada