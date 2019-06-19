import React, { Component } from 'react'
import './static.css';

export class Subreddits extends Component {
    constructor(props){
        super(props);
        this.state = {
            response: null
        }
    };
    componentDidUpdate(prevProps){
        if(prevProps.subbredits_data !== this.props.subbredits_data){
          this.setState({response: this.props.subbredits_data})
    };
    }
    render() {
        let sub_container;
        if(this.state.response === null){
            sub_container = <h1 className="error">Something went wrong. Please reload the page</h1>;
        }
        else{
            sub_container = this.state.response.map((object, index) =>
            <div>
            {object.url.match(/\.(jpeg|jpg|gif|png)$/) != null ? 
            <div key={index} className="sub_container">
            <div id="sub_header">
            <h2>Score: {object.upvotes}&nbsp;&nbsp;&nbsp;&nbsp;{object.title}</h2>
            <h4 id="upvotes">r/{object.subreddit}. Posted by u/{object.author}</h4>
            </div>
            <img className="pic3" src={object.url}/>
            </div>: 
            <div key={index} className="sub_container_small">
            <div id="sub_header">
            <h2>Score: {object.upvotes}&nbsp;&nbsp;&nbsp;&nbsp;{object.title}</h2>
            <h4 id="upvotes">r/{object.subreddit}. Posted by u/{object.author}</h4>
            </div>
            </div>} 
            </div>
        );
        }
        return (
            <div className="column">
                {sub_container}   
            </div>
        )
    }
}
export default Subreddits
