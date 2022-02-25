<script lang="ts" setup>
    import { storeToRefs } from "pinia";
    import { reactive } from "vue";
    import { MusicInfoStore } from "~/store/musicInfo"
    import MusicPlayer from "~/components/MusicPlayer.vue"

    const musicInfo = MusicInfoStore()
    const { musicStatus, musicSongs } = storeToRefs(musicInfo)

    const form = reactive({
        phone: '',
        password: '',
        musicList: ''
    })

    const login = () => {
        musicInfo.login(form.phone, form.password, form.musicList)
    }
</script>

<template>
<n-grid x-gap="12" :cols="3">
    <n-gi>
    </n-gi>
    <n-gi>
      <n-card>
            <n-form>
              <n-form-item-row label="网易云邮箱">
                <n-input v-model:value="form.phone" />
              </n-form-item-row>
              <n-form-item-row label="密码">
                <n-input 
                  type="password"
                  show-password-on="mousedown"
                  placeholder="密码"
                v-model:value="form.password" />
              </n-form-item-row>
              <n-form-item-row label="歌单号">
                <n-input v-model:value="form.musicList" />
              </n-form-item-row>
            </n-form>
            <n-button type="primary" block secondary strong @click="login">
              登录
            </n-button>
      </n-card>
    </n-gi>
    <n-gi>
    </n-gi>
  </n-grid>
</template>

<style>
</style>