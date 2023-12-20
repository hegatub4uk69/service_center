import {createStore} from "vuex";
import axios from "axios";
import API from "@/axios";

export const store = createStore({
  state: {
    accessToken: localStorage.getItem('token') || null,
    uid: null,
    user_data: {
      staff_full_name: null,
      staff_phone: null,
      login: null
    }
  },
  mutations: {
    updateStorage(state, {access}) {
      state.accessToken = access
    },
    destroyToken(state) {
      localStorage.removeItem('token')
      state.accessToken = null
    },
    setUserData(state, {login, uid}) {
      state.user_data.login = login
      state.user_data.uid = uid
    },
    setStaffData(state, {staff_full_name, staff_phone}) {
      state.user_data.staff_full_name = staff_full_name
      state.user_data.staff_phone = staff_phone
    }
  },
  getters: {
    loggedIn(state) {
      return state.accessToken != null
    },
    userId(state) {
      return state.uid
    },
    staffDataExist(state) {
      return state.user_data.login != null
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
    },
    userData(context) {
      if (context.getters.loggedIn) {
        return new Promise((resolve, reject) => {
          API.get('auth/users/me/')
            .then(response => {
              context.commit('setUserData', {login: response.data.username, uid: response.data.id})
              console.log(response.data.username, response.data.id)
              API.post('get-staff-data', response.data.id)
                .then(response => {
                  context.commit('setStaffData', {
                    staff_full_name: response.data.result[0]['full_name'],
                    staff_phone: response.data.result[0]['phone']
                  })
                  console.log(response.data.result[0]['full_name'],)
                  resolve()
                }).catch(err => {
                reject(err)
              })
              resolve()
            }).catch(err => {
            reject(err)
          })
        })
      }
    }
  }
})
