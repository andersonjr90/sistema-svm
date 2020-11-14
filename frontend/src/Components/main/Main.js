import React from 'react';
import Calendar from './Calendar';
import ToDoList from './ToDoList';
import WaitingList from './WaitingList';
import WorkSpace from './WorkSpace';

export default class Main extends React.Component{

    render(){
        return(
            <div className="Main">
                <Calendar/>
                <ToDoList/>
                <WaitingList/>
                <WorkSpace/>
            </div>
        );
    }
}