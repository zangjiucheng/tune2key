// Demos.jsx
import React from "react";
import "./Demos.css"; // Import the CSS file for styles

const Demos = () => {
  return (
    <div className="demo-container">
      <div className="song-item">
        <div className="song-info">
          <h2>APT</h2>
          <p>Bruno Mars & Rose</p>
        </div>
        <button className="play-button">▶</button>
      </div>

      <div className="song-item">
        <div className="song-info">
          <h2>Victory</h2>
          <p>Two Steps From Hell</p>
        </div>
        <button className="play-button">▶</button>
      </div>

      <div className="footer">
        <button className="back-button">←</button>
        <div className="song-info">
          <h2>Track in Time</h2>
          <p>Dennis Kuo</p>
        </div>
      </div>
    </div>
  );
};

export default Demos;