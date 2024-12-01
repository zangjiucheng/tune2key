import { React, useState, useEffect } from 'react';

import UploadPage from './pages/UploadPage'
import MainPage from './pages/MainPage'

import './App.css';
import {BoxesCore} from './components/templates/BoxesCore';
import Header from './components/Header'

function App() {
  const [inMp3Filename, setInMp3Filename] = useState(null); // the mp3 file that user gives

  // testing only
  useEffect(() => {
    console.log(inMp3Filename, "inMp3Filename")
  }, [inMp3Filename])


  return (
    <>
      <Header />
      <div className="app-container">
        <div className='overlay' />
        <BoxesCore />
        <div className="content-container">
          {
            inMp3Filename && inMp3Filename.length !== 0
              ? <UploadPage mp3Filename={inMp3Filename}/>  // page for user to upload the mp3 file, can also play hardcoded songs which will set inMp3File and will show pdf display/download page
              : <MainPage setInMp3Filename={setInMp3Filename} />  // page where user can see actual sheet music (as pdf), can download, can click buttons to make it harder/make it easier
          }
        </div>
      </div>
    </>
  )
}

export default App;
