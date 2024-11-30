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
                    <div className="input-text-supported">
                        (.mp3 .midi .pdf)
                    </div>
                </label>
            </div>

            <label htmlFor="file" className="file-label">
                <svg
                    fill="#000000"
                    viewBox="0 0 32 32"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path d="M15.331 6H8.5v20h15V14.154h-8.169z" />
                    <path d="M18.153 6h-.009v5.342H23.5v-.002z" />
                </svg>
                <p>Not selected file</p>
                <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M5.16565 10.1534C5.07629 8.99181 5.99473 8 7.15975 8H16.8402C18.0053 8 18.9237 8.9918 18.8344 10.1534L18.142 19.1534C18.0619 20.1954 17.193 21 16.1479 21H7.85206C6.80699 21 5.93811 20.1954 5.85795 19.1534L5.16565 10.1534Z"
                        stroke="#000000"
                        strokeWidth={2}
                    />
                    <path
                        d="M19.5 5H4.5"
                        stroke="#000000"
                        strokeWidth={2}
                        strokeLinecap="round"
                    />
                    <path
                        d="M10 3C10 2.44772 10.4477 2 11 2H13C13.5523 2 14 2.44772 14 3V5H10V3Z"
                        stroke="#000000"
                        strokeWidth={2}
                    />
                </svg>
            </label>
            <input id="file" type="file" />
        </div>

    );
}

export default Upload;
