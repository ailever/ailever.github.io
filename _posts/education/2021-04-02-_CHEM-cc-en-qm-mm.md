---
title: QM/MM
prev1_title: Computational Chemistry
prev2_title: Chemistry
date: 2021-04-02
description: Quantum Mechanics/Molecular Mechanics 
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
  <button class="top_btn" type="button" style="background-color:blue;" onclick="location.href='https://ailever.github.io/education/2021/03/03/_PHY-qm-en-atomic-orbitals/'">Atomic Orbitals</button>
  <button class="top_btn" type="button" style="background-color:blue;" onclick="location.href='https://ailever.github.io/education/2021/04/02/_CHEM-pc-en-periodic-table/'">Periodic Table</button>
  <button class="top_btn" type="button" style="background-color:blue;" onclick="location.href='https://ailever.github.io/education/2021/04/02/_CHEM-ic-en-molecular-orbitals/'">Molecular Orbitals</button>
</div>
<!-- Top Block -->

## Combined QM/MM Modeling Methods
### Interactions in the QM/MM coupling
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$E_{total} = E_{QM} + E_{MM} + E_{QM/MM}$$
$$
E_{QM/MM} = E_{ES}(QM/MM) + E_{vdW}(QM/MM) + E_{bonded}(QM/MM)
$$
<br><br></div>

The effective Hamiltonian
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$H_{eff} = H_{QM} + H_{ES}(QM/MM)$$  
<br><br></div>

<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>

<br><br><br>
## Average Solvent Potential in Mean-Field Theory
### The mutual solute–solvent polarization
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The ASEP/MD Hamiltonian
$$
H = H_{QM} + H_{class} + H_{int}  
$$

The effective Schrodinger equation
$$
(H_{QM}+H_{int}) \left | \Psi \right \rangle = E \left | \Psi \right \rangle
$$

The interaction Hamiltonian associated to the electrostatic and van der Waals contributions
$$
H_{int} = H^{elect}_{int} + H^{vdw}_{int}
$$

The MFA electrostatic interaction(a statistical average over configurations)
$$
\left \langle H^{elect}_{int} \right \rangle = \int {\hat{\rho} \cdot \left \langle V_{S}(r) \right \rangle } \, dr
$$
- $\hat{\rho}$ : the solute charge density operator <br>
- $\left \langle V_{S}(r) \right \rangle$ : the average electrostatic potential by the solvent <br>

<br>
The effective Schrodinger equation considering the MFA energy
$$
(H_{QM} + \left \langle H_{int} \right \rangle) \left | \Psi \right \rangle = E \left | \Psi \right \rangle
$$

<br><br></div>
### Location of critical points on free energy surfaces
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The force on the Helmholtz free energy surface
$$
G = -k_{B}T\ln{Z_{NVT}}
$$
$$
\left \langle F(R) \right \rangle
= - \frac{\partial G(R)}{\partial R}
= - \left \langle \frac{\partial E}{\partial R} \right \rangle
= - \left \langle \frac{\partial E_{QM}}{\partial R} \right \rangle - \left \langle \frac{\partial E_{int}}{\partial R} \right \rangle
$$


<br><br></div>

### Calculation of free energy differences
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
Within the ASEP/MD methodology, the free energy difference in solution between two given states
$$
\Delta G_{s} = \Delta E_{solute} + \Delta G_{int} + \Delta ZPE_{solute}
$$
$$
\Delta E_{solute} = E_{B} - E_{A} = \left \langle \Psi_{B} | H^{0}_{B} | \Psi_{B} \right \rangle - \left \langle \Psi_{A} | H^{0}_{A} | \Psi_{A} \right \rangle 
$$
  
<br><br></div>



<br><br><br>
## The Electronic Structure
### Statistical mechanics sampling for many-body interacting systems in condensed phases
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The Hamiltonian of the system
$$H = -\frac{1}{2}\sum_{A=1}^{M}{\frac{1}{M_{A}}\nabla^{2}_{M}} -\frac{1}{2}\sum_{i=1}^{N}{\nabla^{2}_{N}} + V(\vec{r_{i}};\vec{R_{A}},\vec{X})$$ 
<br><br></div>

