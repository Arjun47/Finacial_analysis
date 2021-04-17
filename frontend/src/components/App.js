import React from 'react';
import ReactDOM from 'react-dom';
//router
import Header from "./layout/Header";
 
class App extends React.Component{
    render() {
        return(
            <div>
            <Header/>
            </div>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));