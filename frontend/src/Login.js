import React, {useState} from 'react';
import './Login.css';
import logo from './Components/header/brasao-sem-fundo.png';
import * as api from './Services/api';
//import firebase from '../data/Firebase';

export default function Login() {
  
  const [formState, setFormState] = useState({
    "user": {
      "email": "",
      "password": "",
    }
  });

  const handleLoginSubmit = async (e) => {
    e.preventDefault()

    await api.login(formState)
    window.location.reload()
  };

  const handleInputChange = (e) => {
    e.persist()
    const value = e.target.value;
    
    setFormState( () => {
      let next = formState
      next.user[e.target.name] = value
      return next
    })
  };

  return (
    <div class="Container">
      <img src={logo} alt="logo" /> 
      <h1>Seja bem vindo!</h1>
      <h2>Faça login para continuar.</h2>
      <form className="login-form" onSubmit={handleLoginSubmit} onChange={handleInputChange}>
        <input type="text" name="email" placeholder="Email"/>
        <input type="password" name="password" placeholder="Senha"/>
        <input className="btn-preset" type="submit" placeholder="Entrar"/>
      </form>
    </div>   

  );
}