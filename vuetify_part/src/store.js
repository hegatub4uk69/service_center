import {createStore} from "vuex";
import axios from "axios";
import {API} from "@/axios";

export const store = createStore({
  state: {
    accessToken: localStorage.getItem('token') || null,
  },
  mutations: {
    updateStorage(state, {access}) {
      state.accessToken = access
    },
    destroyToken(state) {
      state.accessToken = null
      localStorage.removeItem('token')
    }
  },
  getters: {
    loggedIn(state) {
      return state.accessToken != null
    }
  },
  actions: {
    userLogout(context) {
      if (context.getters.loggedIn) {
        return new Promise((resolve, reject) => {
          API.post('auth/token/logout')
            .then(response => {
              console.log(response)
              context.commit('destroyToken')
              resolve()
            })
            .catch(err => {
              context.commit('destroyToken')
              reject(err)
            })
        })
      }
    },
    userLogin(context, usercredentials) {
      return new Promise((resolve, reject) => {
        axios.post('http://localhost:8000/get-token', {
          username: usercredentials.username,
          password: usercredentials.password
        })
          .then(response => {
            localStorage.setItem('token', response.data.token)
            context.commit('updateStorage', {access: response.data.token})
            axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`
            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    }
  }
})
