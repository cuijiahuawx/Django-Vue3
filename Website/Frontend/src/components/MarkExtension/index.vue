<template>
  <NormalToolBar title="mark" @on-click="markHandler">
    <template #trigger>
      <n-icon size="20" style="margin-top:1px">
        <LightbulbFilament16Regular />
      </n-icon>
    </template>
  </NormalToolBar>
</template>

<script setup lang="ts">
import type { PropType } from 'vue';
import MdEditor from 'md-editor-v3'
import { LightbulbFilament16Regular } from '@vicons/fluent'

const NormalToolBar = MdEditor.NormalToolbar
const props = defineProps({
  editorId: {
    type: String as PropType<string>,
    default: ''
  }
});

const emit = defineEmits(['onChange']);

const markHandler = () => {
  // 获取输入框
  const textarea = document.querySelector(
    `#${props.editorId}-textarea`
  ) as HTMLTextAreaElement;
  // 获取选中的内容
  const selection = window.getSelection()?.toString();
  // 获取鼠标位置
  const endPoint = textarea.selectionStart;

  // 生成标记文本
  const markStr = `@${selection}@`;

  // 根据鼠标位置分割旧文本
  // 前半部分
  const prefixStr = textarea.value.substring(0, endPoint);
  // 后半部分
  const suffixStr = textarea.value.substring(endPoint + (selection?.length || 0));

  emit('onChange', `${prefixStr}${markStr}${suffixStr}`);

  setTimeout(() => {
    textarea.setSelectionRange(endPoint, markStr.length + endPoint);
    textarea.focus();
  }, 0);
};
</script>

<script lang="ts">
export default {
  name: 'MarkExtension'
};
</script>
