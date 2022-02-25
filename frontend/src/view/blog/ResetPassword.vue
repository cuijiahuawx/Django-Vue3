<script lang="ts" setup>
    import { reactive } from 'vue'
    import { Http } from '~/api/request';
    import { useRouter ,useRoute} from 'vue-router';
    import { UserInfoStore } from '~/store/userInfo';
    
    // 引入路由管理
    const router = useRouter()
    const route = useRoute()
    const token = route.params['token']
    // 引入Pinia存储
    const userInfo = UserInfoStore()

    const form = reactive({
        password: ''
    })
    
    const changePassword = () => {
        Http.post('user/change_password/', {    // 可用，请求重置密码
                password: form.password,
                token: token
            },
            {
                headers: { 
                    'Authorization': `Bearer ${token}`
                } 
            })
            .then(response => {
                userInfo.logout()
                router.push({path: '/login'})
            })
    }
</script>

<template>
    <n-grid x-gap="12" :cols="3" style="margin-top: 5em;">
        <n-gi></n-gi>
        <n-gi>
            <n-form
                :label-width="80"
            >
                <n-form-item label="密码" path="user.name">
                    <n-input v-model:value="form.password" 
                            placeholder="输入新密码" 
                            type="password"
                            show-password-on="mousedown"/>
                </n-form-item>
                <n-form-item>
                    <n-button @click="changePassword" attr-type="button" type="error">更改密码</n-button>
                </n-form-item>
            </n-form>
        </n-gi>
        <n-gi></n-gi>
    </n-grid>
</template>

<style>
</style>