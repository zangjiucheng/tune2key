import { React, useState, useEffect } from 'react';

import UploadPage from './pages/UploadPage'
import MainPage from './pages/MainPage'

import './App.css';

function App() {
  const [inMp3File, setInMp3File] = useState(null); // the mp3 file that user gives

  return (
    <>
      {
        !inMp3File
        ? <UploadPage />  // page for user to upload the mp3 file, can also play hardcoded songs which will set inMp3File and will show pdf display/download page
        : <MainPage />  // page where user can see actual sheet music (as pdf), can download, can click buttons to make it harder/make it easier
      }
    </>
  )
}

export default App;
