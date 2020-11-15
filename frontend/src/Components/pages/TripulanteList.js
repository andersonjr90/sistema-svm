import React, {Component} from 'react';
import TripulanteService from '../../Services/TripulanteService';

const tripulanteService = new TripulanteService();

class TripulanteList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            tripulantes: [],
            nextPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }

    componentDidMount() {
        const self = this;
        tripulanteService.getTripulantes().then(function (result) {
            self.setState(
                {tripulantes: result.data, nextPageURL: result.nextlink}
            )
        });
    }

    handleDelete(e, pk) {
        const self = this;
        tripulanteService.deleteTripulante({pk: pk}).then(() => {
            let newArr = self.state.tripulantes.filter(function (obj) {
                return obj.pk !== pk;
            });
            self.setState({tripulantes: newArr})
        });
    }

    nextPage() {
        const self = this;
        tripulanteService.getTripulantesByURL(this.state.nextPageURL).then((result) => {
            self.setState({tripulantes: result.data, nextPageURL: result.nextlink})
        });
    }


    render() {

        return (
            <div className="tripulantes--list">
                <table className="table">
                    <thead key="thead">
                    <tr>
                        <th>#</th>
                        <th>Nome</th>
                        <th>Contato</th>
                        <th>Data de nascimento</th>
                        <th>Setor</th>
                        <th>Militar</th>
                        <th>Patente</th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.state.tripulantes.map(t =>
                        <tr key={t.pk}>
                            <td>{t.pk}  </td>
                            <td>{t.nome}</td>
                            <td>{t.contato}</td>
                            <td>{t.dt_nasc}</td>
                            <td>{t.setor}</td>
                            <td>{t.militar}</td>
                            <td>{t.patente}</td>
                            <td>
                                <button onClick={(e) => this.handleDelete(e, t.pk)}> Delete</button>
                                <a href={"/tripulante/" + t.pk}> Update</a>
                            </td>
                        </tr>)}
                    </tbody>
                </table>
                <button className="btn btn-primary" onClick={this.nextPage}>Next</button>
            </div>
        );
    }
}

export default TripulanteList;