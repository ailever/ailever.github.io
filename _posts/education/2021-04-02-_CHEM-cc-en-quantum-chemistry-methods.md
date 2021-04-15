---
title: Quantum Chemistry Methods
prev1_title: Computational Chemistry
prev2_title: Chemistry
date: 2021-04-02
description: Quantum Chemistry Methods
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

## Molecular Quantum Mechanics
- Valence Bond Theory : Bond Length, Bond Strength, Bonding Angle
- Molecular Orbital theory(LCAO-MO)

### Born-Oppenheimer Approximation
#### Hydrogen-Molecule
- parahydrogen, orthohydrogen

![image](https://user-images.githubusercontent.com/52376448/114892305-9aafa100-9e47-11eb-8fea-c66066ecfcb2.png)
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$H_{H_{2}}\Psi_{H_{2}} = E_{H_{2}}\Psi_{H_{2}}$$

Hamiltonian
$$\begin{align*}
H_{H_{2}} &= -\frac{\hbar^2}{2M_{N}}(\nabla^{2}_{A} + \nabla^{2}_{B}) 
-\frac{\hbar^2}{2m_{e}}(\nabla^{2}_{1} + \nabla^{2}_{2}) - \frac{e^{2}}{4\pi\epsilon_{0}}
\left (  
\frac{1}{r_{1A}} + \frac{1}{r_{1B}} + \frac{1}{r_{2A}} + \frac{1}{r_{2B}} -\frac{1}{r_{12}} - \frac{1}{R_{AB}}
\right ) \\

&\approx -\frac{\hbar^2}{2m_{e}}(\nabla^{2}_{1} + \nabla^{2}_{2}) - \frac{e^{2}}{4\pi\epsilon_{0}}
\left (  
\frac{1}{r_{1A}} + \frac{1}{r_{1B}} + \frac{1}{r_{2A}} + \frac{1}{r_{2B}} -\frac{1}{r_{12}} - \frac{1}{R}
\right )
\end{align*}$$

Wave Function for radial variables $r_{1}, r_{2}$
$$\Psi_{H_{2}}(r_{1},r_{2},R_{A},R_{B}) \approx \varphi_e(r_{1},r_{2},R)\varphi_{ncl}(R_{A}, R_{B})$$

<br><br></div>

#### Hydrogen-Ion
![image](https://user-images.githubusercontent.com/52376448/114894979-0c88ea00-9e4a-11eb-8cd6-99c437d9685c.png)

<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
$$H_{H_{2}^{+}}\Psi_{H_{2}^{+}} = E_{H_{2}^{+}}\Psi_{H_{2}^{+}}$$

Hamiltonian
$$\begin{align*}
H_{H_{2}} &= -\frac{\hbar^2}{2M_{N}}(\nabla^{2}_{A} + \nabla^{2}_{B}) 
-\frac{\hbar^2}{2m_{e}}\nabla^{2} - \frac{e^{2}}{4\pi\epsilon_{0}}
\left (  
\frac{1}{r_{A}} + \frac{1}{r_{B}} - \frac{1}{R_{AB}}
\right ) \\

&\approx -\frac{\hbar^2}{2m_{e}}\nabla^{2} - \frac{e^{2}}{4\pi\epsilon_{0}}
\left (  
\frac{1}{r_{A}} + \frac{1}{r_{B}} - \frac{1}{R}
\right )
\end{align*}$$

Wave Function for radial variables $r_{1}, r_{2}$
$$\Psi_{H_{2}^{+}}(r_{1},r_{2},R_{A},R_{B}) \approx \varphi_e(r_{1},r_{2},R)\varphi_{ncl}(R_{A}, R_{B})$$

<br><br></div>

<br><br></div>


<br><br><br>
## QM-Based Force Fields
## QM Calculations of Ligand Binding Sites


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
  <li><a href="https://link.springer.com/article/10.1007/s10853-019-03671-w">(2019) Theories of molecular reaction dynamics: the microscopic foundation of chemical kinetics</a></li>
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
  <li><a href="https://ailever.github.io/education/2021/04/02/_CHEM-cc-en-qm-mm/">QM/MM : Quantum Mechanics/Molecular Mechanics</a></li>
</ol>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-04-02-_CHEM-cc-en-quantum-chemistry-methods.md" target="_blank" style="color:white">Edit</a></span>
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


