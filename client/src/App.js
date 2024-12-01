import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import UploadPage from './pages/UploadPage';
import MainPage from './pages/MainPage';

import './App.css';
import { BoxesCore } from './components/templates/BoxesCore';
import Header from './components/Header';

function App() {
  return (
    <div>
      <BrowserRouter>
      <Header />
      <div className="app-container">
        <div className="overlay" />
        <BoxesCore />
        <div className="content-container">
          <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/upload" element={<UploadPage />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
    </div>
    
  );
}

export default App;
