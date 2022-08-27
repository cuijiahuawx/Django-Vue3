<script lang="ts" setup>
// 引入官方相关库
import { onMounted, reactive, ref } from 'vue';
// Pinia引入存储
import { storeToRefs } from 'pinia';
import { UserInfoStore } from '~/store/userInfo';
// 引入网络请求
import { Http } from '~/api/request'
import { useRouter } from 'vue-router';
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
 * 1. 获取博客标签数据
 * 2. 创建博客逻辑实现
 * 3. Markdown编辑器设置
 * 4. 响应Click事件的函数
 */


// 0. 组件全局相关设置
// Pinia存储设置
const userInfo = UserInfoStore()
const { userID, access, refresh } = storeToRefs(userInfo)
// 路由管理设置
const router = useRouter()


// 1. 获取博客标签数据
interface Option {
    label: string,
    value: string
}
const data = reactive({
    options: [] as Option[],
    title: ''
})
const types = ref([])
onMounted(() => {
    Http.get('blog/types')
        .then(response => {
            for (const type of response['data']) {
                data.options.push({
                    label: type.name,
                    value: type.id
                })
            }
        })
})


// 2. 创建博客逻辑实现
const blog = reactive({
    title: '',
    content: '',
})
const newBlog = () => {
    Http.post('api/token/verify/', {
        token: access.value
    })
        .then(() => {
            Http.post('blog/newBlog/', {
                "title": blog.title,
                "content": blog.content,
                "author": userID.value,
                "blog_type": types.value
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
                Http.post('blog/newBlog/', {
                    "title": blog.title,
                    "content": blog.content,
                    "author": userID.value,
                    "blog_type": types.value
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


// 3. Markdown编辑器设置
const state = reactive({
    id: 'my-editor',
    theme: 'vuepress',
    codeTheme: 'atom',
    catalogList: [] as string[],
    placeHolder: '请在此输入内容',
})
const onChange = (v: string) => (blog.content = v)
// 自定义工具栏配置
const mdText = ref("hello vite!")
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
</script>

<template>
    <n-space vertical>
        <n-input v-model:value="blog.title" type="text" placeholder="文章标题" />
        <n-space vertical>
            <n-select v-model:value="types" multiple :options="data.options" />
        </n-space>
        <MdEditor :placeholder="state.placeHolder" :footers="footers" :editorId="state.id" :modelValue="blog.content"
            :preview-theme="state.theme" :code-theme="state.codeTheme" :showCodeRowNumber=true :toolbars="toolBars"
            @onChange="(v: string) => (blog.content = v)">
            <template #defToolbars>
                <EmojiExtension :editor-id="state.id" @on-change="onChange" />
                <MarkExtension :editor-id="state.id" @on-change="onChange" />
                <ReadExtension :mdText=mdText />
            </template>
            <template #defFooters>
                <TimeNow />
            </template>
        </MdEditor>
        <n-button type="primary" @click="newBlog">
            创建新博客
        </n-button>
    </n-space>

</template>

<style scoped>
</style>