# Machine Learning

## Notes Class 2021-2022

### Prerequisites

---

- Linear agebra
- Calculus
- Probability
- Statitics
- Programming skills
  
### Books

---

- the elements of statistical Learning
- MLCC videos
- Stanford CS229 Machine Learning

### Machine Learning

---
What is machine learning?

ML Is the field that allows to infer knowledge from data. So data is a key element in machine learning.

this is a basic ML course, and provides an introduction to the fundamental method at the core of modern machine learning
it covers theoretical foundations as well as essential algorithms for machine learning and practical lab lessons with python and jupyter notebooks.

what we use ML for:

- intelligent systems
  - Artificial Intellicence vs Human intellicence
    - research is trying to reducing the gap
  - system that react to environment and take decisions
  - systems that organize in a " smart way " informations

How we can measure intelligence?

- Turing Test for AI
- QI test for Humans

**Def:** Machine Learning is trained of data instead of being programmed

### Regression
---


we represent a problem with pairs of input observations and outputs.

$$ (x_1, y_1),...,(x_n,y_n) $$

I can try to derive a mathematical relation in this way $$y_i \approx f(x_i)$$

- the function should be able to behave "nicely" on the data we provide.
- when I have a new input this function should behave "nicely" this is called *generalization* property

it refers to a supervised learning problem meaning that we have a set of known data.


### Classification problem
---
What we want to do is what is the best way to discriminate between classes.

$$ (x_1,y_1),...,(x_n,y_n) $$

$$ x_i \in \mathbb{R^p} \text{ and } y_i \mathbb{Y} = \{-1,1\}, i=1,..,n $$

$$\begin{bmatrix} 
  x_{11}&x_{12}&x_{13}&.&.&.&.&x_{1p}\\
  .&.&.&.&.&.&.&.\\
  .&.&.&.&.&.&.&.\\
  .&.&.&.&.&.&.&.\\
 \end{bmatrix} $$
$$\begin{bmatrix} x_{11}&x_{12}&x_{13}&.&.&.&.&x_{1n} \end{bmatrix} $$
