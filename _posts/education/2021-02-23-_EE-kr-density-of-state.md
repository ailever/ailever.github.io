---
title: Density of State
date: 2021-02-23
description: Quantum Dot, Wire, Well, Box
_previous: https://ailever.github.io/education/2020/05/30/Electronics/
categories:
  - education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Electronics.png
author_staff_member: dongmyeong
---

<!-- Content Block -->
## Intro
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
　<b>현존하는 대부분의 고체 관련 이론(Solid State Physics, Condensed Matter Physics)들은 대부분 양자이론(Quantum Theory)에 근간을 두고 있습니다.</b> 반도체 역시, 양자이론 없이는 우리가 이해할 수 없는 대상입니다. 양자이론에 의하면, 전자의 상태(State of Electron)는 항상 양자화 되어있습니다. 예를 들어, 고전적 관념 하에 전자에게 가능하지 않은 속력(상태)은 없습니다. 이를 양자이론 관점에 비추어 보면, 속력 $1m/s$인 상태, 속력 $2m/s$인 상태, 속력 $3m/s$인 상태, … , 이러한 특정한 상태들만 전자의 가능한 상태로서 주어진다는 것 입니다. <br><br>

　전자에게 주어진 이러한 상태들이 무엇인지 파악해야만 전자들의 거동을 이해할 수 있기 때문에, 과학자들은 이러한 상태에 대한 분석을 '슈뢰딩거 방정식'을 통해 시도합니다. 그러나 물질 내의 전자는 매우 많고, 복잡하기 이를 데 없어, 정확히 어떠한 상태들이 전자에게 허용 가능한 상태로서 주어지는지 알아낼 수가 없었습니다. 그렇기 때문에, 물질 내에서 전자에게 주어진 상태들이 정확히 무엇인지는 몰라도, '낮은 에너지 범주에 속하는 상태들이 전자에게 많이 주어지는지, 높은 에너지 범주에 속하는 상태들이 전자에게 많이 주어지는지'에 대해 초점을 맞추게 됩니다. <br><br>

　<b><span style="color:red;">Density of State(DOS)</span>는 '물질 내에서, 단위 에너지당 전자에게 주어진 상태의 개수'로 정의됩니다.</b> 예를 들어, 어떠한 물질 내에서, 에너지 $1eV$에 대응되는 상태가 전자에게 $100$개 주어진다는 것이죠. DOS개념은 사실, 양자이론이 '전자의 허용 가능한 상태는 정해져 있다'고 제한을 걸었기 때문에, 필연적으로 나타날 수 밖에 없는 개념입니다. 만일 '전자의 상태가 제한적'이라는 양자현상이 나타나지 않는다고 생각해본다면, DOS는 의미 없는 개념이 되고 말았을 것 입니다. 고전적인 관념하에, 전자에게는 모든 상태가 허용되니, 항상 'DOS = ∞' 일테니깐요. 앞으로 DOS에 대해 구체적으로 논의해 보도록 하죠. <br><br>  
<br><br></div>

---


<div style="font-size:medium;"><br><br>
　오늘의 주제는 모두들 한 번 쯤은 들어 보셨으리라 생각되는 'Density of State(DOS)' 입니다.
<br><br></div>

<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
  $$Density\ of\ State(DOS)\ =\ 단위\ 에너지당\ 상태의\ 갯수$$
<br><br></div>

<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
　고체 내에 돌아다니는 전자들에 대해, 전자에게 허용된 상태들이 몇 가지 존재할 것인데, DOS는 에너지가 높은 전자의 상태들이 많은지, 아니면 에너지가 낮은 전자의 상태들이 많은지 알려주는 개념입니다. 우선 고체 내부를 돌아다니는 전자(electron)를 생각해 보도록 하죠.
<br><br></div>

