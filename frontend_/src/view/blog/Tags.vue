<template>
<p>标签列表</p>
    <el-space direction="vertical">
        <el-badge v-for="tag in tagsInfo.tagInfo" :key="tag.id" :value="tag.blog_count" class="item">
                <el-tag >{{tag.name}}</el-tag>
        </el-badge>
    </el-space>
</template>

<script lang="ts" setup>
    import { ref, onMounted, reactive, watch } from 'vue'
    import { Http } from '~/api/request';

    interface Tag {
        "id": string,
        "name": string,
        "blog_count": string,
    }

    const tagsInfo = reactive({
        tagInfo: [] as Tag[]
    })

    onMounted(()=>{
        Http.get('/blogs/types/')
        .then(response => {
            tagsInfo.tagInfo = response['data']
        })
    })

</script>

<style>

</style>