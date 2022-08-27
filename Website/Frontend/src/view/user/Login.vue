<script lang="ts" setup>
// 引入官方相关库
import { ref, reactive } from 'vue'
// Pinia引入存储
import { storeToRefs } from "pinia"
import { UserInfoStore } from "~/store/userInfo"
// 引入网络请求
import { Http } from '~/api/request'
import { useRouter } from 'vue-router';
// 引入第三方组件
// 引入自定义组件


/**
 * 0. 组件全局相关设置
 * 1. 记住登陆状态
 * 2. 处理登录逻辑
 * 3. 获取验证码
 * 4. 处理注册逻辑
 * 5. 处理忘记密码逻辑
 */


// 0. 组件全局相关设置
// 组件表单变量
const form = reactive({
  userName: '',
  email: '',
  password: '',
  check: ''
})
// Pinia存储
const userInfo = UserInfoStore()
const { status } = storeToRefs(userInfo)
// 路由管理
const router = useRouter()


// 1. 记住登陆状态
const active = ref(false)
const handleRemember = (value: boolean) => {
  if (!value) {
    userInfo.remember = false
  }
  else {
    userInfo.remember = true
  }
}


// 2. 处理登录逻辑
const login = () => {
  const email = form.email
  const password = form.password
  userInfo.login(email, password)
  setTimeout(() => {
    if (status.value == true) {
      router.push({ path: '/' })
    }
  }, 1000)
}


// 3. 获取验证码
interface CodeResponseData {
  code: string,
}
interface CodeResponse {
  data: CodeResponseData
}
const code = ref('')
const getCode = () => {
  Http.get('/user/send_code/', {
    params: {
      email: form.email,
    }
  }
  )
    .then((response: CodeResponse) => {
      window?.$message?.success("已发送验证码，请到注册邮箱查看功")
      code.value = response.data['code']
    })
}


// 4. 处理注册逻辑
interface RegisterResponseData {
  status: boolean,
}
interface RegisterResponse {
  data: RegisterResponseData
}
const checkCode = ref('')
const register = () => {
  if (checkCode.value == code.value && form.check == form.password) {
    Http.post('/user/register/', {
      user_name: form.userName,
      email: form.email,
      password: form.password
    })
      .then((response: RegisterResponse) => {
        if (response.data['status'] == true) {
          window?.$message?.success("注册成功")
          setTimeout(() => {
            router.push({ path: '/login' })
          }, 1000)
        }
        else {
          window?.$message?.error("注册出现错误")
        }
      })
      .catch((error: any) => {
        window?.$message?.error("注册出现错误")
      })
  }
  else if (checkCode.value != code.value) {
    window?.$message?.error("验证码错误")
  }
  else {
    window?.$message?.error("两次密码不一致")
  }
}


// 5. 处理忘记密码逻辑
const forget = () => {
  router.push({ path: '/changePassword' })
}
</script>

<template>
  <n-grid x-gap="12" :cols="3">
    <n-gi>
    </n-gi>

    <n-gi>
      <n-card>
        <n-tabs default-value="signin" size="large">
          <!-- 登录 -->
          <n-tab-pane name="signin" tab="登录">
            <n-form>
              <n-form-item-row label="登录邮箱">
                <n-input v-model:value="form.email" />
              </n-form-item-row>
              <n-form-item-row label="密码">
                <n-input type="password" show-password-on="mousedown" placeholder="密码" v-model:value="form.password" />
              </n-form-item-row>
            </n-form>
            <n-switch v-model:value="active" @update:value="handleRemember">
              <template #checked>
                已记住登陆状态
              </template>
              <template #unchecked>
                记住登陆状态
              </template>
            </n-switch>
            <n-button type="primary" block strong @click="login">
              登录
            </n-button>
            <n-button style="margin-top: 1em;" type="error" block strong @click="forget">
              忘记密码？
            </n-button>
          </n-tab-pane>
          <!-- 注册 -->
          <n-tab-pane name="signup" tab="注册">
            <n-form>
              <n-form-item-row label="用户名">
                <n-input v-model:value="form.userName" />
              </n-form-item-row>
              <n-form-item-row label="登录邮箱">
                <n-input v-model:value="form.email" />
              </n-form-item-row>
              <n-form-item-row label="验证码">
                <n-input v-model:value="checkCode" />
                <n-button type="error" strong @click="getCode">
                  发送验证码
                </n-button>
              </n-form-item-row>
              <n-form-item-row label="密码">
                <n-input v-model:value="form.password" type="password" show-password-on="mousedown" placeholder="密码" />
              </n-form-item-row>
              <n-form-item-row label="重复密码">
                <n-input v-model:value="form.check" type="password" show-password-on="mousedown" placeholder="重复密码" />
              </n-form-item-row>
            </n-form>
            <n-button type="primary" block strong @click="register">
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