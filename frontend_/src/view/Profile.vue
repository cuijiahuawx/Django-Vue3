<template>
<BaseHeader :msg="userinfo"/>
  <el-row>
    <el-col :span="8"></el-col>
    <el-col :span="8">
      <el-tabs v-model="activeName" type="border-card" stretch="true"> 
          <el-tab-pane label="信息" name="info">
            <el-form size="small" label-position="top">
              <p>注册邮箱： {{loginEmail}}</p>
              <p>用户名： {{name}}</p>
              <p>头像:<el-avatar index="1" :size="50" :src=avatar>头像</el-avatar>
              </p>
            </el-form>
          </el-tab-pane>

          <el-tab-pane label="修改" name="edit">
            <el-form size="small" label-position="top">
              <el-form-item label="用户名称">
                <el-input v-model="name"></el-input>
              </el-form-item>
              <el-form-item label="头像（请提交头像的网络地址）">
                <el-input v-model="avatar"></el-input>
              </el-form-item>
              <el-button type="success" @click="changeProfile" >提交</el-button>
              <el-row>
                <el-col :span="12">

                </el-col>
                <el-col :span="12">
                  <el-button type="danger" @click="changePassword" round>修改密码</el-button>
                  <el-button type="danger" @click="changeEmail" round>修改邮箱</el-button>
                </el-col>
              </el-row>
            </el-form>
          </el-tab-pane>
        </el-tabs>
    </el-col>
    <el-col :span="8"></el-col>
  </el-row>
 
</template>

<script lang="ts" setup>
  import { Http } from '~/api/request';
  import { ref, reactive } from 'vue'
  import { storeToRefs } from "pinia";
  import { UserInfoStore } from "~/store/userInfo";
  import { useRouter } from 'vue-router';
  import { ElMessage } from 'element-plus'


  // 引入Pinia存储
  const userInfo = UserInfoStore()
  const { access, refresh, loginEmail, name, avatar } = storeToRefs(userInfo)

  const activeName = ref('info')
  const userinfo = ref('yes')
  // 引入路由管理
  const router = useRouter()

  const form = reactive({
    email: '',
    password: '',
  })
  // 更改用户信息逻辑
  const changeProfile = () => {
    Http.post('api/token/verify/',{
        token: access.value
      })
    .then(response => {
      Http.post('user/edit_profile/', {
        token: access.value,
        user_name:name.value,
        avatar: avatar.value,
      },
      {
        headers: { 
            'Authorization': `Bearer ${access.value}`
          } 
      })
      .then(response => {
        ElMessage('更改用户信息成功！')
        router.push({path: '/profile'})
      })
    })
    .catch(error => {
      Http.post('api/token/refresh/', {
        "refresh": refresh.value
      })
      .then(response => {
        access.value = response.data['access'];
        refresh.value = response.data['refresh'];
      })
      setTimeout(()=>{
        Http.post('user/edit_profile/', {
          token: access.value,
          user_name: name.value,
          avatar: avatar.value,
        },
        {
          headers: { 
              'Authorization': `Bearer ${access.value}`
            } 
        })
        .then(response => {
          ElMessage('更改用户信息成功！')
          router.push({path: '/profile'})
        })
      },1000)
    })
  }
  // 更改密码逻辑
  const changePassword = () => {
    router.push({path: '/changePassword'});
  }
  // 更改邮箱逻辑
  const changeEmail = () => {
    router.push({path: '/resetEmail'})
  }
</script>

<style>

</style>