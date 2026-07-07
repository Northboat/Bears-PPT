---
theme: seriph
background: /xdu.jpg
class: 'text-center'
# highlighter: shiki
lineNumbers: false
info: |
  A Novel RFID Authentication Protocol Based on a Block-Order-Modulus Variable Matrix Encryption Algorithm.
drawings:
  persist: false
transition: fade-out
css: unocss
---

## 基于块-阶-模可变矩阵加密算法的新型RFID认证协议

<div class="pt-6">
  <span @click="$slidev.nav.next" class="px-4 py-2 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    <p class="text-xl">A Novel RFID Authentication Protocol Based on a Block-Order-Modulus Variable Matrix Encryption Algorithm</p>
    <p class="text-md mt-6 text-gray-500">论文分享与核心创新点解读</p>
    <p class="text-sm mt-2 text-gray-400">IEEE TRANSACTIONS ON INFORMATION FORENSICS AND SECURITY, 2025</p>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
</div>

---

# 目录

<div class="max-h-[350px] overflow-y-auto pr-4">
  <Toc></Toc>
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

# 研究背景与挑战

低成本标签与移动RFID系统

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

## 什么是移动 RFID 系统？

传统的 RFID 系统通常使用固定的阅读器（Reader），阅读器与后端服务器（Server）之间的通信被认为是安全且有线的。

但在**移动 RFID 系统**中，阅读器为便携式或手持设备（例如物流扫码终端），由此引入以下特性：
- **无线通信**：阅读器与服务器之间通过无线信道通信，存在被窃听的风险。
- **动态拓扑**：标签（Tag）、阅读器与服务器之间的物理位置可能持续变化。
- **安全性需求**：需在服务器-阅读器、阅读器-标签两个环节均实现**双向认证**（Two-way Authentication）。

<div class="flex justify-center mt-6">
  <div class="bg-gray-100 dark:bg-gray-800 p-4 rounded-lg shadow-md w-3/4 transform scale-90 origin-top">

```mermaid
    graph LR
        T((Tag)) <==>|无线/不安全| R[Handheld Reader]
        R <==>|无线/不安全| S{Backend Server}
        style T fill:#f9f,stroke:#333,stroke-width:2px
        style R fill:#bbf,stroke:#333,stroke-width:2px
        style S fill:#bfb,stroke:#333,stroke-width:2px
```

  </div>
</div>

---

## 低成本标签的安全困境

RFID 标签（如商品溯源标签）的硬件成本受限，其**计算能力与存储空间均较为有限**。

<div class="grid grid-cols-2 gap-8 mt-6">
<div>
<h3 class="text-red-500">❌ 传统成熟加密算法</h3>
<ul>
  <li>如 <b>ECC, RSA</b> 等非对称加密。</li>
  <li>需要数千甚至上万个逻辑门。</li>
  <li><b>局限：</b> 计算开销较大，低成本标签难以承载。</li>
</ul>
</div>

<div>
<h3 class="text-orange-500">⚠️ 轻量级哈希/位运算</h3>
<ul>
  <li>如 XOR, 位移, 简单 Hash。</li>
  <li><b>局限：</b> 安全强度较弱，难以抵抗去同步、伪造、重放等攻击。</li>
</ul>
</div>
</div>

<div class="mt-8 bg-blue-50 dark:bg-blue-900 p-4 rounded-lg border-l-4 border-blue-500">
  <p class="font-bold">💡 矩阵加密算法（Matrix Encryption）</p>
  <p>矩阵加密在计算开销与安全性之间提供了折中方案。然而传统矩阵加密通常采用<b>固定的密钥矩阵和模数</b>，密钥空间有限。若通过预存大量备用矩阵以增强密钥多样性，将<b>显著增加标签的存储开销</b>。</p>
</div>

---
layout: center
class: text-center
---

# 核心创新：三大可变矩阵加密算法

在不增加存储开销的前提下提升安全性

---

## 设计思路：在不增加存储开销的前提下扩充密钥空间

论文的基本思路是：在标签存储受限的条件下，借助**数学变换**，由少量基础矩阵与参数动态生成大量等效的新矩阵。

