import React, { useState, useEffect } from "react";
import "./Demos.css";

const Demos = ({ setInputFilename, setUploaded, download_pdf, download_mp3 }) => {
    const [demoNumber, setDemoNumber] = useState(-1);
    useEffect(() => {
        let filename;
        if (demoNumber === 1) {
            filename = "ROSÉ & Bruno Mars - APT";
        } else if (demoNumber === 2) {
            filename = "Two Steps From Hell - Victory (Piano Version).pdf";
        } else if (demoNumber === 3) {
            filename = "Dennis Kuo - Track in Time - Piano Cover (Tutorial)";
        } else {
            console.warn("this isn't a proper demo number");
            return;
        }
        setUploaded(true);

        console.debug("downloading " + filename);
        try {
            console.log(filename, "filename in Demos")
            download_pdf(filename);
            download_mp3(filename);
        } catch (e) {
            console.error("error in calling in Demos: " + e)
        }
        setInputFilename(filename);
    }, [demoNumber])

    return (
        <div className="demo-container">
            <div className="song-item">
                <div className="song-info">
                    <h2>APT</h2>
                    <p>ROSÉ & Bruno Mars</p>
                </div>
                <button className="play-button" onClick={() => setDemoNumber(1)}>▶</button>
            </div>
            <div className="song-item">
                <div className="song-info">
                    <h2>Victory</h2>
                    <p>Two Steps From Hell</p>
                </div>
                <button className="play-button" onClick={() => setDemoNumber(2)}>▶</button>
            </div>

            <div className="song-item">
                <div className="song-info">
                    <h2>Track in Time</h2>
                    <p>Dennis Kuo</p>
                </div>
                <button className="play-button" onClick={() => setDemoNumber(3)}>▶</button>
            </div>
        </div>
    );
};

export default Demos;