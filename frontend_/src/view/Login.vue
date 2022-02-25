<template>
<BaseHeader :msg="userinfo"/>
  <el-row>
    <el-col :span="8"></el-col>
    <el-col :span="8">
      <el-tabs v-model="activeName" type="border-card" stretch="true"> 
        <!-- 登录标签页 -->
        <el-tab-pane label="登录" name="login">
          <el-form size="small" label-position="top">
            <el-form-item label="登录邮箱">
              <el-input v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="form.password" show-password></el-input>
            </el-form-item>
          </el-form>
          <el-button type="success" @click="login">提交</el-button>
          <el-button type="danger" @click="changePassword" round>忘记密码？</el-button>
        </el-tab-pane>
        <!-- 注册标签页 -->
        <el-tab-pane label="注册" name="register">
          <el-form size="small" label-position="top" ref="ruleFormRef"
            :model="ruleForm"
            status-icon
            :rules="rules">
            <el-form-item label="用户名">
              <el-input v-model="form.userName"></el-input>
            </el-form-item>
            <el-form-item label="登录邮箱">
              <el-input v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass">
              <el-input v-model="ruleForm.pass" autocomplete="off" show-password ></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPass">
              <el-input v-model="ruleForm.checkPass" autocomplete="off"  show-password  ></el-input>
            </el-form-item>
            <el-button type="success" @click="register">提交</el-button>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </el-col>
    <el-col :span="8"></el-col>
  </el-row>
 
</template>

<script lang="ts" setup>
  import { ref, reactive } from 'vue'
  import { storeToRefs } from "pinia"
  import { useRouter } from 'vue-router'
  import { Http } from '~/api/request'
  import { UserInfoStore } from "~/store/userInfo"
  // 解析JWT
  import jwtDecode from 'jwt-decode'  
  // 密码验证
  import type { ElForm } from 'element-plus'
  // 消息提示
  import { ElMessage } from 'element-plus'
  // 组件设置
  const activeName = ref('login')
  const userinfo = ref('no')
  // 引入路由管理
  const router = useRouter()
  // 引入Pinia存储
  const userInfo = UserInfoStore()
  const {status, userId, access, refresh, is_useful, loginEmail, name, avatar } = storeToRefs(userInfo)
  // 组件表单变量
  const form = reactive({
    userName: '',
    email: '',
    password: '',
    check: ''
  })
  // 处理登录逻辑
  interface Decode {
    user_id: string
    avatar: string
    name: string
    email: string
  }
  const login = () => {
    const email = form.email
    const password = form.password
    userInfo.login(email, password)
    setTimeout(()=>{
      if(status.value == true && is_useful.value == true) {
        router.push({path: '/'});
      }
      else{
        ElMessage.error('该用户不可用，你是否激活了注册邮箱？')
      }
    }, 1000);
  }


  // 忘记密码
  const changePassword = () => {
    router.push({path: '/changePassword'});
  }
  // 处理注册逻辑
  const register = () => {
    Http.post('user/', {
      "user_name": form.userName,
      "email": form.email,
      "password": ruleForm.pass
    })
    .then(response => {
      ElMessage('请到注册邮箱激活账户后再登录')
      setTimeout(()=>{
        router.push({path: '/login'})
            },5000)
    })
    .catch(error => {
      ElMessage.error('用户名或者邮箱已注册，请更换！')
    })
  }
  // 表单验证
  type FormInstance = InstanceType<typeof ElForm>
  const ruleFormRef = ref<FormInstance>()
  const validatePass = (rule: any, value: any, callback: any) => {
    if (value === '') {
      callback(new Error('请输入密码'))
    } else {
      if (ruleForm.checkPass !== '') {
        if (!ruleFormRef.value) return
        ruleFormRef.value.validateField('checkPass', () => null)
      }
      callback()
    }
  }
  const validatePass2 = (rule: any, value: any, callback: any) => {
    if (value === '') {
      callback(new Error('再次输入，确认密码'))
    } else if (value !== ruleForm.pass) {
      callback(new Error("两次输入的不一致!"))
    } else {
      callback()
    }
  }
  const ruleForm = reactive({
    pass: '',
    checkPass: '',
  })
  const rules = reactive({
    pass: [{ validator: validatePass, trigger: 'blur' }],
    checkPass: [{ validator: validatePass2, trigger: 'blur' }],
  })
</script>

<style>
.el-tabs {
  text-align: center;
}
</style>