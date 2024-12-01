import React from 'react';

import './DownloadButton.css'

const EasyDifficultyButton = ({download_pdf, download_mp3, filename}) => {

    const makeEasier = () => {
        console.log("input filename " + filename)
        try {
            const simpleFilename = filename + '_simple'
            download_pdf(simpleFilename);
            download_mp3(simpleFilename);
            console.debug("made " + simpleFilename + " easier and set the pdf and audio file again.");
        } catch (e) {
            console.warn("in EasyDifficultyButton:" + e);
        }
    }

    return (
        <button className="download-button"
            onClick={() => makeEasier()}
        >
            Easier?!
        </button>
    );
}
 
export default EasyDifficultyButton;