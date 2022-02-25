<template>
  <n-space>
    <n-button @click="handleConfirm"> 警告 </n-button>
  </n-space>
</template>

<script>
import { defineComponent } from 'vue'
import { useMessage, useDialog } from 'naive-ui'

export default defineComponent({
  setup () {
    const message = useMessage()
    const dialog = useDialog()
    return {
      handleConfirm () {
        dialog.warning({
          title: '警告',
          content: '你确定？',
          positiveText: '确定',
          negativeText: '不确定',
          onPositiveClick: () => {
            message.success('确定')
          },
          onNegativeClick: () => {
            message.error('不确定')
          }
        })
      },
      handleSuccess () {
        dialog.success({
          title: '成功',
          content: '厉害',
          positiveText: '哇',
          onPositiveClick: () => {
            message.success('耶！')
          }
        })
      },
      handleError () {
        dialog.error({
          title: '错误',
          content: '错了',
          positiveText: '啊',
          onPositiveClick: () => {
            message.success('我就知道')
          }
        })
      }
    }
  }
})
</script>