// Demos.jsx
import React, { useState, useEffect } from "react";
import "./Demos.css";

const Demos = ({ setUploaded, download_pdf, download_mp3 }) => {

    const [demoNumber, setDemoNumber] = useState(-1);

    useEffect(() => {
        setUploaded(false);
        let pdfName, mp3Name;

        if (demoNumber === 1) {
            pdfName = ""
            mp3Name = ""
        } else if (demoNumber === 2) {
            pdfName = ""
            mp3Name = ""
        } else if (demoNumber === 3) {
            pdfName = ""
            mp3Name = ""
        } else {
            console.warn("this isn't a proper demo number");
        }

        download_pdf(pdfName);
        download_mp3(mp3Name);
        setUploaded(true);


    }, [demoNumber])


    return (
        <div className="demo-container">
            <div className="song-item">
                <div className="song-info">
                    <h2>APT</h2>
                    <p>Bruno Mars & Rose</p>
                </div>
                <button className="play-button" onChange={() => setDemoNumber(1)}>▶</button>
            </div>

            <div className="song-item">
                <div className="song-info">
                    <h2>Victory</h2>
                    <p>Two Steps From Hell</p>
                </div>
                <button className="play-button" onChange={() => setDemoNumber(2)}>▶</button>
            </div>

            <div className="footer">
                <div className="song-info">
                    <h2>Track in Time</h2>
                    <p>Dennis Kuo</p>
                    <button className="play-button" onChange={() => setDemoNumber(3)}>▶</button>
                </div>
            </div>
        </div>
    );
};

export default Demos;