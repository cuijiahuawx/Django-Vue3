<script lang="ts" setup>
// 引入官方相关库
// Pinia引入存储
import { storeToRefs } from "pinia"
import { UserInfoStore } from "~/store/userInfo"
// 引入网络请求
import { Http } from '~/api/request'
import { useRouter } from 'vue-router'
// 引入第三方组件
// 引入自定义组件


/**
 * 0. 组件全局相关设置
 * 1. 更改用户信息逻辑
 * 2. 更改密码逻辑
 * 3. 更改邮箱逻辑
 */

// 0. 组件全局相关设置
// 引入Pinia存储
const userInfo = UserInfoStore()
const { access, refresh, loginEmail, name, avatar, musicEmail, musicID } = storeToRefs(userInfo)
// 引入路由
const router = useRouter()


// 1. 更改用户信息逻辑
const changeProfile = () => {
    Http.post('api/token/verify/', {
        token: access.value
    })
        .then(() => {
            Http.post('user/edit_profile/', {
                token: access.value,
                user_name: name.value,
                avatar: avatar.value,
                musicEmail: musicEmail.value,
                musicID: musicID.value
            },
                {
                    headers: {
                        'Authorization': `Bearer ${access.value}`
                    }
                })
                .then(() => {
                    window?.$message?.success("更改信息成功")
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
            setTimeout(() => {
                Http.post('user/edit_profile/', {
                    token: access.value,
                    user_name: name.value,
                    avatar: avatar.value,
                    musicEmail: musicEmail.value,
                    musicID: musicID.value
                },
                    {
                        headers: {
                            'Authorization': `Bearer ${access.value}`
                        }
                    })
                    .then(response => {
                        window?.$message?.success("更改信息成功")
                    })
            }, 1000)
        })
}


// 2. 更改密码逻辑
const changePassword = () => {
    router.push({ path: '/changePassword' });
}


// 3. 更改邮箱逻辑
const changeEmail = () => {
    router.push({ path: '/changeEmail' })
}
</script>

<template>
    <n-grid x-gap="12" :cols="3" style="margin-top: 3em;">
        <n-gi></n-gi>
        <n-gi>
            <n-card>
                <n-tabs default-value="signin" size="large">
                    <n-tab-pane name="signin" tab="用户信息">
                        <n-space vertical>
                            <n-space>
                                用户名：{{ name }}
                            </n-space>
                            <n-space>
                                注册邮箱： {{ loginEmail }}
                            </n-space>
                            <n-space>
                                头像:
                                <n-avatar round :size="55" :src="avatar" />
                            </n-space>
                            <n-space>
                                音乐邮箱： {{ musicEmail }}
                            </n-space>
                            <n-space>
                                音乐号： {{ musicID }}
                            </n-space>
                        </n-space>
                    </n-tab-pane>
                    <n-tab-pane name="signup" tab="修改信息">
                        <n-form>
                            <n-form-item-row label="用户名">
                                <n-input v-model:value="name" />
                            </n-form-item-row>
                            <n-form-item-row label="头像地址">
                                <n-input v-model:value="avatar" />
                            </n-form-item-row>
                            <n-form-item-row label="音乐邮箱">
                                <n-input v-model:value="musicEmail" />
                            </n-form-item-row>
                            <n-form-item-row label="音乐号">
                                <n-input v-model:value="musicID" />
                            </n-form-item-row>
                        </n-form>
                        <n-button type="primary" block secondary strong @click="changeProfile">
                            更改信息
                        </n-button>
                        <n-space style="margin-top: 1em;">
                            <n-button type="error" block secondary strong @click="changePassword">
                                更改密码
                            </n-button>
                            <n-button type="error" block secondary strong @click="changeEmail">
                                更改邮箱
                            </n-button>
                        </n-space>
                    </n-tab-pane>
                </n-tabs>
            </n-card>
        </n-gi>
        <n-gi></n-gi>
    </n-grid>
</template>

<style>
</style>