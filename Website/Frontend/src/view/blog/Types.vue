<script lang="ts" setup>
// 引入官方相关库
import { onMounted, reactive } from 'vue';
// Pinia引入存储
// 引入网络请求
import { Http } from '~/api/request'
import { useRouter } from 'vue-router';
// 引入第三方组件
// 引入自定义组件


/**
 * 0. 组件全局相关设置
 * 1. 获取博客标签数据
 * 2. 响应Click事件的函数
 */


// 0. 组件全局相关设置
// 引入路由管理
const router = useRouter()


// 1. 获取博客标签数据
interface Type {
    "id": number,
    "name": string,
    "blog_count": number
}
const data = reactive({
    types: [] as Type[],
})
onMounted(() => {
    Http.get('blog/types')
        .then(response => {
            for (const type of response['data']) {
                data.types.push({
                    id: type.id,
                    name: type.name,
                    blog_count: type.blog_count
                })
            }
        })
})

// 2. 响应Click事件的函数
// 转到标签博客列表
const typeBlogs = (typeName: string) => {
    for (const type of data.types) {
        if (type.name == typeName) {
            router.push({ path: `/typeBlogs/${type.id}` })
        }
    }
}
</script>


<template>
    <n-space v-for="type in data.types" vertical>
        <n-tag type="success" @click="typeBlogs(type.name)">
            {{ type.name }}
        </n-tag>
    </n-space>
</template>


<style>
</style>