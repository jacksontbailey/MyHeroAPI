import ExpandIcon from './ExpandIcon';
import { useState } from "react";

const TextBox = ({ title, cardNumber, cardKey, content,}) => {
    const [expanded, setExpanded] = useState(false);

    return (
        <div className={`text-box card-${cardNumber}`} key={cardKey}>
            <div className="text-box__header" onClick={() => setExpanded(!expanded)}>
                <ExpandIcon expanded={expanded} />
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