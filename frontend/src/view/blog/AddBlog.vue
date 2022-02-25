<script lang="ts" setup>
    import MdEditor from 'md-editor-v3';
    import 'md-editor-v3/lib/style.css';

    import { onMounted, reactive, ref} from 'vue'
    import { Http } from '~/api/request';
    import { storeToRefs } from "pinia";
    import { UserInfoStore } from "~/store/userInfo";
    import { useRouter } from 'vue-router';

    // 引入路由管理
    const router = useRouter()
    // 引入Pinia存储
    const userInfo = UserInfoStore()
    const { userId, access, refresh } = storeToRefs(userInfo)

    const blog = reactive({
        title: '',
        content: '',
    })

    // 获取博客标签数据
    interface BlogType {
        "id": string,
        "name": string
    }
    interface Option {
        label: string,
        value: string
    }
    const data = reactive({
        types: [] as BlogType[],
        options: [] as Option[],
    })
    const value= ref([])
    onMounted(() => {
        Http.get('blogs/types')
        .then(response => {
            data.types = response['data']
            for(const type of response['data']){
                data.options.push({
                    label: type.name,
                    value: type.id
                })
            }
        })
    })
    // 创建博客逻辑
    const newBlog = () => {
        Http.post('api/token/verify/', {
                token: access.value
            })
            .then(()=> {
                    Http.post('blogs/newBlog/', {
                        "title": blog.title,
                        "content": blog.content,
                        "author": userId.value,
                        "blog_type": value.value
                    },
                    {
                        headers: { 
                            'Authorization': `Bearer ${access.value}`
                        } 
                    })
                    .then(() => {
                        router.push({path: '/blogs'})
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
                    Http.post('blogs/newBlog/', {
                        "title": blog.title,
                        "content": blog.content,
                        "author": userId.value,
                        "blog_type": value.value
                    },
                    {
                    headers: { 
                            'Authorization': `Bearer ${access.value}`
                        } 
                    })
                    .then(() => {
                        router.push({path: '/blogs'})
                    })
                }, 1000)
            }
        )
    }
</script>

<template>
    <n-select v-model:value="value" multiple :options="data.options" />
    <n-input v-model:value="blog.title" type="text" placeholder="笔记标题" />
    <md-editor v-model="blog.content" />
    <n-button style="margin-top:15px;" type="primary" @click="newBlog">
        添加
    </n-button>  
</template>

<style>
</style>