<template>
  <ModalToolbar :visible="state.visible" :is-fullscreen="state.modalFullscreen" show-adjust title="帮助"
    modal-title="编辑预览" width="870px" height="600px" @on-click="state.visible = true" @on-close="state.visible = false"
    @on-adjust="state.modalFullscreen = !state.modalFullscreen">
    <div v-if="state.visible" style="height: 100%; padding: 20px; overflow: auto">
      <MdEditor editor-id="edit2preview" preview-only :model-value="props.mdText" />
    </div>
    <template #trigger>
      <n-icon size="20" style="margin-top:1px">
        <Flashlight24Regular />
      </n-icon>
    </template>
  </ModalToolbar>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue';
import type { PropType } from 'vue';

import MdEditor from 'md-editor-v3'
import { Flashlight24Regular } from '@vicons/fluent'



const ModalToolbar = MdEditor.ModalToolbar

const props = defineProps({
  mdText: {
    type: String as PropType<string>,
    default: "hello"
  }
});

const state = reactive({
  visible: false,
  modalFullscreen: false
});


</script>

<script lang="ts">
export default {
  name: 'ReadExtension'
};
</script>
