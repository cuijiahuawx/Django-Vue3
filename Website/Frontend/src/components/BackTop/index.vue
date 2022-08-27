<template>
  <div v-if="scrollTop > 20" class="back-top" @click="backTop">
    <n-icon size="40" style="margin-top:1px">
      <ArrowCircleUp12Regular />
    </n-icon>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { ArrowCircleUp12Regular } from '@vicons/fluent'

onMounted(() => {
  console.log("hello arrow")
})

const scrollTop = ref(0)

const backTop = () => {
  document.documentElement.scroll({
    top: 0,
    behavior: 'smooth'
  });
};

onMounted(() => {
  document.addEventListener('scroll', () => {
    scrollTop.value = document.documentElement.scrollTop;
  });
});
</script>

<script lang="ts">
export default {
  name: 'IzBackTop'
};
</script>

<style>
.back-top {
  position: fixed;
  right: 40px;
  bottom: 30px;
  font-size: 26px;
  cursor: pointer;
}
</style>
