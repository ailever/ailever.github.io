---
title: Molecular Mechanics and Dynamics
prev1_title: Computational Chemistry
prev2_title: Chemistry
date: 2021-04-02
description: Molecular Mechanics and Dynamics
_previous: https://ailever.github.io/education/2020/05/30/Chemistry/
categories:
  - education
HL1: education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Chemistry.png
author_staff_member: anonym
---

<!-- Top Block -->
<div align="center" class="top_btn_box">
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Help:Displaying_a_formula'">Mathematical Formula</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Force_field_(chemistry)'">Force-Field</button>
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Morse_potential'">Morse potential</button>
  <button class="top_btn" type="button" style="background-color:blue;" onclick="location.href='https://ailever.github.io/education/2021/03/03/_PHY-qm-en-atomic-orbitals/'">Atomic Orbitals</button>
  <button class="top_btn" type="button" style="background-color:blue;" onclick="location.href='https://ailever.github.io/education/2021/04/02/_CHEM-pc-en-periodic-table/'">Periodic Table</button>
  <button class="top_btn" type="button" style="background-color:blue;" onclick="location.href='https://ailever.github.io/education/2021/04/02/_CHEM-ic-en-molecular-orbitals/'">Molecular Orbitals</button>
</div>
<!-- Top Block -->

## Basic Molecular Dynamics
- Key Factors : The bond lengths, bond dihedral angles, bond valence angles, and non-bonded interactions like van der Waals and electrostatic interactions contribute to the total energy of the systems
- Various Methods : Periodic Boundary Conditions, Ewald Summation Techniques, Particle Mesh Ewald Method, Thermostats in MD, Solvent Models, Energy-Minimization Methods in MD Simulations

### Verlet algorithm
From the Newton's equation for N-body problem
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$F_{i}=m_{i}a_{i}$$
$$F_{i}=-\frac{\partial \mathcal{V}(r_{1},r_{2},\cdots,r_{N} )}{\partial r_{i}}$$

Numerically approach 
$$\begin{align*}
  x(t+\Delta t) &= x(t) +\dot{x}(t)\Delta t + \frac{1}{2}\ddot{x}(t)\Delta t^{2} + \frac{1}{6}\dddot{x}(t)\Delta t^{3} + \frac{1}{24}\ddddot{x}(t)\Delta t^{4} + \cdots \\
  x(t-\Delta t) &= x(t) -\dot{x}(t)\Delta t + \frac{1}{2}\ddot{x}(t)\Delta t^{2} - \frac{1}{6}\dddot{x}(t)\Delta t^{3} + \frac{1}{24}\ddddot{x}(t)\Delta t^{4} + \cdots \\  
\end{align*}$$

$$
\therefore x(t+\Delta t) = 2x(t) - x(t-\Delta t) + \ddot{x}\Delta t^{2} + \mathcal{O}(\Delta t^{4})  
$$
<br><br></div>

### Shadow Trajectory
- Molecular Chaos : Lyapunov instability

Lagrangian Classical Mechanics
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$J=\int_{t_{b}}^{t_{e}} \mathcal{L} dt $$
$$\mathcal{L} = \mathcal{L}(\dot{r}, r) = \sum_{i=1}^{N} \frac{1}{2}m_{i}\dot{r}_{i}^{2} - \mathcal{V}(r_{1},r_{2},\cdots,r_{N})$$
<br><br></div>

### Monte Carlo (MC) simulation
### Langevin dynamics

<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<br><br></div>

