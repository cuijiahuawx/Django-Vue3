import axios from "axios";

const Http =  axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 5000
})

export {Http}