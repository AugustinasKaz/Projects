import React, { Component } from 'react'
import axios from "axios";
import styles from './Form.module.css'

export class All_comments extends Component {
    constructor(props){
        super(props);
        this.state = {
            response: []
        }
        this.LoadData = this.LoadData.bind(this);
    }
    async LoadData(){
        const promise = await axios.get("http://127.0.0.1:8000/api/all_comments");
        const status = promise.status;
        if(status===200)
        {
          const data = promise.data.response;
          this.setState({response:data});
        }
        else{
          console.log(status)
        }
    }

    componentWillMount(){
        this.LoadData();
    }

    render(){
       const ResponseComments = this.state.response.map(result =>(
            <div key={result.id} className={styles.comment_container}>
            <h3>Posted at: {result.date} Author: {result.author}</h3>
            <h2>Comment{result.text}</h2>
            
            </div>
         ));
        return (
            <div className={styles.body}>
                <h1 className={styles.comment_header}>Comments</h1>
                <br/>
                {ResponseComments}
                <br/>
            </div>
        )
    }
}

export default All_comments
