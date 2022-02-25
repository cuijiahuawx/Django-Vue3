<template>
  <router-view/>
  <BaseHeader :msg="userinfo"/>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const userinfo = ref('yes')

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
