import React from 'react';
import './Upload2.css'

const Upload2 = ({ setInMp3Filename }) => {
    

    const handleFileChange = (e) => {
        const uploadedFile = e.target.files[0]
        const uploadedFilename = uploadedFile.name;

        // force .mp3 or .midi or .pdf files only
        if (!uploadedFilename.includes('.'))
            return false;
        const fileExtension = uploadedFilename.split('.').pop();
        if (fileExtension !== "mp3" && fileExtension !== "midi" && fileExtension !== "pdf") {
            console.log(`${uploadedFilename} has .${fileExtension} extension, which is disallowed`);
            return false;
        }
        setInMp3Filename(uploadedFilename);
        
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
            setInMp3Filename(null);
            console.log('err')
        }
    }
    return (
        <label htmlFor="file" className="custum-file-upload">
            <div className="icon">
                <svg
                    class="h-6 w-6 text-white/60"
                    stroke-linejoin="round"
                    stroke-linecap="round"
                    stroke-width="2"
                    stroke="white"
                    fill="none"
                    viewBox="0 0 24 24"
                    height="70"
                    width="70"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2"></path>
                    <path d="M7 9l5 -5l5 5"></path>
                    <path d="M12 4l0 12"></path>
                </svg>
            </div>
            <div className="text">
                <span>Click to upload .mp3 .midi .pdf</span>
            </div>
            <input id="file" type="file" onChange={handleFileChange} />
        </label>
    );
}
export default Upload2