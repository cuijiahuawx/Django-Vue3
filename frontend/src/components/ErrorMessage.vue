<script lang="ts" setup>
    import { useMessage } from 'naive-ui'

    const message = useMessage()

    const showMessage = (msg: string) => {
        message.error(msg)
    }
    defineExpose({
        showMessage
    })
</script>

<template>
</template>

<style>
</style>