<script setup>
import { ref, onUnmounted, nextTick } from 'vue'

const activeStep = ref(-1)
const scrollContainer = ref(null)
const isPlaying = ref(false)
const isFinished = ref(false)
let timerId = null

const steps = [
  {
    id: 0,
    actor: 'Reader', target: 'Tag',
    action: '1. 发送 "Query"',
    detail: '发起查询请求',
    direction: 'right'
  },
  {
    id: 1,
    actor: 'Tag', target: '',
    action: '2. Tag 计算',
    detail: '生成随机数 Nt\n加密 C1 = E(Nt || S, A, p)',
    direction: 'center'
  },
  {
    id: 2,
    actor: 'Tag', target: 'Reader',
    action: '3. 发送 C1',
    detail: 'Tag 将密文 C1 发给 Reader',
    direction: 'left'
  },
  {
    id: 3,
    actor: 'Reader', target: 'Server',
    action: '4. Reader 计算与转发',
    detail: '解密核对S (先查询后认证)\n生成Nr, 加密 C2 = E(Nr || S, A, p)\n发送 C2',
    direction: 'right'
  },
  {
    id: 4,
    actor: 'Server', target: 'Reader',
    action: '5. Server 计算与下发',
    detail: '验证 Reader\n生成更新参数 Sd, Sp, Sc\n加密 C3 = E(Nr || Sd || Sp || Sc, A, p)\n发送 C3',
    direction: 'left'
  },
  {
    id: 5,
    actor: 'Reader', target: 'Tag',
    action: '6. Reader 转发下行认证',
    detail: '解密 C3 验证 Nr\n加密 C4 = E(Nt || Sd || Sp || Sc, A, p)\n发送 C4',
    direction: 'left'
  },
  {
    id: 6,
    actor: 'Tag', target: '',
    action: '7. Tag 验证与自更新',
    detail: '解密 C4, 验证 Nt\n根据 Sd, Sp, Sc 更新模数 q 和 Anew\n加密 C5 = E(Nt+1 || ID, Anew, q)',
    direction: 'center'
  },
  {
    id: 7,
    actor: 'Tag', target: 'Reader',
    action: '8. 完成认证',
    detail: '发送 C5, 证明更新成功',
    direction: 'left'
  }
]

const clearTimer = () => {
  if (timerId) {
    clearTimeout(timerId)
    timerId = null
  }
}

const scrollToBottom = () => {
  nextTick(() => {
    if (scrollContainer.value) {
      scrollContainer.value.scrollTop = scrollContainer.value.scrollHeight
    }
  })
}

const playStep = () => {
  if (activeStep.value < steps.length - 1) {
    activeStep.value++
    scrollToBottom()
    timerId = setTimeout(playStep, 2000)
  } else {
    isPlaying.value = false
    isFinished.value = true
  }
}

const play = () => {
  if (isFinished.value) {
    activeStep.value = -1
    isFinished.value = false
  }
  isPlaying.value = true
  timerId = setTimeout(playStep, 300)
}

const pause = () => {
  clearTimer()
  isPlaying.value = false
}

const replay = () => {
  clearTimer()
  activeStep.value = -1
  isFinished.value = false
  isPlaying.value = true
  if (scrollContainer.value) scrollContainer.value.scrollTop = 0
  timerId = setTimeout(playStep, 300)
}

onUnmounted(() => {
  clearTimer()
})
</script>

<template>
  <div class="relative w-full h-[320px] bg-gray-900 rounded-xl overflow-hidden border border-gray-700 shadow-2xl flex flex-col p-3 my-2 font-sans text-gray-200">

    <!-- Entities row -->
    <div class="flex justify-between items-center w-full px-12 mt-4 z-20">
      <div class="flex flex-col items-center">
        <div class="w-16 h-16 bg-blue-600 rounded-full flex items-center justify-center text-2xl shadow-[0_0_15px_rgba(37,99,235,0.6)]">🏷️</div>
        <div class="mt-2 font-bold text-blue-400">Tag</div>
      </div>
      <div class="flex flex-col items-center">
        <div class="w-16 h-16 bg-green-600 rounded-full flex items-center justify-center text-2xl shadow-[0_0_15px_rgba(22,163,74,0.6)]">📡</div>
        <div class="mt-2 font-bold text-green-400">Reader</div>
      </div>
      <div class="flex flex-col items-center">
        <div class="w-16 h-16 bg-purple-600 rounded-full flex items-center justify-center text-2xl shadow-[0_0_15px_rgba(147,51,234,0.6)]">💻</div>
        <div class="mt-2 font-bold text-purple-400">Server</div>
      </div>
    </div>

    <!-- Communication lines background -->
    <div class="absolute top-[80px] bottom-10 left-[110px] w-0.5 bg-gray-700 border-dashed border-l-2 border-gray-600 opacity-30 z-0"></div>
    <div class="absolute top-[80px] bottom-10 left-1/2 w-0.5 bg-gray-700 border-dashed border-l-2 border-gray-600 opacity-30 z-0"></div>
    <div class="absolute top-[80px] bottom-10 right-[110px] w-0.5 bg-gray-700 border-dashed border-l-2 border-gray-600 opacity-30 z-0"></div>

    <!-- Message Display Area -->
    <div class="flex-1 relative mt-4 z-10 w-full overflow-y-auto max-h-[160px] pb-6 pr-2 custom-scrollbar" ref="scrollContainer">
       <transition-group name="list" tag="div" class="flex flex-col items-center space-y-3">
         <div v-for="(step, index) in steps" :key="step.id"
              v-show="activeStep >= index"
              class="w-full flex"
              :class="{
                'justify-center': step.direction === 'center',
                'justify-start pl-[20%]': step.actor === 'Tag' && step.direction === 'right',
                'justify-start pl-[50%]': step.actor === 'Reader' && step.direction === 'right',
                'justify-end pr-[50%]': step.actor === 'Reader' && step.direction === 'left',
                'justify-end pr-[20%]': step.actor === 'Server' && step.direction === 'left',
              }">

           <div class="max-w-[40%] bg-gray-800 border-l-4 p-3 rounded shadow-lg transform transition-all"
                :class="{
                  'border-blue-500 opacity-100 scale-100': activeStep === index,
                  'border-gray-500 opacity-40 scale-95': activeStep > index,
                  'border-green-500': step.actor === 'Reader',
                  'border-purple-500': step.actor === 'Server',
                  'border-blue-400': step.actor === 'Tag',
                }">
             <div class="text-sm font-bold flex items-center gap-2"
                  :class="activeStep === index ? 'text-white' : 'text-gray-400'">
                <span v-if="step.direction === 'right'" class="text-xs">➡️</span>
                <span v-if="step.direction === 'left'" class="text-xs">⬅️</span>
                <span v-if="step.direction === 'center'" class="text-xs">⚙️</span>
                {{ step.action }}
             </div>
             <div class="text-xs mt-1 font-mono whitespace-pre-wrap"
                  :class="activeStep === index ? 'text-cyan-300' : 'text-gray-500'">
               {{ step.detail }}
             </div>
           </div>

         </div>
       </transition-group>
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
      <span class="text-[10px] font-mono text-gray-400 pl-0.5 pr-0.5 select-none leading-none">{{ Math.max(activeStep + 1, 0) }}/{{ steps.length }}</span>
    </div>
  </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: rgba(31, 41, 55, 0.5);
  border-radius: 4px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(75, 85, 99, 0.8);
  border-radius: 4px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: rgba(107, 114, 128, 1);
}

.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

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
