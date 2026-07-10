# 秋招信息新增 Skill — job-hunt

每次用户贴入新招聘信息，按本 skill 操作，将其转换成一页标准格式的 Slidev 信息页，插入 `slides.md` 对应分类章节下。

---

## 1. 文件位置

编辑目标：项目根目录 `slides.md`

## 2. 分类规则

用户贴入信息后，先判断公司归属：

| 分类 | 判断标准 | 章节关键词 |
|---|---|---|
| 大厂 | 字节、腾讯、阿里、华为、百度（如用户重新分类）等头部 | `# 大厂` |
| 中厂 | 米哈游、百度、科大讯飞、网易、京东等中型互联网 | `# 中厂` |
| 国央企 | 中国移动、国家电网、中兴、中国电信等 | `# 国央企` |
| 研究所 | 中科院、各高校研究院、军工研究所等 | `# 研究所` |

若用户明确说明归属，以用户说法为准。

新增页面插入位置：对应分类的**最后一个 `##` 页面之后**，下一个 `---` 之前。

同时更新对应章节页（`# 大厂` / `# 中厂` 等）的入口卡片，加上新公司图标和名称。

---

## 3. 标准信息页模板

每家公司一页，使用以下模板，左侧 Hero 卡 + 右侧亮点卡：

```markdown
---

## 公司名

<div class="grid grid-cols-5 gap-5 mt-4 h-70">

<div class="col-span-2 bg-gradient-to-br from-COLOR-600 to-COLOR-900 rounded-2xl p-5 flex flex-col justify-between text-white shadow-xl shadow-COLOR-900/40">
  <div>
    <div class="text-4xl mb-3">EMOJI</div>
    <div class="text-2xl font-black tracking-wide">公司名</div>
    <div class="text-xs opacity-60 mt-1 font-medium uppercase tracking-widest">英文名 · 项目/批次名</div>
  </div>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between border-b border-white/15 pb-1.5">
      <span class="opacity-50">岗位</span><span class="font-semibold">岗位内容</span>
    </div>
    <div class="flex justify-between border-b border-white/15 pb-1.5">
      <span class="opacity-50">对象</span><span class="font-semibold">届次 + 学历要求</span>
    </div>
    <div class="flex justify-between border-b border-white/15 pb-1.5">
      <span class="opacity-50">地点</span><span class="font-semibold">城市（若有）</span>
    </div>
    <div class="flex justify-between">
      <span class="opacity-50">截止</span><span class="font-bold text-yellow-300">YYYY.MM.DD（若有）</span>
    </div>
  </div>
  <a href="投递链接" target="_blank" class="mt-4 block text-center text-xs bg-white/15 hover:bg-white/25 rounded-xl py-2 font-bold transition-all tracking-wide">🔗 投递链接文字</a>
</div>

<div class="col-span-3 flex flex-col gap-3">
  <div class="text-xs font-bold text-COLOR-500 uppercase tracking-widest pl-1">项目/活动名称</div>
  <div class="grid grid-cols-2 gap-2.5 flex-1">
    <div class="bg-gradient-to-br from-COLOR1-500 to-COLOR1-600 rounded-xl p-3.5 text-white shadow-md shadow-COLOR1-500/30">
      <div class="font-black text-sm">亮点一标题</div>
      <div class="text-xs opacity-80 mt-0.5">亮点一说明</div>
    </div>
    <div class="bg-gradient-to-br from-COLOR2-500 to-COLOR2-600 rounded-xl p-3.5 text-white shadow-md shadow-COLOR2-500/30">
      <div class="font-black text-sm">亮点二标题</div>
      <div class="text-xs opacity-80 mt-0.5">亮点二说明</div>
    </div>
    <div class="bg-gradient-to-br from-COLOR3-500 to-COLOR3-600 rounded-xl p-3.5 text-white shadow-md shadow-COLOR3-500/30">
      <div class="font-black text-sm">亮点三标题</div>
      <div class="text-xs opacity-80 mt-0.5">亮点三说明</div>
    </div>
    <div class="bg-gradient-to-br from-COLOR4-500 to-COLOR4-600 rounded-xl p-3.5 text-white shadow-md shadow-COLOR4-500/30">
      <div class="font-black text-sm">亮点四标题</div>
      <div class="text-xs opacity-80 mt-0.5">亮点四说明</div>
    </div>
  </div>
  <div class="bg-COLOR-50 rounded-xl px-4 py-2.5 border border-COLOR-100 text-xs text-COLOR-900 shadow-sm">
    补充说明或时间流程一行摘要
  </div>
</div>

</div>
```