<div class="grid grid-cols-3 gap-4 mt-6 text-center">
  <div class="bg-green-100 dark:bg-green-900 p-6 rounded-xl shadow transition-transform hover:scale-105">
    <div class="text-4xl mb-4">🔢</div>
    <h3 class="font-bold">AM 算法</h3>
    <p class="text-sm mt-2">自适应模数<br>(Adaptive Modulus)</p>
    <p class="text-xs text-gray-500 mt-2">更新模数</p>
  </div>
  <div class="bg-purple-100 dark:bg-purple-900 p-6 rounded-xl shadow transition-transform hover:scale-105">
    <div class="text-4xl mb-4">🔄</div>
    <h3 class="font-bold">SUEO 算法</h3>
    <p class="text-sm mt-2">自更新加密顺序<br>(Self-Updating Order)</p>
    <p class="text-xs text-gray-500 mt-2">更新加密乘法顺序</p>
  </div>
  <div class="bg-yellow-100 dark:bg-yellow-900 p-6 rounded-xl shadow transition-transform hover:scale-105">
    <div class="text-4xl mb-4">🔀</div>
    <h3 class="font-bold">DBLTKM 算法</h3>
    <p class="text-sm mt-2">对角块局部转置<br>(Block Local Transpose)</p>
    <p class="text-xs text-gray-500 mt-2">更新密钥矩阵结构</p>
  </div>
</div>

---

## AM 算法：自适应模数

**原理**：在传统矩阵加密中，密文 c = A &times; t (mod p)。模数 p 是固定的。
AM 算法表明，若 A 在模 p 下存在逆矩阵，则在 p 的**任意整数因子** q 下同样存在逆矩阵。

<div class="grid grid-cols-2 gap-8 mt-6">
<div>
<p class="text-sm"><b>引理：</b> 若 det(A) 与 p 互质，且 q 是 p 的约数，则 det(A) 与 q 也互质。</p>

<p class="text-sm mt-4"><b>执行流程：</b></p>
<ol class="text-sm">
  <li>提前设定一个合数 p。</li>
  <li>找出 p 的所有正整数约数集合。</li>
  <li>根据当前的私密值 S，动态选择其中一个约数 q 作为当前的加密模数。</li>
</ol>
</div>

<div class="relative h-48 bg-gray-50 dark:bg-gray-800 rounded-lg overflow-hidden flex items-center justify-center border border-gray-200">
  <div class="absolute inset-0 flex flex-col items-center justify-center" style="animation: pulse 2s infinite;">
    <div class="text-2xl font-bold">p = 16</div>
    <div class="flex gap-4 mt-4 text-blue-500">
      <span class="bg-blue-100 dark:bg-blue-900 px-3 py-1 rounded">q=2</span>
      <span class="bg-blue-100 dark:bg-blue-900 px-3 py-1 rounded">q=4</span>
      <span class="bg-blue-100 dark:bg-blue-900 px-3 py-1 rounded">q=8</span>
    </div>
  </div>
</div>
</div>

<p class="mt-6 text-sm text-gray-500 bg-gray-100 dark:bg-gray-800 p-2 rounded">
  <b>性质：</b> 攻击者即便截获当前模数 q，亦无法反推上一轮或下一轮所使用的模数，并且无需额外存储模数表。
</p>

---

## SUEO 算法：自更新加密顺序

**原理**：矩阵乘法**不满足交换律**（A &times; B &ne; B &times; A）。
若存在 N 个基本矩阵，通过改变其连乘顺序，可生成数量可观的复合矩阵。

<div class="mt-6">
  <mermaid>
  graph LR
      A[Matrix A] -->|x| B[Matrix B] -->|Result| AB[Matrix AB]
      B2[Matrix B] -->|x| A2[Matrix A] -->|Result| BA[Matrix BA]
      AB -.->|≠| BA
  </mermaid>
</div>

**计算复杂度与 Winograd 加速**：
- 矩阵连乘会引入较多乘法运算，对低成本标签的算力构成显著负担。
- **解决方法**：引入 **Winograd 快速卷积算法**，通过代数重构将部分**乘法运算转换为加法运算**（标签端加法的能耗显著低于乘法）。
- **效果**：在 n=18 维矩阵情形下，Winograd 算法使乘法操作数减少约 **44.44%**。

---

## 插页：什么是 Winograd 快速卷积算法？

<div class="flex items-center justify-center gap-2 mt-2 text-sm font-mono">
  <span class="text-xl">C =</span>
  <span class="matrix">
    <span>a</span><span>b</span>
    <span>c</span><span>d</span>
  </span>
  <span class="text-lg">&times;</span>
  <span class="matrix">
    <span>e</span><span>f</span>
    <span>g</span><span>h</span>
  </span>
  <span class="text-lg">=</span>
  <span class="matrix">
    <span>C<sub>11</sub></span><span>C<sub>12</sub></span>
    <span>C<sub>21</sub></span><span>C<sub>22</sub></span>
  </span>
  <span class="text-xs text-gray-500 ml-3">如何用最少的乘法得到这 4 个结果元素？</span>
