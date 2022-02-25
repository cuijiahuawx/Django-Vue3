import {createRouter, createWebHistory, createWebHashHistory } from 'vue-router'

import Home from '~/view/Home.vue'
import Login from '~/view/Login.vue'
import Profile from '~/view/Profile.vue'
import ChangePassword from '~/view/ChangePassword.vue'
import ResetPassword from '~/view/ResetPassword.vue'
import ResetEmail from '~/view/ResetEmail.vue'
import VerifyEmail from '~/view/VerifyEmail.vue'

import Blogs from '~/view/blog/Blogs.vue'
import NewBlog from '~/view/blog/NewBlog.vue'
import BlogDetail from '~/view/blog/BlogDetail.vue'

const routes = [
    // 主页面路由
    {path: '/', component: Home},
    // 登录页面路由
    {path: '/login', component: Login},
    // 邮箱验证路由
    {path: '/verify/:token', component: VerifyEmail},
    // 更改用户信息页面路由
    {path: '/profile', component: Profile},
    // 重设密码相关路由
    {path: '/changePassword', component: ChangePassword},
    {path: '/resetPassword/:token', component: ResetPassword},
    // 重设邮箱相关路由
    {path: '/resetEmail', component: ResetEmail},
    // 博客列表
    {path: '/blogs', component: Blogs},
    {path: '/newBlog', component: NewBlog},
    {path: '/detail/:id', component: BlogDetail},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router
