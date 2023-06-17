import ExpandIcon from './ExpandIcon';
import { useState } from "react";

const TextBox = ({ cardNumber, cardKey, content, }) => {
    const [expanded, setExpanded] = useState(false);
    const [isLoaded, setisLoaded] = useState(false);

    const handleClick = () => {
        setisLoaded(true);
        setExpanded(!expanded)
    };

    return (
        <div className={`text-box card-${cardNumber}`} key={cardKey}>
            <div className="text-box__header" onClick={() => handleClick()}>
                <ExpandIcon isExpanded={expanded} isLoaded={isLoaded} />
                <p className="text-box__header-number">{cardNumber}:</p>
                <p className="text-box__header-bracket">{`{}`}</p>
                <p className="text-box__header-number">{content.length} keys</p>
            </div>
            {expanded && (
                <div className="text-box__content">
                    {content.map((item, index) =>
                        Object.entries(item).map(([key, value]) => (
                            <div key={index} className="text-box__content-item">
                                <p className="text-box__content-key">{key}:</p>
                                <p className="text-box__content-value">{value}</p>
                            </div>
                        ))
                    )}
                </div>
            )}
        </div>
    );
};

export default TextBox;