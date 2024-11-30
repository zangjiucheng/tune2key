import React, { useState } from 'react';
import './Upload.css';

function Upload() {


    const handleFileChange = (e) => {
        const uploadedFile = e.target.files[0]
        const formData = new FormData()
        formData.append('file', uploadedFile)
        transcribe(formData)
    }
    const transcribe = async (formData) => {
        try {
            const response = await fetch('http://127.0.0.1:5000/transcribe', {
                method: 'POST',
                body: formData
            })
            if (response.ok) {
                console.log('ok')
            }
        }
        catch (err) {
            console.log('err')
        }
    }
    return (
        <div className="upload-wrapper">
            <div className="container">
                <div className="folder">
                    <div className="front-side">
                        <div className="tip"></div>
                        <div className="cover"></div>
                    </div>
                    <div className="back-side cover"></div>
                </div>
                <label className="custom-file-upload">
                    <input className="title" type="file" />
                    Choose a file
                </label>
            </div>

            
        </div>

    );
}

export default Upload;
