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
  <a href="https://github.com/Northboat" target="_blank" alt="GitHub"
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

<h2>变色龙哈希</h2>

变色龙哈希在椭圆曲线 ECC 上的实现，他能寻找哈希碰撞使哈希值保持不变

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
这时，明文变化前后，其变色龙哈希值保持不变，在某些具体场景下，能保证认证权限不变，但假名更新，实现权限切换

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

<h2>可擦除签名</h2>

可擦除签名 / 可净化签名在 RSA 上的实现，基于前文的变色龙哈希 $CH(m,r)$，他能够擦除明文中的特定内容并使签名仍然有效

签名参与者包括：签名者、擦除者和验签者

假设我们有明文 M

```json
M = {m1, m2} = { "姓名": "张三", "身份证号": "43070320011129xxxx" }
```

其中，为了保证用户隐私，身份证号是可擦除的数据

初始化 RSA 密钥为 $sk=d,\, pk=(e,N)$，使用私钥 sk 对明文 M 进行签名
$$
\sigma=H(C)^d = H(c_1\,||\,c_2)=H(CH(m_1,r_1)\,||\,CH(m_2,r_2))
$$
得到最后的签名结构
$$
\Sigma=(\sigma,r_1,r_2)
$$
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

在擦除阶段，擦除者对明文 M 中的敏感信息 $m_2$ 进行擦除，将其替换为无意义的 $m_2'=123456789$，而后利用变色龙哈希计算新的随机数 $r_2'$ 使得
$$
c_2'=CH(m_2',r_2')=c_2=CH(m_2,r_2)
$$
于是得到擦除后的签名结构
$$
\Sigma=(\sigma,r_1,r_2')
$$
同时替换明文信息为 $M'=\{m_1,m_2'\}$

