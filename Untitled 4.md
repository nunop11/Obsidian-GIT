- Temos então as correçõees:
$$dD=\begin{cases}
m_{1}R+b_{1} & , & R<685 \\
m_{2}R+b_{2} & , & R\ge685
\end{cases}$$
ou seja temos as equações que definem aquilo que medimos:
$$D = \begin{cases}
(1+m_{1})R+b_{1} & , & R<685 \\
(1+m_{2})R+b_{2} & , & R\ge685
\end{cases}$$
- Mas queremos inverter, ou seja:
$$\begin{align*}
D&= (1+m)R+b&&,&&R>x\\
D-b&= (1+m)R&&,&&R>x\\
R&= \frac{1}{1+m}D-\frac{b}{1+m}&&,&&R>x\\
R&= \frac{1}{1+m}D-\frac{b}{1+m}&&,&&\frac{D-b}{1+m}>x\\
R&= \frac{1}{1+m}D-\frac{b}{1+m}&&,&&D-b>(1+m)x\\
R&= \frac{1}{1+m}D-\frac{b}{1+m}&&,&&D>(1+m)x+b\\
\end{align*}$$
- Logo temos a equação de calibração:
$$R=\begin{cases}
\frac{1}{1+m_{1}}D- \frac{b_{1}}{1+m_{1}} & , & (1+m_{1})685+b_{1} \\
\frac{1}{1+m_{2}}D- \frac{b_{1}}{1+m_{2}} & , & (1+m_{2})685+b_{2} \\
\end{cases}$$
