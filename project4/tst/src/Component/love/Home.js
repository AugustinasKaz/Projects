import React, { Component } from 'react'
import axios from "axios";
import styles from './Form.module.css'

export class Home extends Component {
  constructor(props){
    super(props);
    this.state = {
      response: []
    };
    this.LoadData = this.LoadData.bind(this);
  }

  async LoadData(){
    const promise = await axios.get("http://127.0.0.1:8000/api/response");
    const status = promise.status;
    if(status===200)
    {
      const data = promise.data.response.filter(obj => obj.id == this.props.ids);
      this.setState({response:data});
    }
    else{
      console.log(status)
    }
  }
  
  componentWillMount(){
    
    this.LoadData();
  }
  componentDidUpdate(prevProps, prevState) {
    if(prevProps.ids !== this.props.ids){
      this.LoadData();
    }
  }
  render(){
    const error_prop = this.props.error;
    let ResponseCalculation;
    
    if(error_prop === false){
      ResponseCalculation = this.state.response.map(result =>(
       <div key={result.id} className={styles.result}>
       <h3>These are the results of the calculations by Dr. Love:  {result.percentage}%</h3>
       <h2>{result.first_name} {result.second_name}</h2>
       <h2>{result.result}</h2>
       </div>
    ));
    }
    else{
      ResponseCalculation = this.state.response.map(result =>(
        <div key={result.id} className={styles.result}>
        <h3>{result.message}</h3>
        </div>
      ));
    }
    return (
      <div className={styles.result}>
        {ResponseCalculation}
      </div>
    )
  }
}

export default Home

