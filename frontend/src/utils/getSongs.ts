import { MusicHttp } from '~/api/musicRequest';

interface Song {
    src: string
    title: string
    artist: string
    pic: string
    lrc: string
}

const getSongUrl = (songId: string) : string => {
    var result = ''
    MusicHttp.get(`/song/url?id=${songId}`).then(
        (response) => {
            result = response.data['data'][0]['url']
        }
    )
    console.log(result)
    return result
}

const getLyric = (songId: string) : string => {
    var result = ''
    MusicHttp.get(`/lyric?id=${songId}`).then(
        (response) => {
            result = response.data['lrc']['lyric']
        }
    )
    console.log(result)
    return result
}

const getSongs = (songsId: string) :Song[] => {
    const songList: Song[] = []
    MusicHttp.get(`playlist/track/all?id=${songsId}`, {withCredentials: true}).then(
        (response) => {
            for (const song of response.data['songs']) {
                const id = song['id']
                const title = song['name']
                const artist = song['ar'][0]['name']
                const pic = song['al']['picUrl']

                var src = ''
                var lrc = ''         
                MusicHttp.get(`/lyric?id=${id}`).then(
                    (response) => {
                        console.log("获取歌词")
                        lrc = response.data['lrc']['lyric']
                    }
                )

                MusicHttp.get(`/song/url?id=${id}`).then(
                    (response) => {
                        src = response.data['data'][0]['url']
                    }
                )
                const songInfo:Song = {
                    src: src,
                    title: title,
                    artist: artist,
                    pic: pic,
                    lrc: lrc,
                }
                songList.push(songInfo)
            }
        }
    )
    return songList
}
export default getSongs