---
title: Lagrangian Mechanics
prev1_title: Classical Mechanics
prev2_title: Physics
date: 2021-03-03
description: Lagrangian Mechanics
_previous: https://ailever.github.io/education/2020/05/30/Physics/
categories:
  - education
HL1: education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Physics.png
author_staff_member: anonym
---

<!-- Top Block -->
<div align="center" class="top_btn_box">
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Help:Displaying_a_formula'">Mathematical Formula</button>
  <button class="top_btn" type="button" onclick="location.href='#'">B</button>
  <button class="top_btn" type="button" onclick="location.href='#'">C</button>
</div>
<!-- Top Block -->


## Calculous of Variations
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
Maupertuis's principle of least action
$$
J[y] = \int_{x_{1}}^{x_{2}} f(y(x), \frac{dy(x)}{dx}, x) \, dx 
$$
$$
\delta J = \delta \int_{x_{1}}^{x_{2}} f(y,y_{x},x) \, dx  
$$

Restricting attention to functions f(x) within given path of $y$
$$J(\alpha) = \int_{x_{1}}^{x_{2}} f(y(x, \alpha), y_{x}(x, \alpha), x) \, dx$$
$$y(x, \alpha) = y(x, 0) + \eta(x) $$
$$\eta (x_{1}) = \eta (x_{2}) = 0$$


$$\left [ \frac{\partial J(\alpha)}{\partial \alpha} \right ]_{\alpha} = 0$$

Least action
$$\frac{\partial J(\alpha)}{\partial \alpha} = \int_{x_{1}}^{x_{2}} \left [ \frac{\partial f}{\partial y}\frac{\partial y}{\partial \alpha} + \frac{\partial f}{\partial y_{x}}\frac{\partial y_{x}}{\partial \alpha} \right ] \, dx = 0$$
$$\delta J = \int_{x_{1}}^{x_{2}} \left (  \frac{\partial f}{\partial y} - \frac{d}{dx}\frac{\partial f}{\partial y_{x}} \right ) \delta y \, dx = 0$$
$$\because \text{Stationary value of}\ J,\quad \left [ \frac{\partial J(\alpha)}{\partial \alpha} \right ]_{\alpha} = 0$$
<br><br></div>

### Euler equation
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\frac{\partial \mathcal{L}}{\partial x} - \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{x}} = 0 $$
<br><br></div>

#### Newton's equation of motion
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
Let say Lagrangian $\mathcal{L}$ is $T - V$, where $T$ is the total kinetic energy of given system, $V$ is the potential energy of the system.
$$\begin{align*}
\frac{\partial \mathcal{L}}{\partial q^{i}} &= 
  \frac{\partial}{\partial q^{i}} \left ( \frac{1}{2}{m\dot{q}^{i}}^{2} - V(q^{i})\right ) 
  = -\frac{\partial V(q^{i})}{\partial q^{i}} \\
\frac{\partial \mathcal{L}}{\partial \dot{q}^{i}} &= 
   \frac{\partial}{\partial \dot{q}^{i}} \left ( \frac{1}{2}{m\dot{q}^{i}}^{2} - V(q^{i})\right )
  = m\dot{q}^{i}\\
\end{align*}$$  

$$\therefore F=m\ddot{q}\quad \text{under conservative systems}$$

<br><br></div>

#### Maxwell Equation
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>

#### Schrodinger Equation
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>


## d'Alembert's Principle
### Virtual Displacement
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\vec{r}_{i}=\vec{r}_{i}(q_{1},q_{2},\cdots,\q_{n},t)$$
$$delta \vec{r}_{i} = \sum_{j} \frac{r_{i}}{q_{j}}\delta q_{j} + \left ( \frac{\partial \vec{r}_{i}}{\partial t} \delta t \right ) $$
<br><br></div>

### Principle of Virtual Work
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\sum \vec{F}_{i}^{(a)} \cdot \delta \vec{r} = 0 \quad \text{at equilibrium}$$
<br><br></div>

### Generalized Force
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$Q_{i} \equiv \sum_{j} \vec{F}_{j}\cdot \frac{\partial \vec{r}_{j}}{\partial q_{i}} $$
<br><br></div>

### d'Alembert's Principle
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\sum \left ( \vec{F}_{i}^{(a)} - \dot{\vec{p}}_{i} \right ) \cdot \delta \vec{r} = 0 \quad \text{at equilibrium}$$
<br><br></div>

### Euler equation by d'Alembert's Principle
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{q_{i}}} - \frac{\partial \mathcal{L}}{\partial q_{i}}= Q_{i} $$
<br><br></div>

<br><br><br>
## Legendre Transform
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\begin{align*}
  \mathcal{H} &= \sum_{i}\dot{q}_{i}p_{i} - \mathcal{L} \\
              &= T+V
\end{align*}$$  
<br><br></div>

### Hamiltonian Equation
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
  
<br><br></div>



<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<!-- Content Block -->

---

<!-- Reference Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='REF'>Reference</b>
<ol>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ol>
<ul>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ul>
</div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ol>
<ul>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ul>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-03-03-_PHY-cm-en-lagrangian-mechanics.md" target="_blank" style="color:white">Edit</a></span>
</div>
<!-- Bottom Block -->

<!-- Notice
# Mathematical Expression
- outline : $  $
- inline  : $$  $$

# Default Div Tag
- align : left, right, center
- font-size : xx-small, x-small, small, medium, large, x-large, xx-large
- font-weight : normal, bold
- color : red, orange, yellow, green, cyan, blue, purple, pink, white, gray, brown
- background-color : red, orange, yellow, green, cyan, blue, purple, pink, white, gray, brown

# Html Ref
- color code : https://htmlcolorcodes.com/
- tags : https://www.w3schools.com/tags/default.asp
- attributes : https://www.w3schools.com/tags/ref_attributes.asp
Notice -->