</div>

<div class="grid grid-cols-2 gap-2 mt-3 text-[11px] leading-snug">

<div class="bg-red-50 dark:bg-red-900/20 p-2 rounded border-l-4 border-red-400">
<p class="font-bold text-xs mb-1">❌ 朴素算法</p>
<div class="font-mono naive-grid">
  <span>C<sub>11</sub> = <b class="text-red-600">a·e</b> + <b class="text-red-600">b·g</b></span>
  <span>C<sub>12</sub> = <b class="text-red-600">a·f</b> + <b class="text-red-600">b·h</b></span>
  <span>C<sub>21</sub> = <b class="text-red-600">c·e</b> + <b class="text-red-600">d·g</b></span>
  <span>C<sub>22</sub> = <b class="text-red-600">c·f</b> + <b class="text-red-600">d·h</b></span>
</div>
<p class="mt-1 text-center"><b>8 次乘法</b> + 4 次加法</p>
</div>

<div class="bg-green-50 dark:bg-green-900/20 p-2 rounded border-l-4 border-green-500">
<p class="font-bold text-xs mb-1">✅ Strassen：先算 7 个中间量</p>
<div class="font-mono p-grid">
  <span>P<sub>1</sub> = <b class="text-green-700">(a+d)(e+h)</b></span>
  <span>P<sub>2</sub> = <b class="text-green-700">(c+d) · e</b></span>
  <span>P<sub>3</sub> = <b class="text-green-700">a · (f−h)</b></span>
  <span>P<sub>4</sub> = <b class="text-green-700">d · (g−e)</b></span>
  <span>P<sub>5</sub> = <b class="text-green-700">(a+b) · h</b></span>
  <span>P<sub>6</sub> = <b class="text-green-700">(c−a)(e+f)</b></span>
  <span>P<sub>7</sub> = <b class="text-green-700">(b−d)(g+h)</b></span>
  <span></span>
</div>
<p class="mt-1 text-center"><b>7 次乘法</b> + 18 次加法</p>
</div>

</div>

<p class="mt-2 text-[11px] font-mono bg-gray-100 dark:bg-gray-800 p-2 rounded">
再用加减组合出 <b>同样的</b> 4 个结果：&nbsp;
C<sub>11</sub>=P<sub>1</sub>+P<sub>4</sub>−P<sub>5</sub>+P<sub>7</sub>，&nbsp;
C<sub>12</sub>=P<sub>3</sub>+P<sub>5</sub>，&nbsp;
C<sub>21</sub>=P<sub>2</sub>+P<sub>4</sub>，&nbsp;
C<sub>22</sub>=P<sub>1</sub>−P<sub>2</sub>+P<sub>3</sub>+P<sub>6</sub>
</p>

<p class="mt-2 text-[11px] text-gray-600 p-2 bg-blue-50 dark:bg-blue-900/30 rounded border-l-4 border-blue-500">
<b>要点：</b>两边 C<sub>11</sub>~C<sub>22</sub> 完全相同，但右边乘法从 8 次减到 7 次。硬件上一次乘法功耗 ≫ 一次加法，所以这笔交换划算；递归到 n=18 时乘法整体减少约 <b>44.44%</b>。
</p>

<style scoped>
.matrix {
  display: inline-grid;
  grid-template-columns: repeat(2, 1.6em);
  grid-auto-rows: 1.5em;
  align-items: center;
  justify-items: center;
  padding: 0 0.4em;
  border-left: 2px solid currentColor;
  border-right: 2px solid currentColor;
  font-style: italic;
  font-size: 1.05em;
}
.naive-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2px 12px;
}
.p-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2px 12px;
}
</style>

---

## DBLTKM 算法：对角块局部转置

**原理**：利用矩阵分块（Block）和转置（Transpose）的数学性质。
det(A<sup>T</sup>) = det(A)，且对角分块矩阵的行列式等于各分块行列式的乘积。

<div class="grid grid-cols-2 gap-4 mt-6">
<div class="text-sm">
通过对存储的 N 个矩阵在主对角线上排列，并对部分子矩阵执行**转置**操作，可构造出数量极大的新矩阵。
<br><br>
由于矩阵 A 存在逆矩阵，其转置 A<sup>T</sup> 同样可逆，因此所构造的分块矩阵仍可正确解密。
</div>

