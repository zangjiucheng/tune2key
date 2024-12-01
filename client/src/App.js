import { React, useState, useEffect } from 'react';

import UploadPage from './pages/UploadPage'
import MainPage from './pages/MainPage'

import './App.css';
import {BoxesCore} from './components/templates/BoxesCore';
import Header from './components/Header'

function App() {
  const [inMp3Filename, setInMp3Filename] = useState(null); // the mp3 file that user gives

  return (
    <>
      <Header />
      <div className="app-container">
        <div className='overlay' />
        <BoxesCore />
        <div className="content-container">
          {
            !inMp3Filename && inMp3Filename.length !== 0
              ? <MainPage setInMp3Filename={setInMp3Filename} />  // page where user can see actual sheet music (as pdf), can download, can click buttons to make it harder/make it easier
              : <UploadPage mp3Filename={inMp3Filename}/>  // page for user to upload the mp3 file, can also play hardcoded songs which will set inMp3File and will show pdf display/download page
          }
        </div>
      </div>
    </>
  )
}

export default App;
