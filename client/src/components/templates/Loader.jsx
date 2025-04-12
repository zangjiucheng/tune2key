import React from "react";
import "./Loader.css"; // Assuming the CSS styles are saved in a separate file named Loader.css

const Loader = () => {
  const [segments, setSegments] = React.useState(0);
  const [currentSegment, setCurrentSegment] = React.useState(0);

  React.useEffect(() => {
    const fetchProgress = async () => {
      try {
        const response = await fetch("http://localhost:5000/process/progress");
        const data = await response.json();
        setSegments(data.total_segments);
        setCurrentSegment(data.current_segment);
      } catch (error) {
        console.error("Error fetching progress:", error);
      }
    };

    fetchProgress();
    const interval = setInterval(fetchProgress, 3000);

    return () => clearInterval(interval);
  }, []);

  // React.useEffect(() => {
  //   const interval = setInterval(() => {
  //     setCurrentSegment((prev) => {
  //       if (prev < segments) {
  //         return prev + 1;
  //       } else {
  //         clearInterval(interval);
  //         return prev;
  //       }
  //     });
  //   }, 1000);

  //   return () => clearInterval(interval);
  // }, [segments]);
  
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%"}}>
      <div className="cube-loader">
        <div className="cube-top"></div>
        <div className="cube-wrapper">
          <span style={{ "--i": 0 }} className="cube-span"></span>
          <span style={{ "--i": 1 }} className="cube-span"></span>
          <span style={{ "--i": 2 }} className="cube-span"></span>
          <span style={{ "--i": 3 }} className="cube-span"></span>
        </div>
      </div>
      <div className="loader-text">Processing...</div>
      <div className="loader">
        <progress
          className="progress-bar"
          max={segments}
          value={currentSegment}
          style={{ width: "100%", height: "10px" }}
        ></progress>
      </div>
      <div className="loader-text">
        Segment {currentSegment} / {segments}
      </div>
    </div>
  );
};

export default Loader;
