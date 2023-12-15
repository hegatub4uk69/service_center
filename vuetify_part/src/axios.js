import axios from "axios";

const getToken = () => {
  let token = null
  const localStorage = window.localStorage.getItem('token')
  if (localStorage) token = localStorage
  return token
}

const API = axios.create({
  baseURL: 'http://localhost:8000/',
})

API.interceptors.request.use((config) => {
  config.headers.Authorization = `Token ${getToken()}`
  return config
})

export default API
