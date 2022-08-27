<script lang="ts" setup>
    import { useWebSocket } from '@vueuse/core'

    const { status, data, send, open, close } = useWebSocket("ws://127.0.0.1:8000/chat/room/123/")

</script> 
<template>
<p>消息</p>
    {{data}}
    <n-button style="margin-top:15px;" type="primary" @click="send('我是VUE3向你发来亲切的问候')">
        发送消息
    </n-button>
</template>
<style scoped>

</style>    