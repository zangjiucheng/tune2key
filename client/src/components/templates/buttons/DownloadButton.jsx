import React from 'react';

import './DownloadButton.css'

const DownloadButton = ({filename}) => {

    const downloadFile = async () => {
        const url = `http://127.0.0.1:5000/download/${filename}`;
        await fetch(url)
            .then(response => {
                if (response.ok) {
                    return response.blob();  // Convert the response into a Blob (binary data)
                }
                throw new Error('File not found');
            })
            .then(blob => {
                const downloadUrl = window.URL.createObjectURL(blob);  // Create a URL for the Blob
                const a = document.createElement('a');  // Create an anchor element
                a.href = downloadUrl;
                a.download = filename;  // Set the download filename
                document.body.appendChild(a);
                a.click();  // Trigger the download
                a.remove();  // Clean up the DOM
            })
            .catch(error => {
                console.error('Error:', error);  // Handle any errors (file not found, etc.)
            });
    }

    return (
        <button className="download-button"
            onClick={() => downloadFile()}>
            Download
        </button>
    );
}

export default DownloadButton;

