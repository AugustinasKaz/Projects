import React, { Component } from 'react';
import Index from './Component/Index.js';
import { BrowserRouter , Route, Switch } from "react-router-dom";

class App extends Component {
  render(){
    return(
      <div>
        <BrowserRouter>
        <Switch>
          <Route path='/' component={Index}/>
        </Switch>
        </BrowserRouter>
      </div>
     )
   }
}      

export default App
