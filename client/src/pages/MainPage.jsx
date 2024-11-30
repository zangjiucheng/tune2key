import React from 'react';
import { BoxesCore } from '../components/templates/BoxesCore';
import './MainPage.css';
import Upload2 from '../components/templates/Upload2';

const MainPage = ( {handleUploadSuccess}) => {
    return (
        <div className="main-container">
            <div className="overlay"></div>
            <BoxesCore />
            <div className="main-content">
                <div className="main-heading">Welcome to Musium</div>
                <p className="main-paragraph">
                    Framer Motion is the best animation library ngl
                </p>
                <Upload2 onUploadSuccess={handleUploadSuccess} />
            </div>

        </div>
    );
};

export default MainPage;
