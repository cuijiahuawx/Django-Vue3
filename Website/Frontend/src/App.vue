<script setup lang="ts">
// 引入官方相关库
import { onMounted, ref } from "vue";
// Pinia引入存储
import { storeToRefs } from "pinia";
import { MusicInfoStore } from "~/store/musicInfo"
// 引入第三方组件
import MusicPlayer from "~/components/MusicPlayer.vue"
import AppProvider from '~/components/AppProvider/index.vue'
// 引入自定义组件
import Navbar from "./components/Navbar.vue";
// Pinia存储设置
const musicInfo = MusicInfoStore()
const { musicStatus } = storeToRefs(musicInfo)

// 解决登陆后是否缓存
let beforeUnloadTime = ref(0)
let gapTime = ref(0)
const beforeunloadHandler = () => {
  beforeUnloadTime.value = new Date().getTime();
}
const unloadHandler = () => {
  gapTime.value = new Date().getTime() - beforeUnloadTime.value;
  const remember = JSON.parse(localStorage.user)["remember"]
  //判断是窗口关闭还是刷新
  if (gapTime.value <= 5 && !remember) {  //浏览器关闭
    localStorage.clear()
  }
}
onMounted(() => {
  //监听页面卸载（关闭）或刷新
  window.addEventListener('beforeunload', () => beforeunloadHandler())
  window.addEventListener('unload', () => unloadHandler())
})
</script>

<template>
  <AppProvider>
    <n-space vertical size="large">
      <n-layout>

        <n-layout-header>
          <Navbar />
        </n-layout-header>

        <n-layout-content>
          <router-view :key="$route.fullPath" />
        </n-layout-content>

        <n-layout-footer>
        </n-layout-footer>

      </n-layout>
      <n-affix v-if="musicStatus">
        <music-player />
      </n-affix>
    </n-space>
  </AppProvider>
</template>

<style>
html,
body {
  padding: 0;
  margin: 0;
}

#app {
  height: 100vh;
  width: 100vw;
}
</style>
