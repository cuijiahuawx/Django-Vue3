<script lang="ts" setup>
    import { reactive } from 'vue'
    import { Http } from '~/api/request';
    import { useRouter } from 'vue-router';

    const form = reactive({
        email: ''
    })

    // 引入路由管理
    const router = useRouter()
    
    const forgetPassword = () => {
        Http.post('user/forget/', {
                email: form.email,
            })
            .then(() => {
                router.push({path: '/login'});
            })
    }
</script>

<template>
<n-grid x-gap="12" :cols="3" style="margin-top: 5em;">
    <n-gi></n-gi>
    <n-gi>
        <n-form
            :label-width="80"
            ref="formRef"
        >
            <n-form-item label="登录邮箱" path="user.name">
                <n-input v-model:value="form.email" placeholder="输入密码所对应的登录邮箱" />
            </n-form-item>
            <n-form-item>
                <n-button @click="forgetPassword" attr-type="button" type="error">更改密码</n-button>
            </n-form-item>
        </n-form>
    </n-gi>
    <n-gi></n-gi>
</n-grid>
</template>

<style>
</style>