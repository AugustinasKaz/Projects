import React, { Component } from 'react';
import { BrowserRouter, Route} from 'react-router-dom'
import Form from  './Component/love/Form.js'
import Comment from  './Component/love/Comment.js'
import All_comments from './Component/love/All_comments.js'
class App extends Component {
  render(){
    return(
      <div>
        <BrowserRouter>
          <Route path='/' component={Form}/>
          <Route path='/' component={Comment}/>
          <Route path='/' component={All_comments}/>
        </BrowserRouter>
      </div>
     )
   }
}      

export default App
