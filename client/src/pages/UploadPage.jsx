import React, { useState } from 'react';
import './UploadPage.css'
import Upload2 from '../components/templates/Upload2';
import DownloadButton from '../components/templates/buttons/DownloadButton';

const UploadPage = () => {
    const [inputFilename, setInputFilename] = useState(null);

    return (
        <>
            <div className="main">
                <div className="left">
                    <Upload2 setInputFilename={setInputFilename} />
                </div>
                <div className="right">
                    <div className="play">

                    </div>
                    <div className="demos">

                    </div>
                    <div className="buttons">
                        <DownloadButton inputFilename={inputFilename} className="left-button"/> 
                        <DownloadButton inputFilename={inputFilename} className="right-button"/> 
                    </div>
                </div>
            </div>
        </>
    );
}

export default UploadPage;

/*inputFilename */