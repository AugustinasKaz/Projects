import React, { Component } from 'react'
import ReactCSSTransitionGroup from 'react-addons-css-transition-group';
import axios from 'axios';
import './static.css';

export class Login extends Component {
    constructor(props){
        super(props);
        this.state = {
            name:"",
            error:"",
            url: '',
        }
        this.send_request = this.send_request.bind(this);
    }
    async send_request(){
        const promise = await axios.post("http://127.0.0.1:8000/login/", {name: this.state.name});
        const status = promise.status;
        if(status===200){
         localStorage.setItem("redirect", 'true');   
         window.location.href = 'http://127.0.0.1:8000/login';
        }
        else{
            this.setState({error: "Something went wrong. Try again"})
        }
        
    }
    handleChange = (e) =>{
          this.setState({name: e.target.value})
    }
    handleSubmit = (e) =>{
        if(!this.state.name){
          this.setState({error: "input fields can not be empty"})
        }
        else{
        this.setState({url:''});    
        this.setState({error: ""})
        this.send_request();
        }
        e.preventDefault();
    }
    render() {
        return (
            <div>
                <ReactCSSTransitionGroup
                transitionName="example"
                transitionAppear={true}
                transitionAppearTimeout={500}
                transitionEnter={false}
                transitionLeave={false}>
                <div className="body">
                <form onSubmit={this.handleSubmit}>
                 <h1>Enter your Reddit username</h1>
                 <input type="text" id="1" value={this.state.name} onChange={this.handleChange} />
                 <p className="error">{this.state.error}</p>
                 <br/>
                 <input className="button" type="submit" value="Submit" />
                </form>
                </div>
                </ReactCSSTransitionGroup>
            </div>
)}};
export default Login
















