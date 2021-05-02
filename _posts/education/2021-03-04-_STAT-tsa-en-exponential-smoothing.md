---
title: Exponential Smoothing
prev1_title: Time Series Analysis
prev2_title: Statistics
date: 2021-03-04
description: Exponential Smoothing
_previous: https://ailever.github.io/education/2020/05/30/Statistics/
categories:
  - education
HL1: education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Statistics.png
author_staff_member: anonym
---

<!-- Top Block -->
<div align="center" class="top_btn_box">
  <button class="top_btn" type="button" onclick="location.href='https://en.wikipedia.org/wiki/Help:Displaying_a_formula'">Mathematical Formula</button>
  <button class="top_btn" type="button" onclick="location.href='#'">B</button>
  <button class="top_btn" type="button" onclick="location.href='#'">C</button>
</div>
<!-- Top Block -->

<div class="math-box">
$$\begin{align*}
\hat{y}_{t+h|t} &= (l_{t} \circ_{b} (b_{t} \circ_{d} \phi )) \circ_{s} s_{t+h-m(k+1)} \\
  l_{t} &= \alpha (y_{t} \ominus_{s} s_{t-m}) + (1-\alpha)(l_{t-1} \circ_{b} (b_{t-1} \circ_{d} \phi ))\\
  b_{t} &= \frac{\beta}{\alpha}(l_{t} \ominus_{b} l_{t-1}) + (1-\frac{\beta}{\alpha})b_{t-1} \\
  s_{t} &= \gamma (y_{t} \ominus_{s}(l_{t-1} \circ_{b}(b_{t-1} \circ_{d} \phi))) +(1-\gamma)s_{t-m}\\
\end{align*}$$
</div>
- <span>$\alpha, \beta, \gamma, \phi$ : smoothing parameters. In particular, $\ \phi_{h} = \phi + \phi^2 + \cdots + \phi^{h}$ means the damping parameter.</span>  
- <span>$k$ : the quotient of $\frac{h-1}{m}$</span>

<br><br><br>
## Exponential Smoothing
### N,N : Simple exponential smoothing
<div class="math-box2">
$$\begin{align*}
y_{t+h|t}  &= l_{t} \\
l_{t}  &= \alpha y_{t} + (1-\alpha) l_{t-1} \\
\end{align*}$$
</div>

### N,A : Simple exponential smoothing with additive seasonal 
<div class="math-box2">
$$\begin{align*}
y_{t+h|t}  &= l_{t} + s_{t+h-m(k+1)}\\
l_{t}  &= \alpha (y_{t} - s_{t-m}) +(1-\alpha)l_{t-1} \\
s_{t}  &= \gamma(y_{t} - l_{t-1}) +(1-\gamma)s_{t-m}\\
\end{align*}$$
</div>

### N,M : Simple exponential smoothing with multiplicative seasonal
<div class="math-box2">
$$\begin{align*}
y_{t+h|t}  &= l_{t} s_{t+h-m(k+1)}\\
l_{t}  &= \alpha (y_{t} / s_{t-m}) +(1-\alpha)l_{t-1} \\
s_{t}  &= \gamma(y_{t} / l_{t-1}) +(1-\gamma)s_{t-m}\\
\end{align*}$$
</div>

### A,N : Holt’s linear method
<div class="math-box2">
$$\begin{align*}
y_{t+h|t}  &= l_{t} + hb_{t}\\
l_{t}  &= \alpha y_{t} +(1-\alpha)(l_{t-1} + b_{t-1})\\
b_{t}  &= \beta^{*}(l_{t} - l_{t-1}) +(1-\beta^{*})b_{t-1}\\
\end{align*}$$
</div>

### A,A : Additive Holt-Winters’ method
<div class="math-box2">
$$\begin{align*}
y_{t+h|t}  &= l_{t} + hb_{t} + s_{t+h-m(k+1)}\\
l_{t}  &= \alpha (y_{t} - s_{t-m}) +(1-\alpha)(l_{t-1} + b_{t-1})\\
b_{t}  &= \beta^{*}(l_{t} - l_{t-1}) +(1-\beta^{*})b_{t-1}\\
s_{t}  &= \gamma(y_{t} - l_{t-1} - b_{t-1}) +(1-\gamma)s_{t-m}\\
\end{align*}$$
</div>

