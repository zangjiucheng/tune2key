import React from 'react';

import './DownloadButton.css'

const EasyDifficultyButton = ({download_pdf, filename}) => {

    const makeEasier = () => {
        console.log("input filename " + filename)
        try {
            const simpleFilename = filename + '_simple'
            download_pdf(simpleFilename);
            console.debug("made " + simpleFilename + " easier and set the pdf again.");

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