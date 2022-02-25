<script setup lang="ts">
  import Navbar from './components/Navbar.vue'
  import { storeToRefs } from "pinia";
  import { MusicInfoStore } from "~/store/musicInfo"
  import MusicPlayer from "~/components/MusicPlayer.vue"
  const musicInfo = MusicInfoStore()
  const { musicStatus } = storeToRefs(musicInfo)
</script>

<template>
    <n-layout style="height: 715px;" ref="container">
        <n-layout-header style="height: 64px;" bordered>
          <Navbar/>
        </n-layout-header>
        <router-view/>
        
        <n-space v-if="musicStatus" >
          <music-player />
        </n-space>
  

    </n-layout>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.light-green {
  height: 108px;
  background-color: rgba(0, 128, 0, 0.12);
}
</style>