验签者得到的明文信息将会是擦除者提供的 $M'$，在通过公钥 pk 进行验签时，计算
$$
C'=c_1\,||\,c_2'=CH(m_1,r_1)\,||\,CH(m_2',r_2')
$$
而后比对
$$
H(C')\stackrel{?}{=}\sigma
$$
实现验签

---
layout: center
class: text-center
---

# PGUS: Pretty Good User Security for Thick MVNOs with a Novel Sanitizable Blind Signature

PGUS：一种基于新型可擦除盲签名的面向厚移动虚拟网络运营商用户的安全协议

IEEE Symposium on Security and Privacy (SP) - May 2025

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

## 应用背景

在传统 5G 网络中，**一个运营商（MNO）同时控制：**

- 基站（gNB）
- 核心网（CN）

用户 UE 同时与二者进行交互，基站和核心网是彼此可信的，二者作为一个整体的安全模型

但在 Thick MVNO（厚 MVNO）中，基站和核心网的控制权被拆开了

- MNO：控制基站 gNB
- MVNO：控制核心网 CN

双方是商业博弈关系（honest-but-curious），后者需要向前者付费以获取服务

> 由于这样的服务拆分，核心网 CN 和基站 gNB 之间变得半可信，传统的认证协议按照没有拆分的逻辑在跑，例如：由于 gNB 的地理位置公开，按照传统协议，核心网 CN 知道是哪一个 gNB 在服务某个用户 UE，这等价于 CN 可以推断 UE 的位置轨迹，从而造成隐私泄露问题

网络被“拆开了”，但认证协议还是按“没拆”的逻辑在跑，这是问题的根源

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

<div style="height: 45%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
  <img src="/cia-report/25-12-14/image-20251214151527645.png" style="max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>

于是，一个新的适用于 Thick MVNO 场景的安全协议急需解决以下三个核心问题

1. 隐私问题：现有 5G-AKA 协议默认 gNB 身份对 CN 可见，但在 Thick MVNO 中，gNB 需要匿名且不可链接
2. 信任问题：gNB 属于 MNO，而 CN 属于 MVNO，现有 AKA 协议假设二者互信，这种假设不成立
3. 可追踪性：MVNO 需要向 MNO 付费，依据是 gNB 服务了多少 UE，如果 gNB 匿名，那么 MNO 可以重复使用一个认证凭据虚报 UE 数量，这要求协议能够追踪匿名目标（Global Traceability）

现有方案中，📌 **没有一个方案同时解决**：UE 隐私 + gNB 匿名 + CN 验证 + 可追责

---

## 方案介绍

PGUS = 一个新的密码学原语 + 两个协议

1. SBS（Sanitizable Blind Signature）
2. PGUS-AKA（认证与密钥协商）
3. PGUS-HO（无缝切换）

其中，SBS 是密码原语（核心创新点），后两个协议都是基于此的应用层协议

> <center><strong>SBS = 盲签名 + 可擦除 + 可追踪</strong></center>
>
> | 属性        | 作用                 |
> | ----------- | -------------------- |
> | Blind       | CN 看不到 gNB 的证书 |
> | Sanitizable | gNB 可更新证书       |
> | Trace       | 多次作弊可被识别     |

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

SBS 共分七个步骤：密钥生成 KGen、**数据提炼 Extract**、签名 Sign、**签名派生 Derive**、签名擦除 Sanit、验签 Verify 和**追踪 Trace**（其中加粗的步骤是 SBS 在 Sanitizable Signatures 的基础上加入的）

<div grid="~ cols-2 gap-4">
<div>

SBS 操作定义在椭圆曲线上，包括三个群、三个生成元和一个双线配对函数
$$
BG=(\boldsymbol{G_1},\boldsymbol{G_2},\boldsymbol{G_T},G_1,G_2,G_T,e,q)
$$
密钥生成 KGen：输出用于签名和擦除的公私钥对
$$
(pk_{sig},sk_{sig}),\, (pk_{san},sk_{san})\leftarrow KGen_{san}(1^\lambda,1^l)
$$

> - SPSEQ 指 Structure-Preserving Signatures on Equivalence Classes，结构保持的等价类签名，他允许在不重新签名的情况下，把签名**合法地迁移**到等价表示上（比如前文提到的可擦除的 RSA 签名）
> - TRS 指 Traceable Ring Signatures，可追踪环签名

</div>

<div style="height:65%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">


<img src="/cia-report/25-12-14/image-20251214191130031.png" style="margin-top: 20%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">

</div>

</div>

---

数据提炼 Extract：主要是把待签名的明文数据 $m$ 进行分块处理，并加入 $ADM$ 的判断，置空可擦除的字段，并输出用于签名的随机数组

<div grid="~ cols-2 gap-4">
<div>


这个算法接收一个明文消息 $m\in\{0,1\}^*$，签名者的公钥 $pk_{sig}$ 和擦除者的公钥 $pk_{san}$，以及可擦除字段的描述 $ADM$

$$
(dt,st)\leftarrow Extract(ADM,m,pk_{sig},pk_{san})
$$

输出由随机数组 $x_i,y_i$ 生成的 $\boldsymbol{G_1}$ 上随机数据 $dt=(X_i,Y_i)\in\boldsymbol{G_1}$ 用作下一阶段的签名输入，用户自身保留根据明文 $m$ 分块的当前状态 $st$

> - PKE 是指 Public Key Encryption，即普通的公钥加密

</div>

<div style="height:55%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214190949514.png" style="margin-top: 25%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">

</div>

</div>

---

签名 Sign：签名算法输入数据 $dt$、签名私钥 $sk_{sig}$、清理公钥 $pk_{san}$，并输出签名 $\sigma_{inner}$，签名过程如下图所示

<div style="height:35%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214201215955.png" style="margin-top: 4%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>

对用户精炼后的数据 $dt=(X_i,Y_i)$ 利用 SPSEQ 签名私钥 $ssksig$ 进行 SPSEQ 签名，分别得到 $\pi_{SS}=(\mu,\eta)$

再通过 TRS 签名，利用 TRS 签名私钥 $tsksig$ 对 TRS 签名公钥 $tpksig$、TRS 擦除公钥 $tpksan$ 以及 $\pi_{TRS}=pk_{sig}\,||\,pk_{san}\,||\,\pi_{SS}$ 进行签名，得到 $\sigma_{TRS}$

最后输出签名结构
$$
\sigma_{inner}=(\pi_{SS},\sigma_{TRS})
$$

---

签名派生 Derive

<div style="height:20%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214202749819.png" style="margin-top: 4%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>

---

签名擦除 Sanit

<div grid="~ cols-2 gap-4">
<div>


这个算法接收

</div>

<div style="height:55%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214202816595.png" style="margin-top: 15%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>


</div>



---

验签 Verify

<div style="height:35%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214202834877.png" style="margin-top: 4%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>



---

追踪 Trace

<div style="height:35%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214202853873.png" style="margin-top: 4%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>



---

PGUS-AKA

<div style="height:70%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
>
> 先由 gNB 执行 $SBS.Extract$ 生成匿名认证信息 $(dt,st)$
>

<img src="/cia-report/25-12-14/image-20251214205131093.png" style="margin-top: 4%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">

> - $Com_{ck'}$
> - ZK.P 指 Zero-Knowledge Proof 零知识证明
> - ZK.V 指

</div>

---

<div style="height:70%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214223130190.png" style="margin-top: 4%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">

</div>


---

PGUS-HO

<div style="height:70%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">


nmsl


<img src="/cia-report/25-12-14/image-20251214205039131.png" style="margin-top: 4%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">

wcnm

</div>

---
layout: center
class: text-center
---

# Towards Resilience 5G-V2N: Efficient and  Privacy-Preserving Authentication Protocol for  Multi-Service Access and Handover

迈向高可信性的 5G-V2N，一种面向多业务接入与切换的高效且隐私保护的认证协议

IEEE Transactions on Mobile Computing - January 2025


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

## 应用背景



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

## 方案介绍





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

# Thinking on RFID

基于变色龙哈希实现受控身份更新的 RFID 权限转移

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

<h2>问题思考</h2>

考虑一个这样的问题

> 标签 a 和阅读器 A 预留有认证数据（标签 a 属于阅读器 A），如何在不涉及后端服务器的情况下，标签 a 向阅读器 B 证明其合法性以及其所有权如何从 A 转移到 B



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

<h2>方案考量</h2>



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
