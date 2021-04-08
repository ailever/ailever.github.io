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
  <button class="top_btn" type="button" onclick="location.href='#'">A</button>
  <button class="top_btn" type="button" onclick="location.href='#'">B</button>
  <button class="top_btn" type="button" onclick="location.href='#'">C</button>
</div>
<!-- Top Block -->

## QM/MM Methodology and Applications
Energy Expression Schemes
- Subtractive scheme
- Additive scheme

### Free Energy Perturbation(FEP)
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$\Delta F_{AB} = -k_{B}T\ln{\left < e^{-\frac{E_{B}-E_{A}}{k_{B}T}} \right >_{A}}$$
Ensemble average of a function
<br><br></div>


## Thermodynamic Integration(TI)
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



- Implementing Quantum Mechanics into Molecular Mechanics—Combined QM/MM Modeling Methods
- Extending the Range of Computational Spectroscopy by QM/MM Approaches: Time-Dependent and Time-Independent Routes
- Use of the Average Solvent Potential Approach in the Study of Solvent Effects
- QM/MM Approaches to the Electronic Spectra of Hydrogen-Bonding Systems with Connection to Many-Body Decomposition Schemes
- Molecular Dynamics of Polypeptides and Their Inclusion Compounds with b-Cyclodextrin in Aqueous Solution Using DC–SCC–DFTB/UFF Approach
- Computer Simulations of Photobiological Processes: The Effect of the Protein Environment
- Ab Initio Quantum Mechanical Charge Field Molecular Dynamics—A Nonparametrized First-Principle Approach to Liquids and Solutions
- Applications of Mixed-Quantum/Classical Trajectories to the Study of Nuclear Quantum Effects in Chemical Reactions and Vibrational Relaxation Processes
- Development of a Quantum Chemical Method Combined with a Theory of Solutions—Free-Energy Calculation for Chemical Reactions by Condensed Phase Simulations



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


