import { defineStore } from "pinia";
import { MusicHttp } from '~/api/musicRequest';
import { Names } from './names'

interface Song {
    src: string
    title: string
    artist: string
    pic: string
    lrc: string
    theme: string
}

export const MusicInfoStore = defineStore(Names.musicInfo, {
    state: () => ({
        musicStatus: false,
        musicList: '',
        musicSongs: [] as Song[],
        current: {} as Song
    }),
    getters: {
    },
    actions: {
        async getSongUrl(songId: string) {
            var result = ''
            await MusicHttp.get(`/song/url?id=${songId}`).then(
                (response: any) => {
                    result = response.data['data'][0]['url']
                }
            )
            return result
        },
        async getLyric(songId: string) {
            var result = ''
            await MusicHttp.get(`/lyric?id=${songId}`).then(
                (response: any) => {
                    result = response.data['lrc']['lyric']
                }
            )
            return result
        },
        async getSongs(songsId: string) {
            MusicHttp.get(`playlist/track/all?id=${songsId}`, { withCredentials: true }).then(
                async (response: any) => {
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
                        const songInfo: Song = {
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
        login(email: any, password: string, musicList: any) {
            MusicHttp.post('/login/', {
                email: email.value,
                password: password
            })
                .then(async (response) => {
                    this.musicList = musicList.value
                    await this.getSongs(this.musicList).then(() => {
                        console.log("current")
                        this.current = this.musicSongs[0]
                        this.musicStatus = true
                    })
                })
        },
        logout() {
            this.musicStatus = false
            this.musicList = ''
            this.musicSongs = [] as Song[]
            this.current = {} as Song
            localStorage.removeItem('music')
        }
    },
    persist: {
        enabled: true,
        strategies: [
            {
                key: 'music',
                storage: localStorage,
            },
        ]
    }
})