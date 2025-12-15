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

## 基于变色龙哈希和可擦除签名的认证及权限移交协议分享

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

变色龙哈希的私钥持有者能够轻易的找到哈希碰撞，以下是变色龙哈希在椭圆曲线 ECC 上的实现样例

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

可擦除签名基于前文的变色龙哈希 $CH(m,r)$，能够修改明文和签名中的特定内容并保持签名的合法性，以下是一个可擦除签名在 RSA 上的实现样例

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

<br>

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

<br>

签名派生 Derive：派生算法输入状态 $st$ 和内部签名 $\sigma_{inner}$，然后输出推导签名 $\sigma$

<div style="margin-top: 7%; margin-bottom: 9%; height:25%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214202749819.png" style="max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>



本质上就是根据 gNB 的当前状态 $st$，将内部签名 $\sigma_{inner}$ 中的 $\pi_{SS}$ 字段和 $st$ 中的 $\{h_i,X_i,Y_i\}_{i\in\{l\}},c$ 组合起来，变成一个能够标记当前 gNB 的状态签名 $\sigma_{SS}$，与 TRS 签名 $\sigma_{TRS}$ 共同构成当前签名


---

签名擦除 Sanit：擦除算法输入明文 $m\in\{0, 1\}^*$，对 $m$ 的修改的修改指令 $MOD\in\boldsymbol{N}×\{0, 1\}^l$、签名 $\sigma$、公共签名密钥 $pk_{sig}$ 和擦除私钥 $sk_{san}$，然后输出清理后的消息 $m'$ 和 相应的清理签名 $\sigma'$

<div grid="~ cols-2 gap-4">
<div>

> SBS.sanit 的执行过程：先修改明文 $m\rightarrow m'$，而后重随机化 $(X_i,Y_i)\rightarrow (X_i',Y_i')$，再根据重随机化的 $(X_i',Y_i')$ 对原有的签名 $\mu,\eta$ 进行 $SPSEQ.ChgRep$ 擦除，得到新签 $\pi_{SS}'=(\mu',\eta')$，最后将新的明文 $m'$ 和随机数进行绑定得到 $h_i'$
>
> 1. 允许“受控修改”消息内容：把旧消息 $m$ 合法地变成新消息 $m'$
>2. 重随机化（rerandomization）整个签名表示：对所有中间群元素 $X_i, Y_i$ 进行随机指数变换，并同步调用 SPSEQ.ChgRep，得到新签名 $\sigma'$​，使其在数学上与旧签名等价，但在表示上完全不可链接
> 3. 重新绑定“可验证关系”：sanit 最后还做了一件验证层面的关键工作，即更新 $h_i = H(i || pksan || m_i)^{\zeta_i}$，确保 verifier 还能检查“签名 ⇔ 当前消息”的正确绑定
>
> 在这一复杂的 Sanit 变换中，SBS 实现了：匿名性（明文被重组隐藏）；每次更新无需“重新签名”；不允许“关联会话”（重随机化导致不可链接）；保留了追责能力（擦除者使用同一把擦除私钥）

</div>

<div style="height:55%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214202816595.png" style="margin-top: 15%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>


</div>



---

验签 Verify：验签算法输入消息 $m$、签名 $\sigma$、签名公钥 $pk_{sig}$、擦除公钥 $pk_{san}$，然后输出位 $b\in\{0, 1\}$，如果有效性成立则输出 1，否则输出 0

<div style="height:35%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214202834877.png" style="margin-top: 4%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>


在签名 $\sigma$ 中得到随机数 $(X_i,Y_i)$ 和，从 $\pi_{SS}$ 中拿到签名 $(\mu,\eta)$，当下述验证全部通过时，验签成功

