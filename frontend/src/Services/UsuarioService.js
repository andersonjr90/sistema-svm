import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class UsuarioService{

    constructor(){}

    getUsuarios() {
        const url = `${API_URL}/api/usuario/`;
        return axios.get(url).then(response => response.data);
    }
    getUsuariosByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getUsuario(pk) {
        const url = `${API_URL}/api/usuario/${pk}/`;
        return axios.get(url).then(response => response.data);
    }
    deleteUsuario(usuario){
        const url = `${API_URL}/api/usuario/${usuario.pk}/`;
        return axios.delete(url);
    }
    createUsuario(usuario){
        const url = `${API_URL}/api/usuario/`;
        return axios.post(url,usuario);
    }
    updateUsuario(usuario){
        const url = `${API_URL}/api/usuario/${usuario.pk}/`;
        return axios.put(url,usuario);
    }
}