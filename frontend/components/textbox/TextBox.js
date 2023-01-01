import ExpandIcon from './ExpandIcon';
import { useState } from "react";

const TextBox = ({ title, content}) => {
    const [expanded, setExpanded] = useState(false);

    return (
        <div className="text-box">
            <div className="text-box__header" onClick={() => setExpanded(!expanded)}>
                <ExpandIcon expanded={expanded} />
                <p>{title}</p>
            </div>
            {expanded && (
                <div className="text-box__content">
                    <p>{content}</p>
                </div>
            )}
        </div>
    );
};

export default TextBox;