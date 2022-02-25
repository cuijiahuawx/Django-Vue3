import { defineStore } from "pinia";
import { Http } from '~/api/request';
import jwtDecode from 'jwt-decode'

interface Decode {
  is_useful: boolean,
  user_id: string,
  avatar: string,
  name: string,
  email: string
}

interface TokenResponseData {
  access: string,
  refresh:  string
}

interface TokenResponse {
  data: TokenResponseData
}

export const UserInfoStore = defineStore("userInfo", {
    state: () => ({
        status: false,
        userId: '',
        access: '',
        refresh: '',
        
        is_useful: false,
        loginEmail: '',
        name: '',
        avatar: '',
    }),
    getters: {
    },
    actions: {
        login (email: string, password: string) {
            Http.post('api/token/', {
                email: email,
                password: password
              })
              .then((response: TokenResponse) => {
                // 获取Token
                this.access = response.data['access'];
                this.refresh = response.data['refresh'];
                // 从Token中解析出信息
                const decode: Decode =  jwtDecode(this.access);
                this.is_useful = decode['is_useful'];
                if (this.is_useful) {
                  console.log("可用")
                  this.userId = decode['user_id'];
                  this.avatar = decode['avatar'];
                  this.name = decode['name'];
                  this.loginEmail = decode['email'];
                  this.status = true;
                }
                else{
                  this.logout()
                }
              });
          },
        logout () {
            this.status = false
            this.access = ''
            this.refresh = ''
            this.is_useful = false
            this.loginEmail =  ''
            this.name = ''
            this.avatar = ''
        }
    }
})