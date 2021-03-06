---
title: Complementarity Problems
prev1_title: Convex Analysis
prev2_title: Mathmatics
date: 2021-03-01
description: Complementarity Problems
_previous: https://ailever.github.io/education/2020/05/30/Mathematics/
categories:
  - education
HL1: education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Mathematics.png
author_staff_member: anonym
---

<!-- file name code
2021-03-01-_MATH-[]-en-[].md
-->

<!-- Top Block -->
<div align="center" class="top_btn_box">
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Help:Displaying_a_formula'">Mathematical Formula</button>
  <button class="top_btn" type="button" onclick="location.href='#'">B</button>
  <button class="top_btn" type="button" onclick="location.href='#'">C</button>
</div>
<!-- Top Block -->

## Linear Programming (LP)
<div class="math-box1">
$$\begin{array}{lcl}

\text{minimize} & c^{T}x + d \\
\text{subject to} & Gx \le h \\ 
                  & Ax = b \\ 
\text{where }G \in \mathbb{R}^{m \times n} \text{ and } A \in \mathbb{R}^{p \times n}&  \\ 

\end{array}$$
</div>

<br><br><br>
## Quadratic Programming (QP)
<div class="math-box1">
$$\begin{array}{lcl}

\text{minimize} & \frac{1}{2}x^{T}Px + q^{T}x + r \\
\text{subject to} & Gx \le h \\ 
                  & Ax = b \\ 
\text{where }G \in \mathbb{R}^{m \times n} \text{ and } A \in \mathbb{R}^{p \times n}&  \\ 

\end{array}$$
</div>

<br><br><br>
## Quadratically Constrained Quadratic Programming (QCQP)
<div class="math-box1">
$$\begin{array}{lcl}

\text{minimize} & \frac{1}{2}x^{T}P_{0}x + q_{0}^{T}x + r_{0} \\
\text{subject to} & \frac{1}{2}x^{T}P_{i}x + q_{i}^{T}x + r_{i} \le 0, i=1, \cdots, m \\ 
                  & Ax = b \\ 
\text{where }P \in \mathbb{S}^{n}_{+} \text{for } i=1,\cdots,m \text{ and } A \in \mathbb{R}^{p \times n}&  \\ 

\end{array}$$
</div>

<br><br><br>
## Second-Order Cone Programming (SOCP)
<div class="math-box1">
$$\begin{array}{lcl}

\text{minimize} & f^{T}x \\
\text{subject to} & \parallel A_{i}x + b_{i} \parallel_{2} \leq c_{i}^{T}x + d_{i}, i=1,\cdots,m \\ 
                  & Fx = g \\ 
\text{where }x \in \mathbb{R}^{n} \text{ is the optimization variable, } &\\
A_{i} \in \mathbb{R}^{n_{i} \times n} \text{ and } F \in  \mathbb{R}^{p \times n} &\\ 

\end{array}$$
</div>

<br><br><br>
## Semidefinite Programming (SDP)
<div class="math-box1">
$$\begin{array}{lcl}

\text{minimize} & c^{T}x + d \\
\text{subject to} & x_{1}F_{1} + \cdots + x_{n}F_{n} + G \leq 0 \\ 
                  & Ax = b \\ 
\text{where }G, F_{1}, \cdots, F_{n} \in \mathbb{S}^{k} \text{ and } A \in \mathbb{R}^{p \times n}&  \\ 

\end{array}$$
</div>

<br><br><br>
## Conic Programming (CP)
<div class="math-box1">
$$\begin{array}{lcl}

\text{minimize} & c^{T}x + d \\
\text{subject to} & Fx + g \leq_{K} 0 \\ 
                  & Ax = b \\ 
\text{where }c, x \in \mathbb{R}^{n}, A \in \mathbb{R}^{p \times n} \text{ and } b \in \mathbb{R}^{p} &  \\ 
\end{array}$$
</div>


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
  <li><a href="https://wikidocs.net/book/1896">Convex Optimization For All</a></li>
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
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-03-01-_MATH-ca-en-complementarity-problems.md" target="_blank" style="color:white">Edit</a></span>
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

