import React from 'react';

import { BrowserRouter, Router, Switch, Route, Redirect } from 'react-router-dom';
import { isAuthenticated } from "../Services/auth";

import Login from '../Login';
import Register from '../Register';
import Agenda from './pages/Agenda';
import FilaDeEspera from './pages/FilaDeEspera';
import Tarefas from './pages/Tarefas';

const user = JSON.parse(localStorage.getItem("user"));

const Routes = () => (
    <BrowserRouter>
        <Switch>
            <Route exact path="/login">
                <Login />
            </Route>
            <Route path="/register">
                <Register />
            </Route>
            <Route exact path="/">
                {localStorage.getItem("admin") ? <Redirect to="/" /> : <Redirect to="/login" />}
                <Agenda />
            </Route>
            <Route path="/fila-de-espera">
                {localStorage.getItem("admin") ? <Redirect to="/fila-de-espera" /> : <Redirect to="/login" />}
                <FilaDeEspera />
            </Route>
            <Route path="/tarefas">
                {localStorage.getItem("admin") ? <Redirect to="/tarefas" /> : <Redirect to="/login" />}
                <Tarefas />
            </Route>
        </Switch>
    </BrowserRouter>
)

export default Routes;