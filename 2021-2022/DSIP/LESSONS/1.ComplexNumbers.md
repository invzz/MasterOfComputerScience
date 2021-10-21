# Digital Signals and Image Processing

Notes on 2021-2022 class by Andrès Coronado.

## 1 Complex Numbers

### **Solutions to Complex numbers Exercises**

These Solutions are proposed and written by Andrés Coronado,  MAT 2761046

#### Andrés notes

Hoping to unfog my mind while I'm writing I will try to explain what the exercises mean to me in English words before I move to the math language.

two generic complex numbers:
$$
\begin{align*}
z &= a+ib, \\
w &= c+id \\
\end{align*}
$$

#### Ex.1

- Prove that the module of a complex number is equal to the module of it conjugate.
$$
|z| = |z^*|\\
\sqrt{a^2+b^2} = \sqrt{a^2+(-b)^2}
$$

---

- Prove that the conjugate of a conjugate of a complex number, it's the original complex number.
$$
\begin{align*}
(z^*)^*= z \\
(a -ib)^* = z \\
(a - (-i(b))) = a+ib = z
\end{align*}
$$

---

- prove that If a complex number has module 0 it must be the number 0.
$$
\begin{align*}
|z| = 0 \text{ iff } z = 0 \\
a^2 + b^2 = 0 \\
a^2 = -(b^2) \\
\end{align*}
$$

Nb. being $ -(b^2) $ always negative for any $ n > 0 $ the only complex number that has module $ 0 $ is $ 0 $.

---

#### Ex.2

Compute the Product between a generic complex number and a conjugate of another generic complex number:

$$
\begin{align*}
zw^* &=(a+ib)\cdot(c-id) \\ &= ac-i^2bd + ibc - iad   \\ &= ac + bd + ibc - iad
\\\text{separating real} &\text{ and imaginary part} :
\\&= (ac -bd) -i (ad-bc)
\\\text{observe:}\\
zw &= (ac - bc) + i(ad + bc)\\
\end{align*}
$$

---
Compute the division between two generic complex numbers:
$$
\begin{align*}
\dfrac{z}{w} &= \dfrac{z}{w} \cdot  \dfrac{w^*}{w^*} \\
&=\dfrac{zw^*}{ww^*}\\
&=\dfrac{(ac+bd)-i(ad-bc)}{c^2+d^2}
\end{align*}
$$

---
**Ex. 3**
Find the polar representation of $2, -3, 4i, -5i,1+i$ and $i^4$

$$
\begin{align*}
2 &= \rho\cos(\theta) = 2 \cos 0 +i2\sin(0) \\
-3 &= \rho\cos(\theta) = 3 \cos \pi + i3\sin(\pi) \\
4i &= \rho i\sin(\theta) =  \cos\dfrac{\pi}{2} +  i 4\sin\left(\dfrac{\pi}{2}\right)   \\
-5i &= \rho i\sin(\theta) =  \cos\dfrac{\pi}{2} +  i 5\sin\left(-\dfrac{\pi}{2}\right) \\
1+i &= \rho(\cos(\theta) + i\sin(\theta)) = \sqrt2\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)
\end{align*}
$$
****