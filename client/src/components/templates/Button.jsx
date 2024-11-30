import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Button.css'; // Import the CSS file

const Button = () => {
    const navigate = useNavigate();

    return (
        <button className="button-upload" onClick={() => {navigate('/upload')}}>
            <span className="spinning-bg" />
            <span className="button-content">
                <svg
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    fill="none"
                    className="left-icon"
                >
                    <path
                        d="M11 19l-7-7 7-7m8 14l-7-7 7-7"
                        strokeWidth={2}
                        strokeLinejoin="round"
                        strokeLinecap="round"
                    />
                </svg>
                <span className="button-text" >
                    Upload Now!
                </span>
                <svg
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    fill="none"
                    className="right-icon"
                >
                    <path
                        d="M13 5l7 7-7 7M5 5l7 7-7 7"
                        strokeWidth={2}
                        strokeLinejoin="round"
                        strokeLinecap="round"
                    />
                </svg>
            </span>
        </button>
    );
};

export default Button;
