<template>
<BaseHeader :msg="userinfo"/>
<el-row>
    <el-col :span="8"></el-col>
    <el-col :span="8">
        <el-form size="small">
            <el-form-item label="密码所对应的登录邮箱">
                <el-input v-model="email" :placeholder=loginEmail autocomplete="dasd"></el-input>
            </el-form-item>
        </el-form>
        <el-button type="success" @click="find">更改密码</el-button>
    </el-col>
    <el-col :span="8"></el-col>
</el-row>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import { Http } from '~/api/request';
    import { useRouter } from 'vue-router';
    import { ElMessage } from 'element-plus'
    import { storeToRefs } from "pinia";
    import { UserInfoStore } from "~/store/userInfo";

    const userinfo = ref('no')
    const email = ref('')
    // 引入Pinia存储
    const userInfo = UserInfoStore()
    const { loginEmail } = storeToRefs(userInfo)
    // 引入路由管理
    const router = useRouter()

    const find = () => {
        Http.post('user/forget/', {
            email: email.value,
            })
            .then(response => {
                ElMessage({
                        message: '请在注册邮箱提供的链接中重设密码',
                        type: 'warning'
                    })
                router.push({path: '/login'});
            })
    }
</script>

<style>

</style>