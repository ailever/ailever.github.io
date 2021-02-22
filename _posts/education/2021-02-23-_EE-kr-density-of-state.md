---
title: Density of State
date: 2021-02-23
description: Quantum Dot, Wire, Well, Box
categories:
  - education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Electronics.png
author_staff_member: dongmyeong
---

## Intro
<div style="font-size:medium;">
　현존하는 모든 고체이론(Solid State Physics, Condensed Matter Physics)은 대부분 양자이론(Quantum Theory)에 근간을 두고 있습니다. 반도체 역시, 양자이론 없이는 우리가 이해할 수 없는 대상입니다. 양자이론에 의하면, 전자의 상태(State of Electron)는 항상 양자화 되어있습니다. 예를 들어, 고전적 관념 하에 전자에게 가능하지 않은 속력(상태)은 없습니다. 이를 양자이론 관점에 비추어 보면, 속력 1m/s인 상태, 속력 2m/s인 상태, 속력 3m/s인 상태, … , 이러한 특정한 상태들만 전자의 가능한 상태로서 주어진다는 것 입니다. <br><br>

　전자에게 주어진 이러한 상태들이 무엇인지 파악해야만 전자들의 거동을 이해할 수 있기 때문에, 과학자들은 이러한 상태에 대한 분석을 '슈뢰딩거 방정식'을 통해 시도합니다. 그러나 물질 내의 전자는 매우 많고, 복잡하기 이를 데 없어, 정확히 어떠한 상태들이 전자에게 허용 가능한 상태로서 주어지는지 알아낼 수가 없었습니다. 그렇기 때문에, 물질 내에서 전자에게 주어진 상태들이 정확히 무엇인지는 몰라도, '낮은 에너지 범주에 속하는 상태들이 전자에게 많이 주어지는지, 높은 에너지 범주에 속하는 상태들이 전자에게 많이 주어지는지'에 대해 초점을 맞추게 됩니다. <br><br>

　Density of State(DOS)는 '물질 내에서, 단위 에너지당 전자에게 주어진 상태의 개수'로 정의됩니다. 예를 들어, 어떠한 물질 내에서, 에너지 1eV에 대응되는 상태가 전자에게 100개 주어진다는 것이죠. DOS개념은 사실, 양자이론이 '전자의 허용 가능한 상태는 정해져 있다'고 제한을 걸었기 때문에, 필연적으로 나타날 수 밖에 없는 개념입니다. 만일 '전자의 상태가 제한적'이라는 양자현상이 나타나지 않는다고 생각해본다면, DOS는 의미 없는 개념이 되고 말았을 것 입니다. 고전적인 관념하에, 전자에게는 모든 상태가 허용되니, 항상 'DOS = ∞' 일테니깐요. 앞으로 DOS에 대해 구체적으로 논의해 보도록 하죠. <br><br>
</div>

---

<div style="font-size:medium;">
오늘의 주제는 모두들 한 번 쯤은 들어 보셨으리라 생각되는 'Density of State(DOS)' 입니다.
</div>

<div align="center" style="color:red;font-weight:bold;font-size:medium;">
<br>Density of State(DOS) = 단위 에너지당 상태의 갯수<br>　
</div>

<div style="font-size:medium;">
고체 내에 돌아다니는 전자들에 대해, 전자에게 허용된 상태들이 몇 가지 존재할 것인데, DOS는 에너지가 높은 전자의 상태들이 많은지, 아니면 에너지가 낮은 전자의 상태들이 많은지 알려주는 개념입니다. 우선 고체 내부를 돌아다니는 전자(electron)를 생각해 보시죠.
</div><br>

![image](https://user-images.githubusercontent.com/52376448/108737302-d3cd4280-7575-11eb-84a7-1638230eab54.png)
 

<div style="font-size:medium;font-weight:bold;">1. 물질 내의 전자에게 허용된 상태가 있을 것입니다.</div>
<div style="font-size:medium;">
예를 들어,

왼쪽방향으로 움직이는, 에너지 10인 전자의 상태
오른쪽방향으로 움직이는, 에너지 9인 전자의 상태
아래방향으로 움직이는, 에너지 10인 전자의 상태
등등,

우리가 주목할 부분은 바로 상태!




왜 상태에 주목하냐 물으실 수 있는데,

상태에 주목하는 이유는

양자이론에 의하면, 전자(Electron)는
모든 상태가 다 가능한 것이 아니라,

특정한 or 제한적인 or 특수한
상태만 취할 수 있기 때문입니다.

그렇기에, 반도체 내 돌아다니는 전자를
분석할 때는, 전자가 아닌 전자의
허용된 상태에 관심을 갖습니다.


예를 들어, 전자(Electron)는 반도체 내에서
에너지 10인 상태는 가능하지만,
에너지 10.1인 상태는 애시당초 불가능하다.
<br></div>



<div style="font-size:medium;font-weight:bold;">2. 위와 같은 전자의 상태들에 대해서, 각 상태에 대응되는 에너지 값이 있을 것입니다.</div>
<div style="font-size:medium;">
예를 들어, 상태1 에너지 : 10eV, 상태2 에너지 : 12eV, 상태3 에너지 : 10eV 등..
<br></div>

<div style="font-size:medium;font-weight:bold;">3. 위와 같은 전자의 상태들에 대해서, 에너지 분포를 생각해 볼 수 있을 것입니다.</div>
<div style="font-size:medium;">
예를 들어,

에너지 영역대 10eV~11eV에
속하는 전자 상태의 개수 : 100개

에너지 영역대 11eV~12eV에
속하는 전자 상태의 개수 : 200개

에너지 영역대 12eV~13eV에
속하는 전자 상태의 개수 : 300개
등등등,

이것이 바로
단위 에너지당 상태의 갯수!
(Density of State)

즉, Density of State는
전자의 상태가 가지는
에너지 분포라고 생각해주세요!







자 그렇다면, 다음 아래의
사진을 보시죠!

아래 사진이야 말로
Density of State(DOS)의
진정한 의미를 담고 있으니까요.



Density of State(DOS)
=
단위 에너지당 상태의 갯수!

</div>

![image](https://user-images.githubusercontent.com/52376448/108737679-31fa2580-7576-11eb-809f-17197500760d.png)


