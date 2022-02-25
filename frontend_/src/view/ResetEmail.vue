<template>
<el-dialog v-model="dialogFormVisible" title="注意！！！更改邮箱后你需要使用新的邮箱进行登录，旧的邮箱将被废弃。">
    <el-form :model="form">
        <el-form-item label="输入密码：">
            <el-input v-model="form.password" autocomplete="off" show-password></el-input>
        </el-form-item>
    </el-form>
    <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">退出</el-button>
        <el-button type="primary" @click="changeEmail">确认</el-button>
    </span>
</el-dialog>
<BaseHeader :msg="userinfo"/>
<el-row>
    <el-col :span="8"></el-col>
    <el-col :span="8">
        <el-form size="small">
            <el-form-item label="新的邮箱">
                <el-input v-model="newEmail"></el-input>
            </el-form-item>
        </el-form>
        <el-button type="success" @click="dialogFormVisible = true">更改邮箱</el-button>
    </el-col>
    <el-col :span="8"></el-col>
</el-row>
</template>

<script>

</script>

<script setup lang="ts">
    import { ref, reactive } from 'vue'
    import { Http } from '~/api/request';
    import { useRouter, useRoute } from 'vue-router';
    import { ElMessage } from 'element-plus'
    import { storeToRefs } from "pinia"
    import { UserInfoStore } from "~/store/userInfo"


    const dialogFormVisible = ref(false)
    const form = reactive({
        password: '',
    })

    const userinfo = ref('no')
    const newEmail = ref('')
    // 引入路由管理
    const router = useRouter()
    const route = useRoute()

    // 引入Pinia存储
    const userInfo = UserInfoStore()
    const { access, refresh } = storeToRefs(userInfo)

    const changeEmail = () => {
        dialogFormVisible.value = false
        Http.post('api/token/verify/', {
            token: access.value
        })
        .then(response => {
            console.log(access.value, newEmail.value)
            Http.post('user/change_email/', {
                    token: access.value,
                    email: newEmail.value,
                    password: form.password
                },{
                headers: { 
                    'Authorization': `Bearer ${access.value}`
                    }
                })
                .then(response => {
                    ElMessage('更改邮箱成功，请到登录页面登录')
                    router.push({path: '/login'});
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
                    Http.post('user/change_email/', {
                            token: access.value,
                            email: newEmail.value,
                            password: form.password
                        },{
                        headers: { 
                            'Authorization': `Bearer ${access.value}`
                            }
                        })
                        .then(response => {
                            ElMessage('更改邮箱成功，请到登录页面登录')
                            router.push({path: '/login'});
                        })            
                }, 1000)
        })
    }
</script>


<style>
.el-button--text {
  margin-right: 15px;
}
.el-input {
  width: 300px;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>