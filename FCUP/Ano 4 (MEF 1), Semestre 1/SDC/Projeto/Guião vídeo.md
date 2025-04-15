## Ex7
### Explanation
- In this exercise we want to make a system like this:
![[feedback 2.png|600]]
- From the classes we know that the error will follow an exponential equation:
$$e(t)=e_{0}e^{(A-K_{e}C)t}$$
- We also know that the maximum error is determined by the highest eigenvalue of the exponent $A-K_{e}C$. Because we want a maximum error of 10% in 2 seconds we get that the highest eigenvalue is -1.15:
$$\begin{align*}
e^{\lambda_{max}t}&\le e_{max}\\
e^{2\lambda_{max}}&\le 0.1\\
\lambda_{max}&\le -1.15
\end{align*}$$

- Here we faced a problem: the $C$ matrix has a 2x2 shape, and so will $K_{e}$, but it usually is a vector. To solve this we used the fact that the inclinometer only measures the angle, so we changed to $C$ to 
$$C=\begin{pmatrix}1 & 0\end{pmatrix}$$

- Because the system is observable, so we can place the eigenvalues of the exponent by changing $K_{e}$. We decided to place both eigenvalues at $-2$:
$$\det (sI-A+K_{e}C)=s^{2}+k_{e1}s+k_{e2}-79=(s+2)^{2}$$
which gave us this components of $K_{e}$:
$$\begin{align*}
k_{e1}&= 4\\
k_{e2}&= 83
\end{align*}$$

- Using this we plotted of the evolution of the true-state angle VS the estimated angle over time:
![[projeto sdc.png|450]]
- We can see that the estimation follows the true-state angle, although it goes to a higher maximum angle and doesn't overshoot.
- This happens because the estimator reacts to the true state, so it is delayed and smoother.

- We also plotted the error in a logarithmic scale:
![[projeto sdc 2.png|525]]
it follows our requirements.

