<template>
  <DropdownToolbar title="emoji" :visible="state.visible" @on-change="onChange">
    <template #overlay>
      <div>
        <ol class="emojis">
          <li v-for="(emoji, index) of emojis" :key="`emoji-${index}`" @click="emojiHandler(emoji)" v-text="emoji"></li>
        </ol>
      </div>
    </template>
    <template #trigger>
      <n-icon size="20" style="margin-top:1px">
        <EmojiLaugh20Regular />
      </n-icon>
    </template>
  </DropdownToolbar>
</template>

<script lang="ts" setup>
import { onMounted, reactive } from 'vue';
import type { PropType } from 'vue';
import { emojis } from './data';
import { EmojiLaugh20Regular } from '@vicons/fluent'
import MdEditor from 'md-editor-v3'
const DropdownToolbar = MdEditor.DropdownToolbar

const props = defineProps({
  editorId: {
    type: String as PropType<string>,
    default: ''
  }
});

const emit = defineEmits(['onChange']);

const state = reactive({
  visible: false
});

const emojiHandler = (emoji: string) => {
  // 获取输入框
  const textarea = document.querySelector(
    `#${props.editorId}-textarea`
  ) as HTMLTextAreaElement;
  // 获取选中的内容
  const selection = window.getSelection()?.toString();
  // 获取鼠标位置
  const endPoint = textarea.selectionStart;

  // 根据鼠标位置分割旧文本
  // 前半部分
  const prefixStr = textarea.value.substring(0, endPoint);
  // 后半部分
  const suffixStr = textarea.value.substring(endPoint + (selection?.length || 0));

  emit('onChange', `${prefixStr}${emoji}${suffixStr}`);

  setTimeout(() => {
    textarea.setSelectionRange(endPoint, endPoint + 1);
    textarea.focus();
  }, 0);
};

const onChange = (visible: boolean) => {
  state.visible = visible;
};
</script>

<script lang="ts">
export default {
  name: 'EmojiExtension'
};
</script>
<style scoped>
.emojis {
  position: relative;
  width: 363px;
  margin: 10px;
  padding: 0;
  background-color: #fff;
}

li {
  cursor: pointer;
  float: left;
  border: 1px solid #e8e8e8;
  height: 24px;
  width: 28px;
  overflow: hidden;
  margin: -1px 0 0 -1px;
  padding: 4px 2px;
  text-align: center;
  list-style: none;
  z-index: 11;
}
</style>
