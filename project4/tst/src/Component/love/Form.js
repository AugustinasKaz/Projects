import React, { Component } from 'react'
import axios from 'axios'
import Home from './Home.js'
import styles from './Form.module.css'
class Form extends Component {
  constructor(props){
    super(props);
    this.state = {
      name1: "",
      name2: "",
      send_id: null,
      error: false,
      input_message: '',
    };
    this.SendNames = this.SendNames.bind(this);
  }
    
    async SendNames(){
     const promise = await axios.post("http://127.0.0.1:8000/api/names/", {name1: this.state.name1, name2: this.state.name2});
     const post_response = promise.data;
     this.setState({send_id: post_response.ids, error: post_response.err})  
    }
    
    handleChange = (e) =>{
      if(e.target.id === "2"){
        this.setState({name2: e.target.value})
      }
      if(e.target.id === "1"){
        this.setState({name1: e.target.value})
      }
    }

    handleSubmit = (e) =>{
      if(!this.state.name1 || !this.state.name2){
        this.setState({input_message: "input fields can not be empty"})
      }
      else if(/^[a-zA-Z]+$/.test(this.state.name1) === false || /^[a-zA-Z]+$/.test(this.state.name2) === false){
        this.setState({input_message: "input fields can not contain numeric values"});
      }
      else{
      this.setState({input_message: ""})
      this.SendNames();
      }
      e.preventDefault();
    }
  
  render() {
    return (
      <div className={styles.body}>
      <h1>Love calculator</h1>
      <h2>Fill the form to get answer from love calculator</h2>
      <form onSubmit={this.handleSubmit} className={styles.form1}>
        <span className={styles.label}><label>
          Name1:
          <input type="text" id="1" value={this.state.name1} onChange={this.handleChange} />
        </label></span>

        <span className={styles.label}><label>
          Name2:
          <input type="text" id="2" value={this.state.name2} onChange={this.handleChange} />
        </label></span>
        <input type="submit" value="Submit" />
      </form>
      <div>
        <p>{this.state.input_message}</p>
      </div>
      <Home error={this.state.error} ids={this.state.send_id}/>
      </div>
    )
  }
}

export default Form
