import React from 'react';
import Nav from "./Nav";
import ButtonMenu from "./ButtonMenu";
import Logo from "./Logo";
import User from "./User";

import "./Header.css";

export default class Header extends React.Component{

    render(){
        return(
            <div className="Header">
                
                <ButtonMenu/>
                <User/>
                <Nav/>
                <Logo/>
            </div>
        );
    }
}