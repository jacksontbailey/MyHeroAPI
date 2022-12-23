import React from 'react';
import Link from 'next/link';

const ResponseMessage = ({ messageType, message }) => {
    let boxColor = messageType === 'error' ? 'red' : 'green';
    let timeout = messageType === 'error' ? 5000 : 3000;

    setTimeout(() => {
        Link.push('/');
    }, timeout);

    return (
        <div style={{ backgroundColor: boxColor, color: 'white', padding: '20px', textAlign: 'center' }}>
            {message}
        </div>
    );
};

export default ResponseMessage;