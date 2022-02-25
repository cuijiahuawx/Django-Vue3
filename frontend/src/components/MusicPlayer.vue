<script lang="ts" setup>
    import { storeToRefs } from 'pinia';
    import { onMounted, reactive, ref, watch } from 'vue';
    import Aplayer from 'vue3-aplayer'
    import { MusicInfoStore } from "~/store/musicInfo"

import ColorThief from 'colorthief/dist/color-thief.mjs'

const colorThief = new ColorThief();
const t = ref('')

    const musicInfo = MusicInfoStore()
    const { musicSongs } = storeToRefs(musicInfo)


    const mode = ref(true)
    const changeMode = () => {
        console.log('change')
        if(mode.value == true){
            mode.value = false
            current.song = musicSongs.value[index.value]
        }else if (mode.value == false){
           mode.value = true
           current.song = musicSongs.value[index.value]
        } 
console.log('over')
                    let domImg = document.querySelector('#background');
                    let colorthief = new ColorThief();
                    console.log(domImg)
     t.value = colorthief.getColor(domImg);
                                            console.log(t.value)
    }
    const index = ref(0)
    const current = reactive({
        song: {
            title: '',
            artist: '',
            src: '',
            pic: '',
            lrc: ''
        }
    })
    const max = ref(musicSongs.value.length-1)
    const min = ref(0)
    const status = ref(true)
    const active = () => {
        status.value = false
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

const hide = ref(false)
    onMounted(() => {

    })
</script>

<template>
{{t}}
<img src="https://p2.music.126.net/0Yq1-QfMt6rVgbwIi5yJvA==/3276544652384849.jpg" v-show="hide" id="background" crossorigin="anonymous">
    <n-space vertical>
        <n-button size="tiny" type="info" dashed @click="active" v-if="status">
            激活
        </n-button>
        <n-button size="tiny" type="info" dashed @click="changeMode">
            改变模式
        </n-button>
        <n-badge :value="index+1">
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
    </n-space>
    <n-space v-if="mode">
        <n-button size="tiny" type="info" dashed @click="pre" v-if="index > min">
            上一首
        </n-button>
        <n-button size="tiny" type="info" dashed @click="next" v-if="index < max">
            下一首
        </n-button>
    </n-space>
</template>

<style>
</style>