## Functional Form in Molecular System
![image](https://user-images.githubusercontent.com/52376448/114148491-c832b100-9954-11eb-8102-a0bd892c0d16.png)
[REF|<a href="#REF">1</a>]
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\begin{align*}
E & = {\color{red}{E_{covalent}}} + {\color{blue}{E_{noncovalent}}} \\
& = {\color{red}{E_{bond}}} + {\color{red}{E_{angle}}} + {\color{red}{E_{dihedral}}} + {\color{blue}{E_{electrostatic}}} + {\color{blue}{E_{van der Waals}}} \\
\end{align*}$$

</div>
- Force Fields : AMBER, GROMOS, and CHARMM

<br><br><br>
## Polarizable Force Fields
### AMOEBA Polarizable Potential Energy Model
The AMOEBA potential function
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\mathcal{V} = \mathcal{V}_{bond} + \mathcal{V}_{angle} + \mathcal{V}_{b\theta} + \mathcal{V}_{oop} + \mathcal{V}_{torsion} + \mathcal{V}_{vdW} + \mathcal{V}_{e}^{perm} + \mathcal{V}_{e}^{ind}$$  
<br><br></div>
Energy by empirical functions
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\begin{align*}
  \mathcal{V}_{bond} &= K_{b}(b-b_{0})^{2} \left [ 1-2.55(b-b_{0})+3.793125(b-b_{0})^{2} \right ] \\
  \mathcal{V}_{angle} &= K_{b}(b-b_{0})^{2} \left [ 
  1-0.014(\theta-\theta_{0}) 
  + 5.6\times 10^{-5}(\theta-\theta_{0})^{2} 
  - 7.0 \times 10^{-7} (\theta - \theta_{0})^{3} 
  + 2.2 \times 10^{-8} (\theta-\theta_{0})^{4} \right ] \\ 
  \mathcal{V}_{b\theta} &= k_{b\theta}\left [ (b-b_{0}) - (b^{\prime} - b^{\prime}_{\theta} ) \right ] (\theta - \theta_{0}) \\ 
\end{align*}$$

Energy by Wilson–Decius–Cross function<br>
$
  \mathcal{V}_{oop} = k_{\chi} \chi^{2}
$<br><br>

Bell torsion Energy<br>
$
\mathcal{V}_{torsion} = \sum_{n} {K_{n\phi}[1+cos(n\phi \pm \delta)]}
$<br><br>

The pairwise additive vdW interaction<br>
$
\mathcal{V}_{vdW}(ij) = \epsilon_{ij} + \left ( \frac{1.07}{\varrho_{ij} + 0.07} \right )^{7} \left ( \frac{1.12}{\varrho_{ij}^{7}+0.12} -2 \right )
$<br><br>

Permanent Electrostatic Interactions in Cartesian polytensor formalism<br>
$
\mathcal{V}_{e}^{perm} = 
\begin{bmatrix}
q_{i} &  \\
d_{ix} &  \\
d_{iy} & \\
d_{iz} & \\
Q_{ixx} & \\
\vdots & 
\end{bmatrix}^{t}

\begin{bmatrix}
1                               & \frac{\partial}{\partial x_{j}}                    & \frac{\partial}{\partial y_{j}} & \frac{\partial}{\partial z_{j}} & \cdots \\
\frac{\partial}{\partial x_{i}} & \frac{\partial^{2}}{\partial x_{i} \partial x_{j}} & \frac{\partial^{2}}{\partial x_{i} \partial y_{j}} & \frac{\partial^{2}}{\partial x_{i} \partial z_{j}} & \cdots \\
\frac{\partial}{\partial y_{i}} & \frac{\partial^{2}}{\partial y_{i} \partial x_{j}} & \frac{\partial^{2}}{\partial y_{i} \partial y_{j}} & \frac{\partial^{2}}{\partial x_{i} \partial z_{j}} & \cdots \\
\frac{\partial}{\partial z_{i}} & \frac{\partial^{2}}{\partial z_{i} \partial x_{j}} & \frac{\partial^{2}}{\partial z_{i} \partial y_{j}} & \frac{\partial^{2}}{\partial x_{i} \partial z_{j}} & \cdots \\
\vdots                          & \vdots                                             & \vdots & \vdots & \ddots \\
\end{bmatrix}

\left ( \frac{1}{r_{ji}} \right )

\begin{bmatrix}
q_{j} &  \\
d_{jx} &  \\
d_{jy} & \\
d_{jz} & \\
Q_{jxx} & \\
\vdots & 
\end{bmatrix}

$<br><br>

Polarization Energy<br>
$
\mathcal{V}_{e}^{ind} = -\frac{1}{2} \sum_{i} \alpha_{i} \left ( \sum_{j \ne i} T^{1}_{ij}M_{j} - \sum_{k \ne i} T^{11}_{ik}\mu_{k} \right )^{T}E_{i}
$<br><br>

<br><br></div>




<br><br><br>
## Dynamics in Fluid System

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
  <li><a href="https://en.wikipedia.org/wiki/Force_field_(chemistry)">Force Field</a></li>
  <li><a href="http://www.chem.cmu.edu/courses/09-560/docs/msi/ffbsim/B_AtomTypes.html">Force-Field Terms and Atom Type</a></li>
  <li></li>
  <li></li>
</ol>
<ul>
  <li><a href="https://www.cambridge.org/core/books/nonequilibrium-molecular-dynamics/7F7B15A46CD6D0CD7C2BE3452C98D662">(2017) Nonequilibrium Molecular Dynamics, Theory, Algorithms and Applications</a></li>
</ul>
</div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li><a href="https://ailever.github.io/education/2021/03/03/_PHY-cm-en-lagrangian-mechanics/">[Physics] Lagrangian Mechanics</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-ab-initio-methods/">[Chemistry] Ab initio methods</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-density-functional-theory/">[Chemistry] Density Functional Theory</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-quantum-chemistry-methods/">[Chemistry] Quantum Chemistry Methods</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-qm-mm/">[Chemistry] QM/MM : Quantum Mechanics/Molecular Mechanics</a></li>
</ol>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-04-02-_CHEM-cc-en-molecular-mechanics-and-dynamics.md" target="_blank" style="color:white">Edit</a></span>
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


