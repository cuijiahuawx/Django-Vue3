<template>
    <BaseHeader :msg="userinfo"/>
    <el-row v-if="status">
        <el-col :span="4"></el-col>
        <el-col :span="16">
            <p>标签</p>
            <el-checkbox-group v-model="data.tags" size="small">
                <div v-for="type in data.types" :key="type.id">
                     <el-checkbox :label=type.name border></el-checkbox>
                </div>
            </el-checkbox-group>
        <el-divider></el-divider>
            <el-form size="small" label-position="top">
            <el-form-item label="标题">
                <el-input v-model="blog.title"></el-input>
            </el-form-item>
            </el-form>
        <el-divider></el-divider>
            <p>内容</p>
            <md-editor v-model="blog.content" />      // 博客内容
        <el-divider></el-divider>
            <el-button type="success" @click="newBlog" >提交</el-button>
        </el-col>
        <el-col :span="4"></el-col>
    </el-row>
    <p v-else>你需要登录后才能访问此页面！！！</p>
</template>

<script lang="ts" setup>
    import { onMounted, reactive, ref, watch} from 'vue'
    import { Http } from '~/api/request';
    import { storeToRefs } from "pinia";
    import { UserInfoStore } from "~/store/userInfo";
    import { ElMessage } from 'element-plus'
    import { useRouter } from 'vue-router';
    import MdEditor from 'md-editor-v3';
    import 'md-editor-v3/lib/style.css';
    // 引入路由管理
    const router = useRouter()
    // 引入Pinia存储
    const userInfo = UserInfoStore()
    const { userId, status, access, refresh } = storeToRefs(userInfo)

    const userinfo = ref('yes')
    const fill = ref(true)

    const checkboxGroup1 = ref(['Option1'])

    const blog = reactive({
        title: '',
        content: '',
    })

    interface BlogType {
        "id": string,
        "name": string
    }

    const data = reactive({
        types: [] as BlogType[],
        tags: [],
        tagsID: [] as string[],
    })

    onMounted(() => {
        Http.get('blogs/types')
        .then(response => {
            data.types = response['data']
            console.log(data.types)
        })
    })
    // 创建博客逻辑
    const newBlog = () => {
        for(const tag of data.tags) {
            for(const t of data.types){
                if(tag==t.name){
                    data.tagsID.push(t.id)
                }
            }
        }
        Http.post('api/token/verify/', {
                token: access.value
            })
            .then(response => {
                    Http.post('blogs/newBlog/', {
                        "title": blog.title,
                        "content": blog.content,
                        "author": userId.value,
                        "blog_type": data.tagsID
                    },
                    {
                        headers: {
                            'Authorization': `Bearer ${access.value}`
                        }
                    })
                    .then(response => {
                        ElMessage('创建新博客成功！')
                        router.push({path: '/blogs'})
                    })
                })
                .catch(error => {
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
                        "blog_type": data.tagsID
                    },
                    {
                    headers: {
                            'Authorization': `Bearer ${access.value}`
                        }
                    })
                    .then(response => {
                        ElMessage('创建新博客成功！')
                        router.push({path: '/blogs'})
                    })
                }, 1000)
            }
        )
    }
</script>

<style>

</style>
