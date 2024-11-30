import Upload from "./templates/Upload";
import './Main.css'
import React, {useState} from "react";

const Main = () => {

    const [uploaded, isUploaded] = useState(false)

    return <>
        <div className="main">
            <div className="left">
                {isUploaded? <Upload />: <></> }
            </div>
            <div className="right">
                hi
            </div>
        </div>
    </>
}

export default Main