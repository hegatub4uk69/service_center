import axios from "axios";

  export const API = axios.create({
  baseURL: 'http://localhost:8000/',
  timeout: 1000,
  headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
})
