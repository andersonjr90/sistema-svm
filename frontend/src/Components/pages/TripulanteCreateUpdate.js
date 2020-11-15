import React, {Component} from 'react';
import TripulanteService from '../../Services/TripulanteService';

const tripulanteService = new TripulanteService();

class TripulanteCreateUpdate extends Component {

    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount() {
        console.log(this.props);
        const { match: { params } } =  this.props;
        if(params  &&  params.pk)
        {
            tripulanteService.getTripulante(params.pk).then((t)=>{
                this.refs.nome.value  =  t.nome;
                this.refs.contato.value  =  t.contato;
                this.refs.dt_nasc.value  =  t.dt_nasc;
                this.refs.setor.value  =  t.setor;
                this.refs.militar.value  =  t.militar;
                this.refs.patente.value  =  t.patente;
            })
        }
    }

    handleSubmit(event) {
        const {match: {params}} = this.props;
        if (params && params.pk) {
            this.handleUpdate(params.pk);
        } else {
            this.handleCreate();
        }
        event.preventDefault();
    }

    handleCreate() {
        tripulanteService.createTripulante(
            {
                "nome": this.refs.nome.value,
                "contato": this.refs.contato.value,
                "dt_nasc": this.refs.dt_nasc.value,
                "setor": this.refs.setor.value,
                "militar": this.refs.militar.value,
                "patente": this.refs.patente.value
            }).then((result) => {
            alert("Tripulante criado!");
        }).catch(() => {
            alert('Ocorreu um erro! Por favor verifique o formulário');
        });
    }

    handleUpdate(pk) {
        tripulanteService.updateTripulante(
            {
                "pk": pk,
                "nome": this.refs.nome.value,
                "contato": this.refs.contato.value,
                "dt_nasc": this.refs.dt_nasc.value,
                "setor": this.refs.setor.value,
                "militar": this.refs.militar.value,
                "patente": this.refs.patente.value
            }).then((result) => {
            alert("Tripulante atualizado!");
        }).catch(() => {
            alert('Ocorreu um erro! Por favor verifique o formulário');
        });
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <div className="form-group">
                    <label>
                        Nome:</label>
                    <input className="form-control" type="text" ref='nome'/>
                    <label>
                        Contato:</label>
                    <input className="form-control" type="text" ref='contato'/>
                    <label>
                        Data de nascimento:</label>
                    <input className="form-control" type="date" ref='dt_nasc'/>
                    <label>
                        Setor:</label>
                    <input className="form-control" type="text" ref='setor'/>
                    <label>
                        Militar:</label>
                    <input className="form-control" type="text" ref='militar'/>
                    <label>
                        Patente:</label>
                    <input className="form-control" type="text" ref='patente'/>
                    <input className="btn btn-primary" type="submit" value="Submit"/>
                </div>
            </form>
        );
    }
}

export default TripulanteCreateUpdate;