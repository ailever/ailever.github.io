---
title: Density Functional Theory
prev1_title: Computational Chemistry
prev2_title: Chemistry
date: 2021-04-02
description: Density Functional Theory
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
  <button class="top_btn" type="button" onclick="location.href='#'">B</button>
  <button class="top_btn" type="button" onclick="location.href='#'">C</button>
</div>
<!-- Top Block -->

## Elementary quantum mechanics
### The Schrodinger equation
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The Schrodinger equation
$$H\Psi_{i} = E_{i}\Psi_{i}$$
  
The Hamiltonian for a system consisting of $M$ nuclei and $N$ electrons  
$$H = -\frac{1}{2} \sum_{i=1}^{N} {\nabla^{2}_{i}}
-\frac{1}{2} \sum_{A=1}^{M} {\frac{1}{M_{A}}\nabla^{2}_{A}}
-\sum_{i=1}^{N} \sum_{A=1}^{M} {\frac{Z_{A}}{r_{iA}}}
+ \sum_{i=1}^{N} \sum_{j>i}^{N} {\frac{1}{r_{ij}}}
+ \sum_{A=1}^{M} \sum_{B>A}^{M} {\frac{Z_{A}Z_{B}}{R_{AB}}}$$

Born-Oppenheimer approximation
$$H_{elec}\Psi_{elec} = E_{elec}\Psi_{elec}$$
$$H_{elec} = -\frac{1}{2} \sum_{i=1}^{N} {\nabla^{2}_{i}}
-\sum_{i=1}^{N} \sum_{A=1}^{M} {\frac{Z_{A}}{r_{iA}}}
+ \sum_{i=1}^{N} \sum_{j>i}^{N} {\frac{1}{r_{ij}}}$$
$$E_{tot}=E_{elec}+E_{nuc}\qquad \text{where } E_{nuc}=\sum_{A=1}^{M}\sum_{B>A}^{M}\frac{Z_{A}Z_{B}}{R_{AB}}$$
<br><br></div>

### The variational principle for the ground state
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$E[\Psi]=\frac{\left \langle\Psi|H|\Psi\right \rangle}{\left \langle\Psi|\Psi\right \rangle} \qquad \text{where} \left \langle \Psi|H|\Psi \right \rangle = \int {\Psi^{*}H\Psi},\ d\overrightarrow{x} $$  
$$E_{0}=\min_{\Psi \rightarrow N}{E[\Psi]} = \min_{\Psi \rightarrow N}{\left \langle | T + V_{Ne} + V_{ee} | \right \rangle}$$
<br><br></div>

### The Hartree-Fock approximation
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The Slater determinant  
$$\Psi_{0} \approx \Psi_{HF} = \frac{1}{\sqrt{N!}} 
\begin{vmatrix}
\psi_{1}(\overrightarrow{x_{1}}) & \psi_{2}(\overrightarrow{x_{1}}) & \cdots & \psi_{N}(\overrightarrow{x_{1}})\\
\psi_{1}(\overrightarrow{x_{2}}) & \psi_{2}(\overrightarrow{x_{2}}) & \cdots & \psi_{N}(\overrightarrow{x_{2}}) \\
\vdots & \vdots & & \vdots \\
\psi_{1}(\overrightarrow{x_{N}}) & \psi_{2}(\overrightarrow{x_{N}}) & \cdots & \psi_{N}(\overrightarrow{x_{N}}) \\
\end{vmatrix}
$$
  
The Hartree-Fock approximation  
$$
E_{HF}=min_{\Psi_{HF}\rightarrow N}E[\Psi_{HF}]
$$
$$
E_{HF} = \left \langle \Psi_{HF} | H | \Psi_{HF} \right \rangle = \sum_{i=1}^{N} {H_{i}} + \frac{1}{2} \sum_{i,j=1}^{N} {(J_{ij}-K_{ij})}
$$
$$
H_{i} \equiv \int {\psi^{*}_{i}(\overrightarrow{x})[-\frac{1}{2}\nabla^{2}- V_{ext}(\overrightarrow{x})]\psi_{i}(\overrightarrow{x})} \, d\overrightarrow{x}
$$