<div class="bg-gray-100 dark:bg-gray-700 p-4 rounded text-center">
  <p class="mb-2 font-bold">块矩阵构造示例</p>
  <table class="m-auto border-collapse border border-gray-400">
    <tbody>
      <tr>
        <td class="border border-gray-400 p-2 bg-blue-200 dark:bg-blue-800">A<sub>1</sub></td>
        <td class="border border-gray-400 p-2">0</td>
      </tr>
      <tr>
        <td class="border border-gray-400 p-2">0</td>
        <td class="border border-gray-400 p-2 bg-green-200 dark:bg-green-800">A<sub>2</sub><sup>T</sup></td>
      </tr>
    </tbody>
  </table>
</div>
</div>

<p class="mt-6 text-sm text-gray-500 p-2 border-l-4 border-green-500">
  <b>说明：</b> 仅需存储少量基础矩阵，通过排列组合与转置即可使密钥空间（Key Space）按指数规模扩展，而标签端的存储开销基本不增加。
</p>

---

## 联合算法：AM-SUEO-DBLTKM

将上述三种算法组合，构成最终的**联合加密算法**。
在每一轮认证交互结束后，协议根据通信过程中的随机数与共享密钥，动态确定下一轮所使用的：
1. **块矩阵构造方式**（DBLTKM）
2. **加密乘法顺序**（SUEO）
3. **使用的模数 q**（AM）

<CryptoAnim />

---
layout: center
class: text-center
---

# 协议设计

AM-SUEO-DBLTKM-RFID 身份认证协议

---

## 协议实体与预共享信息

该双向认证协议包含三个实体：**标签 (Tag)**，**阅读器 (Reader)**，**服务器 (Server)**。
三方在初始化阶段预共享了基础密钥矩阵与索引表。

<div class="grid grid-cols-3 gap-4 text-sm mt-6">
  <div class="bg-gray-100 dark:bg-gray-800 p-4 rounded border-t-4 border-blue-500">
    <h3 class="font-bold mb-2 text-blue-500">Tag</h3>
    <ul class="list-disc pl-4">
      <li>加密矩阵 A, B</li>
      <li>初始模数 p</li>
      <li>标签私密值 S</li>
      <li>AM/SUEO/DBLTKM 索引表</li>
    </ul>
  </div>
  <div class="bg-gray-100 dark:bg-gray-800 p-4 rounded border-t-4 border-green-500">
    <h3 class="font-bold mb-2 text-green-500">Reader</h3>
    <ul class="list-disc pl-4">
      <li>解密矩阵 A<sup>-1</sup>, B<sup>-1</sup></li>
      <li>所有标签的私密值 S</li>
      <li>AM/SUEO/DBLTKM 索引表</li>
    </ul>
  </div>
  <div class="bg-gray-100 dark:bg-gray-800 p-4 rounded border-t-4 border-purple-500">
    <h3 class="font-bold mb-2 text-purple-500">Server</h3>
    <ul class="list-disc pl-4">
      <li>与Reader同样的解密参数</li>
      <li>负责生成更新密钥</li>
      <li>完整的数据库后端</li>
    </ul>
  </div>
</div>

---

## 协议流程图 (1/2)：查询与上行认证

<div class="mt-6 text-sm max-h-[300px] overflow-y-auto pr-2 transform scale-90 origin-top">

```mermaid
  sequenceDiagram
      participant T as Tag (标签)
      participant R as Reader (阅读器)
      participant S as Server (服务器)
      
      R->>T: 1. 发送 "Query" 查询请求
      Note over T: 2. 生成随机数 Nt<br/>加密: C1 = E(Nt || S, A, p)
      T->>R: 3. 发送密文 C1
      Note over R: 4. 解密 C1 得到 S。<br/>"先查询后认证": 在本地核对 S。<br/>生成随机数 Nr, 加密 C2 = E(Nr || S, A, p)
      R->>S: 5. 发送密文 C2
      Note over S: 6. 解密 C2 得到 S, 验证 Reader。<br/>生成更新参数 Sd, Sp, Sc。
```

</div>

<p class="text-sm mt-2 p-2 bg-yellow-50 dark:bg-yellow-900 rounded">
  <b>核心机制：先查询后认证 (Query before authentication)</b><br>
  阅读器解密后须在本地数据库中检索到合法的私密值 S 方可继续通信，可有效抵抗 <b>DoS 拒绝服务攻击</b>（来自恶意标签的非法数据会被直接丢弃）。
