# 1 - Exemplo de aplicação da hipótese de Broglie
![[difraçao onda-eletrao.png]]
- Consideremos o caso acima:
    - Uma radiação de comprimento de onda $\lambda$ indicide num anteparo com 2 fendas de diâmetro $d$. As ondas sofrem difração e embatem numa parede, a uma distância $L$ do anteparo. Na parede podemos observar 2 máximos consecutivos a uma distância $H$.
    - Consideramos que $L\gg d$

- Tal como vimos em Ondas e Meios Contínuos, temos que a diferença de fase entre as 2 ondas difratadas, $\delta$, é dada por $\Large \delta=d\sin\theta$
- E como queremos estudar os máximos da onda total que incide na parede, estamos a considerar interferências construtivas, pelos que temos $$d\sin\theta=m \lambda \quad \quad; \quad m=1,2,\dots$$
- Como $L\gg d$ podemos dizer que:
$$H\approx L\tan\theta \approx L\sin\theta \approx L \frac{\lambda}{d}$$
(aqui consideramos o 1º e 2º pico, pelo que $m=1$)

- Assim, considerando esta experiência para luz visível, $\lambda=500~nm$, com $d=0.5~mm$ e $L=3~m$
    - Temos $\Large H\approx L \frac{\lambda}{d}=3~mm$

- Consideremos agora um feixe de eletrões com uma energia cinética de $25~eV$ a colidir com o anteparo, sendo que $d=0.5~mm,~~L=3~m$
    - Apliquemos a hipótese de Broglie: $$\lambda=\frac{h}{|\vec{p}|} = \frac{h}{\sqrt{2mE_{c}}}=\frac{hc}{\sqrt{2mc^{2}E_{c}}}=\frac{1.24\cdot10^{3}~eVnm}{\sqrt{2(511\cdot10^{3}~eV)(25~eV)}}\approx 0.2453~nm$$
    (de notar que se usou $E_{c}=\frac{1}{2}mv^{2}=\frac{|\vec{p}|^{2}}{2m}$. Multiplicou-se ainda as 2 partes da fração por $c$ para ficar com $hc$ e $mc$, valor que conhecemos expressar com $eV$ e $nm$)
    - Neste caso temos $$H\approx L \frac{\lambda}{d}=1~\mu m$$

# 2 - Experiência de Davisson e Germer
![[exp davidsson-germer.png]]
- Temos a montagem acima. Eletrões libertados pelo filamento $F$ são acelerados por uma DDP $V$. Atingem um cristal de níquel, $C$, eles são difundidos e alguns chegam ao detetor, $D$.

- Assim, queremos saber quantos eletrões chegam a $D$, para uma certa DDP aceleradora $V$.
- Experimentalmente, verificou-se que:
![[davidsson-germer graficos.png]]

- Novamente, iremos interpretar os eletrões que indicem no cristal como ondas. Assim, temos eletrões (ondas) a incidir num cristal (onda). Ora, para compreender os picos dos gráficos acima, queremos então estudar os momentos em que há _interferência construtiva_, tendo-se a __*Lei de Bragg*__:
$$\delta=d\sin\theta=m\lambda \quad \quad;\quad m=1,2,\dots$$
A colisão que temos é do tipo:
![[difusao eletrao em cristal.png]]
Sendo:
    - $d$ - Distância entre 2 planos do cristal
    - $D$ - Distência entre 2 átomos do cristal
    - $\varphi$ - ângulo de difusão do eletrão; $\varphi=\pi-2\theta$
    - $\theta$ - ângulo de Bragg: temos aqui uma reflexão de Bragg, daí ter o mesmo ângulo $\theta$ dos 2 lados.

- Temos:
$$2d\sin\theta=m\lambda \leftrightarrow 2d\sin \left( \frac{\pi}{2}- \frac{\varphi}{2}\right)=m\lambda\longleftrightarrow 2d\cos \frac{\varphi}{2}=m\lambda$$

---
Assim, não só os eletrões, mas todos os materiais têm comportamento de partícula quando absorvem ou libertam energia, e comportamento de onda quando estão em movimento. No entanto, quanto menor for o _comprimento de onda de Broglie_, mais difícil é estudar o comportamento de onda.

#moderna #fisica #ondas