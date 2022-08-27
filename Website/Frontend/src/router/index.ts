import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('~/Home.vue')
    },
    {
        path: '/test/',
        name: 'test',
        component: () => import('~/Test.vue')
    },
    {
        path: '/musicSettings/',
        name: 'musicSettings',
        component: () => import('~/view/music/MusicSettings.vue'),
        meta: {
            loginRequire: true
        }
    },
    {
        path: '/login/',
        name: 'login',
        component: () => import('~/view/user/Login.vue'),
        meta: {
            title: 'login'
        }
    },
    {
        path: '/profile/',
        name: 'profile',
        component: () => import('~/view/user/Profile.vue'),
        meta: {
            loginRequire: true
        }
    },
    {
        path: '/todoList/',
        name: 'todoList',
        component: () => import('~/view/todoList/TodoList.vue'),
    },
    {
        path: '/blogs/',
        name: 'blogs',
        component: () => import('~/view/blog/Blog.vue'),
    },
    {
        path: '/userBlogs/:userID/',
        name: 'userBlogs',
        component: () => import('~/view/blog/UserBlogs.vue'),
    },
    {
        path: '/typeBlogs/:typeID/',
        name: 'typeBlogs',
        component: () => import('~/view/blog/TypeBlogs.vue'),
    },
    {
        path: '/create/',
        name: 'create',
        component: () => import('~/view/blog/Create.vue'),
    },
    {
        path: '/detail/:id/',
        name: 'detail',
        component: () => import('~/view/blog/Detail.vue'),
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
