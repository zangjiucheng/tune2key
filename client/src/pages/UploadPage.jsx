import React, { useState, useEffect, useRef } from 'react';
import './UploadPage.css';
import MyToggleButton from '../components/templates/MyToggleButton';

const UploadPage = ({ handleUploadSuccess }) => {
    const [uploaded, setUploaded] = useState(false);
    const [pdfUrl, setPdfUrl] = useState(null);
    const [audioUrl, setAudioUrl] = useState(null);
    const [isPlaying, setIsPlaying] = useState(false);
    const [currentTime, setCurrentTime] = useState(0);
    const [duration, setDuration] = useState(0);

    const audioRef = useRef(null);
    const handleFileChange = (e) => {
        const uploadedFile = e.target.files[0];
        const formData = new FormData();
        formData.append('file', uploadedFile);
        transcribe(formData);
    };

    const transcribe = async (formData) => {
        setUploaded(true); // Set uploaded to true
        try {
            const response = await fetch('http://127.0.0.1:5000/transcribe', {
                method: 'POST',
                body: formData,
            });
            if (response.ok) {
                console.log('ok');
                setUploaded(true); // Set uploaded to true
                handleUploadSuccess();
            }
        } catch (err) {
            console.log('err');
        }
    };

    const download_pdf = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/download/sample.pdf');
            if (response.ok) {
                const blob = await response.blob();
                const url = URL.createObjectURL(blob);
                setPdfUrl(url); // Set the PDF URL to display
            } else {
                console.log('Error downloading PDF');
            }
        } catch (error) {
            console.log('Error fetching PDF:', error);
        }
    };
    const download_mp3 = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/download/PERFECT.mp3');
            if (response.ok) {
                const blob = await response.blob();
                const url = URL.createObjectURL(blob);
                setAudioUrl(url); // Set the audio URL to play
            } else {
                console.log('Error downloading MP3');
            }
        } catch (error) {
            console.log('Error fetching MP3:', error);
        }
    };
    // Use useEffect to call download_pdf when uploaded is true
    useEffect(() => {
        if (uploaded) {
            download_pdf();
            download_mp3();
        }
    }, [uploaded]);

    const handlePlayPause = () => {
        if (isPlaying) {
            audioRef.current.pause();
        } else {
            audioRef.current.play();
        }
        setIsPlaying(!isPlaying);
    };

    const handleSeek = (event) => {
        const newTime = Number(event.target.value);
        setCurrentTime(newTime);
        audioRef.current.currentTime = newTime;
    };

    // Update currentTime as the audio plays
    const handleTimeUpdate = () => {
        setCurrentTime(audioRef.current.currentTime);
    };

    // Set the duration of the audio when it loads
    const handleLoadedMetadata = () => {
        setDuration(audioRef.current.duration);
    };

    return (
        <>
            <div className="main">
                <div className="left">
                    {!uploaded ? (
                        // Show upload button when not uploaded
                        <label htmlFor="file" className="custum-file-upload">
                            <div className="icon">
                                <svg
                                    className="h-6 w-6 text-white/60"
                                    strokeLinejoin="round"
                                    strokeLinecap="round"
                                    strokeWidth="2"
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
                    ) : pdfUrl ? (
                        // Display the PDF when uploaded and pdfUrl is available
                        <iframe
                            src={pdfUrl}
                            width="100%"
                            height="100%"
                            style={{ border: 'none' }}
                            title="PDF Viewer"
                        ></iframe>
                    ) : (
                        // Show loading message while fetching the PDF
                        <p>Loading PDF...</p>
                    )}
                </div>
                <div className="right">
                    {audioUrl ? (
                        <div className="audio-player" onChange={() => { handlePlayPause(); console.log('playing') }}>
                            <audio
                                ref={audioRef}
                                src={audioUrl}
                                onTimeUpdate={handleTimeUpdate}
                                onLoadedMetadata={handleLoadedMetadata} 
                                />
                            <MyToggleButton />

                            {/* Scroll Bar */}
                            <input
                                type="range"
                                min="0"
                                max={duration || 0} // Prevent NaN if duration is not loaded
                                value={currentTime}
                                onChange={handleSeek}
                            />

                            {/* Display Current Time and Duration */}
                            <div>
                                <span>{formatTime(currentTime)}</span> / <span>{formatTime(duration)}</span>
                            </div>
                        </div>
                    ) : (
                        <p>Loading Audio...</p>
                    )}
                </div>
            </div>
        </>
    );
};

const formatTime = (time) => {
    if (isNaN(time)) return '0:00';
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60).toString().padStart(2, '0');
    return `${minutes}:${seconds}`;
};

export default UploadPage;
