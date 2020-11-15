import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class TripulanteService{

    constructor(){}


    getTripulantes() {
        const url = `${API_URL}/api/tripulante/`;
        return axios.get(url).then(response => response.data);
    }
    getTripulantesByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getTripulante(pk) {
        const url = `${API_URL}/api/tripulante/${pk}/`;
        return axios.get(url).then(response => response.data);
    }
    deleteTripulante(tripulante){
        const url = `${API_URL}/api/tripulante/${tripulante.pk}/`;
        return axios.delete(url);
    }
    createTripulante(tripulante){
        const url = `${API_URL}/api/tripulante/`;
        return axios.post(url,tripulante);
    }
    updateTripulante(tripulante){
        const url = `${API_URL}/api/tripulante/${tripulante.pk}/`;
        return axios.put(url,tripulante);
    }
}