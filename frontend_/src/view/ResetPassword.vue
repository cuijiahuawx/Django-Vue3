<template>
<BaseHeader :msg="userinfo"/>
<el-row>
    <el-col :span="8"></el-col>
    <el-col :span="8">
        <el-form size="small">
            <el-form-item label="更改密码">
                <el-input v-model="password" show-password></el-input>
            </el-form-item>
        </el-form>
        <el-button type="success" @click="changePassword">确认</el-button>
    </el-col>
    <el-col :span="8"></el-col>
</el-row>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import { Http } from '~/api/request';
    import { useRouter ,useRoute} from 'vue-router';
    import { ElMessage } from 'element-plus'
    import { UserInfoStore } from '~/store/userInfo';
    

    const userinfo = ref('no')
    const password = ref('')
    // 引入路由管理
    const router = useRouter()
    const route = useRoute()
    const token = route.params['token']
    // 引入Pinia存储
    const userInfo = UserInfoStore()
    
    const changePassword = () => {
        console.log(password.value, token)
        Http.post('user/change_password/', {                           // 可用，请求重置密码
            password: password.value,
            token: token
        },
        {
            headers: { 
                'Authorization': `Bearer ${token}`
            } 
        })
        .then(response => {
            ElMessage('更改密码成功！请用原密码和新邮箱重新登录')
            userInfo.logout()
            router.push({path: '/login'})
        })
    }
</script>

<style>

</style>