</p>

---

## 协议流程图 (2/2)：下行认证与密钥自更新

<div class="mt-6 text-sm max-h-[300px] overflow-y-auto pr-2 transform scale-90 origin-top">

```mermaid
  sequenceDiagram
      participant T as Tag (标签)
      participant R as Reader (阅读器)
      participant S as Server (服务器)
      
      Note over S: 加密 C3 = E(Nr || Sd || Sp || Sc, A, p)
      S->>R: 7. 发送密文 C3
      Note over R: 8. 解密 C3，验证 Nr 是否一致。<br/>若一致，提取参数。<br/>加密 C4 = E(Nt || Sd || Sp || Sc, A, p)
      R->>T: 9. 发送密文 C4
      Note over T: 10. 解密 C4，验证 Nt。<br/>根据 Sd, Sp, Sc 更新模数 q 和新矩阵 Anew。<br/>加密 C5 = E(Nt+1 || ID, Anew, q)
      T->>R: 11. 发送密文 C5，证明更新成功
```

</div>

<p class="text-sm mt-2 text-gray-500">
  在第 10 步之后，加密体系（矩阵顺序、分块结构、模数）根据 S<sub>d</sub>, S<sub>p</sub>, S<sub>c</sub> 完成更新，下一轮通信将基于新的矩阵参数进行。
</p>

---

## 协议完整流程展示：双向认证与自更新

<ProtocolAnim />

<p class="text-sm mt-2 p-2 bg-yellow-50 dark:bg-yellow-900 rounded">
  <b>核心机制：先查询后认证 (Query before authentication)</b><br>
  阅读器解密后须在本地核对 S 方可继续通信，可有效抵抗 DoS 攻击。下行认证完成后，加密参数依据 S<sub>d</sub>, S<sub>p</sub>, S<sub>c</sub> 完成更新，下一轮通信将基于新的矩阵参数进行。
</p>

---
layout: center
class: text-center
---

# 安全性分析与形式化证明

安全性论证与攻击模型分析

---

## 形式化证明：BAN 逻辑 (BAN Logic)

为从形式化逻辑层面论证协议的安全性，论文采用 **BAN 逻辑** 进行验证。

<div class="grid grid-cols-2 gap-4 mt-6">
<div class="text-sm">
<b>证明目标：</b><br>
1. 阅读器相信标签发送了随机数 N<sub>t</sub> 和密钥 S。<br>
2. 服务器相信阅读器发送了 N<sub>r</sub> 和 S。<br>
3. 标签和阅读器相信收到了合法的更新参数 S<sub>d</sub>, S<sub>p</sub>, S<sub>c</sub>。
</div>

<div class="bg-gray-100 dark:bg-gray-800 p-2 rounded text-xs overflow-hidden">
<code>
推理过程示意：<br>
从 M1, A1 和 R1 导出：R|≡ T|~{Nt || S}<br>
从 A2 和 R4 导出：R|≡ #{Nt || S}<br>
结合新鲜性 R2，导出：R|≡ T|≡{Nt || S}<br>
最终达成目标 G1：R|≡{Nt || S}
</code>
</div>
</div>

<p class="mt-6 text-sm text-green-600 font-bold">
  结论：BAN 逻辑推导可形成闭环，从形式化层面证明了三方之间的相互认证（Mutual Authentication）成立。
</p>

---

## 抵御典型攻击机制

通过三种可变矩阵加密算法与随机数（N<sub>t</sub>, N<sub>r</sub>）的结合，协议可抵御以下常见 RFID 攻击：

