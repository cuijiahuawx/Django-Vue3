import { defineStore } from "pinia"
import { Http } from '~/api/request'
import jwtDecode from 'jwt-decode'
import { Names } from './names'

interface Decode {
    user_id: string,
    avatar: string,
    userName: string,
    email: string,
    musicID: string,
    musicEmail: string
}

interface TokenResponseData {
    access: string,
    refresh:  string
}

interface TokenResponse {
    data: TokenResponseData
}

export const UserInfoStore = defineStore(Names.userInfo, {
    state: () => ({
        status: false,
        userID: '',
        access: '',
        refresh: '',
        remember: false,
        loginEmail: '',
        name: '',
        avatar: '',
        musicID: '',
        musicEmail: '',
    }),
    getters: {
    },
    actions: {
        login (email: string, password: string) {
            Http.post('/api/token/', {
                    email: email,
                    password: password
                })
                .then((response: TokenResponse) => {
                    // 获取Token
                    this.access = response.data['access']
                    this.refresh = response.data['refresh']
                    // 从Token中解析出信息
                    const decode: Decode =  jwtDecode(this.access);
                    this.userID = decode['user_id']
                    this.avatar = decode['avatar']
                    this.name = decode['userName']
                    this.loginEmail = decode['email']
                    this.musicID = decode['musicID']
                    this.musicEmail = decode['musicEmail']
                    this.status = true;
                })
                .catch((error: any) => {
                    window?.$message?.error("登录出现错误")
                })
            },
        logout () {
            this.status = false
            this.access = ''
            this.refresh = ''
            this.remember = false
            this.loginEmail =  ''
            this.name = ''
            this.avatar = ''
            this.musicID = ''
            this.musicEmail = ''
        },
        checkRemember () {
            this.remember = true
        }
    },
    persist: {
        enabled: true,
        strategies: [
            {
                key: 'user',
                storage: localStorage, paths: [
                    "userID",
                    "loginEmail",
                    "name",
                    "avatar",
                    "musicID",
                    "musicEmail",
                    'access',
                    'refresh',
                    "status",
                    'remember',
                ],
            },
        ]
    }
})