### A,M : Multiplicative Holt-Winters’ method
<div class="math-box2">
$$\begin{align*}
y_{t+h|t}  &= ( l_{t} + hb_{t} ) s_{t+h-m(k+1)}\\
l_{t}  &= \alpha (y_{t} / s_{t-m}) +(1-\alpha)(l_{t-1} + b_{t-1})\\
b_{t}  &= \beta^{*}(l_{t} - l_{t-1}) +(1-\beta^{*})b_{t-1}\\
s_{t}  &= \gamma(y_{t} / (l_{t-1} - b_{t-1})) +(1-\gamma)s_{t-m}\\
\end{align*}$$
</div>

### Ad,N : Additive damped trend method
<div class="math-box2">
$$\begin{align*}
y_{t+h|t}  &= l_{t} + \phi_{h}b_{t}\\
l_{t}  &= \alpha y_{t} +(1-\alpha)(l_{t-1} + \phi b_{t-1})\\
b_{t}  &= \beta^{*}(l_{t} - l_{t-1}) +(1-\beta^{*})\phi b_{t-1}\\
\end{align*}$$
</div>

### Ad,A : Additive damped trend method with additive seasonal
<div class="math-box2">
$$\begin{align*}
y_{t+h|t}  &= l_{t} + \phi_{h}b_{t} + s_{t+h-m(k+1)}\\
l_{t}  &= \alpha (y_{t} - s_{t-m}) +(1-\alpha)(l_{t-1} + \phi b_{t-1})\\
b_{t}  &= \beta^{*}(l_{t} - l_{t-1}) +(1-\beta^{*})\phi b_{t-1}\\
s_{t}  &= \gamma(y_{t} - l_{t-1} - \phi b_{t-1}) +(1-\gamma)s_{t-m}\\
\end{align*}$$
</div>

### Ad,M : Holt-Winters’ damped method
<div class="math-box2">
$$\begin{align*}
y_{t+h|t}  &= ( l_{t} + \phi_{h}b_{t} ) s_{t+h-m(k+1)}\\
l_{t}  &= \alpha (y_{t} / s_{t-m}) +(1-\alpha)(l_{t-1} + \phi b_{t-1})\\
b_{t}  &= \beta^{*}(l_{t} - l_{t-1}) +(1-\beta^{*})\phi b_{t-1}\\
s_{t}  &= \gamma(y_{t} / (l_{t-1} - \phi b_{t-1})) +(1-\gamma)s_{t-m}\\
\end{align*}$$
</div>



<br><br><br>
## ETS Models
### Additive models
<div class="math-box1">
$$e_{t} = y_{t} - \hat{y}_{t|t-1}$$
</div>

#### ETS(A,N,N)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= l_{t-1} + \epsilon_{t} \\
l_{t}  &= l_{t-1} + \alpha \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(A,N,A)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= l_{t-1} + s_{t-m} + \epsilon_{t} \\
l_{t}  &= l_{t-1} + \alpha \epsilon_{t} \\
s_{t}  &= s_{t-m} + \gamma \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(A,N,M)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= l_{t-1} s_{t-m} + \epsilon_{t} \\
l_{t}  &= l_{t-1} + \alpha \epsilon_{t}/s_{t-m} \\
s_{t}  &= s_{t-m} + \gamma \epsilon_{t}/l_{t-1} \\
\end{align*}$$
</div>

#### ETS(A,A,N)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= l_{t-1} + b_{t-1} + \epsilon_{t} \\
l_{t}  &= l_{t-1} + b_{t-1} + \alpha \epsilon_{t} \\
b_{t}  &= b_{t-1} + \beta \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(A,A,A)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= l_{t-1} + b_{t-1} + s_{t-m} + \epsilon_{t} \\
l_{t}  &= l_{t-1} + b_{t-1} + \alpha \epsilon_{t} \\
b_{t}  &= b_{t-1} + \beta \epsilon_{t} \\
s_{t}  &= s_{t-m} + \gamma \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(A,A,M)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= (l_{t-1} + b_{t-1}) s_{t-m} + \epsilon_{t} \\
l_{t}  &= l_{t-1} + b_{t-1} + \alpha \epsilon_{t}/s_{t-m} \\
b_{t}  &= b_{t-1} + \beta \epsilon_{t}/s_{t-m} \\
s_{t}  &= s_{t-m} + \gamma \epsilon_{t}/(l_{t-1} + b_{t-1}) \\
\end{align*}$$
</div>

