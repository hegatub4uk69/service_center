import {createStore} from "vuex";
import axios from "axios";

export const store = createStore({
  state: {
      accessToken: null,
  },
  mutations: {
    updateStorage(state, {access}) {
      state.accessToken = access
    },
    destroyToken(state) {
      state.accessToken = null
    }
  },
  getters: {
    loggedIn(state) {
      return state.accessToken != null
    }
  },
  actions: {
    userLogout(context, state) {
      if (context.getters.loggedIn) {
        return new Promise((resolve, reject) => {
          axios.post('http://localhost:8000/auth/token/logout', {
            headers: {Authorization: `Token ${state.accessToken}`}
          })
            .then(response => {
              console.log(response)
              context.commit('destroyToken')
              resolve()
            })
            .catch(err => {
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
            context.commit('updateStorage', {access: response.data.token})
            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    }
  }
})
