import React from 'react';
import Header from '../header/Header';
import Footer from '../Footer';
import Main from '../main/Main';

export default class Agenda extends React.Component{

    render(){
        return(
            <div className='Agenda'>
                <Header/>
                <h1>Fila de Espera</h1>
                <Main/>
                <Footer/>
            </div>
        );
    }
}