#### ETS(A,Ad,N)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= l_{t-1} + \phi b_{t-1} + \epsilon_{t} \\
l_{t}  &= l_{t-1} + \phi b_{t-1} + \alpha \epsilon_{t} \\
b_{t}  &= \phi b_{t-1} + \beta \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(A,Ad,A)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= l_{t-1} + \phi b_{t-1} + s_{t-m} + \epsilon_{t} \\
l_{t}  &= l_{t-1} + \phi b_{t-1} + \alpha \epsilon_{t} \\
b_{t}  &= \phi b_{t-1} + \beta \epsilon_{t} \\
s_{t}  &= s_{t-m} + \gamma \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(A,Ad,M)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= (l_{t-1} + \phi b_{t-1}) s_{t-m} + \epsilon_{t} \\
l_{t}  &= l_{t-1} + \phi b_{t-1} + \alpha \epsilon_{t}/s_{t-m} \\
b_{t}  &= \phi b_{t-1} + \beta \epsilon_{t}/s_{t-m} \\
s_{t}  &= s_{t-m} + \gamma \epsilon_{t}/(l_{t-1} + \phi b_{t-1}) \\
\end{align*}$$
</div>


### Multiplicative models
<div class="math-box1">
$$e_{t} = \frac{y_{t}}{\hat{y}_{t|t-1}} - 1$$
</div>

#### ETS(M,N,N)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= l_{t-1}(1 + \epsilon_{t})  \\
l_{t}  &= l_{t-1}(1 + \alpha \epsilon_{t}) \\
\end{align*}$$
</div>

#### ETS(M,N,A)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= (l_{t-1} + s_{t-m})(1 + \epsilon_{t}) \\
l_{t}  &= l_{t-1} + \alpha (l_{t-1} + s_{t-m}) \epsilon_{t} \\
s_{t}  &= s_{t-m} + \gamma (l_{t-1} + s_{t-m}) \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(M,N,M)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= l_{t-1} s_{t-m}(1 + \epsilon_{t}) \\
l_{t}  &= l_{t-1} (1 + \alpha \epsilon_{t}) \\
s_{t}  &= s_{t-m} (1 + \gamma \epsilon_{t}) \\
\end{align*}$$
</div>

#### ETS(M,A,N)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= (l_{t-1} + b_{t-1})(1 + \epsilon_{t})  \\
l_{t}  &= (l_{t-1} + b_{t-1})(1 + \alpha \epsilon_{t}) \\
b_{t}  &= b_{t-1} + \beta (l_{t-1} + b_{t-1}) \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(M,A,A)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= (l_{t-1} + b_{t-1} + s_{t-m})(1 + \epsilon_{t})  \\
l_{t}  &= l_{t-1} + b_{t-1} + \alpha (l_{t-1} + b_{t-1} + s_{t-m}) \epsilon_{t} \\
b_{t}  &= b_{t-1} + \beta (l_{t-1} + b_{t-1} + s_{t-m}) \epsilon_{t} \\
s_{t}  &= s_{t-m} + \gamma (l_{t-1} + b_{t-1} + s_{t-m}) \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(M,A,M)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= (l_{t-1} + b_{t-1}) s_{t-m} (1 + \epsilon_{t})  \\
l_{t}  &= (l_{t-1} + b_{t-1})(1 + \alpha \epsilon_{t}) \\
b_{t}  &= b_{t-1} + \beta (l_{t-1} + b_{t-1}) \epsilon_{t} \\
s_{t}  &= s_{t-m}( 1 + \gamma \epsilon_{t}) \\
\end{align*}$$
</div>

#### ETS(M,Ad,N)
<div class="math-box2">
$$\begin{align*}
y_{t}  &= (l_{t-1} + \phi b_{t-1})(1 + \epsilon_{t})  \\
l_{t}  &= (l_{t-1} + \phi b_{t-1})(1 + \alpha \epsilon_{t}) \\
b_{t}  &= \phi b_{t-1} + \beta (l_{t-1} + \phi b_{t-1}) \epsilon_{t} \\
\end{align*}$$
</div>

#### ETS(M,Ad,A)

#### ETS(M,Ad,M)

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
  <li><a href="https://otexts.com/fpp3/">Forecasting: Principles and Practice (3rd ed)</a></li>
  <li><a href="https://www.statsmodels.org/devel/generated/statsmodels.tsa.exponential_smoothing.ets.ETSModel.html?highlight=etsmodel#statsmodels.tsa.exponential_smoothing.ets.ETSModel">Statsmodels - ETSModel</a></li>
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
  <span class="bottom_btn"><a href="https://github.com/ailever/ailever.github.io/blob/master/_posts/education/2021-03-04-_STAT-tsa-en-exponential-smoothing.md" target="_blank" style="color:white">Edit</a></span>
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

