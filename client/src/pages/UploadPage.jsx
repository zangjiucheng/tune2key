import React from 'react';
import './UploadPage.css'

import DownloadButton from '../components/templates/buttons/DownloadButton';

const UploadPage = () => {
    return (
        <>
            <div className="main">
                <div className="left">
                </div>
                <div className="right">
                    hi
                    <DownloadButton filename={"PERFECT.pdf"}/>
                </div>
            </div>
        </>
    );
}

export default UploadPage;