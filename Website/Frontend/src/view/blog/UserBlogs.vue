<script lang="ts" setup>
// 引入官方相关库
import { onMounted, reactive, ref, toRefs, watch } from 'vue';

// Pinia引入存储
// 引入网络请求
import { Http } from '~/api/request'
import { useRoute, useRouter } from 'vue-router';
// 引入第三方组件
// 引入自定义组件
// Pinia存储设置


/**
 * 0. 组件全局相关设置
 * 1. 获取特定用户的博客
 * 2. 分页设置
 * 3. 响应Click事件的函数
 */


// 0. 组件全局相关设置
// 引入路由管理
const router = useRouter()

// 1. 获取特定用户的博客
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

const route = useRoute()
const userID = route.params['userID']
onMounted(() => {
    Http.get(`/blog/userBlogs/${userID}`)
        .then((response) => {
            currentPageData.currentPage = response.data
            console.log(response.data)
        })

})


// 2. 分页设置
const onUpdatePage = (p: number) => {
    Http.get(`http://127.0.0.1:8000/blog/userBlogs/${userID}?page=${p}&size=${pageSize.value}`)
        .then((response) => {
            currentPageData.currentPage = response.data
        })
        .catch((error) => {
            console.log(error)
        })
}
const onUpdatePageSize = (ps: number) => {
    pageSize.value = ps
    Http.get(`http://127.0.0.1:8000/blog/userBlogs/${userID}?page=${page.value}&size=${ps}`)
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


// 3. 响应Click事件的函数
// 转到博客详情
const blogDetail = (id: number) => {
    router.push({ path: `/detail/${id}` })
}
// 转到特定用户博客
const userBlog = (userID: string) => {
    router.push({ path: `/userBlogs/${userID}` })
}
</script>


<template>
    <n-list bordered>
        <template #header>
            博客
        </template>
        <template #footer>
            <n-pagination v-model:page="page" :item-count="currentPage.count" v-model:page-sizes="pageSizes"
                :page-size="pageSize" :page-slot="pageSlot" :onUpdate:page="onUpdatePage"
                :default-page-size="defaultPageSize" :on-update:page-size="onUpdatePageSize" size="medium"
                show-quick-jumper show-size-picker />
        </template>
        <n-list-item>
            <n-grid x-gap="12" :cols="2" v-for="blog in currentPage.results">
                <n-gi>
                    <h1 @click="blogDetail(blog.id)">{{ blog.title }}</h1>
                </n-gi>
                <n-gi>
                    <h2 @click="userBlog(blog.author)">{{ blog.authorName }}</h2>
                </n-gi>
                <n-gi>
                    <p>{{ blog.content.substring(0, 100).concat(' ...') }}</p>
                </n-gi>

            </n-grid>
        </n-list-item>
    </n-list>
</template>


<style scoped>
</style>