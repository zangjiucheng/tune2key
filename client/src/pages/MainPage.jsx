import React from 'react';
import './MainPage.css';
import Upload2 from '../components/templates/Upload2';
import Button from '../components/templates/Button';

const MainPage = ({ setInMp3Filename }) => {
    return (
        <div className="main-content">
            <div className="main-heading">Welcome to Tune2Key</div>
            <p className="main-paragraph">
            Welcome to our innovative sheet music platform! Transform audio, MIDI, or PDF files into beautifully rendered sheet music with ease. 
            Whether you're a beginner looking to simplify a piece or an expert aiming for a challenge, our AI-powered tool adjusts difficulty levels to match your needs. 
            Perfect for musicians of all skill levels, our platform makes music creation and customization effortless.
            </p>
            <Upload2 setInMp3Filename={setInMp3Filename} />
        </div>


    );
};

export default MainPage;
