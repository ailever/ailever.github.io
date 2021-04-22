---
title: The Portfolio Management Problem
prev1_title: Portfolio Management
prev2_title: Finance
date: 2021/02/24
description: The Portfolio Management Problem
_previous: https://ailever.github.io/education/2020/05/30/Finance/
categories:
  - education
HL1: education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Finance.png
author_staff_member: anonym
---

<!-- Top Block -->
<div align="center" class="top_btn_box">
  <button class="top_btn" type="button" onclick="location.href='#'">A</button>
  <button class="top_btn" type="button" onclick="location.href='#'">B</button>
  <button class="top_btn" type="button" onclick="location.href='#'">C</button>
</div>
<!-- Top Block -->

## Risk and Return
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
Scalar Form
$$E(r_{i})=\sum_{j=1}^M {P_{ij} r_{ij}}$$
$$\sigma_{i}^2 = \sum_{j=1}^M {P_{ij}(r_{ij}-E(r_{i}))^2}$$
<ul>
<li>$E$ : the expected return</li>
<li>$\sigma$ : the variance of return</li>
<li>$r_{ij}$ : the return of a security $i$ during a time period $j$</li>
<li>$P_{ij}$ : the possibility of the return $j$ for the security $i$</li>
$$r_{\mathcal{P}j} = \sum_{i^{*}=1}^N {\omega_{i^{*}}r_{i^{*}j}}$$
$$E(r_{\mathcal{P}j}) = \sum_{i^{*}=1}^N {\omega_{i^{*}}E(r_{i^{*}})}$$
$$\sigma_{\mathcal{P}}^2 = \sum_{i^{*}=1}^N {\omega_{i^{*}}^2\sigma_{i^{*}}^2} + \sum_{i^{*}=1}^N \sum_{j=1,j \ne i^{*}}^N {\omega_{i^{*}}\omega_{j}\sigma_{i^{*}j}}$$
<li>$r_{\mathcal{P}j}$ : the return of a portfolio</li>
<li>$\mathcal{P}$ : a portfolio which include $N$ securities</li>
</ul>
<br><br></div>

<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
Vector Form
$$E(r_{\mathcal{P}}) = \mathbf{r^T \omega}$$
$$\sigma_{\mathcal{P}}^2 = \mathbf{\omega^T V \omega}$$
$$\sigma_{ij} = \frac{1}{M} \sum_{t=1}^M {[r_{it}-E(r_{i})][r_{jt}-E(r_{j})]}$$
<br><br></div>

<br><br><br>
## Portfolio Diversification

<div class="math-box1">
Uncorrelated Securities
$$\begin{align*}
  \sigma_{\mathcal{P}}^{2} &= \sum_{i=1}^{N} \omega_{i}^{2}\sigma_{i}^{2} \\
                 &= \sum_{i=1}^{N} \left ( \frac{1}{N} \right )^{2} \sigma_{i}^{2} \\
                 &= \frac{1}{N} \sum_{i=1}^{N} \left ( \frac{\sigma_{i}^{2}}{N} \right ) \\
                 &= \frac{1}{N} \bar{\sigma}_{i}^{2}
\end{align*}$$

Correlated Securities
$$\begin{align*}
  \sigma_{\mathcal{P}} &= \sum_{i=1}^{N} \left ( \frac{1}{N} \right )^{2} \sigma_{i}^{2} 
             + \sum_{i=1}^{N}\sum_{j=1, j \ne i}^{N} \left ( \frac{1}{N} \right )^{2} \sigma_{ij}  \\
             &= \frac{1}{N} \left ( \sum_{i=1}^{N} \frac{\sigma_{i}^{2}}{N} \right )
             + \frac{N-1}{N} \left ( \sum_{i=1}^{N}\sum_{j=1, j \ne i}^{N} \frac{\sigma_{ij}}{N(N-1)} \right ) \\
             &= \frac{1}{N} \bar{\sigma}_{i}^{2} + \frac{N-1}{N}\bar{\sigma}_{ij} \\
             &= \frac{1}{N} \left ( \bar{\sigma}_{i}^{2} - \bar{\sigma}_{ij} \right ) + \bar{\sigma}_{ij} \\

\end{align*}$$
</div>

<br><br><br>
## Calculating Efficient Frontiers
<div class="math-box1">
Risk-Free Security
$$
  r_{FP} = \omega_{\mathcal{P}}E(r_{\mathcal{P}}) + (1-\omega_{\mathcal{P}})r_{F}
$$
  
Portfolio standard deviation
$$\begin{align*}
  \sigma_{F\mathcal{P}} &= \sqrt{\omega_{\mathcal{P}}^{2}\sigma_{\mathcal{P}}^{2} + (1-\omega_{\mathcal{P}})^{2} \sigma_{F}^{2} + 2\omega_{\mathcal{P}}(1-\omega_{\mathcal{P}})\rho_{F\mathcal{P}}\sigma_{F}\sigma_{\mathcal{P}} } \\
  &= \omega_{\mathcal{P}}\sigma_{\mathcal{P}}\\
\end{align*}$$

</div>

<div>
$$\begin{align*}
\omega_{\mathcal{P}} &= \frac{\sigma_{F\mathcal{P}}}{\sigma_{\mathcal{P}}} \\
r_{F\mathcal{P}} &= r_{F} + \frac{E(r_{\mathcal{P}}) - r_{F}}{\sigma_{\mathcal{P}}} \sigma_{F\mathcal{P}}
\end{align*}$$
</div>

<!-- Content Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<!-- Content Block -->

---

<!-- Reference Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Reference</b>
<ol>
  <li></li>
  <li></li>
  <li></li>
</ol>
<br><br></div>
<!-- Reference Block -->

<!-- Article Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b id='ART'>Related Articles</b>
<ol>
  <li></li>
  <li></li>
  <li></li>
</ol>
</div>
<!-- Article Block -->

<!-- Bottom Block -->
<div align="center" class="bottom_btn_box">
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-02-24-_FI-pm-en-the-portfolio-management-problem.md" target="_blank" style="color:white">Edit</a></span>
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


