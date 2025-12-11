---
theme: seriph
background: /xdu.jpg
class: 'text-center'
# highlighter: shiki
lineNumbers: false
info: |
  Presentation slides for developers.
  Learn more at [Sli.dev](https://sli.dev)
drawings:
  persist: false
transition: fade-out # slide-left
css: unocss
---

## 基于变色龙哈希和可擦除签名的认证协议分享

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    <p>熊舟桐</p>
    <p>2025.12.17</p>
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


# 目录

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
layout: center
class: text-center
---

# Chameleon Hash & Sanitizable Signatures

变色龙哈希和可擦除签名

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

## Chameleon Hash

变色龙哈希在椭圆曲线 ECC 上的实现

对于加密方，其持有私钥 $x\in Z_p$，有公钥 $(G\in G_1, Y=xG)$，定义一个变色龙哈希 $CH$ 为
$$
CH(m, r)=r\cdot G+H(m)\cdot Y
$$
其中 $m$ 是待加密的明文，$r$ 是本次哈希的随机数，现在我将明文 $m$ 进行一次更新，假设更新为 $m'$，我可以计算一份新的随机数 $r'$
$$
r'=r+x(H(m)-H(m'))
$$
使得变色龙哈希发生碰撞
$$
CH(m, r)=CH(m',r')
$$
这时，明文变化前后，其变色龙哈希值保持不变，在某些具体场景下，能保证认证权限不变，但假名更新，实现认证对象的切换，即 Handover

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

## Sanitizable Signatures

可擦除签名 / 可净化签名在 RSA 上的实现，基于前文的变色龙哈希 $CH(m,r)$

<!-- <div grid="~ cols-2 gap-4"> -->

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
layout: center
class: text-center
---

# PGUS: Pretty Good User Security for Thick MVNOs with a Novel Sanitizable Blind Signature

PGUS：一种基于新型可擦除盲签名的面向重型 MVNO 用户的安全协议

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

# Towards Resilience 5G-V2N: Efficient and  Privacy-Preserving Authentication Protocol for  Multi-Service Access and Handover

迈向高可信性的 5G-V2N，一种面向多业务接入与切换的高效且隐私保护的认证协议


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

# Scheme in RFID

基于零知识证明与变色龙哈希实现标签在阅读器之间的快速权限切换

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
