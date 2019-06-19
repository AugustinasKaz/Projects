import React, { Component } from 'react'
import Subreddits from './Subreddits.js'
import './static.css'
import pic from './red_pic.png'
import axios from 'axios';

export class Home extends Component {
    constructor(props){
        super(props);
        this.state = {
            client: "",
            response: null,
            num: 1,
            select_value: 'home'
        }
        this.request_subrreddits = this.request_subrreddits.bind(this);
    }
    async request_subrreddits(){
        const promise = await axios.post("http://127.0.0.1:8000/data/", {sort: this.state.select_value});
        const status = promise.status;
        if(status === 200){
          const data = promise.data;
          this.setState({response:data});     
        }
    }
    componentDidMount(){
       this.request_subrreddits();
    }
    handle_select = (event) => {
        this.setState({select_value: event.target.value})
        this.request_subrreddits();
    } 
        render() {
            return (
            <div>
                <div className="container">
                <div id="pic">
                <img className="pic2"src={pic}/>
                </div>
                <div id="center">
                <div className="select1">
                 <select onChange={this.handle_select}>
                     <option value="home">Home</option>
                     <option value="popular">Popular</option>
                     <option value="all">All</option>
                 </select>
                </div>
                </div>
                <div id="right">
                <h1>Logged in as: {this.state.client}</h1>
                </div>
                </div>
                <Subreddits subbredits_data = {this.state.response}/>
            </div>
        )
    }
}

export default Home
