---
theme: seriph
background: /neuq.webp
class: 'text-center'
# highlighter: shiki
lineNumbers: false
info: |
  Presentation slides for developers.
  Learn more at [Sli.dev](https://sli.dev)
drawings:
  persist: false
transition: slide-left
css: unocss
---

## The Great Gatsby

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    《了不起的盖茨比》 西方文学选读汇报 - 熊舟桐 马旭洋
    <!--<carbon:arrow-right class="inline"/>-->
  </span>
</div>



<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/Arkrypto" target="_blank" alt="GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

---
transition: fade-out
---

# Index

目录

<Toc></Toc>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---

# Background

作者介绍

<div grid="~ cols-2 gap-4">
<div>
Author Introduction: F.Scott Fitzgerald

- **Identity**: Iconic American writer of the "Jazz Age", key figure of the "Lost Generation".
- **Life**: Born in Minnesota, dropped out of Princeton; his wife Zelda was both his muse and downfall.
- **Works**: *The Great Gatsby* (1925), *Tender Is the Night*, *This Side of Paradise*.
- **Legacy**: Known for lyrical prose exposing the emptiness of wealth, called "the poet of the American Dream".
- **End**: Died of a heart attack at 44, plagued by alcoholism and depression.

</div>

<div>
<img src="/en-gatsby/F._Scott_and_Zelda_Fitzgerald_grave.png">

<!--

作者介绍：**F. 斯科特·菲茨杰拉德**

- **身份**：美国"爵士时代"（Jazz Age）代表作家，"迷惘的一代"重要成员
- **生平**：生于明尼苏达州，普林斯顿大学辍学；妻子泽尔达（Zelda）是其缪斯与悲剧来源
- **代表作**：《了不起的盖茨比》（1925）、《夜色温柔》、《人间天堂》
- **文学地位**：以华丽文风揭露浮华下的空虚，被誉为"美国梦的解剖师"
- **结局**：因酗酒和抑郁早逝，44岁死于心脏病

-->

</div>

</div>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>
---

# Introduction

核心剧情介绍

<div grid="~ cols-2 gap-8">
<div>


Setting: Set in the **Jazz Age** of 1920s America, Long Island, New York. The story is narrated by Nick Carraway, an outsider observer.

1️⃣ **The Enigmatic Gatsby**: Jay Gatsby, a self-made millionaire, hosts extravagant parties but hides his past. He obsessively longs for Daisy Buchanan (now married to wealthy Tom).

2️⃣ **Reunion and Conflict**: Gatsby reconnects with Daisy through Nick (her cousin), but Tom exposes Gatsby’s criminal wealth, leading to a confrontation.

3️⃣ **Tragedy**: Daisy accidentally kills Tom’s mistress Myrtle; Gatsby takes the blame and is murdered. His empty funeral symbolizes the death of the American Dream.


</div>

<div>


背景设定：故事发生在 1920 年代美国"爵士时代"的纽约长岛，故事通过旁观者尼克·卡拉威的视角展开

主人公杰伊·盖茨比是长岛新贵，以奢华宴会闻名，但身世成谜。他痴恋旧日情人黛西·布坎南（现为富豪汤姆的妻子）

盖茨比通过尼克（黛西的表弟）与黛西重逢，但黛西的丈夫汤姆揭露他非法致富，矛盾爆发

黛西驾车意外撞死汤姆的情妇茉特尔，盖茨比替她顶罪，最终被误杀。葬礼无人出席，象征梦想的彻底破灭

</div>

</div>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---
layout: center
class: text-center
---

# Character Analysis

盖茨比信仰的那盏绿灯，是渐行渐远的未来


<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>
---

## Gatsby

盖茨比是：一个不断追逐梦想的理想主义者；一个用金钱和幻想包装爱情的悲剧人物；一个被社会边缘化的“新贵”；一个在堕落世界中仍保有“纯净之心”的象征性人物；是**美国梦的缔造者，也是其受害者**

身份与出身：美国梦的追逐者

- 盖茨比原名詹姆斯·盖兹（James Gatz），出身寒微，是个农民的儿子。他不满足于贫穷的现实，早年离家，靠自己的努力逐步“塑造”了盖茨比这个崭新的“身份”
- 他通过非法手段（如走私酒类）迅速积累了巨额财富，买下豪宅、举办盛大的派对，只为接近他曾爱过的黛西（Daisy）

爱情与幻想：理想主义的悲剧

- 盖茨比最显著的动机是对黛西的执念。他将黛西理想化，把她当作完美爱情与美好生活的象征。但事实上，黛西早已成为现实社会中庸俗、利己的代表
- 盖茨比试图“重拾过去”，却忽视了时间的不可逆与现实的残酷。尼克（叙述者）说他是“唯一真正相信美国梦的人”，也暗示了他是一位理想主义者，但终究无法战胜现实

<style>
h2 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---

金钱与社会：阶级的边界

- 尽管盖茨比极其富有，但他始终未被“上流社会”真正接纳。他的派对门庭若市，但他的人生是孤独的。他属于“新富”（nouveau riche），而黛西和汤姆则属于“老钱”（old money）
- 这种阶层分化和社会偏见贯穿整部小说，也让盖茨比的努力看起来带有悲剧色彩。他可以买来一切，却买不来真正的归属感

人格与象征：美国梦的化身

- 盖茨比象征着美国梦：只要努力，人人都可以成功。但小说指出这种梦在现实中是脆弱的、被腐化的——美国梦沦为了对金钱与享乐的追逐
- 他也是“希望”的象征。小说中反复提到的“绿灯”（Green Light）就象征着他对未来的希望——但这种希望是虚幻的，是他无法企及的“幻象”

盖茨比的结局：悲剧的终点

- 最终，盖茨比为黛西背黑锅，被乔治·威尔逊枪杀。他的葬礼冷清，只有尼克真正为他哀悼
- 他死得孤独，但带有某种高贵的“纯粹”：在一个堕落、虚伪的社会中，他是为梦想而死的“理想主义者”

---

## Daisy

黛西是：一位外表纯洁优雅、内心软弱冷漠的“金丝雀”；一种令人着迷、却又令人绝望的虚幻之美；上流社会的象征，是“老钱”阶层无动于衷、自私自利的缩影

- 更深层地，她是**美国梦的幻灭**：一个被理想化的目标，最终暴露出空洞与冷酷的真相

身份与背景：上流社会的代表

- 黛西出生于路易斯维尔的富裕家庭，后来嫁给了同样出身显赫的汤姆·布坎南（Tom Buchanan）。她生活在“老钱”阶层（Old Money）之中，象征着稳定的特权地位和传统的美国上层社会
- 她的名字“Daisy”本身就是一种白色花朵，表面纯洁美丽，但内部却空洞虚弱，暗喻其虚伪与空洞的本质

爱情与婚姻：被动与现实主义

- 黛西年轻时曾真心爱过盖茨比，但在他参军后，她很快便接受了汤姆的追求。盖茨比认为她是因“物质诱惑”背叛了爱情，但黛西的选择其实更体现了她的“现实主义”：她选择了更安全、更稳固的生活方式，而不是等待一个“可能永远不会回来的穷军官”
- 在面对盖茨比与汤姆之间的抉择时，黛西犹豫不决，最后选择了回归婚姻，哪怕她知道汤姆有外遇

<style>
h2 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---

性格与心理：软弱、虚荣、逃避责任

- 黛西是一个看似温柔动人、实则内心空虚的角色。她说话轻柔、带着“令人心碎的声音”，让人着迷，却无法真正承担情感与责任
- 她是一个典型的享乐主义者，追求浪漫、感性与富足，但一旦浪漫需要牺牲，她便选择退缩：她放弃等待贫穷的盖茨比嫁给汤姆，撞死人后让盖茨比顶罪并悄然离去，都暴露了她逃避现实与责任的本质

象征意义：美国梦的幻影

- 盖茨比心中的黛西，是梦想与幸福的化身。但现实中的黛西却是腐朽上流社会的代表。她象征着：美国梦中“幸福与富足”的承诺，同时也是这个梦想如何在现实中被金钱与权力腐蚀的体现
- 她就像小说中的“绿灯”——闪耀但永远无法触碰，承载着盖茨比全部幻想，却注定无法给予真正的回应

角色结局：逃避与循环

- 在小说结尾，黛西没有受到任何惩罚，也没有觉醒。她与汤姆像“粗鲁的人”一样“毁了事物后退到自己的金钱中”，继续过着无知却富足的生活。这暗示着现实中，像黛西这样的人，往往能够轻松逃脱道德责任，而真正为他们的选择买单的，是像盖茨比这样的“理想主义者”

---
layout: center
class: text-center
---

<center><img src="/en-gatsby/20181207144623.jpg" style="width:70%"></center>

"So we beat on, boats against the current, borne back ceaselessly into the past."

于是我们奋力前行，如同逆水行舟，却不断被浪潮推回过去

The past cannot be relived

旧梦不能重温

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---
layout: center
class: text-center
---

# Thanks for Watching

感谢观看

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>
