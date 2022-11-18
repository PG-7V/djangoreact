import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from "./components/Navigation/Navbar";
import CategoryDetail from "./components/Category/CategoryDetail";
import PostDetail from "./components/Posts/PostDetail";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";



function App() {

    return (
        <div className="App">
            <Router>
                <Navbar/>
                <Switch>
                    <Route path="/posts/:id" exact component={PostDetail}/>
                    <Route path="/category/:id" exact component={CategoryDetail}/>
                </Switch>
            </Router>
        </div>
    );
}

export default App;
