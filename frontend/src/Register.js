import React, {Component} from 'react';
import UsuarioService from "./Services/UsuarioService";

const usuarioService = new UsuarioService();

class Register extends Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount() {
    }

    render() {
        return (
            <div>
                <h1>Criar usuário</h1>
                <form onSubmit={this.handleSubmit}>
                    <div className="form-group">
                        <label>Nome:</label>
                        <input className="form-control" type="text" ref='nome'/>
                        <label>Email:</label>
                        <input className="form-control" type="text" ref='email'/>
                        <label>Permissão: </label>
                        <input className="form-control" type="text" ref='permissao'/>
                        <label>Tipo de usuário:</label>
                        <input className="form-control" type="text" ref='tipo_usuario'/>
                        <label>Senha:</label>
                        <input className="form-control" type="password" ref='senha'/>
                        <input className="btn btn-primary" type="submit" value="Salvar"/>
                    </div>
                </form>
            </div>
        )
    }

    handleSubmit(event) {
        this.handleCreate();
        event.preventDefault();
    }

    handleCreate() {
        usuarioService.createUsuario(
            {
                "nome": this.refs.nome.value,
                "email": this.refs.email.value,
                "permissao": this.refs.permissao.value,
                "tipo_usuario": this.refs.tipo_usuario.value,
                "senha": this.refs.senha.value
            }).then((result) => {
            alert("Usuário criado!");
        }).catch(() => {
            alert('Ocorreu um erro! Por favor verifique o formulário');
        });
    }
}

export default Register;