<div class="grid grid-cols-2 gap-4 mt-6 text-sm">
  <div class="p-4 bg-red-50 dark:bg-red-900/30 rounded border-l-4 border-red-500">
    <p class="font-bold text-red-600">重放攻击 (Replay Attack)</p>
    <p>每轮通信均引入新的随机数 N，且加密模数 q 与矩阵结构每轮动态更新，截获的历史密文在后续轮次中不可重用。</p>
  </div>
  <div class="p-4 bg-red-50 dark:bg-red-900/30 rounded border-l-4 border-red-500">
    <p class="font-bold text-red-600">去同步攻击 (De-synchronization)</p>
    <p>标签与阅读器预存索引表，即便某次握手中断导致状态不同步，双方亦可回退至上一轮参数重新协商。</p>
  </div>
  <div class="p-4 bg-red-50 dark:bg-red-900/30 rounded border-l-4 border-red-500">
    <p class="font-bold text-red-600">前向安全性 (Forward Secrecy)</p>
    <p>合数模数 p 的约数 q 具有不可反推性（见图）。攻击者即便获取当前模数 q，也无法反推合数 p 及其他因子。</p>
  </div>
  <div class="p-4 bg-red-50 dark:bg-red-900/30 rounded border-l-4 border-red-500">
    <p class="font-bold text-red-600">位置追踪 (Location Tracking)</p>
    <p>每次返回的密文均由新随机数与自更新矩阵生成，密文呈现伪随机特征，难以通过指纹特征对特定标签进行物理追踪。</p>
  </div>
</div>

---
layout: center
class: text-center
---

# 性能评估与对比

存储与计算复杂度对比

---

## 标签存储开销对比 (Tag Storage Overhead)

在保持等效密钥空间规模的前提下，传统算法与本文所提出的**联合算法**在标签存储开销上存在显著差异。

<div class="text-sm mt-6 bg-gray-50 dark:bg-gray-800 p-4 rounded shadow">
<p>传统无优化算法的存储量：</p>
<p class="text-red-500 font-mono text-xs overflow-hidden whitespace-nowrap overflow-ellipsis">
S<sub>traditional</sub> = C(2N) &times; Z<sub>AM</sub> &times; (2n)<sup>2</sup> + ... + C(2N)<sup>N</sup> &times; Z<sub>AM</sub> &times; (Nn)<sup>2</sup> + 1
</p>
<p class="mt-4">AM-SUEO-DBLTKM 联合算法的存储量（仅需保存少量基础矩阵）：</p>
<p class="text-green-500 font-mono text-xs overflow-hidden whitespace-nowrap overflow-ellipsis">
S<sub>proposed</sub> = N &times; n<sup>2</sup> + Z<sub>AM</sub> + Z<sub>SUEO</sub> + Z<sub>DBLTKM</sub>
</p>
</div>

**存储节省率 (K) 测试结果**：
当基础密钥矩阵数 N=2、明文长度 n=2、模数因子数 Q=2 时，联合算法的标签存储节省率达到 **99.59%**；随参数规模扩大，节省率趋近于 **99.9%**。

---

## 计算复杂度优化 (Computational Complexity)

对于低成本 RFID 标签而言，计算资源往往比存储资源更为紧张。
其中矩阵乘法所涉及的 **乘法门（Multiplication Gates）** 功耗较高。

<div class="grid grid-cols-2 gap-4 mt-6 items-center">
  <div>
    <p class="font-bold text-blue-500 mb-2">Winograd 算法加速</p>
    <ul class="text-sm list-disc pl-4 space-y-2">
      <li>传统矩阵乘法：n<sup>3</sup> 次乘法</li>
      <li>Winograd 加速：乘法次数减少，部分被替换为低功耗的加法操作</li>
      <li>在 n=18 维度下，乘法操作减少约 <b>44.44%</b></li>
      <li>加法操作约增加 15%</li>
    </ul>
  </div>
  
  <div class="bg-gray-100 dark:bg-gray-800 p-4 rounded-xl flex items-center justify-center h-48 relative">
    <div class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center w-full">
      <div class="text-4xl">📉 -44%</div>
      <div class="text-sm text-gray-500 mt-2">Multiplication Cost</div>
    </div>
  </div>
</div>

---
layout: center
class: text-center
---

# 总结

Conclusions

---

## 论文核心贡献总结

<div class="text-left mt-6 space-y-4">

1. **三种轻量级矩阵变换机制：**
   - 提出 AM（模数自适应）、SUEO（乘法顺序自更新）、DBLTKM（块对角局部转置）三种加密机制，在**不增加额外存储**的前提下，使矩阵密钥空间呈指数级扩展。

2. **面向标签端的计算优化：**
   - 引入 **Winograd 快速卷积算法**，以少量加法运算的增加换取近一半乘法开销的降低，缓解了矩阵加密在低成本标签上的计算压力。

3. **双向认证协议设计：**
   - 设计了完整的 `AM-SUEO-DBLTKM-RFID` 移动协议流程。
   - 通过 BAN 逻辑完成形式化正确性证明，在保持安全强度的同时实现 **99.59%** 的存储节省，适用于资源受限的 IoT 与 6G 移动传感网络场景。

</div>

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
