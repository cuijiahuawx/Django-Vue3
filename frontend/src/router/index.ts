import {createRouter, createWebHashHistory } from 'vue-router'

import Home from '~/view/Home.vue'

import Login from '~/view/blog/Login.vue'
import Verify from '../view/blog/Verify.vue'
import Profile from '../view/blog/Profile.vue'
import ChangePassword from '../view/blog/ChangePassword.vue'
import ChangeEmail from '../view/blog/ChangeEmail.vue'
import ResetPassword from '../view/blog/ResetPassword.vue'

import MusicSettings from '~/view/music/MusicSettings.vue'
import AddBlog from '~/view/blog/AddBlog.vue'

const routes = [
    // 主页面路由
    {path: '/', component: Home},
    {path: '/login/', component: Login},
    {path: '/verify/:token', component: Verify},
    {path: '/profile/', component: Profile},
    {path: '/changePassword/', component: ChangePassword},
    {path: '/changeEmail/', component: ChangeEmail},
    {path: '/resetPassword/:token', component: ResetPassword},

    {path: '/addBlog/', component: AddBlog},

    {path: '/musicSettings/', component: MusicSettings},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router
