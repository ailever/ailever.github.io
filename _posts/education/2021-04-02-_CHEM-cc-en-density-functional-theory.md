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
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Density_functional_theory'">Density Functional Theory</button>
  <button class="top_btn" type="button" style="background-color:blue;" onclick="location.href='https://ailever.github.io/education/2021/03/03/_PHY-qm-en-atomic-orbitals/'">Atomic Orbitals</button>
  <button class="top_btn" type="button" style="background-color:blue;" onclick="location.href='https://ailever.github.io/education/2021/04/02/_CHEM-pc-en-periodic-table/'">Periodic Table</button>
  <button class="top_btn" type="button" style="background-color:blue;" onclick="location.href='https://ailever.github.io/education/2021/04/02/_CHEM-ic-en-molecular-orbitals/'">Molecular Orbitals</button>
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
$$E[\Psi]=\frac{\left \langle\Psi|H|\Psi\right \rangle}{\left \langle\Psi|\Psi\right \rangle} \qquad \text{where} \left \langle \Psi|H|\Psi \right \rangle = \int {\Psi^{*}H\Psi}\, d\overrightarrow{x} $$  
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

Non-Classical Contribution(Self-Interaction correction) : Coulomb integrals and Exchange integrals
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
### The electron density
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The electron density
$$\rho(\overrightarrow{r}) = N \int \cdots \int {\left \vert \Psi(\overrightarrow{x_{1}},\overrightarrow{x_{2}},\cdots,\overrightarrow{x_{N}}) \right \vert^{2} } ,\ ds_{1}d\overrightarrow{x_{1}}d\overrightarrow{x_{2}} \cdots d\overrightarrow{x_{N}}$$

$$
\rho( \overrightarrow{r} \rightarrow \infty ) = 0 \qquad \int {\rho(\overrightarrow{r})} \, d\overrightarrow{r}= N 
$$

$$
\lim_{r_{i}A \to 0} {[\nabla_{r}+2Z_{A}]\overline{\rho}(\overrightarrow{r})} = 0  
$$

$$
\rho(\overrightarrow{r}) \sim e^{-2\sqrt{2I}\left \vert \overrightarrow{r} \right \vert}
$$
<br><br></div>
### The Thomas-Fermi model
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$
T_{TF}[\rho(\overrightarrow{r})] = \frac{3}{10}(3\pi^{2})^{2/3} \int \rho^{5/3}(\overrightarrow{r}) \, d\overrightarrow{r}  
$$

$$
E_{TF}[\rho(\overrightarrow{r})] = \frac{3}{10}(3\pi^{2})^{2/3} \int \rho^{5/3}(\overrightarrow{r}) \, d\overrightarrow{r} 
-Z \int {\frac{\rho(\overrightarrow{r})}{r}}\, d\overrightarrow{r}
+ \frac{1}{2} \iint \frac{\rho(\overrightarrow{r_{1}})\rho(\overrightarrow{r_{2}})}{r_{12}} \,d\overrightarrow{r_{1}} \,d\overrightarrow{r_{2}}
$$

<br><br></div>


<br><br><br>
## The Hohenberg-Kohn theorems
### The first Hohenberg-Kohn theorem
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The exact kinetic energy of a non-interacting reference system with the same density as the real
$$\begin{align*}
T_{S} &= -\frac{1}{2} \sum_{i}^{N} \left \langle \psi_{i} | \nabla^2 | \psi_{i} \right \rangle\\
\rho_{S}(\vec{r}) &= \sum_{i}^{N} \sum_{s} \left \vert \psi_{i}(\vec{r},s) \right \vert^{2} = \rho(\vec{r}) \\
\end{align*}$$

Separation of the functional $F[\rho]$
$$E[\rho] = E_{Ne}[\rho] + T[\rho] + E_{ee}[\rho] = \int {\rho(\vec{r})V_{Ne}(\vec{r})} \, d\vec{r} + F_{HK}[\rho]$$  
$$\color{red}{F_{HF}[\rho]} = \color{red}{T[\rho]} + E_{ee}[\rho]$$
$$E_{ee}[\rho] = \frac{1}{2} \iint {\frac{\rho(\vec{r_{1}})\rho(\vec{r_{2}})}{r_{12}}} \,d\vec{r_{1}} \,d\vec{r_{2}} + E_{ncl}
= J[\rho] + \color{red}{E_{ncl}[\rho]}$$
<br><br></div>

### The second Hohenberg-Kohn theorem
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$
E_{0} \le E[\tilde{\rho}] = T[\tilde{\rho}] + E_{Ne}[\tilde{\rho}] + E_{ee}[\tilde{\rho}]  
$$
   
<br><br></div>

