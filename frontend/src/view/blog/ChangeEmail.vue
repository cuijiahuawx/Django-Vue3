<script lang="ts" setup>
    import { ref, reactive } from 'vue'
    import { Http } from '~/api/request'
    import { useRouter, useRoute } from 'vue-router'
    import { storeToRefs } from "pinia"
    import { UserInfoStore } from "~/store/userInfo"

    // 引入路由管理
    const router = useRouter()
    const route = useRoute()

    // 引入Pinia存储
    const userInfo = UserInfoStore()
    const { access, refresh } = storeToRefs(userInfo)

    const form = reactive({
        email: '',
        password: ''
    })
    const changeEmail = () => {
        Http.post('api/token/verify/', {
            token: access.value
        })
        .then(response => {
            Http.post('user/change_email/', {
                    token: access.value,
                    email: form.email,
                    password: form.password
                },{
                headers: { 
                    'Authorization': `Bearer ${access.value}`
                    }
                })
                .then(response => {
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
                        email: form.email,
                        password: form.password
                    },{
                    headers: { 
                        'Authorization': `Bearer ${access.value}`
                        }
                    })
                    .then(response => {
                        router.push({path: '/login'});
                    })            
            }, 1000)
        })
    }
    const showModal = ref(false)
    const show = () => {
        showModal.value = true
    }
   
</script>

<template>
  <n-modal v-model:show="showModal">
    <n-card
      style="width: 600px;"
      title="需要密码确认"
      :bordered="false"
      size="huge"
      role="dialog"
      aria-modal="true"
    >
            <n-form
                :label-width="80"
                ref="formRef"
            >
                <n-form-item label="密码" path="user.name">
                    <n-input v-model:value="form.password" placeholder="输入密码" 
                                    type="password"
                                    show-password-on="mousedown"/>
                </n-form-item>
                <n-form-item>
                        <n-dialog-provider>
                            <n-button @click="changeEmail" attr-type="button" type="error">确认修改</n-button>
                        </n-dialog-provider>
                </n-form-item>
            </n-form>
    </n-card>
  </n-modal>
    <n-grid x-gap="12" :cols="3" style="margin-top: 5em;">
        <n-gi></n-gi>
        <n-gi>
            <n-form
                :label-width="80"
                ref="formRef"
            >
                <n-form-item label="邮箱" path="user.name">
                    <n-input v-model:value="form.email" placeholder="输入新的邮箱" />
                </n-form-item>
                <n-form-item>
                        <n-dialog-provider>
                            <n-button @click="show" attr-type="button" type="error">更改邮箱</n-button>
                        </n-dialog-provider>
                </n-form-item>
            </n-form>
        </n-gi>
        <n-gi></n-gi>
    </n-grid>
</template>

<style>
</style>