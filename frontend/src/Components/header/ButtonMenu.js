import React from 'react';
import icon from "./bars-solid.svg";

export default class ButtonMenu extends React.Component{

    render(){
        return(
            <div className="ButtonMenu">
                <i class="fas fa-bars">
                    <span>Menu</span>
                    <img src={icon} alt="menu" />
                </i>
            </div>
        );
    }
}