![image](https://user-images.githubusercontent.com/52376448/108737302-d3cd4280-7575-11eb-84a7-1638230eab54.png)

<div align="center" style="font-size:large;font-weight:bold;color:black;background-color:unset;">
  <span style="background-color:yellow">1. 물질 내의 전자에게 허용된 상태가 있을 것입니다.</span>
</div>

<div align="center" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
예를 들어, <br>

전자의 상태1 : 에너지 $10eV$으로 왼쪽방향으로의 움직임을 갖는 <b>상태</b> <br>
전자의 상태2 : 에너지 $11eV$으로 오른쪽방향으로의 움직임을 갖는 <b>상태</b> <br>
<br><br></div>


<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　
　우리가 주목할 부분은 바로 <b>상태</b>입니다. 왜 상태에 주목하냐 물으실 수 있는데, 상태에 주목하는 이유는 양자이론에 의하면 <b>전자(Electron)는 모든 상태가 다 가능한 것이 아니라 <span style="color:red">특정한</span> or <span style="color:red">제한적인</span> or <span style="color:red">특수한</span> 상태만 취할 수 있기</b> 때문입니다. 그렇기에 반도체 내부를 돌아다니는 전자를 분석할 때는 전자가 아닌 전자의 허용된 상태에 관심을 갖습니다. <u>예를 들어, 전자(Electron)는 반도체 내에서 에너지 10인 상태는 가능하지만, 에너지 10.1인 상태는 애시당초 불가능하다.</u>
<br><br></div>

  
<br>
<div align="center" style="font-size:large;font-weight:bold;color:black;background-color:unset;">
  <span style="background-color:yellow">2. 위와 같은 전자의 상태들에 대해서, 각 상태에 대응되는 에너지 값이 있을 것입니다.</span>
</div>


<div align="center" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
예를 들어, <br>

전자의 상태1 : <b>에너지 $10eV$</b>으로 왼쪽방향으로의 움직임을 갖는 상태 <br>
전자의 상태2 : <b>에너지 $11eV$</b>으로 오른쪽방향으로의 움직임을 갖는 상태 <br>
<br><br></div>

<div align="center" style="font-size:large;font-weight:bold;color:black;background-color:unset;">
 <span style="background-color:yellow">3. 위와 같은 전자의 상태들에 대해서, 에너지 분포를 생각해 볼 수 있을 것입니다.</span>
</div>


<div align="center" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
예를 들어, <br><br>

에너지 영역대 $10\sim 11eV$에 <br>
속하는 전자 상태의 개수 : $100$개 <br><br>

에너지 영역대 $11\sim 12eV$에 <br>
속하는 전자 상태의 개수 : $200$개 <br><br>

에너지 영역대 $12\sim 13eV$에 <br>
속하는 전자 상태의 개수 : $300$개 <br>
<br><br></div>


<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
이렇게 단위 에너지당 상태의 가짓 수가 몇 가지인지를 추산할 수 있을 것 입니다. 즉, Density of State는 전자의 상태가 가지는 에너지 분포라고 생각해주세요. 더 나아가 다음 아래의 그래프를 바라보죠. 아래 그래프야 말로 Density of State(DOS)의 진정한 의미를 담고 있으니까요.
<br><br></div>

<div align="center" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
  $$Density\ of\ State(DOS)\ =\ 단위\ 에너지당\ 상태의\ 갯수$$
<br><br></div>

![image](https://user-images.githubusercontent.com/52376448/108737679-31fa2580-7576-11eb-809f-17197500760d.png)



<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
그래프(y축:DOS, x축:Energy)에 대한 해석은 <b>고체의 형상</b>을 기준으로 합니다. 고체의 모양이 기하학적으로 무엇을 닮아있는지를 살펴보는 것 입니다.
<br><br></div>

<div align="center" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
고체의 형상 : 네모 박스(3차원)와 유사<br>
고체의 형상 : 널판지(2차원)와 유사<br>
고체의 형상 : 막대기(1차원)와 유사<br>
고체의 형상 : 점(0차원)와 유사<br>
<br><br></div>


<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
고체의 형태(차원)에 따라 Density of State(전자 상태 에너지 분포)가 달라짐을 볼 수 있습니다. <b>네모 박스(3차원의 공간)</b>와 닮아 있는 경우 대체적으로 높은 에너지를 갖는 전자 상태가 많습니다. <b>널판지(2차원의 면)</b>와 닮아 있는 경우 대체적으로 높은 에너지를 갖는 전자 상태의 개수와 대체적으로 낮은 에너지를 갖는 전자 상태의 개수는 동등합니다. <b>막대기(1차원의 선)</b>와 닮아 있는 경우 대체적으로 낮은 에너지를 갖는 전자 상태가 많습니다. 마지막으로 <b>0차원의 점</b>의 경우 단 하나의 에너지 영역대에, 거의 모든 전자 상태가 밀집되어 있습니다. 역으로 말하면, ‘전자가 어떠한 상태이던지간에 갖는 에너지는 얼추 다 비슷하다’ 입니다. 왜 이러한 현상이 나타나는 걸까요? 양자 역학적인 접근으로 설명한다면 복잡한 설명이 되겠지만, 고전적인 접근 방법(쉬운 설명법)으로 설명하면 그리 어렵지 않으니 살펴보도록 하죠.
<br><br></div>

<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
고체 내에 돌아다니는 전자에 영향을 가장 크게 미치는 것은 ‘고체를 이루고 있는 원자들이 어떠한 주기성을 가지고 배열되어 있느냐’ 일 것 입니다. 고체의 주기성이 1차원적으로 반복되는지, 2차원적으로 반복되는지, 3차원 적으로 반복되는지 말이죠. 역시나 글보다는 그림이 이해를 더 도와줄때네요. 이 내용이 이해가지 않으신다면 아래 그림을 보고서 이해하도록 하죠. 우선 1차원 형태의 고체부터 살펴보겠습니다.
<br><br></div>

![image](https://user-images.githubusercontent.com/52376448/108739844-5fe06980-7578-11eb-9747-488f080aff45.png)
 
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
전자가 가질 수 있는 <b>운동방향은 좌측과 우측, 두 가지 뿐</b>이라고 가정하겠습니다(1차원 고체의 정의이기 때문입니다.). 여기서, 전자들에게 에너지를 더 가해주면 좌측 or 우측 방향으로 에너지가 커질 것 이고 일정 에너지 수준을 넘어가면 이 전자들은 다른 unit cell로 이동할 것입니다. 결론적으로, 운동방향이 2가지 방향으로 한정되어 있기에 위 붉은색 박스 unit cell 내에서 높은 에너지를 갖기 힘듭니다. 즉, 전자가 취할 수 있는 대부분의 상태는 낮은 에너지 영역대에 속해 있다고 대략적으로 추측해 볼 수 있습니다.
<br><br></div>


<div align="center" style="font-size:small;font-weight:normal;color:blue;background-color:unset;">
<b>주의사항 : 전자와 전자의 상태를 구분할 것!</b> <br><br>

'전자가 취할 수 있는 대부분의<br>
상태가 낮은 에너지 영역대에<br>
속해 있다'라는 의미와<br><br>

'전자들 대부분(실제로)이<br>
낮은 에너지를 갖는다'의 의미는 다릅니다.<br><br>


전자들 대부분(실제로)이<br>
낮은 에너지를 갖기 위해서는,<br>
아래의 두 가지 조건이<br>
충족되어야 합니다.<br><br>

1. 전자가 취할 수 있는 대부분의 상태가<br>
낮은 에너지 영역대에 속해 있다.<br>
2. 전자가 낮은 에너지 상태들과<br>
높은 에너지 상태들 중, 낮은 에너지<br>
상태들을 선택할 확률이 높아야 한다.<br><br>
  
<br><br></div>



<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;"><br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;"><br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;"><br><br></div>






<div style="font-size:medium;">

<br><br></div>




<div style="font-size:medium;">

<br><br></div>

![image](https://user-images.githubusercontent.com/52376448/108740100-a766f580-7578-11eb-8775-a73df533ee91.png)



<div style="font-size:medium;">
붉은 색 박스 내의 그래프에서
'에너지(E)가 높아질 수록, ρDOS가
줄어든다'는 것을 체크해주세요!

이상적인 상황 : ρDOS(1D)∝E-1/2

<br><br></div>



<div style="font-size:medium;">
다음은
2차원 형태의 고체입니다.

<br></div>

![image](https://user-images.githubusercontent.com/52376448/108740250-d2e9e000-7578-11eb-978c-79a9011230fc.png)


<div style="font-size:medium;">
전자가 가질 수 있는
운동방향은 평면 내에서만
움직인다고 가정 하겠습니다.
(2차원 고체의 정의이므로!)

여기서, 전자들에게 에너지를
더 가해주면 평면에서 가능한
방향 모두 에너지가 커질 것이고,

일정 에너지 수준을 넘어가면
이 전자들은 다른 unit cell로
이동할 것입니다.


위에서 설명한 1차원 고체와
비교해보면, 2차원 고체 내의
전자들의 상태들이, 더 높은
에너지를 가질 가능성이
높아진다는 것을 파악할 수 있습니다.

즉, 전자가 취할 수 있는 대부분의 상태는
모든 에너지 영역대에 걸쳐 골고루
나타날 것 이라고 대략적으로 추측해
볼 수 있습니다.

<br><br></div>


<div style="font-size:medium;">
주의사항 : 전자와 전자의 상태를 구분할 것!

'전자가 취할 수 있는 대부분의
상태는 모든 에너지 영역대에
걸쳐 골고루 나타난다'라는 의미와

'전자들 대부분(실제로)이 고른 에너지
분포를 갖는다'의 의미는 다릅니다.


전자들 대부분(실제로)이
고른 에너지 분포를 갖기 위해선
아래의 두 가지 조건이
충족되어야 합니다.

1. 전자가 취할 수 있는 대부분의 상태가
낮은 에너지 영역대에 속해 있다.
2. 전자가 낮은 에너지 상태들과
높은 에너지 상태들 중, 높은 에너지
상태들을 선택할 확률이 높아야 한다.
(조건2는 다음 포스팅 주제)
or
1. 전자가 취할 수 있는 대부분의 상태가
낮은 에너지 영역대와 높은 에너지 영역대
관계없이 고르게 분포하고 있어야 한다.
2. 전자가 낮은 에너지 상태들과
높은 에너지 상태들 중, 낮은 에너지
상태들을 선택할 확률이 동등해야 한다.
(조건2는 다음 포스팅 주제)
or
1. 전자가 취할 수 있는 대부분의 상태가
높은 에너지 영역대에 속해 있다.
2. 전자가 낮은 에너지 상태들과
높은 에너지 상태들 중, 낮은 에너지
상태들을 선택할 확률이 높아야 한다.
(조건2는 다음 포스팅 주제)

<br><br></div>

![image](https://user-images.githubusercontent.com/52376448/108740413-fdd43400-7578-11eb-8c24-c856ee63f3e3.png)

<div style="font-size:medium;">
붉은 색 박스 내의 그래프에서
'에너지(E)에 관계없이, ρDOS가
일정하다'는 것을 체크해주세요!

이상적인 상황 : ρDOS(1D)∝E0

<br></div>


<div style="font-size:medium;">
  마지막으로 3차원 형태의 고체입니다.
<br></div>

![image](https://user-images.githubusercontent.com/52376448/108740664-412ea280-7579-11eb-8eb3-ce53de941f1e.png)

<div style="font-size:medium;">
전자가 가질 수 있는 운동방향은
모든 방향으로 운동할 수 있다고 가정하겠습니다.
(3차원 고체의 정의이므로)

여기서, 전자들에게 에너지를 더 가해주면
각각의 방향 모두 에너지가 커질 것이고,

일정 에너지 수준을 넘어가면
이 전자들은 다른 unit cell로 이동할 것입니다.


결론적으로, 운동방향이 모든 방향이기에
붉은색 박스 unit cell 내에서
높은 에너지를 갖기 쉽습니다.

즉, 전자가 취할 수 있는 대부분의 상태는
높은 에너지 영역대에 속해 있다고
대략적으로 추측해 볼 수 있습니다.

<br><br></div>


<div style="font-size:medium;">
주의사항 : 전자와 전자의 상태를 구분할 것!

'전자가 취할 수 있는 대부분의
상태가 높은 에너지 영역대에
속해 있다'라는 의미와

'전자들 대부분(실제로)이
높은 에너지를 갖는다'의
의미는 다릅니다.


전자들 대부분(실제로)이
높은 에너지를 갖기 위해서는,
아래의 두 가지 조건이 충족되어야 합니다.

1. 전자가 취할 수 있는 대부분의 상태가
높은 에너지 영역대에 속해 있다.
2. 전자가 낮은 에너지 상태들과
높은 에너지 상태들 중, 높은 에너지
상태들을 선택할 확률이 높아야 한다.

<br><br></div>

![image](https://user-images.githubusercontent.com/52376448/108740801-66bbac00-7579-11eb-9bdf-3820a0c2e643.png)


<div style="font-size:medium;">
붉은 색 박스 내의 그래프에서
'에너지(E)가 높아질 수록, ρDOS가
높아진다'는 것을 체크해주세요!

이상적인 상황 : ρDOS(1D)∝E1/2


<br><br></div>



<div style="font-size:medium;">
참고로, Density of State에는
여러가지 모델이 존재하는데,

지금까지 설명한 DOS는
가장 단순한 모델의 DOS임을
알아두세요.

<br><br></div>


<div style="font-size:medium;">
아! 한 가지만 더요!

이런것을 왜 배우냐구요?

핸드폰을 만들던지
디스플레이를 만들던지

우리는 구성요소(반도체)들을
최대한 작게 만들어야 합니다.



그렇기 때문에, 그동안 대부분
3차원적 물질로 구성요소를 만들었지만


최근에는
3차원 물질(Quantum box)
2차월 물질(Quantum well),
1차원 물질(Quantum wire),
0차원 물질(Quantum dot)과
같은 저(낮은)차원 물질을 통해

산업에 응용하고자 하는 시도가 활발합니다.


실제, 삼성에서 내어놓은
QLED(Quantum Dot
Light Emitting Diodes)의 경우도
대표적인 예로 들 수 있겠네요.





뿐만 아니라, 반도체 물질의 전기 전도도를
책임지고 있는 캐리어들이, 반도체 내에
실질적으로 얼마나 많이 포함되어 있을지는,

Density of State가 클수록 유리합니다.




이런데도, DOS를 만만하게 보거나
간과하지만은 않으시겠죠?

<br><br></div>




<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">　<br><br></div>
<!-- Content Block -->

---

<!-- Reference Block -->
<div align="left" style="font-size:medium;font-weight:normal;color:black;background-color:unset;">
<b>Reference</b>
<ol>
  <li> Physics of Semiconductor Devices  -Wiley-Interscience (2006)</li>
  <li> Donald Neamen-Semiconductor physics and devices_ basic principles-McGraw-Hill (2012)</li> 
  <li> Ben G. Streetman, Sanjay Kumar Banerjee-Solid State Electronic Devices, 6th Edition (2005)</li>
  <li> Dimitrijev, Sima-Principles of Semiconductor Devices (2nd Edition)-Oxford University Press (2012)</li>
  <li> Robert F. Pierret-Semiconductor Device Fundamentals-Addison Wesley (1996)</li>
  <li> Betty Lise Anderson, Richard L. Andersn-Fundamentals of Semiconductor Devices (2005)</li>
  <li> S. O. Kasap-Principles of Electronic Materials and Devices. S.O. Kasap  -McGraw-Hill Education (2005)</li>
</ol>
<br><br></div>
<!-- Reference Block -->


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

