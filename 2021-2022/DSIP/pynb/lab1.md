# DSIP Lab 1 


## warmup :

A little **warmup** on looking the behaviour of multiplying the argument of $\sin$ and $\cos$ functions and getting familiar with Python tools, especially np  dot product which came quite handy in calculating some otherwise "difficult" integrals. At some point the following exercise asked to resize in amplitude and "vertical shift"  a triangular wave.

![image-20211021164021233](C:\Users\andres.coronado\Documents\UNI\MasterOfComputerScience\2021-2022\DSIP\pynb\sinusoids)



## Approximating using fseries 

**fseries** function which was tricky to get right due to the "double" amplitude resizing factior that comes out when using dot product. Since we assumed functions defined beetween $ \left[0, 2\pi\right]$ the first normalizzation comes around considering the number of samples and the second (and third!) when I wanted to calculate the $a_n $ and $b_n $ terms whith the dot product (projecting to an orthonormal function ). Summing up the overall right amplitude normalization to the hole series was:
$$
\dfrac{(b-a)}{n} * \dfrac{1}{\sqrt{\pi}} * \dfrac{1}{\sqrt{\pi}} = \dfrac{(2\pi)}{n\pi}  = \dfrac{2}{n}
$$



---

**Parsival** Remembering how orthogonality works, I like to think Parsival's equality as a generalization of Pythagoras theorem over a more generalized structure: Leaving all the details behind the concept here is that the sum of all (infinite and mutually orthogonal) projections *dotted*  with themselves ( and then normalized in amplitude ) is equal to the signal's squared norm. When we take the difference within the two quantities, we have a **delta** that can be viewed as a measure of the approximation.  Having this tools we can get any approximation we want with a discrete number of harmonics 

It seems that the first $k$ harmonics of the Fourier series can indeed contain as much information we need out of a signal, the other harmonics are intuitively "less important" giving a little contribute on the final approximation. 



## **Plotting the signals** 

**Case 1** that was a signal $$\sin(x), x\in[0,2\pi]$$ of course it needs only the first harmonic of the series as $\sin(x)$ itself is a part of the basis in which we have to project the signal. the delta is in the order of $10^{-6}$ 



**Case 2** was a triangle wave which is continuous and does not have discontinuity points, but is not as "smooth" as the previous signal: As a matter of fact to obtain a $\Delta \leq 10^{-5}\ $ I needed **15** Fourier series terms



![image-20211021164356390](C:\Users\andres.coronado\Documents\UNI\MasterOfComputerScience\2021-2022\DSIP\pynb\case1-2)



**Case 3** Things became a little with a discontinuous square signal. After summing up 63 Fourier series terms I had $\Delta \leq 10^{-3}\ $. This time I can notice weird oscillations around the 4 edges of the square, it looks like things get worst when the area of the square is concentrated around a single value, meaning same area but smaller base as shown in the following plots:

![image-20211021164752730](C:\Users\andres.coronado\Documents\UNI\MasterOfComputerScience\2021-2022\DSIP\pynb\square)



In the worst case, (the case 3c.) even with a thousand Fourier terms and 3 minutes of CPU workload I just got close to $\Delta = 0.15$.  



**Gibbs**  Discontinuous signals that have "jumps" from one value to another may look easy to understand, but not for Fourier series: As the approximation goes near those discontinuity points, a bad oscillating behaviour starts to happened slowing the speed in which the *delta* reduces as the number $k$ of harmonics grows. 

![image-20211021162917914](C:\Users\andres.coronado\Documents\UNI\MasterOfComputerScience\2021-2022\DSIP\pynb\gibbs)

![image-20211021163040610](C:\Users\andres.coronado\Documents\UNI\MasterOfComputerScience\2021-2022\DSIP\pynb\gibbs2)


## Additional questions



---



