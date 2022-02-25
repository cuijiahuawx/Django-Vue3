<script lang="ts" setup>
    import { ref } from 'vue';
    import { useRouter ,useRoute} from 'vue-router';
    import { Http } from '~/api/request';
    import { UserInfoStore } from '~/store/userInfo';
    import SuccessMessage from '~/components/SuccessMessage.vue'
    // 使用消息
    const successMsg = ref()
    // 引入Pinia存储
    const userInfo = UserInfoStore()
    // 引入路由管理
    const router = useRouter()
    const route = useRoute()
    // 获取路由参数
    const token = route.params['token']

    const verify = () => {
        Http.post('user/verify_email/', {
            token: token
        },
        {
            headers: { 
                'Authorization': `Bearer ${token}`
            } 
        })
        .then(() => {
            successMsg.value.showMessage("用户激活成功，请登录")
            userInfo.logout()
            router.push({path: '/login'})
        })
    }

</script>

<template> 
<n-message-provider>
  <SuccessMessage ref="successMsg" />
</n-message-provider>
<n-grid style="margin-top: 1em;" x-gap="12" :cols="3">
    <n-gi>
    </n-gi>
    <n-gi>
        <n-button type="primary" @click="verify">
            激活邮箱
        </n-button>
    </n-gi>
    <n-gi>
    </n-gi>
</n-grid>
</template>

<style>
</style>