### Electronic spectra in QM/MM
#### A QM solute(M) and MM solvent molecules(I) system 
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The QM/MM coupling schemes
$$E_{QM/MM}[M] = E[M] = E_{QM}(M) + E_{MM}(\{ I \}) + E_{int}$$
$$E_{QM}(M) = \left \langle \Psi(\vec{r};\vec{R};\vec{X})| H | \Psi(\vec{r};\vec{R};\vec{X}) \right \rangle$$

Mechanical coupling
$$E_{int}(el) = \sum_{A\alpha}\frac{q_{A}q_{\alpha}}{r_{A\alpha}} $$  

Electrostatic coupling : Mechanical coupling with QM polarization considering potential for the solvent
$$E_{int}(el) = \left \langle \Psi(r_{i};R_{A};q_{\alpha}) | \sum_{\alpha}\frac{q_{\alpha}}{r_{i\alpha}} | \Psi(r_{i};R_{A};q_{\alpha}) \right \rangle + \sum_{A\alpha}\frac{q_{A}q_{\alpha}}{r_{A\alpha}} $$  

The wavefunctions for both ground and excited states
$$\begin{align*}
\Psi^{0} &= \Phi^{0}_{(0)} + \Phi^{0}_{(1)} + \Phi^{0}_{(2)} + \cdots \\
\Psi^{*} &= \Phi^{*}_{(0)} + \Phi^{*}_{(1)} + \Phi^{*}_{(2)} + \cdots \\
\end{align*}$$

QM Expectation for the excitation energy
$$\begin{align*}
\omega_{(0)} &= \left \langle \Phi^{*}_{(0)} | H | \Phi^{*}_{(0)} \right \rangle - \left \langle \Phi^{0}_{(0)} | H | \Phi^{0}_{(0)} \right \rangle \\
\omega_{(1)} &= \left \langle \Phi^{*}_{(0)} | \frac{q_{\alpha}}{r_{i\alpha}} | \Phi^{*}_{(0)} \right \rangle - \left \langle \Phi^{0}_{(0)} | \frac{q_{\alpha}}{r_{i\alpha}} | \Phi^{0}_{(0)} \right \rangle \\
\omega_{(2)} &= \left \langle \Phi^{*}_{(0)} | \frac{q_{\alpha}}{r_{i\alpha}} | \Phi^{*}_{(1)} \right \rangle - \left \langle \Phi^{0}_{(0)} | \frac{q_{\alpha}}{r_{i\alpha}} | \Phi^{0}_{(1)} \right \rangle \\
&\vdots \\
\omega_{(n)} &= \left \langle \Phi^{*}_{(0)} | \frac{q_{\alpha}}{r_{i\alpha}} | \Phi^{*}_{(n-1)} \right \rangle - \left \langle \Phi^{0}_{(0)} | \frac{q_{\alpha}}{r_{i\alpha}} | \Phi^{0}_{(n-1)} \right \rangle \\
\end{align*}$$
<br><br></div>

#### Many body system expansion
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The QM/MM coupling schemes  
$$E_{QM/MM} = E[M] = \left \langle \Psi | H+\sum_{\alpha}\frac{q_{\alpha}}{r_{i}r_{\alpha}} | \Psi \right \rangle + E_{MM}(solvent) + E_{int}(vdW) $$

The total system energy expression making a distinction between the solute M and the solvent molecules {I}
$$E = E[M] + \sum_{I \neq M}{E[I]} + \sum_{I \neq M}{(E[MI]-E[M]-E[I])} + \sum_{I>J\ \& \ i,j \neq M}{(E[IJ]-E[I]-E[J])}$$

The energy difference between the ground($M^{0}$) and a specific excited($M^{*}$) state
$$\begin{align*}
\Delta E = &E[M^{*}] - E[M^{0}] \\
&+ \sum_{I \neq M}{\Delta E[I]} \\
&+ \sum_{I \neq M}{(E[M^{*}I]-E[M^{0}I] -E[M^{*}]+E[M^{0}] -\Delta E[I])} \\
&+ \sum_{I>J\ \& \ i,j \neq M}{(\Delta E[IJ] -\Delta E[I] -\Delta E[J])} \\
\end{align*}$$
$$\text{where } \Delta E[I] = E[I]_{M^{*}} - E[I]_{M^{0}}$$

