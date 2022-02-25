import { defineStore } from "pinia";
import { MusicHttp } from '~/api/musicRequest';
import { useCookies } from "vue3-cookies";


interface Song {
    src: string
    title: string
    artist: string
    pic: string
    lrc: string
    theme: string
}

const { cookies } = useCookies()

export const MusicInfoStore = defineStore("musicInfo", {
    state: () => ({
        musicStatus: false,
        musicList: '',
        musicSongs: [] as Song[],
        musicCookie: '',
    }),
    getters: {
    },
    actions: {
        async getSongUrl(songId: string){
            var result = ''
            await MusicHttp.get(`/song/url?id=${songId}`).then(
                (response) => {
                    result = response.data['data'][0]['url']
                }
            )
            return result
        },
        async getLyric(songId: string) {
            var result = ''
            await MusicHttp.get(`/lyric?id=${songId}`).then(
                (response) => {
                    result = response.data['lrc']['lyric']
                }
            )
            return result
        },
        async getSongs (songsId: string){
            MusicHttp.get(`playlist/track/all?id=${songsId}`, {withCredentials: true}).then(
                async (response) => {
                            for (const song of response.data['songs']) {
                                const id = song['id']
                                const title = song['name']
                                const artist = song['ar'][0]['name']
                                const pic = song['al']['picUrl']
                                var src = ''
                                var lrc = ''
                                await this.getSongUrl(id).then(res => {
                                    src = res
                                });
                                await this.getLyric(id).then(res => {
                                    lrc = res
                                });
                                const songInfo:Song = {
                                    src: src,
                                    title: title,
                                    artist: artist,
                                    pic: pic,
                                    lrc: lrc,
                                    theme: 'pic'
                                }
                                this.musicSongs.push(songInfo)
                            }
                        }
            )
        },
        login (phone: string, password: string, musicList: string) {
            MusicHttp.post('/login/', {
                email: phone,
                password: password
            })
            .then(async (response) => {
                this.musicList = musicList
                await this.getSongs(musicList).then(() => {
                    this.musicStatus = true
                })
            })
        },
        logout () {
            this.musicStatus = false
            this.musicList = ''
        }
    }
})