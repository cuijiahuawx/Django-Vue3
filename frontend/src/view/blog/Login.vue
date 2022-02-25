<script lang="ts" setup>
  import { ref, reactive } from 'vue'
  import { storeToRefs } from "pinia"
  import { useRouter } from 'vue-router'
  import { Http } from '~/api/request'
  import { UserInfoStore } from "~/store/userInfo"
  import SuccessMessage from '~/components/SuccessMessage.vue'
  import ErrorMessage from '~/components/ErrorMessage.vue'

  // 组件表单变量
  const form = reactive({
    userName: '',
    email: '',
    password: '',
    check: ''
  })

  // 使用消息
  const successMsg = ref()
  const errorMsg = ref()
  // 引入Pinia存储
  const userInfo = UserInfoStore()
  const {status, is_useful} = storeToRefs(userInfo)
  // 引入路由管理
  const router = useRouter()

  // 处理登录逻辑
  const login = () => {
    successMsg.value.showMessage("登陆成功")
    const email = form.email
    const password = form.password
    userInfo.login(email, password)
    setTimeout(()=>{
      if(status.value == true && is_useful.value == true) {
          router.push({path: '/'})
        }
    }, 1000)
  }

  // 处理注册逻辑
  const register = () => {
    Http.post('user/', {
      "user_name": form.userName,
      "email": form.email,
      "password": form.password
    })
    .then(() => {
      errorMsg.value.showMessage("注意！！！你需要到注册邮箱激活链接才可以登录账户")
      setTimeout(()=>{
        router.push({path: '/login'})
            }, 1000)
    })
    .catch((error: any) => {
    })
  }

  // 处理忘记密码逻辑
  const forget = () => {
    router.push({path: '/changePassword'})
  }
</script>

<template>
<n-message-provider>
  <SuccessMessage ref="successMsg" />
  <ErrorMessage ref="errorMsg" />
</n-message-provider>
<n-grid x-gap="12" :cols="3">
    <n-gi>
    </n-gi>
    <n-gi>
      <n-card>
        <n-tabs default-value="signin" size="large">
          <n-tab-pane name="signin" tab="登录">
            <n-form>
              <n-form-item-row label="登录邮箱">
                <n-input v-model:value="form.email" />
              </n-form-item-row>
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
            <n-button style="margin-top: 1em;" type="error" block secondary strong @click="forget">
              忘记密码？
            </n-button>
          </n-tab-pane>
          <n-tab-pane name="signup" tab="注册">
            <n-form>
              <n-form-item-row label="用户名">
                <n-input v-model:value="form.userName"/>
              </n-form-item-row>
              <n-form-item-row label="登录邮箱">
                <n-input v-model:value="form.email"/>
              </n-form-item-row>
              <n-form-item-row label="密码">
                <n-input 
                  v-model:value="form.password"
                  type="password"
                  show-password-on="mousedown"
                  placeholder="密码"/>
              </n-form-item-row>
              <n-form-item-row label="重复密码">
                <n-input 
                  v-model:value="form.check"
                  type="password"
                  show-password-on="mousedown"
                  placeholder="重复密码"/>
              </n-form-item-row>
            </n-form>
            <n-button type="primary" block secondary strong @click="register">
              注册
            </n-button>
          </n-tab-pane>
        </n-tabs>
      </n-card>
    </n-gi>
    <n-gi>
    </n-gi>
  </n-grid>
</template>

<style>

</style>