import axios from "axios";

axios.defaults.withCredentials = true

const MusicHttp =  axios.create({
    baseURL: 'http://127.0.0.1:4000',
    timeout: 5000,
})



export {MusicHttp}