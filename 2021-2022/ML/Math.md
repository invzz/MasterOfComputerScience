# Formal Supervised learning

---

We call our collected data the  **Training set**

The Training set is a collection of pair $S_n = \{(x_i,y_i),...,(x_n,y_n)\}$
It follows that $S_n \subseteq X\times Y$

A $(x,y)$ pair is called **sample**

*Observation* both $x$ vector and $y$ vector can have any dimension we want
For instance :

- Scalar regression
- Vectorial regression
- Binary classification
- Multiclass classification
  
---
**The goal** of superviesed learning is to learn a function $f:X \rightarrow Y$ such that $f(x_i)\approx y_i$ where $i = 1,.., n$

if i provide a new input, our learned function should provide the correct value in the output space $f(x_{new}) \approx y_{new}$

---

**Assumption 1** The generated input/data pairs have been generated accordint to a (joint) probability distribution $p(x,y)$ which is *fixed* but *unknown*. All the samples are assumed to be indipendent and identically distributed *iid*.

---

**Assumption 2** $p(x,y)$ can be factorized $p(x,y)=p(x)\cdot p(y|x)$. This is reminiscent of Bayes Theorem

---

**Loss / risk Function** : the loss function is a function we use to evaluate how much we loos if instead of using the real output $y_{i}$ we use our target function $f(x_i)$ so the loss function is defined usually this way: $l : Y \times Y \rightarrow \mathbb{R}^+$

**example** Square loss: $l(f(x_i), y_i) = (f(x_i) - y_i)^2$

We are happy when the loss function has "Low values" as close to 0 as we can!

---

**Expected loss / Expected risk** $$\Epsilon(f)=\mathbb{E[l(f(x),y)]}=\int_{X \times Y}l(f(x),y)p(x,y)dxdy$$

Given a loss function $f$, the input/output relationship $f : X \rightarrow Y $ is the one minimizing the expected risk

$$ f^*=argmin(E(f)) $$ where $$ f \in \mathcal{F} $$which is the set of all possible target function.

---

**There is a problem** $p(x,y)$ is by assumption Unknown!

For this reason we have to move from expected risk to empirical risk!

---
**Learing algorithm** A learning algorithm allows you to go from $S_n$ (the training set) to $f_n$ (the function we are looking for)

**observation** both training set and target function are dependent on data $n$.

---
our goal is to have a function that have $E(f_n)\approx E(f^*)$

**Empirical risk/loss**  if $n$ is the number of samples:

$$
E(f) =  \dfrac{1}{n}\sum_{i=1}^nl(y_i,f(x_i))
$$

where $(x_i,y_i) \in S_n$

---

**Consistency** $$\lim_{n\to\infty}\mathbb{E}[E(f_n) - E(f^*)] = 0$$