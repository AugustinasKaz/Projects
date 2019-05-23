import React, { Component } from 'react'
import styles from './Form.module.css'
import axios from 'axios'


class Comment extends Component {
  constructor(props){
    super(props);
    this.state = {
      name: "",
      comment: "",
      input_message: ''
    }
    this.sendComment = this.sendComment.bind(this);
  }
  
  async sendComment(){
    await axios.post("http://127.0.0.1:8000/api/comment/", {user: this.state.name, comment: this.state.comment}).then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
    
  }
  handleChange = (e) =>{
    if(e.target.id === "2"){
      this.setState({comment: e.target.value})
    }
    if(e.target.id === "1"){
      this.setState({name: e.target.value})
    }
  }

  handleSubmit = (e) =>{
    if(!this.state.name || !this.state.comment){
      this.setState({input_message: "input fields can not be empty"})
    }
    else{
    this.setState({input_message: ""})
    this.sendComment();
    }
    e.preventDefault();
  }

  render() {
    return (
      <div className={styles.body}>
      <h3>Leave a comment</h3>
      <div>
        <span>{this.state.input_message}</span>
      </div>
      <form onSubmit={this.handleSubmit}>
        <label>
          Your Name:
          <input className={styles.center}type="text" id="1" value={this.state.name} onChange={this.handleChange}/>
        </label>
        <br/>
        <label>
          Comment:
          <textarea type="text" id="2"className={styles.center} value={this.state.comment} onChange={this.handleChange}/>
        </label>
        <br/>
        <input type="submit" value="Submit" onSubmit={this.handleSubmit}/>
      </form>
      </div>
    )
  }
}

export default Comment
