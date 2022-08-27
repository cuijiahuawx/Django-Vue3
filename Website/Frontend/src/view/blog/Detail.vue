<script lang="ts" setup>
// 引入官方相关库
import { onMounted, reactive, ref } from 'vue';
// Pinia引入存储
import { storeToRefs } from 'pinia';
import { UserInfoStore } from '~/store/userInfo';
// 引入网络请求
import { Http } from '~/api/request'
import { useRoute, useRouter } from 'vue-router';
// 引入第三方组件
import MdEditor, { Footers, ToolbarNames } from 'md-editor-v3'
import 'md-editor-v3/lib/style.css';
import TimeNow from '~/components/TimeNow/index.vue'
import EmojiExtension from '~/components/EmojiExtension/index.vue'
import MarkExtension from '~/components/MarkExtension/index.vue'
import ReadExtension from '~/components/ReadExtension/index.vue'
// 引入自定义组件


/**
 * 0. 组件全局相关设置
 * 1. 页面加载时，请求博客列表
 * 2. Markdown编辑器设置
 * 3. 删除博客逻辑实现
 * 4. 更新博客逻辑实现
 */


// 0. 组件全局相关设置
// Pinia存储
const userInfo = UserInfoStore()
const { status, access, refresh, userID } = storeToRefs(userInfo)
// 路由管理
const router = useRouter()


// 1. 页面加载时，请求博客列表
interface BlogDetail {
    "id": number,
    "title": string,
    "content": string,
    "created_time": string,
    "last_update_time": string,
    "author": string,
    "authorName": string,
    "blog_type": string[]
}
const data = reactive({
    blogDetail: {} as BlogDetail
})
const route = useRoute()
const id = route.params['id']
onMounted(() => {
    Http.get(`/blog/detail/${id}/`)
        .then(response => {
            data.blogDetail = response['data']
        })
})


// 2. Markdown编辑器设置
const state = reactive({
    id: 'my-editor',
    theme: 'vuepress',
    codeTheme: 'atom',
    catalogList: [] as string[],
    placeHolder: '请在此输入内容',
})
// 工具栏配置
const toolBars = ref([
    'bold',
    'underline',
    'italic',
    'strikeThrough',
    '-',
    'title',
    'sub',
    'sup',
    'quote',
    'unorderedList',
    'orderedList',
    '-',
    'codeRow',
    'code',
    'link',
    'image',
    'table',
    'mermaid',
    'katex',
    0,
    1,
    2,
    '-',
    'revoke',
    'next',
    'save',
    '=',
    'prettier',
    'pageFullscreen',
    'fullscreen',
    'preview',
    'htmlPreview',
    'catalog',
] as ToolbarNames[])
// 底栏配置
const footers = ['markdownTotal', 0, '=', 1, 'scrollSwitch'] as Footers[]
// 自定义工具栏配置
const mdText = ref("hello vite!")
// 内容实时变化绑定
const onChange = (v: string) => (data.blogDetail.content = v)


// 更新博客逻辑实现
const editBlog = () => {
    Http.post('api/token/verify/', {
        token: access.value
    })
        .then(() => {
            Http.put(`/blog/detail/${id}/`, {
                "title": data.blogDetail.title,
                "content": data.blogDetail.content,
                "blog_type": data.blogDetail.blog_type
            },
                {
                    headers: {
                        'Authorization': `Bearer ${access.value}`
                    }
                })
                .then(() => {
                    router.push({ path: '/blogs' })
                })
        })
        .catch(() => {
            Http.post('api/token/refresh/', {
                "refresh": refresh.value
            })
                .then(response => {
                    access.value = response.data['access'];
                    refresh.value = response.data['refresh'];
                })
            setTimeout(() => {
                Http.put(`/blog/detail/${id}/`, {
                    "title": data.blogDetail.title,
                    "content": data.blogDetail.content,
                    "blog_type": data.blogDetail.blog_type
                },
                    {
                        headers: {
                            'Authorization': `Bearer ${access.value}`
                        }
                    })
                    .then(() => {
                        router.push({ path: '/blogs' })
                    })
            }, 1000)
        })
}


// 删除博客逻辑实现
const delBlog = () => {
    Http.post('api/token/verify/', {
        token: access.value
    })
        .then(() => {
            Http.delete(`/blog/detail/${id}/`,
                {
                    headers: {
                        'Authorization': `Bearer ${access.value}`
                    }
                })
                .then(() => {
                    router.push({ path: '/blogs' })
                })
        })
        .catch(() => {
            Http.post('api/token/refresh/', {
                "refresh": refresh.value
            })
                .then(response => {
                    access.value = response.data['access'];
                    refresh.value = response.data['refresh'];
                })
            setTimeout(() => {
                Http.delete(`/blog/detail/${id}/`,
                    {
                        headers: {
                            'Authorization': `Bearer ${access.value}`
                        }
                    })
                    .then(() => {
                        router.push({ path: '/blogs' })
                    })
            }, 1000)
        })
}
</script>

<template>
    <div v-if="data.blogDetail.id">
        <MdEditor :placeholder="state.placeHolder" :footers="footers" :editorId="state.id"
            :modelValue="data.blogDetail.content" :preview-theme="state.theme" :code-theme="state.codeTheme"
            :showCodeRowNumber=true :toolbars="toolBars" @onChange="(v: string) => (data.blogDetail.content = v)"
            :previewOnly="!(userID == data.blogDetail.author)">
            <template #defToolbars>
                <EmojiExtension :editor-id="state.id" @on-change="onChange" />
                <MarkExtension :editor-id="state.id" @on-change="onChange" />
                <ReadExtension :mdText=mdText />
            </template>
            <template #defFooters>
                <TimeNow />
            </template>
        </MdEditor>
        <div v-if="status && (userID == data.blogDetail.author)">
            <n-button type="primary" @click="editBlog">
                更改
            </n-button>
            <n-button type="error" @click="delBlog">
                删除
            </n-button>
        </div>
    </div>
    <div v-else>
        无此博客
    </div>
</template>

<style scoped>
</style>