1. 先判断 $Y_i$ 的合法性，要求所有 $Y_i\in\boldsymbol{G_1}$
2. 在通过 $QPSEQ.Verify$ 根据签名公钥 $spksig$ 分别对 $(X_i,\mu)$ 和 $(Y_i,\eta)$ 进行验签
3. 再根据擦除方的公钥 $pksan$ 进行双线性配对的验证 $e(X_i,h_i)\stackrel{?}{=}e(Y_i,H(i||[pksan||m_i]))$
4. 最后再根据 TRS 的签名公钥和擦除公钥对 TRS 签名进行验证




---

追踪 Trace：追踪算法输入两个签名 $(\sigma,\sigma')$，以及签名公钥 $pk_{sig}$ 和擦除公钥 $pk_{san}$

<div style="height:35%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251214202853873.png" style="margin-top: 4%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>
该算法输出以下字符串之一

- "indep"
- $pk_i\quad i\in\{sig,san\}$

该算法应用非常灵活，如果任何一个公钥包含在环 T 中的成员想要证明一个签名 $\sigma$ 是或者不是自己生成的，他可以使用相同的私钥生成另一个不同的签名 $\sigma^*$，并将 $(\sigma,\sigma^*)$提交给 Trace 算法

如果输出为 "indep"，则证明该签名不属于自己；如果输出是公钥 $pk_i$，则证明签名是由 $i\in\{sig, san\}$ 本身生成的


---

**PGUS-AKA**：PGUS-AKA 要解决的是在 Thick MVNO 中 $gN\in MNO, CN\in MVNO$ 场景下，在 **gNB 匿名、CN 不可跟踪、UE 隐私保护、gNB 可追责**的前提下，完成 UE ↔ CN ↔ gNB 的双向认证与会话密钥协商

<div style="height:75%; width: 100%; margin-top: 3%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">




> 系统注册阶段 gNB ↔ CN，首先是 gNB 发起注册请求
>
> 1. gNB 首先根据自身标识 $id_{gNB}$ 和时间戳 $\tau$ 生成证书 $C_{gNB}$，而后根据 CN 公钥 $pk_{sig}^{CN}$ 对证书进行数据抽取得到 $(dt,st)$
> 2. 而后根据随机数 $\mu$ 和伪名 $gid$ 生成一个承诺 $com_{gNB}$ 和一个零知识证明 $\pi_{ZK_{gNB}}$
> 3. gNB 将 $dt||com_{gNB}||\pi_{ZK_{gNB}}$ 打包为 $M_1^{SR}$ 发送给 CN

<img src="/cia-report/25-12-14/image-20251214205131093.png" style="margin-left: 2%; margin-right: 2%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">

> CN 收到 $M_1^{SR}$ 后，进行内部签名
>
> 1. CN 首先验证 gNB 的零知识证明，若通过
> 2. 则根据 CN 的签名私钥和 gNB 的擦除公钥以及 gNB 发来的数据 $dt$ 生成签名 $\sigma_{inner}\leftarrow SBS.Sign(sk_{sig}^{CN},pk_{san}^{gNB},dt)$，并将签名作为 $M_2^{SR}$ 回送给 gNB
>
> gNB 收到内生签名 $\sigma_{inner}$ 后
>
> 1. 根据自身状态 $st$ 进行签名的派生：$SBS.Derive(st,\sigma_{inner})$
> 2. 而后验证 $SBS.Verify$ 当前派生的签名 $\sigma_{fix}$ 是由自身公钥和 CN 公钥生成

</div>

---

<div style="height:95%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">




> 初始认证阶段，建立 UE 到 gNB / CN 的信任
>
> 1. gNB 将擦除过的派生签名 $\sigma_{MOD}^{gNB}\leftarrow SBS.Sanit(\sigma_{fix},...)$ 和 gNB 的匿名证书 $C_{MOD}^{gNB}$ 发给 UE
> 2. UE 验证证书合法性并检查 SBS 签名，若都通过，UE 则生成 PKE 的公私钥，计算自身的承诺 $com_{UE}$，零知识证明 $\pi_{ZK_UE}$ 和一个签名 $\sigma^{UE}，PK_U$ 发送给 gNB
> 3. gNB 首先验证 UE 的签名确认身份，而后自身生成一份证明自身身份的签名 $\sigma^{gNB}$，连同 UE 信息 $\pi_{ZK_{UE}},com_{UE},PK_U$ 发送给 CN
> 4. CN 首先验证签名 $\sigma^{gNB}$ 和 $\pi_{ZK_{UE}}$ 确认 gNB 和 UE 身份，都通过后，CN 随机生成一个通用标识符 $UID_i$ 作为切换阶段的用户标识符并存储在本地，再根据 UE 的公钥 $PK_u$ 对 CN 的签名 $\sigma^{CN}$，标识符 $UID$ 和一个时间戳 $\tau_4$ 加密发回给 UE
>

<img src="/cia-report/25-12-14/image-20251214223130190.png" style="max-height: 100%; max-width: 100%; /* 防止图片超出div */">

> 5. UE 利用私钥 $SK_u$ 解密 CN 消息获取 $UID$，并且验证 CN 的签名 $\sigma^{CN}$ 确认 CN 身份，建立与 gNB 和 CN 的信任
>
> <br><br><br><br><br>
>
> 追责阶段：匿名 ≠ 不可监管
>
> - 系统根据 $SBS.Trace(\sigma_{fix},\sigma_{MOD}^{gNB},pk_{sig}^{CN},pk_{san}^{gNB})$ 生成任意基站和 CN 之间的跟踪标识符 $tr$
> - 当发生争议时，UE 能够通过在初始认证阶段获取的 $\sigma_{MOD}^{gNB}$ 和发起追责，结合基站的派生签名 $\sigma_{fix}$，计算第二份标识符 $tr'$ ，与相应的跟踪标识符 $tr$ 比对，即可跟踪到基站行为，从而防止 MNO 虚报用户数和保障 MVNO 计费公平

</div>


---

**PGUS-HO**：确保用户 UE 在不同的网络基站 gNB 之间切换时，能够平稳过渡，且不会中断连接，防止链接攻击和冒充攻击并提供追踪机制

<div style="height:80%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">



> **切换基站 ≠ 重新做一次重认证**
>
> gNB 通过 **SBS.Sanit** 对 UE 已有签名进行合法更新，不需要经过 CN
>
> - UE 无需重新暴露身份
>- CN 仍然无法跟踪轨迹
> - 切换延迟显著降低

<img src="/cia-report/25-12-14/image-20251214205039131.png" style="margin-top: 4%; margin-right: 2%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">

> 1. 目标基站更新其证书 $C^{gNB}_{MOD}$ 并通过 $SBS.Sanit$ 算法生成新的签名 $\sigma^{gNB}_{MOD}$，然后将新的证书和签名发送给用户 UE
> 2. 用户设备 UE 验证新基站的证书和签名的有效性，生成新的公钥 $(PK_u,SK_u)$，并使用零知识证明（ZKP）携带其承诺 $com_{UE}$，通用标识符 $UID$ ，最后生成统一封装的签名 $\sigma^{UE}$ 返回基站
> 3. 基站接收到用户设备的消息后，对时间戳和签名进行验证，并生成一个确认消息 $ACK$ 和相应的签名 $\sigma$，用用户设备的公钥 $PK_u$ 加密发回
> 4. UE 收到密文后，进行解密，并对 gNB 的签名进行验证，实现本次认证流程，并且由于 UE 中保存了最新的 gNB 签名，后续的追责逻辑和 PGUS-AKA 中保持一致

</div>

---

<h2>总结</h2>

研究动机与目标

- 论文的核心目标是解决 5G 网络中厚 MVNO 环境下的隐私和安全问题，整体的 5G 网络架构没变，但在新的场景中（基站与核心网络分离）讨论安全问题
- 由于引入了新的不可信机构（核心网 CN 和基站 gNB 互不可信），老协议无法支撑新模式下的安全性，论文以此为立足点进行讨论

论文没有提出一个完全新颖的架构，而是在现有技术框架下，通过增强现有协议的安全性，提出了符合 5G 未来发展的解决方案，这样写作的优势在于

- 不需要证明已有的安全性，比如 UE 对 gNB 和 CN 的可信建立，因为在之前的论文中都已证明过了，只需要关注自己所提出来的这一部分的安全性，通过引入新的不可信或半可信机构，然后证明问题确实存在并且现有方案没有解决，论文就可以立足
- 比如这篇论文主要就是关注：如何使 gNB 对 CN 匿名，同时满足可追责；并且由于性能也很好，所以是一篇 SP；如果跳出已有标准，需要证明整个系统方案的安全性，工作量大也不容易使人信服

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



<div style="margin-top: 2%; height:35%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251215201212369.png" style="margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>

在 5G 车联网系统中，车辆 UE 通过移动 5G 基站 gNB 连接到网络，这种连接容易受到多种安全漏洞的威胁，例如假基站（FBS）攻击以及基站间切换过程中效率低下等问题。此外，系统通常需要同时支持多个服务（例如紧急服务、信息娱乐、车辆诊断等），这使得传统的身份验证过程显得繁琐且低效

论文中指出了几个主要的安全和效率问题

1. **假基站（FBS）攻击：** 当恶意实体伪装成基站时，可能导致数据被截获或篡改
2. **二次认证失败：** 传统的认证方法无法确保车辆在访问服务时的合法性，特别是在初次连接后
3. **切换效率和安全问题：** 在高速行驶的车辆环境中，基站频繁切换会导致保证持续安全服务的延迟和风险

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

<br><br><br>

论文提出的协议主要考虑以下几个安全问题

1. **多服务访问认证：** 通过引入单次认证请求访问多个服务的机制，减少冗余处理，降低多凭证带来的安全风险
2. **增强的密钥前向/后向保密性（KF/BS）：** 协议确保即使会话密钥被泄露，也无法推导出过去或未来的密钥，从而保护了历史通信会话的安全
3. **隐私保护的无缝切换：** 在切换过程中加入安全措施，以防止 FBS 攻击，并确保车辆和基站的身份隐私保护
4. **安全的基站切换机制：** 提出了安全的 g2g 信道，确保在基站切换时保持安全通信

该系统与现有的 5G 架构兼容，只在控制平面消息中进行扩展，增强了部署的可行性和灵活性


---

## 方案介绍

系统由三方构成：车辆 $V$、基站 $BS_i$ 和服务提供者 $SP_j$，协议分为三个阶段

- 初始接入阶段（Initial Access Phase）：该阶段建立在对 $V2N\,MEC@gNB$ 框架的研究基础上，以执行所提出的二次认证
- 安全的 G2G 信道建立阶段（Secure g2g Channel Establishment）：该阶段在现有 MEC 业务迁移研究的基础上，重新构建了 5G 切换准备阶段
- 切换认证阶段（Handover Authentication Phase）：该阶段重构了 5G 切换执行阶段

其中主要使用的密码原语包括 CRT、ECC 和 Chameleon Hash Function

$SP_j$ 系统初始化

- 发布公钥 $\{q,P,\boldsymbol{G},H_0,H_1,H_2,H_3,H_4,H_5,H_6,H_7,Y_{sp_j}\}$，其中 P 是 ECC 上一点，$\boldsymbol{G}$ 是加法子群，$H_i$ 是哈希函数，$Y_{sp_j}$ 是用于变色龙哈希的公钥
- 保留私钥 $(k_{sp_j},x_{sp_j})$，均用于变色龙哈希

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

初始接入阶段发生在车辆首次进入网络范围并试图通过 5G V2N2V 通信访问 V2X 服务时，核心目标：单请求多服务接入 + 车 - 基站 - 服务提供商间的双向认证 + 密钥协商

<div style="margin-bottom:1%; height:35%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">

<img src="/cia-report/25-12-14/image-20251215211856943.png" style="max-height: 100%; max-width: 100%; /* 防止图片超出div */">

</div>


> 车辆 V 发起复合服务请求至基站 $BS_i$，并由基站 $BS_i$ 转发请求给服务提供者 $SP_j$，服务提供者 $SP_j$ 认证 V 和 $BS_i$ 身份，生成并回送会话密钥和 CRT 聚合参数 Cap
>
> 1. 车辆发请求：V 选择 m 个随机数（对应 m 个组件服务），计算聚合随机值 $R_1=\bigoplus r_j$，通过中国剩余定理（CRT）计算 $\gamma_1$，携伪身份（PID）、时间戳与随机数发送给基站
> 2. 基站转发验证：验证车辆请求合法性，附加自身身份凭证，转发至 SP 组
> 2. SP 双向认证：通过变色龙哈希等式验证车与基站身份，聚合服务能力参数 Cap，生成会话密钥（车 - SP、SP - 基站）并返回响应
> 2. 车 - 基站建立连接：基站解密获取 Cap 并动态调整，与车辆完成双向认证 MA 和密钥协商，建立安全会话

---

安全的 G2G 信道建立阶段，核心目标：源基站 - 目标基站安全信道 + 预共享切换参数

<div style="height:40%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251215213605778.png" style="margin-top: 5%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>

关键逻辑

1. 源基站发起：指定目标基站，携带自身身份凭证（变色龙哈希参数）发送信道建立请求
2. 目标基站响应：验证源基站身份，生成会话密钥（g2g），返回响应并附带完整性校验（MAC）
3. 共享切换参数：建立双向安全隧道，源基站加密传输车辆能力（Cap）、临时身份（TID）、共享密钥（s₁）等切换参数，通知车辆准备切换

---

切换认证阶段，核心目标：快速双向认证 + 增强型 KF/BS + 防伪基站攻击（FBS）

<div style="height:40%; width: 100%; /* 块级默认占满宽度，可自定义 */ display: flex; justify-content: center; align-items: center;">
<img src="/cia-report/25-12-14/image-20251215213626255.png" style="margin-top: 7%; margin-bottom: 4%; max-height: 100%; max-width: 100%; /* 防止图片超出div */">
</div>

关键逻辑

1. 车辆发起切换：基于预共享参数（s₁、TID），携带身份验证凭证，发送切换请求至目标基站
2. 目标基站验证：验证车辆身份（变色龙哈希 + 临时参数校验），生成会话密钥，返回响应（含自身身份凭证）
3. 完成切换：车辆验证目标基站身份，确认会话密钥完整性，动态调整服务能力，双方完成切换并准备下一轮 G2G 参数同步


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

方案考虑

> - 离线验证 → 零知识证明：由于是标签向阅读器证明其合法性，所以需要标签来存储私钥，并且计算零知识证明给阅读器，这样的计算开销在 RFID 中是不被允许的
> - 其次，阅读器大多仅作为消息的中转，不参与核心的认证逻辑，所以如果要考虑所有权的转移，引入后端服务器似乎是无法避免的

但这里的权限转换可以考虑，一般而言，我们认为阅读器与服务器之间是可信的，如果假设二者不可信，可以引入阅读器之间的权限转换，即标记标签是否能被当前阅读器组认证，例如

> 1. 标签 a 属于阅读器组 A，能通过阅读器组 A 向服务器 S 证明自己的合法性
> 2. 在某一次物流移交，标签 a 权限从阅读器组 A 转移到阅读器组 B
> 3. 那么此时，阅读器 A 读取标签 a 将无法通过认证，而只能通过阅读器组 B 实现认证

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
