<script lang="ts" setup>
    import { storeToRefs } from 'pinia';
    import { reactive, ref, watch, onMounted} from 'vue';
    import Aplayer from 'vue3-aplayer'
    import { MusicInfoStore } from "~/store/musicInfo"


    interface Song {
        src: string
        title: string
        artist: string
        pic: string
        lrc: string
        theme: string
    }


    const musicInfo = MusicInfoStore()
    const { musicSongs} = storeToRefs(musicInfo)

    onMounted(() => {
        if (localStorage.music) {
            current.song = JSON.parse(localStorage.music)["musicSongs"][0]
            haveSongs.value = true;
        }
    })


    const hide = ref(false)

    const current = reactive({
        song : {} as Song
    })

    const mode = ref(true)
    const changeMode = () => {
        if(mode.value == true){
            mode.value = false
        }else if (mode.value == false){
            mode.value = true
        }
    }

    const max = ref(musicSongs.value.length-1)
    const min = ref(0)

    const index = ref(0)
    const haveSongs = ref(false)
    const active = () => {
        current.song = musicSongs.value[index.value]
    }

    const next = () => {
        index.value += 1
        current.song = musicSongs.value[index.value]
    }

    const pre = () => {
        index.value -= 1
        current.song = musicSongs.value[index.value]
    }

    watch(current, (nV, oV) => {
            max.value = musicSongs.value.length-1
            current.song = musicSongs.value[index.value]
            }
    )
</script>

<template>
    <div class="container" v-if="haveSongs">
        <img :src=current.song.pic v-show="hide" id="background" crossorigin="anonymous">
        <n-space vertical>
            <n-button size="tiny" type="info" dashed @click="changeMode">
                切换模式
            </n-button>
            <n-button size="tiny" type="info" dashed @click="pre" v-if="index > min">
                上一首
            </n-button>
            <n-button size="tiny" type="info" dashed @click="next" v-if="index < max">
                下一首
            </n-button>
            <n-badge :value="index+1" color="Salmon" v-if="mode">
                <aplayer autoplay
                    :mini="mode"
                    :showLrc=true
                    :list="musicSongs"
                    :music="{
                        title: current.song.title,
                        artist: current.song.artist,
                        src: current.song.src,
                        pic: current.song.pic,
                        theme: 'pic'
                    }"
                />
            </n-badge>
            <aplayer autoplay
                :mini="mode"
                :showLrc=true
                :list="musicSongs"
                :music="{
                    title: current.song.title,
                    artist: current.song.artist,
                    src: current.song.src,
                    pic: current.song.pic,
                    theme: 'pic'
                }"
            v-else/>
        </n-space>
    </div>
</template>

<style scoped>
.container {
    width: 300px;
}
</style>