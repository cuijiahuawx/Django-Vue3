<template>
    <el-container>
        <el-header>
            <BaseHeader :msg="userinfo"/>
        </el-header>
        <el-container>
            <el-aside width="250px">
                <Tags />    <!-- 标签组件 -->
            </el-aside>
            <el-main>
                <el-space direction="vertical" :fill=true wrap>
                    <el-card class="box-card" v-for="blog in data.blogsInfo['results']" :key="blog.id">
                        <div class="card-header">
                            <el-button type="text" @click="blogDetail(blog.id)">{{ blog.title }} </el-button>
                        </div>
                        <el-tag v-for="tag in blog.blog_type" :key="tag.name">{{ tag }}</el-tag>
                    </el-card>
                </el-space>
                <el-pagination
                    v-model:currentPage="currentPage"
                    :page-size="4"
                    :background=true
                    layout="prev, pager, next, jumper"
                    :total=total
                    @prev-click="handlePrevClick"
                    @next-click="handleNextClick"
                    >
                </el-pagination>
            </el-main>
        </el-container>
    </el-container>
</template>

<script lang="ts" setup>
    import { Python } from '@vicons/fa'
    import { Icon } from '@vicons/utils'
    import { ref, onMounted, reactive, watch } from 'vue'
    import { useRouter } from 'vue-router';
    import { Http } from '~/api/request';
    import Tags from '~/view/blog/Tags.vue'

    // 导航栏设置
    const userinfo = ref('yes')
    // 引入路由管理
    const router = useRouter()

    // 转到博客详情
    const blogDetail = (id: string) => {
        router.push({path: `/detail/${id}`})
    }

// 类型定义
    interface BlogType {
        name: string
    }

    interface Blog {
        "id": string,
        "blog_type": BlogType[],
        "title": string,
        "content": string
    }

    interface BlogsInfo {
        "count": string,
        "next": string,
        "previous": string,
        "results": Blog[]
    }

    // 分页变量
    const data = reactive({
        blogsInfo: {} as BlogsInfo
    })
    const currentPage = ref(1)
    const total = ref('1')
    const next = ref('')
    const previous = ref('')

    // 页面加载时，请求博客列表
    onMounted(()=>{
        Http.get('/blogs')
        .then(response => {
            data.blogsInfo = response['data']
            total.value = data.blogsInfo['count']
            next.value = data.blogsInfo['next']
            previous.value = data.blogsInfo['previous']
        })
    })

    // 监听分页的变化
    watch(currentPage, (newValue, oldValue)=>{
        Http.get(`http://127.0.0.1:8000/blogs/?page=${newValue}`)
        .then(response => {
            data.blogsInfo = response['data']
            total.value = data.blogsInfo['count']
            next.value = data.blogsInfo['next']
            previous.value = data.blogsInfo['previous']
        })
    })
// 实现分页逻辑
    const handlePrevClick = () => {
        Http.get(previous.value)
        .then(response => {
            data.blogsInfo = response['data']
            total.value = data.blogsInfo['count']
            next.value = data.blogsInfo['next']
            previous.value = data.blogsInfo['previous']
        })
    }
    const handleNextClick = () => {
        Http.get(next.value)
        .then(response => {
            data.blogsInfo = response['data']
            total.value = data.blogsInfo['count']
            next.value = data.blogsInfo['next']
            previous.value = data.blogsInfo['previous']
        })
    }
</script>

<style>

</style>