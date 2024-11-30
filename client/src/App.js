import { React, useState, useEffect } from 'react';

import UploadPage from './pages/UploadPage'
import MainPage from './pages/MainPage'

import './App.css';
import {BoxesCore} from './components/templates/BoxesCore';
import Header from './components/Header'

function App() {
  const [inMp3File, setInMp3File] = useState(true); // the mp3 file that user gives

  const handleUploadSuccess = () => {
    setInMp3File(true); // Update state when upload is successful
  };
  return (
    <>
      <Header />
      <div className="app-container">
        <div className='overlay' />
        <BoxesCore />
        <div className="content-container">
          {
            !inMp3File
              ? <MainPage onUploadSuccess={handleUploadSuccess} />  // page where user can see actual sheet music (as pdf), can download, can click buttons to make it harder/make it easier
              : <UploadPage />  // page for user to upload the mp3 file, can also play hardcoded songs which will set inMp3File and will show pdf display/download page
          }
        </div>
      </div>
    </>
  )
}

export default App;