<br><br><br>
## The Kohn-Sham approach
### The Kohn-Sham equations
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$F[\rho] = T_{S} + J[\rho] + E_{XC}[\rho]$$  
$$\begin{align*}
  T_{S} &= \frac{1}{2} \sum_{i}^{N} \left \langle \psi_{i} | \nabla^{2} |\psi_{i} \right \rangle \\
  E_{XC}[\rho] &\equiv (T[\rho] - T_{S}[\rho]) + (E_{ee}[\rho] - J[\rho]) \\
\end{align*}$$
  
The energy of the interacting system for uniquely determining the orbitals in our non-interacting reference system
$$\begin{align*}
E[\rho] &= T_{S} + J[\rho] +E_{XC}[\rho] + E_{Ne}[\rho] \\
&= T_{S} + \frac{1}{2} \iint \frac{\rho(\vec{r_{1}})\rho(\vec{r_{2}})}{r_{12}} \,d\vec{r_{1}} \,d\vec{r_{2}} + E_{XC}[\rho] + \int V_{Ne}\rho(\vec{r}) \, d\vec{r} \\
&= \frac{1}{2} \sum_{i}^{N} \left \langle \psi_{i} | \nabla^{2} |\psi_{i} \right \rangle
+ \frac{1}{2} \sum_{i}^{N} \sum_{j}^{N} \iint \left \vert \psi_{i}(\vec{r_{1}}) \right \vert^2 \frac{1}{r_{12}} \left \vert \psi_{j}(\vec{r_{2}}) \right \vert^2 \, d\vec{r_{1}} \,d\vec{r_{2}} \\
&\qquad + E_{XC}[\rho] - \sum_{i}^{N} \int \sum_{A}^{M} \frac{Z_{A}}{r_{1A}} \left \vert \psi_{i}(\vec{r_{1}}) \right \vert^2 \,d\vec{r_{1}}

\end{align*}$$

Kohn-Sham equations
$$
\left ( -\frac{1}{2}\nabla^{2} + \left [ \int {\frac{\rho(\vec{r_{2}})}{r_{12}}} \,d\vec{r_{2}} + V_{XC}(\vec{r_{1}}) - \sum_{A}^{M} {\frac{Z_{A}}{r_{1A}}} \right ] \right ) \psi_{i} = \left ( -\frac{1}{2}\nabla^{2} + V_{S}(\vec{r_{1}}) \right ) \psi_{i} = \epsilon_{i}\psi_{i}
$$

$$
V_{S}(\vec{r_{1}}) = \int \frac{\rho(\vec{r_{2}})}{r_{12}} \, d\vec{r_{2}} + V_{XC}(\vec{r_{1}}) - \sum_{A}^{M}\frac{Z_{A}}{r_{1A}}
$$

$$\text{constraint}\quad \left \langle \psi_{i} | \psi_{j}\right \rangle = \delta_{ij}$$
<br><br></div>

<br><br><br>
## The exchange-correlation functionals
### The local density approximation(LDA)
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$E_{XC}^{LDA}[\rho] = \int \rho(\vec{r})\epsilon_{XC}(\rho(\vec{r})) \, d\vec{r}$$
$$\begin{align*}
  \epsilon_{XC}(\rho(\vec{r})) &= \epsilon_{X}(\rho(\vec{r})) + \epsilon_{C}(\rho(\vec{r}))\\ 
  \epsilon_{X} &= -\frac{3}{4} \left ( \frac{3\rho(\vec{r})}{\pi} \right )^{1/3} \\ 
\end{align*}$$
<br><br></div>

### The generalized gradient approximation
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$E_{XC}^{GGA}[\rho_{\alpha}, \rho_{\beta}] = \int f(\rho_{\alpha}, \rho_{\beta}, \nabla_{\rho_{\alpha}}, \nabla_{\rho_{\beta}}) \, d\vec{r}$$  
<br><br></div>

### Hybrid functional
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$
E_{XC}^{hyb} = \alpha E_{X}^{KS} + (1-\alpha)E_{XC}^{GGA}
$$

<br><br></div>

<br><br><br>
## The basic machinary of DFT
### The LCAO Ansatz in the The Kohn-Sham equations
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The Kohn-Sham one-electron operator from Kohn-Sham equations
$$
\hat{f}^{KS}\psi_{i} = \epsilon_{i}\psi_{i}  
$$

$$
\left ( \int {\frac{\rho(\vec{r_{2}})}{r_{12}}} \,d\vec{r_{2}} + V_{XC}(\vec{r_{1}}) - \sum_{A}^{M} {\frac{Z_{A}}{r_{1A}}} \right ) \psi_{i} = \epsilon_{i}\psi_{i}
$$


K-S orbital
$$
\psi_{i} = \sum_{\mu=1}^{L} c_{\mu i}\eta_{\mu}
$$


