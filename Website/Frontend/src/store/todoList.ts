import { defineStore } from "pinia";
import { Names } from './names'

interface Todo {
    content: string,
    status: boolean,
}

export const TodoListInfoStore = defineStore(Names.todoList, {
    state: () => ({
        todoList: [] as Todo[]
    }),
    actions: {
        add(content: string) {
            const todo: Todo = {
                content: content,
                status: false
            }
            this.todoList.push(todo)
        },
        remove(todo: Todo) {
            const index = this.todoList.indexOf(todo)
            this.todoList.splice(index, 1)
        },
        ok(todo: Todo) {

        },
        clear() {
            localStorage.removeItem('todoList')
            this.todoList.splice(0, this.todoList.length)
        }
    },
    persist: {
        enabled: true,
        strategies: [
            {
                key: 'todoList',
                storage: localStorage,
            },
        ]
    }
})