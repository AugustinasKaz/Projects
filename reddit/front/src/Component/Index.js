import React, { Component } from 'react'
import './static.css';
import pic from './red_pic.png'
import Login from './Login.js'
import Home from './Home.js'

class Index extends Component {
  constructor(){
    super()
    this.state = {
      clicked: false,
      home_component: ''
    }
  }
  componentWillMount(){
    this.setState({home_component: localStorage.getItem('redirect')})
  }
  Change = () => {
     this.setState({clicked: true})
  }
  render(){
    let Response;
    if(this.state.home_component !== 'true'){

     if(this.state.clicked === true){
      Response = <Login/>
    }
     else{
        Response =<div className="Starting_page">
        <img className="red_pic_index" src={pic}/>
        <br/>
        <h1>Reddit v2.0(Augustinas version)</h1>
        <br/>
        <br/>
        <h1>Login using Reddit account</h1>
        <button className="button" onClick={this.Change}><span>Start</span></button>
        </div>}
    }
    else{
      localStorage.setItem("redirect", '');
      Response = <Home/>;
  }
    return (
      <div>
        {Response}
      </div>
    );
  }
}
  export default Index;
