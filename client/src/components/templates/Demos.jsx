import React, { useState, useEffect } from "react";
import "./Demos.css";

const Demos = ({ setInputFilename, setUploaded, download_pdf, download_mp3, present=false }) => {
    const [demoNumber, setDemoNumber] = useState(-1);
    const [songs, setSongs] = useState([]);

    useEffect(() => {
      fetch("http://127.0.0.1:5000/demos")
        .then(response => response.json())
        .then(data => setSongs(data))
        .catch(error => console.error("Error fetching demos: ", error));
    }, []);

    useEffect(() => {
        if (demoNumber === -1 || !songs[demoNumber - 1]) {
            console.warn("Invalid demo number or no song selected");
            return;
        }

        const selectedSong = songs[demoNumber - 1];
        const filename = selectedSong.filename;

        setUploaded(true);
        console.debug("downloading " + filename);

        try {
            console.log(filename, "filename in Demos");
            download_pdf(filename);
            download_mp3(filename);
        } catch (e) {
            console.error("Error in Demos: " + e);
        }

        setInputFilename(filename);
    }, [demoNumber])

    return (
        <div className={present ? "demo-container-present" : "demo-container"}>
            {songs.map((song, index) => (
                <div className="song-item" key={index}>
                    <div className="song-info">
                        <h2>{song.title}</h2>
                        <p>{song.artist}</p>
                    </div>
                    <button
                        className="play-button"
                        onClick={() => setDemoNumber(index + 1)}
                    >
                        ▶
                    </button>
                </div>
            ))}
        </div>
    );
};

export default Demos;