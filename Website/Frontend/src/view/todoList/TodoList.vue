<script lang="ts" setup>
import { h, nextTick, reactive, ref } from "vue"
import { storeToRefs } from "pinia"
import { TodoListInfoStore } from "~/store/todoList"
import { NButton, NInput } from 'naive-ui'
import { DataTableColumns, DropdownOption } from 'naive-ui'

// 引入Pinia存储
const TodoListInfo = TodoListInfoStore()
const { todoList } = storeToRefs(TodoListInfo)

interface Todo {
    content: string,
    status: boolean,
}
const newTodo = reactive({
    content: '',
})
const addNewTodo = () => {
    TodoListInfo.add(newTodo.content)
    newTodo.content = ''
}
// 下拉菜单设置
const focusTodo = ref({
    content: '',
    status: false,
})
const showDropdown = ref(false)
const x = ref(0)
const y = ref(0)
const handleSelect = (key: string) => {
    if (key === 'remove') {
        TodoListInfo.remove(focusTodo.value)
        focusTodo.value = {
            content: '',
            status: false,
        }
    }
    showDropdown.value = false
}
const onClickoutside = () => {
    showDropdown.value = false
}
const options: DropdownOption[] = [
    {
        label: () => h('span', { style: { color: 'red' } }, '删除'),
        key: 'remove'
    }
]
// 数据表格设置
const cols: DataTableColumns<Todo> = [
    {
        title: 'Content',
        key: 'content',
        render(row, index) {
            return h(NInput, {
                value: row.content,
                onUpdateValue(v) {
                    todoList.value[index].content = v
                },
                disabled: row.status
            })
        }
    },

]

const data: Todo[] = todoList.value
const rowProps = (row: Todo) => {
    return {
        onContextmenu: (e: MouseEvent) => {
            focusTodo.value = row
            e.preventDefault()
            showDropdown.value = false
            nextTick().then(() => {
                showDropdown.value = true
                x.value = e.clientX
                y.value = e.clientY
            })
        },
        ondblclick: () => {
            row.status = !row.status
        }
    }
}

</script>

<template>
    <n-space justify="center" vertical>
        <n-space justify="center">
            <n-input v-model:value="newTodo.content" type="text" placeholder="请输入新的todo" />
            <n-button @click="addNewTodo">添加</n-button>
            <n-button @click="TodoListInfo.clear">清除</n-button>
        </n-space>
        <n-space justify="center">
            <n-data-table :columns="cols" :data="data" :row-props="rowProps" />

        </n-space>
    </n-space>
    <n-dropdown placement="bottom-start" trigger="manual" :x="x" :y="y" :options="options" :show="showDropdown"
        :on-clickoutside="onClickoutside" @select="handleSelect" />
</template>

<style scoped>
</style>