Kohn-Sham matrix and overlap matrix
$$\begin{align*}
    F_{\mu \nu}^{KS} &= \int {\eta_{\mu} (\vec{r_{1}}) \hat{f}^{KS}(\vec{r_{1}}) \eta_{\nu}(\vec{r_{1}})
    } \, d\vec{r_{1}} \\
    S_{\mu \nu} &= \int {\eta_{\mu}(\vec{r_{1}})\eta_{\nu}(\vec{r_{1}})
    } \, d\vec{r_{1}}  \\
\end{align*}$$

Extended Kohn-Sham Operator
$$\begin{align*}
    \hat{F}_{\mu \nu}^{KS}
    &= h_{\mu\nu} \int {
        \eta_{\mu} (\vec{r_{1}}) \left ( 
            \int {
                \frac{\rho(\vec{r_{2}})}{r_{12}}
                } \, d\vec{r_{2}} 
            + V_{XC}(\vec{r_{1}})  
            \right )  \eta_{\nu} (\vec{r_{1}})
        } \, d\vec{r_{1}} \\
    
    &= \int {
        \eta_{\mu} (\vec{r_{1}}) \left ( 
            -\frac{1}{2} \nabla^{2}
            - \sum_{A}^{M} \frac{Z_{A}}{r_{1A}} 
            + \int {
                \frac{\rho(\vec{r_{2}})}{r_{12}}
                } \, d\vec{r_{2}} 
            + V_{XC}(\vec{r_{1}})  
            \right )  \eta_{\nu} (\vec{r_{1}})
        } \, d\vec{r_{1}} \\
    
\end{align*}$$


Charge density in the LCAO scheme
$$
\rho(\vec{r}) = \sum_{i}^{L}\left \vert \psi_{i}(\vec{r}) \right \vert^{2} = \sum_{\mu}^{L}\sum_{\nu}^{L}P_{\mu\nu}\eta_{\mu}(\vec{r})\eta_{\nu}(\vec{r})
$$

$$
P_{\mu\nu} = \sum_{i}^{N} c_{\mu i}c_{\nu i}
$$

Coulomb contribution and exchange-correlation and Hartree-Fock exchange integral
$$\begin{align*}
J_{\mu\nu} &= 
  \sum_{\lambda}^{L}\sum_{\sigma}^{L} P_{\lambda\sigma} \iint \eta_{\mu}(\vec{x_{1}})\eta_{\nu}(\vec{x_{1}}) \frac{1}{r_{12}} \eta_{\lambda}(\vec{x_{2}})\eta_{\sigma}(\vec{x_{2}}) \, d\vec{x_{1}}\,d\vec{x_{2}} \\

V_{\mu\nu}^{XC} &= \int \eta_{\mu}(\vec{r_{1}})V_{XC}(\vec{r_{1}})\eta_{\nu}(\vec{r_{1}})\,d\vec{r_{1}}\\

K_{\mu\nu} &= 
  \sum_{\lambda}^{L}\sum_{\sigma}^{L} P_{\lambda\sigma} \iint \eta_{\mu}(\vec{x_{1}})\eta_{\lambda}(\vec{x_{1}}) \frac{1}{r_{12}} \eta_{\nu}(\vec{x_{2}})\eta_{\sigma}(\vec{x_{2}}) \, d\vec{x_{1}}\,d\vec{x_{2}} \\
\end{align*}$$
<br><br></div>



### Basis sets

<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
Slater-Type Orbitals (STO)
$$\eta^{STO} = Nr^{n-1}e^{-\beta r}Y_{lm}(\theta, \phi)$$

Gaussian-Type Orbitals (GTO)
$$\eta^{GTO} = Nx^{l}y^{m}z^{b}e^{-\alpha r}$$

Contracted Gaussian Functions (CGF)
$$
\eta_{tau}^{CGF} = \sum_{a}^{A} d_{a\tau}\eta_{a}^{GTO}
$$
<br><br></div>
 
<br><br><br>
## DFT applications
### Applications in quantum chemistry
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
### Applications in solid state physics
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
### DFT in Molecular Electronics
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
  <li><a href="https://silo.tips/download/introduction-to-density-functional-theory">Introduction to Density Functional Theory(Juan Carlos Cuevas)</a></li>
  <li><a href="https://scifinder.cas.org">SciFinder - Chemical Abstracts Service</a></li>
  <li><a href="http://www.crystallography.net/cod/">Crystallography Open Database</a></li>
</ol>
<ul>
  <li><a href="https://link.springer.com/article/10.1007/s11224-020-01507-x">Computer-aided study of selective flavonoids against chikungunya virus replication using molecular docking and DFT-based approach</a></li>
</ul>
</div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-ab-initio-methods/">Ab initio methods</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-molecular-mechanics-and-dynamics/">Molecular Mechanics and Dynamics</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-quantum-chemistry-methods/">Quantum Chemistry Methods</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-qm-mm/">QM/MM : Quantum Mechanics/Molecular Mechanics</a></li>
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


