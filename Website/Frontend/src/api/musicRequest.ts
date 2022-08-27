import axios from "axios";

axios.defaults.withCredentials = true

const MusicHttp =  axios.create({
    baseURL: 'http://127.0.0.1:3000',
    timeout: 5000,
})

MusicHttp.defaults.withCredentials = true

export {MusicHttp}