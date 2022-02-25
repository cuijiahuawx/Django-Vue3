<template>
    <el-menu mode="horizontal">
        <el-menu-item v-if="! status">
            <el-button type="success" size='small' round @click="loginPage">登录</el-button>
        </el-menu-item>
        <el-sub-menu index="1" v-else>
            <template #title><el-avatar index="1" :size="50" :src=avatar>头像</el-avatar></template>
            <el-menu-item @click="profilePage">
                信息修改
            </el-menu-item>
            <el-menu-item @click="logout">
                退出登录
            </el-menu-item>
        </el-sub-menu>
     
    </el-menu>
</template>

<script lang="ts" setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router';
    import { storeToRefs } from "pinia";
    import { UserInfoStore } from "~/store/userInfo";
    // 引入Pinia存储
    const userInfo = UserInfoStore()
    const {status, userId, access, refresh, loginEmail, name, avatar } = storeToRefs(userInfo)

    const router = useRouter()

    const loginPage = () => {
        router.push({path: '/login'});
    }
    const profilePage = () => {
        router.push({path: '/profile'});
    }
    const logout = () => {
        userInfo.logout()
        router.push({path: '/'});
    }
    const newBlog  = () => {
        router.push({path: '/newBlog'});
    }
</script>