Coulomb integrals and Exchange integrals
$$\begin{align*}
J_{ij} &= \iint \psi_{i}(\overrightarrow{x_{1}}) \psi^{*}_{i}(\overrightarrow{x_{1}}) \frac{1}{r_{12}} \psi_{j}^{*}(\overrightarrow{x_{2}}) \psi_{j}(\overrightarrow{x_{2}}) \, d\overrightarrow{x_{1}} \, d\overrightarrow{x_{2}} \\
K_{ij} &= \iint \psi_{i}^{*}(\overrightarrow{x_{1}}) \psi_{j}(\overrightarrow{x_{1}}) \frac{1}{r_{12}} \psi_{i}(\overrightarrow{x_{2}}) \psi_{j}^{*}(\overrightarrow{x_{1}}) \, d\overrightarrow{x_{1}} \, d\overrightarrow{x_{2}}\\
\end{align*}$$
$$
J_{ij} \ge K_{ij} \ge 0
$$

The minimization of the energy functional with the normalization conditions
$$
\int {\psi_{i}^{*}(\overrightarrow{x})\psi_{j}(\overrightarrow{x})} \, d\overrightarrow{x} = \delta_{ij}
$$

The Hartree-Fock differential equations
$$
f\psi_{i} = \epsilon_{i}\psi_{i}
$$
$$
f = -\frac{1}{2}\nabla^{2}_{i} - \sum_{A}^{M} {\frac{Z_{A}}{r_{iA}}} + V_{HF}(i)
$$

Hartree-Fock potential
$$\begin{align*}
V_{HF}(\overrightarrow{x_{1}}) &= \sum_{j}^{N} {(J_{j}(\overrightarrow{x_{1}})-K_{j}(\overrightarrow{x_{1}}))} \\
J_{j}(\overrightarrow{x_{1}}) &= \int \left \vert \psi_{j}(\overrightarrow{x_{2}}) \right \vert^{2} \frac{1}{r_{12}} \, d\overrightarrow{x_{2}} \\
K_{j}(\overrightarrow{x_{1}}) \psi_{i}(\overrightarrow{x_{1}}) &= \int \psi_{j}^{*}(\overrightarrow{x_{2}}) \frac{1}{r_{12}} \psi_{i}(\overrightarrow{x_{2}}) \, d\overrightarrow{x_{2}} \psi_{j}(\overrightarrow{x_{1}}) \\
\end{align*}$$

<br><br></div>


<br><br><br>
## Early density functional theories
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>

<br><br><br>
## The Hohenberg-Kohn theorems
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>

<br><br><br>
## The Kohn-Sham approach
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>

<br><br><br>
## The exchange-correlation functionals
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>

<br><br><br>
## The basic machinary of DFT
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>



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
  <li><a href="https://en.wikipedia.org/wiki/List_of_quantum_chemistry_and_solid-state_physics_software">List of quantum chemistry and solid state physics software</a></li>
  <li><a href="https://www.ksc.re.kr/kor/index/main">Korea Supercomputing Center</a></li>
  <li><a href="https://www.quantum-espresso.org/">Quantum Espresso</a></li>
  <li><a href="http://www.calypso.cn/">CALYPSO</a></li>
</ol>
<ul>
  <li><a href="https://link.springer.com/article/10.1007/s11224-020-01507-x">Computer-aided study of selective flavonoids against chikungunya virus replication using molecular docking and DFT-based approach</a></li>
  <li><a href="https://scifinder.cas.org">SciFinder - Chemical Abstracts Service</a></li>
  <li><a href="http://www.crystallography.net/cod/">Crystallography Open Database</a></li>
</ul>
</div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-qm-mm/">QM/MM : Quantum Mechanics/Molecular Mechanics</a></li>
  <li><a href="#"></a></li>
</ol>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-04-02-_CHEM-cc-en-density-functional-theory.md" target="_blank" style="color:white">Edit</a></span>
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


