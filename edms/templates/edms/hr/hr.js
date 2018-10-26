'use strict';
import React from 'react';
import ReactDOM from 'react-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.min.css';

import UserTable from './user_table';
import DepTable from './dep_table';
import SeatTable from './seat_table';
import '../my_styles.css'


class HR extends React.Component {
    constructor(props) {
        super(props);
        this.changeLists = this.changeLists.bind(this);
    }

    state = {
        emps: window.emps,
        seats: window.seats,
        deps: window.deps,
    };

    changeLists(name, list) {
        if (name === 'deps') {
            this.setState({
                deps: list,
            });
            console.log('asd')
        }
        else if (name === 'emps') {
            this.setState({
                emps: list,
            })
        }
        else if (name === 'seats') {
            this.setState({
                seats: list
            })
        }
    }

    notify = (message) => toast.error( message,
        {
            position: "bottom-right",
            autoClose: 5000,
            hideProgressBar: true,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
        }
    );

    render() {
        return(
            <div>
                <div className="row css_height">
                    <div className="col-lg-4 p-2">
                        <UserTable emps={this.state.emps} seats={this.state.seats} changeLists={this.changeLists} message={this.notify}/>
                    </div>
                    <div className="col-lg-4 p-2">
                        <DepTable deps={this.state.deps} changeLists={this.changeLists}/>
                    </div>
                    <div className="col-lg-4 p-2">
                        <SeatTable seats={this.state.seats} deps={this.state.deps} changeLists={this.changeLists}/>
                    </div>
                </div>

                {/*Вспливаюче повідомлення*/}
                <ToastContainer />
            </div>
        )
    }
}

ReactDOM.render(
    <HR/>,
    document.getElementById('hr')
);