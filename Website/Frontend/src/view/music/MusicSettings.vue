<script lang="ts" setup>
    import { reactive } from "vue";

    import { storeToRefs } from "pinia"
    import { UserInfoStore } from "~/store/userInfo"
    import { MusicInfoStore } from "~/store/musicInfo"
    // 引入Pinia存储
    const userInfo = UserInfoStore()
    const { musicEmail, musicID } = storeToRefs(userInfo)
    const musicInfo = MusicInfoStore()

    const form = reactive({
        password: ''
    })

    const login = () => {
      musicInfo.logout()
      musicInfo.login(musicEmail, form.password, musicID)
    }
</script>

<template>
<n-grid x-gap="12" :cols="3">
    <n-gi>
    </n-gi>
    <n-gi>
      <n-card>
            <n-form>
              <n-form-item-row label="密码">
                <n-input
                  type="password"
                  show-password-on="mousedown"
                  placeholder="密码"
                v-model:value="form.password" />
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