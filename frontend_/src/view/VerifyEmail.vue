<template>
<BaseHeader :msg="userinfo"/>
<el-row>
    <el-col :span="8"></el-col>
    <el-col :span="8">
        <el-button type="success" @click="verify">确认</el-button>
    </el-col>
    <el-col :span="8"></el-col>
</el-row>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import { useRouter ,useRoute} from 'vue-router';
    import { Http } from '~/api/request';
    import { ElMessage } from 'element-plus'
    import { UserInfoStore } from '~/store/userInfo';
    

    // 引入Pinia存储
    const userInfo = UserInfoStore()

    const userinfo = ref('no')

    // 引入路由管理
    const router = useRouter()
    const route = useRoute()
    // 获取路由参数
    const token = route.params['token']

    const verify = () => {
        Http.post('user/verify_email/', {                           // 可用，请求重置密码
            token: token
        },
        {
            headers: { 
                'Authorization': `Bearer ${token}`
            } 
        })
        .then(response => {
            ElMessage('验证用户成功！请用密码和邮箱登录')
            userInfo.logout()
            router.push({path: '/login'})
        })
    }
</script>

<style>

</style>