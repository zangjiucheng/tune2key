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
                    <DownloadButton inputFilename={inputFilename}/>  
                </div>
            </div>
        </>
    );
}

export default UploadPage;

/*inputFilename */