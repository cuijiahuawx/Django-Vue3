<script lang="ts" setup>
// 引入官方相关库
import { onMounted, reactive, ref, toRefs, } from 'vue';
// Pinia引入存储
// 引入网络请求
import { Http } from '~/api/request'
import { useRoute, useRouter } from 'vue-router';
// 引入第三方组件
// 引入自定义组件
import Types from '~/view/blog/Types.vue'


/**
 * 0. 组件全局相关设置
 * 1. 获取博客
 * 2. 获取博客标签数据
 * 3. 分页设置
 * 4. 响应Click事件的函数
 */


// 0. 组件全局相关设置
// 引入路由管理
const router = useRouter()

// 1. 获取博客
interface Blog {
    "id": number,
    "blog_type": string[],
    "title": string,
    "author": string,
    "authorName": string,
    "content": string,
}
let currentPageData = reactive({
    currentPage: {
        "count": -1,
        "next": '',
        "previous": '',
        "results": [] as Blog[]
    }
})
const { currentPage } = toRefs(currentPageData)
onMounted(() => {
    const route = useRoute()
    const typeID = route.params['typeID']
    Http.get(`blog/typeBlogs/${typeID}`)
        .then((response) => {
            currentPageData.currentPage = response.data
        })
})

// 2. 获取博客标签数据
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


// 3. 分页设置
const onUpdatePage = (p: number) => {
    Http.get(`http://127.0.0.1:8000/blog/?page=${p}&size=${pageSize.value}`)
        .then((response) => {
            currentPageData.currentPage = response.data
        })
        .catch((error) => {
            console.log(error)
        })
}
const onUpdatePageSize = (ps: number) => {
    pageSize.value = ps
    Http.get(`http://127.0.0.1:8000/blog/?page=${page.value}&size=${ps}`)
        .then((response) => {
            currentPageData.currentPage = response.data
        })
        .catch((error) => {
            console.log(error)
        })
}
const defaultPageSize = ref(2)
const pageSizes = ref([2, 3, 4]) // 每页显示条数
const pageSize = ref(2) // 受控模式分页大小
const pageSlot = ref(5) // 	页码显示的个数
const page = ref(1) // 受控模式下的当前页


// 4. 响应Click事件的函数
// 转到博客详情
const blogDetail = (id: number) => {
    router.push({ path: `/detail/${id}` })
}
// 转到特定用户博客
const userBlogs = (userID: string) => {
    router.push({ path: `/userBlogs/${userID}` })
}
// 转到标签博客列表
const typeBlogs = (typeName: string) => {
    console.log("hello")
    for (const type of data.types) {
        if (type.name == typeName) {
            router.push({ path: `/typeBlogs/${type.id}` })
        }
    }
}
</script>

<template>
    <n-layout has-sider class="layout">
        <n-layout-sider content-style="padding: 24px;">
            <Types />
        </n-layout-sider>
        <n-layout>
            <n-layout-header>
                <h1>博客列表 </h1>
            </n-layout-header>
            <n-layout-content content-style="padding: 24px;">
                <n-list bordered>
                    <n-list-item>
                        <n-space v-for="blog in currentPage.results" vertical>
                            <n-space vertical>
                                <h2 @click="blogDetail(blog.id)">{{ blog.title }}</h2>
                                <h3 @click="userBlogs(blog.author)">{{ blog.authorName }}</h3>
                                <n-space v-for="type in blog.blog_type" @click="typeBlogs(type)">
                                    <n-tag type="success">
                                        {{ type }}
                                    </n-tag>
                                </n-space>
                            </n-space>

                            <p>{{ blog.content.substring(0, 100).concat(' ...') }}</p>
                        </n-space>
                    </n-list-item>
                </n-list>
            </n-layout-content>
            <n-layout-footer>
                <n-pagination v-model:page="page" :item-count="currentPage.count" v-model:page-sizes="pageSizes"
                    :page-size="pageSize" :page-slot="pageSlot" :onUpdate:page="onUpdatePage"
                    :default-page-size="defaultPageSize" :on-update:page-size="onUpdatePageSize" size="medium"
                    show-quick-jumper show-size-picker />
            </n-layout-footer>
        </n-layout>
    </n-layout>
</template>

<style scoped>
</style>