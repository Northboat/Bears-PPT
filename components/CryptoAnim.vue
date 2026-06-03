<script setup>
import { ref, onUnmounted } from 'vue'

const activeStep = ref(0)
const isPlaying = ref(false)
const isFinished = ref(false)
let timerId = null

const steps = [
  { id: 0, title: '① 数据准备', desc: '明文 t 与 随机数', icon: '📥' },
  { id: 1, title: '② DBLTKM', desc: '矩阵局部转置 A→Aᵀ', icon: '🔲' },
  { id: 2, title: '③ SUEO', desc: '加密乘法洗牌 Aᵀ×B', icon: '🔀' },
  { id: 3, title: '④ AM', desc: '自适应模数 mod q', icon: '➗' },
  { id: 4, title: '⑤ 生成密文', desc: '输出动态密文 c', icon: '🔒' },
]

const clearTimer = () => {
  if (timerId) {
    clearTimeout(timerId)
    timerId = null
  }
}

const playStep = () => {
  if (activeStep.value < steps.length - 1) {
    timerId = setTimeout(() => {
      activeStep.value++
      playStep()
    }, 2000)
  } else {
    isPlaying.value = false
    isFinished.value = true
  }
}

const play = () => {
  if (isFinished.value) {
    activeStep.value = 0
    isFinished.value = false
  }
  isPlaying.value = true
  playStep()
}

const pause = () => {
  clearTimer()
  isPlaying.value = false
}

const replay = () => {
  clearTimer()
  activeStep.value = 0
  isFinished.value = false
  isPlaying.value = true
  playStep()
}

onUnmounted(() => {
  clearTimer()
})
</script>

<template>
  <div class="relative w-full h-[240px] bg-[#1a1a2e] rounded-xl overflow-hidden border border-gray-700 shadow-2xl flex items-center justify-center p-6 my-6">
    <!-- Background Grid -->
    <div class="absolute inset-0 opacity-20 pointer-events-none" style="background-image: linear-gradient(#4f4f4f 1px, transparent 1px), linear-gradient(90deg, #4f4f4f 1px, transparent 1px); background-size: 20px 20px;"></div>

    <!-- Animated Progress Line -->
    <div class="absolute top-[40%] left-12 right-12 h-1 bg-gray-700 -translate-y-1/2 z-0 rounded-full">
       <div class="h-full bg-cyan-400 transition-all duration-700 ease-in-out shadow-[0_0_10px_cyan]" :style="{ width: (activeStep / (steps.length - 1)) * 100 + '%' }"></div>
    </div>

    <!-- Steps -->
    <div class="flex justify-between w-full relative z-10 px-2">
      <div v-for="step in steps" :key="step.id" class="flex flex-col items-center transition-all duration-500" :class="activeStep >= step.id ? 'opacity-100' : 'opacity-30'">

        <!-- Icon Circle -->
        <div class="w-14 h-14 rounded-full flex items-center justify-center border-2 transition-all duration-500 z-10 bg-[#16213e]"
             :class="activeStep === step.id ? 'border-cyan-400 scale-125 shadow-[0_0_20px_rgba(34,211,238,0.6)]' : (activeStep > step.id ? 'border-green-400 bg-green-900/30' : 'border-gray-600')">
          <span class="text-2xl">{{ step.icon }}</span>
        </div>

        <!-- Text Info -->
        <div class="mt-6 text-center transform transition-all duration-500" :class="activeStep === step.id ? 'scale-110' : ''">
          <div class="font-bold text-sm tracking-wide" :class="activeStep === step.id ? 'text-cyan-300' : 'text-gray-300'">{{ step.title }}</div>
          <div class="text-xs mt-1 font-mono tracking-tighter" :class="activeStep === step.id ? 'text-cyan-100' : 'text-gray-500'">{{ step.desc }}</div>
        </div>

      </div>
    </div>

    <!-- Active Processing Overlay (Optional visual flair) -->
    <div v-if="activeStep > 0 && activeStep < 4 && isPlaying" class="absolute inset-0 pointer-events-none flex items-center justify-center opacity-10">
       <div class="w-full h-full animate-pulse bg-gradient-to-r from-transparent via-cyan-400 to-transparent"></div>
    </div>

    <!-- Control Bar -->
    <div class="ctrl-bar absolute bottom-2 right-2 z-30 flex items-center gap-1 px-2 py-1 bg-black/20 hover:bg-black/50 backdrop-blur-sm rounded-full border border-gray-600/30 hover:border-gray-500/60 shadow transition-all duration-300 opacity-40 hover:opacity-100">
      <button v-if="!isPlaying && !isFinished" @click="play"
              class="ctrl-btn text-cyan-300 hover:text-cyan-100 hover:bg-cyan-500/20"
              title="播放">
        <svg viewBox="0 0 24 24" class="w-3 h-3" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
      </button>
      <button v-if="isPlaying" @click="pause"
              class="ctrl-btn text-amber-300 hover:text-amber-100 hover:bg-amber-500/20"
              title="暂停">
        <svg viewBox="0 0 24 24" class="w-3 h-3" fill="currentColor"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
      </button>
      <button @click="replay"
              class="ctrl-btn text-gray-300 hover:text-white hover:bg-gray-500/20"
              title="重播">
        <svg viewBox="0 0 24 24" class="w-3 h-3" fill="currentColor"><path d="M12 5V1L7 6l5 5V7c3.31 0 6 2.69 6 6s-2.69 6-6 6-6-2.69-6-6H4c0 4.42 3.58 8 8 8s8-3.58 8-8-3.58-8-8-8z"/></svg>
      </button>
      <span class="text-[10px] font-mono text-gray-400 pl-0.5 pr-0.5 select-none leading-none">{{ Math.min(activeStep + 1, steps.length) }}/{{ steps.length }}</span>
    </div>
  </div>
</template>

<style scoped>
.ctrl-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 9999px;
  transition: all 0.2s ease;
}
</style>
