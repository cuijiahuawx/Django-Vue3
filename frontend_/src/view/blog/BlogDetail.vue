<script lang="ts" setup>
    import { Http } from '~/api/request';
    import { ref, onMounted, reactive, watch, getCurrentInstance, PropType, computed } from 'vue'
    import { useRouter ,useRoute} from 'vue-router';
    import Tags from '~/view/blog/Tags.vue'
    import { UserInfoStore } from '~/store/userInfo';
    import { storeToRefs } from 'pinia';
    // 引入Markdown
    import MdEditor from 'md-editor-v3';
    import 'md-editor-v3/lib/style.css';
    // 导航栏设置
    const userinfo = ref('yes')
    // 引入Pinia存储
    const userInfo = UserInfoStore()
    const { name } = storeToRefs(userInfo)
    interface BlogDetail {
        "id": number,
        "title": string,
        "content": string,
        "created_time": string,
        "last_updated_time": string,
        "author": string,
        "blog_type": number[]
    }
    // 控制Markdown类型
    const show = ref(false)
    const edit = () => {
        if(show.value == false){
            show.value = true
        }else if(show.value == true){
            show.value = false
        }
    }
    // 文章保存
    const save = () => {

    }
    // 页面加载时，请求博客列表
    const data =  reactive({
        blogDetail: {} as BlogDetail
    })
    onMounted(() => {
        const route = useRoute()
        const id = route.params['id']
        Http.get(`/blogs/detail/${id}/`)
        .then(response => {
            data.blogDetail = response['data']
        })
    })
    // 获取文章标题列表
    interface CatLog {
        "text": string,
        "level": number
    }
    const catalogList =  ref([] as CatLog[])
    const onGetCatalog = (list: CatLog[]) => {
        catalogList.value = list
    }

    interface TocItem {
        text: string;
        level: number;
        children?: Array<TocItem>;
    }

    const props = defineProps({
    heads: {
        type: Array as PropType<Array<any>>
    }
    });

    const catalogs = computed(() => {
    const tocItems: TocItem[] = [];

    props.heads?.forEach(({ text, level }) => {
        const item = { level, text };

        if (tocItems.length === 0) {
            // 第一个 item 直接 push
            tocItems.push(item);
        } else {
            let lastItem = tocItems[tocItems.length - 1]; // 最后一个 item

            if (item.level > lastItem.level) {
                // item 是 lastItem 的 children
                for (let i = lastItem.level + 1; i <= 6; i++) {
                    const { children } = lastItem;
                    if (!children) {
                        // 如果 children 不存在
                        lastItem.children = [item];
                        break;
                    }

                    lastItem = children[children.length - 1]; // 重置 lastItem 为 children 的最后一个 item

                    if (item.level <= lastItem.level) {
                        // item level 小于或等于 lastItem level 都视为与 children 同级
                        children.push(item);
                        break;
                    }
                }
            } else {
                // 置于最顶级
                tocItems.push(item);
            }
        }
    });
    return tocItems;
    });
</script>

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
                {{show}}
                <el-button v-if="data.blogDetail.author == name" @click="edit">修改内容</el-button>
                <el-button v-if="data.blogDetail.author == name" @click="save">提交修改</el-button>
                <el-descriptions :title=data.blogDetail.title>
                    <el-descriptions-item label="作者">{{ data.blogDetail.author }}</el-descriptions-item>
                    <el-descriptions-item label="标签">{{ data.blogDetail.blog_type }}</el-descriptions-item>
                </el-descriptions>
                {{catalogList}}
                <md-editor v-model="data.blogDetail.content"  v-if="show"/>
                <md-editor v-model="data.blogDetail.content" previewOnly=true @onGetCatalog="onGetCatalog" v-else/>
            </el-main>
        </el-container>
    </el-container>
</template>

<style>
.el-header {
        position: relative;
        width: 100%;
        height: 60px;      
    }
.el-aside {
  display: block;
  position: absolute;
  left: 0;
  top: 60px;
  bottom: 0;
  }
.el-main {
  position: absolute;
  left: 200px;
  right: 0;
  top: 60px;
  bottom: 0;
  overflow-y: scroll;
  }
</style>