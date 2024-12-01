import React from 'react';
import './UploadPage.css'
import Upload2 from '../components/templates/Upload2';

const UploadPage = ( { handleUploadSuccess } ) => {
    return (
        <>
            <div className="main">
                <div className="left">
                    <Upload2 onUploadSuccess={handleUploadSuccess} />
                </div>
                <div className="right">
                    hi
                </div>
            </div>
        </>
    );
}

export default UploadPage;