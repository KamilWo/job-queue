import React, {Component} from 'react';
import FileUpload from './components/FileUpload';
import Footer from './components/Footer';
import Header from './components/Header';

class App extends Component {

  render() {

    return (
      <div>
        <Header/>

        <FileUpload/>

        <Footer/>
      </div>
    );
  }
}

export default App;
