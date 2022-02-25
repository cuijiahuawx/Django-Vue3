<script lang="ts" setup>
    import { h, ref } from 'vue'

    import { NIcon } from 'naive-ui'
    import {
        PersonCircleOutline as UserIcon,
        LogOutOutline as LogoutIcon
    } from '@vicons/ionicons5'

    import { useRouter } from 'vue-router';
    import { UserInfoStore } from '../store/userInfo';
    import { storeToRefs } from 'pinia';

    // 引入Pinia存储
    const userInfo = UserInfoStore()
    const {status, avatar } = storeToRefs(userInfo)

    const renderIcon = (icon: any) => {
        return () => {
        return h(NIcon, null, {
            default: () => h(icon)
        })
        }
    }

    const userOptions = ref([
            {
                label: '用户资料',
                key: 'profile',
                icon: renderIcon(UserIcon)
            },
            {
                label: '退出登录',
                key: 'logout',
                icon: renderIcon(LogoutIcon)
            }
            ])

    const musicOptions = ref([
            {
                label: '音乐设置',
                key: 'musicSettings',
                icon: renderIcon(UserIcon)
            },
            ])
    // 引入路由管理
    const router = useRouter()
    const login = () => {
        router.push({path: '/login'})
    }

    const handleSelect = (key: string) => {
        if ('logout' == key) {
            userInfo.logout()
            router.push({path: '/'})
        }else if ('profile' == key) {
            router.push({path: '/profile'})
        }
    }

    const handleMusicSelect = (key: string) => {
        if ('musicSettings' == key) {
            router.push({path: '/musicSettings'})}
    }
const home = () => {
    router.push({path: '/'})
}
const addBlog = () =>{
    router.push({path: '/addBlog'})
}
</script>

<template>
    <n-grid :cols="4" style="height: 64px;">
        <n-gi>
            <n-button @click="home" style="margin-left:50px;margin-top:4px;" text>
                <h2>主页</h2>
            </n-button>
        </n-gi>
        <n-gi>
            <n-button style="margin-top:15px;" type="primary" @click="addBlog">
                添加笔记
            </n-button>   
        </n-gi>
        <n-gi>
        </n-gi>
        <n-gi style="height: 64px;">
            <n-space v-if="status">
                <n-dropdown :options="userOptions" @select="handleSelect">
                    <n-avatar
                    round
                    :size="55"
                    :src="avatar"
                    />
                </n-dropdown>
                <n-dropdown :options="musicOptions" @select="handleMusicSelect">
                    <n-button style="margin-top: 1em;" type="info" dashed>音乐</n-button>
                </n-dropdown>           
            </n-space>
            <n-button style="margin-top:15px;" type="primary" @click="login" v-else>
                登录
            </n-button>   
        </n-gi>
    </n-grid>
</template>

<style>
</style>