<script lang="ts" setup>
    import { useMessage } from 'naive-ui'

    const message = useMessage()


    const showMessage = (msg: string) => {
        message.success(msg)
    }
    defineExpose({
        showMessage
    })
</script>

<template>
</template>

<style>
</style>