<br><br></div>

####  QM methods for the calculation of electronic spectra
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<br><br></div>

## SCC-DFTB : The self-consistent charge-density functional tight-binding method
### Density functional tight-binding method
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<br><br></div>
### Self-consistent charge–density functional tight-binding
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<br><br></div>
### A posteriori treatment for London dispersion in SCC–DFTB
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<br><br></div>

<br><br><br>
## The Effect of the Protein Environment
### Born–Oppenheimer approximation
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<br><br></div>
### Conical intersections
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<br><br></div>
### Excited state molecular dynamics
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<br><br></div>
### Diabatic surface hopping
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<br><br></div>
### Mixed quantum classical molecular dynamics
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
The potential energy of the system by MM force-field
$$
V_{MM} = \sum_{i}^{N_{bonds}}V^{bond}_{i}
+ \sum_{j}^{N_{angles}} V^{angle}_{j}
+ \sum_{l}^{N_{torsions}} V^{torsion}_{l}
+ \sum_{i}^{N_{MM}}\sum_{j>i}^{N_{MM}} V^{Coulomb}_{ij}
+ \sum_{i}^{N_{MM}}\sum_{j>i}^{N_{MM}} V^{LJ}_{ij}
$$  

<br><br></div>

<br><br><br>
## QM/MM Methodology and Applications
Energy Expression Schemes
- Subtractive scheme
- Additive scheme

### Free Energy Perturbation(FEP)
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\Delta F(A\rightarrow B) = -k_{B}T\ln{\left < e^{-\frac{E_{B}-E_{A}}{k_{B}T}} \right >_{A}}$$
<br><br></div>

### Thermodynamic Integration(TI)
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
Potential energy function
$$U(\lambda) = \lambda U_{A} + (1-\lambda)U_{B}$$
The partition function of the system in the canonical ensemble
$$Q(N,V,T,\lambda) = \sum_{s} e^{-\frac{-U_{s}(\lambda)}{k_{B}T}}$$
The free energy of this system
$$F(N,V,T,\lambda) = -k_{B}T\ln{Q(N,V,T,\lambda)}$$
The ensemble average of the derivative of potential energy with respect to $\lambda$
$$\Delta F(A\rightarrow B) = \int_{0}^{1} {\frac{\partial F(\lambda)}{\partial \lambda}}\, d\lambda = \int_{0}^{1} {\frac{\partial U(\lambda)}{\partial \lambda}}\, d\lambda$$

<br><br></div>



### Enhanced sampling
- Multiple time-step sampling
- Umbrella sampling
- Replica Exchange
- Reaction coordinate-driven methods
- Transition path sampling





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
  <li><a href="http://www.fhi-berlin.mpg.de/~luca/Course_TU/">Theoretical Concepts for Chemical Energy Conversion</a></li>
  <li><a href="#"></a></li>
</ol>
<ul>
  <li><a href="https://www.elsevier.com/books/combining-quantum-mechanics-and-molecular-mechanics-some-recent-progresses-in-qm-mm-methods/sabin/978-0-12-380898-1">(2010) Combining Quantum Mechanics and Molecular Mechanics. Some Recent Progresses in QM/MM Methods</a></li>
  <li><a href="https://www.wiley.com/en-sg/Introduction+to+Computational+Chemistry%2C+3rd+Edition-p-9781118825990">(2016) Introduction to Computational Chemistry, 3rd Edition</a></li>
  <li><a href="#"></a></li>
  <li><a href="#"></a></li>
</ul>
</div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-ab-initio-methods/">Ab initio methods</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-density-functional-theory/">Density Functional Theory</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-molecular-mechanics-and-dynamics/">Molecular Mechanics and Dynamics</a></li>
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-quantum-chemistry-methods/">Quantum Chemistry Methods</a></li>
</ol>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-04-02-_CHEM-cc-en-qm-mm.md" target="_blank" style="color:white">Edit</a></span>
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


