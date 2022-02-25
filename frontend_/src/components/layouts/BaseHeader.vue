<template>
  <el-row>
    <el-col :span="10">
        <el-menu mode="horizontal">
          <el-menu-item @click="homePage">
            主页
          </el-menu-item>
          <el-menu-item @click="blogsPage">
            博客列表
          </el-menu-item>
        </el-menu>     
    </el-col>
    <el-col :span="8">  
      <el-menu mode="horizontal">
        <el-menu-item @click="newBlog" v-if="status">
            我的博客
        </el-menu-item>
        <el-menu-item @click="newBlog" v-if="status">
            添加博客
        </el-menu-item>
        <el-menu-item @click="newBlog" v-if="status">
            修改博客
        </el-menu-item>
      </el-menu>

    </el-col>
    <el-col :span="4">
      <UserInfo v-if="msg==='yes'"/>
    </el-col>
  </el-row>
</template>

<script lang="ts" setup>
  import {ref} from 'vue'
  import { useRouter } from 'vue-router';
  import { storeToRefs } from "pinia";
  import { UserInfoStore } from "~/store/userInfo";
  // 引入Pinia存储
  const userInfo = UserInfoStore()
  const {status, userId, access, refresh, loginEmail, name, avatar } = storeToRefs(userInfo)
  interface Props{
      msg ?: string,
    }
    withDefaults(defineProps<Props>(), {
      msg: 'yes'
    })

  const router = useRouter()
  const loginPage = () => {
    router.push({path: '/login'});
  }
  const homePage = () => {
    router.push({path: '/'});
  }

  const blogsPage = () => {
    router.push({path: '/blogs'});
  }
    const newBlog  = () => {
        router.push({path: '/newBlog'});
    }
</script>