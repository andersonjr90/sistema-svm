import React from "react";
/*
import { Link } from "react-router-dom";

export default function ProductsBtn() {
  return (
    <div>
      <Link to="/tarefas" className="btn">
        Tarefas
      </Link>
    </div>
  );
}
*/
import '../../../node_modules/primereact/resources/themes/md-light-indigo/theme.css';
import '../../../node_modules/primereact/resources/primereact.min.css';
import '../../../node_modules/primeicons/primeicons.css';

import {Menubar} from 'primereact/menubar';
import {withRouter} from 'react-router-dom';

class Nav extends React.Component{

    render(){
        
        const menuitems = [
            {
              label:'Agenda',
              icon:'pi pi-fw pi-home',
              command:() => this.props.history.push('/')
            },
            {
              label:'Fila de Espera',
              icon:'pi pi-fw pi-user',
              command:() => this.props.history.push('/fila-de-espera')
            },
            {
              label:'Tarefas',
              icon:'pi pi-fw pi-comment',
              command:() => this.props.history.push('/tarefas')
            }
        ];
        
        return(
            <div className="Nav">
                <Menubar model={menuitems}/>
                <div id="main">
                    <main>
                        <div className="content" id="content">
                            {this.props.children}
                        </div>
                    </main>
                </div>
            </div>
        );
    }
}

export default withRouter(Nav);
