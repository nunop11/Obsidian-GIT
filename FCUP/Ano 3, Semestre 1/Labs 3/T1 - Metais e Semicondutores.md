# Notas do protocolo
## Intro Teorica
### Metais
- De acordo com o modelo de Drude a condutividade de um metal é dada por:
$$\sigma=\frac{N e^{2} \tau}{m} \quad \quad \quad \Biggr|\substack{N-\textsf{densidade volúmica eletrões}\\e-\textsf{carga unitária}\\\tau-\textsf{tempo de relaxação}\\m-massa eletrão}$$
- Ora, num metal $N$ não depende da temperatura $T$. Mas $\tau$ (e consequentemente $\sigma$) depende.
- Para temperaturas acima de 100K, verifica-se experimentalmente que a resistividade de um material $\rho$ varia linearmente com a temperatura. Sendo $T_{0}$ a temperatura ambiente temos:
$$\rho(T)=\rho_{0}[1+\alpha(T-T_{0})]$$
em que $\alpha$ é o coeficiente de variação relativa com a temperatura.

- Em metais temos $N$ muito elevado. A resistividade destes materiais é então dependente da mobilidade elétrica destes: $\mu=e\tau/m$.
- Num qualquer material, mesmo que perfeito, temos que as oscilações térmicas dos átomos afetam/dificultam o movimento dos eletrões de condução.
- Temos ainda impurezas e defeitos (como lacunas atómicas) em materiais reais, de forma que:
$$\rho_{total}=\rho_{termico}+\rho_{impurezas}+\rho_{defeitos}$$

### Banda proibida de semicondutor
![[Pasted image 20231118234022.png]]
- Um díodo consiste na junção de 2 semicondutores com dopagens opostas. Gera-se uma região de depleção.
- Se o díodo for polarizado inversamente, ele não deixa passar corrente. Se for polarizado diretamente, ele conduz.
- No entanto, na realidade mesmo com o díodo polarizado inversamente verifica-se uma corrente da escala de $\mu A$. Isto ocorre porque alguns eletrões e lacunas têm energia térmica e conseguem saltar a banda de condução. Ora, isto vai depender da relação entre a energia disponível e a banda proibida caraterística do material. A excitação térmica será descrita pela distribuição de Maxwell-Boltzmann e temos:
$$I=A e^{\frac{-\Delta}{k_{B}T}}\quad \quad \quad \substack{A-\textsf{constante}\\\Delta-\textsf{energia da banda proibida}}$$
de notar que esta corrente não depende da DDP aplicada.

### Medida de pequenas resistências com LCR
- O método que os multimetros usam para medir resistencias consiste em passar corrente por resistência e determinar a DDP nos terminar. Portanto, se a resistência for muiiiiito baixa, este método começa a falhar: a certo ponto a resistência do fio condutor usado e dos terminais começa a interferir.
- Quando temos sinais oscilatórios podemos definir a *impedância* de um componente:
$$Z=R+jX \quad \quad \quad \substack{R-\textsf{resistência caraterística}\\X - \textsf{reatância}}$$
em que
$$X=X_{C}+X_{L}=- \frac{1}{\omega C}+\omega L$$
em que $X_{C},X_{L}$ são as impedâncias capacitivas e indutivas; $C$ é a capacidade e $L$ a indutância.

- O LCR é portanto um instrumento que mede indutâncias, capacidades e resistências.
- Podemos definir o *fator de dissipação*:
$$D=\frac{\text{Re}(Z)}{\text{Im}(Z)}=\frac{R}{X}$$
- A medida de $D$ para um condensador diz-nos se ele está a funcionar bem (se $D$ for muito elevado, então $R\gg X$ e o condensador comporta-se como uma resistência)

