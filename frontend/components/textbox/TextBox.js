import ExpandIcon from './ExpandIcon';
import { useState } from "react";

const TextBox = ({ title, cardNumber, cardKey, content,}) => {
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
                <p>{title}</p>
            </div>
            {expanded && (
                <div className="text-box__content">
                    {content}
                </div>
            )}
        </div>
    );
};

export default TextBox;