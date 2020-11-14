import React from 'react';
import logo from './brasao-sem-fundo.png';

export default class Logo extends React.Component{

    render(){
        return(
            <div className="Logo">
                <img src={logo} alt="logo" />
            </div>
        );
    }
}
