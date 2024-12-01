import React, { useState, useEffect } from 'react';
import './UploadPage.css'

import DownloadButton from '../components/templates/buttons/DownloadButton';

const UploadPage = ({mp3Filename}) => {
    const [filename, setFilename] = useState();

    // get rid of mp3Filename file extension
    useEffect(() => {
        setFilename(mp3Filename.split('.')[0]);
    }, [])

    return (
        <>
            <div className="main">
                <div className="left">
                </div>
                <div className="right">
                    <DownloadButton filename={filename+".pdf"}/> // download pdf
                </div>
            </div>
        </>
    );
}

export default UploadPage;