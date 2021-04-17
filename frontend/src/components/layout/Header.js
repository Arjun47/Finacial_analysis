import React, { Component } from 'react';
import { Button,  Navbar } from 'reactstrap';
import axios from 'axios';

export class Header extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: {},
        };
    }
    componentDidMount() {
        var self = this;
        axios({
            method: 'GET',          
            url: 'dash/dashboard/',//can use any url
            // data: "allData",
        })
        .then(function(response) {
            console.log(response.data)
            self.setState({data:response.data})
        })
        .catch(function (error) {
            console.log(error);
        });
          console.log(self.state.data);
    }

    render() {
        return (
            <div>
            <Navbar className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <Button className="navbar-toggler" outline type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"> HI Button</span>
                </Button>
                <div className="collapse navbar-collapse" id="navbarTogglerDemo01">
                <a className="navbar-brand" href="#">Financial Analysis</a>
                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                    <li className="nav-item">
                    <a className="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li className="nav-item">
                    <a className="nav-link" href="#">Link</a>
                    </li>
                    <li className="nav-item">
                    <a className="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                    </li>
                </ul>
                </div>
            </div>
            </Navbar>
            <div>
                <h1>
                { this.state.data.id }
                { this.state.data['name'] }
                </h1>
            </div>

            </div>
        )
    }
}

export default Header
