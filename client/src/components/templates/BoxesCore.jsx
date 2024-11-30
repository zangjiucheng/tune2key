import React from 'react';
import './BoxesCore.css';

const colors = [
    '#7dd3fc', // sky-300
    '#f9a8d4', // pink-300
    '#6ee7b7', // green-300
    '#fde047', // yellow-300
    '#f87171', // red-300
    '#c084fc', // purple-300
    '#60a5fa', // blue-300
    '#818cf8', // indigo-300
    '#a78bfa', // violet-300
];

export const BoxesCore = ({ className, ...rest }) => {
    const rows = new Array(150).fill(1);
    const cols = new Array(100).fill(1);

    const getRandomColor = () => {
        return colors[Math.floor(Math.random() * colors.length)];
    };

    return (
        <div className={`root-div ${className}`} {...rest}>
            {rows.map((_, i) => (
                <div key={`row${i}`} className="row-div">
                    {cols.map((_, j) => (
                        <div
                            key={`col${j}`}
                            className="col-div"
                            onMouseEnter={(e) => {
                                e.currentTarget.style.backgroundColor = getRandomColor();
                            }}
                            onMouseLeave={(e) => {
                                e.currentTarget.style.backgroundColor = '';
                            }}
                        >
                            {j % 2 === 0 && i % 2 === 0 ? (
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                    strokeWidth="1"
                                    className="svg-icon"
                                >
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M12 6v12m6-6H6" />
                                </svg>
                            ) : null}
                        </div>
                    ))}
                </div>
            ))}
        </div>
    );
};

export const Boxes = React.memo(BoxesCore);