---

## 4. 颜色分配规则

Hero 卡主色按分类统一，右侧亮点卡用固定的四色搭配：

| 分类 | Hero 卡主色 COLOR | 右侧四色 COLOR1~4 |
|---|---|---|
| 大厂 | `orange` | orange · blue · emerald · rose |
| 中厂 | 公司自定（blue/amber/violet…） | 同左或自选 |
| 国央企 | `emerald` | emerald · blue · amber · rose |
| 研究所 | `sky` | sky · blue · emerald · violet |

已有公司颜色参考：
- 百度：`blue`
- 米哈游：`amber/orange`
- 科大讯飞：`violet`

新公司颜色不得与同一章节下已有公司重复。

---

## 5. 亮点卡提取规则

从原始招聘信息中提取**最多 4 个核心亮点**，优先顺序：

1. 特殊流程（免笔试、提前批、内推加速）
2. 核心数字（扩招比例、薪资范围、轮岗年限）
3. 培养方式（导师制、管培项目、晋升通道）
4. 优先条件（专业/经历要求）

亮点卡标题控制在 **4~6 个汉字**，说明控制在 **10 个字以内**。

---

## 6. 链接处理

- 有内推链接 → `<a href="..." target="_blank">` 放在 Hero 卡底部按钮
- 有内推码 → 在右侧底部加深色 bar：
  ```html
  <div class="bg-slate-800 rounded-xl px-4 py-2.5 flex items-center justify-between shadow-lg shadow-slate-900/40">
    <span class="text-xs text-amber-300 font-semibold uppercase tracking-widest">专属内推码</span>
    <span class="text-xl font-black font-mono tracking-widest text-yellow-400">XXXX</span>
  </div>
  ```
- 无链接 → 按钮区域省略

---

## 7. 章节页入口卡片更新

每次新增公司后，找到对应的章节页（`layout: center` + `# 大厂/中厂/...`），在入口卡片 div 中追加：

```html
<div class="px-8 py-4 bg-COLOR-500 rounded-2xl shadow-lg transition-transform hover:scale-105 cursor-pointer">
  <div class="text-3xl mb-1">EMOJI</div>
  <div class="text-sm font-bold text-white">公司名</div>
</div>
```

章节页若当前显示"信息整理中"占位卡，将其替换为真实公司卡。

---

## 8. 编译安全规则（来自主 SKILL.md）

- **禁止在 SVG / HTML 内写 `<!-- 注释 -->`**，Vue 模板解析器会报错
- **禁止 `<feMerge>` 等嵌套 SVG filter 标签**
- **禁止内容溢出**：单页内容高度固定为 `h-70`，不加滚动 div
- **链接必须用 `<a href="..." target="_blank">`**，不能是纯文本 URL

---

## 9. 操作 Checklist

收到用户贴入的招聘信息后，按顺序执行：

- [ ] 判断公司分类
- [ ] 读取 `slides.md` 找到对应章节最后一个公司页的位置
- [ ] 按模板生成新页面，填入提取的信息
- [ ] 将新页面插入正确位置
- [ ] 更新对应章节页的入口卡片
- [ ] 确认没有 HTML 注释、没有内容溢出
