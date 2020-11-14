import axios from "axios";
import { getToken } from "./auth";

const api = axios.create({
  baseURL: "http://127.0.0.1:3333"
});

api.interceptors.request.use(async config => {
  const token = getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

const user = JSON.parse(localStorage.getItem('user'));

async function check_admin(setIsAdmin) {
  if (user){
    const axiosConfig = {
      headers: {
        "Content-Type": "application/json",   
        "Authorization": user.token
      },
    };
  
    api.get("/admin", axiosConfig)
      .then(response => {
        setIsAdmin(true)
        localStorage.setItem("admin", true)
      }).catch(error => {
        localStorage.setItem("admin", false)
      })
  }
}

async function login(formState) {
  await api.post("/login", formState)
    .then( response => {
      localStorage.setItem('user', JSON.stringify(response.data))
      check_admin()
    }).catch ( error => {
      window.alert("Não foi possível fazer o login. Verifique suas informações e tente novamente")
    })
}

export { 
  login,
  check_admin,
  api
}