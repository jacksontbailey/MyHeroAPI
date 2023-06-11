import { FaChevronDown } from 'react-icons/fa';

const ExpandIcon = ({ isExpanded, isLoaded }) => {
    return <FaChevronDown className={`expand-icon${isExpanded ? '__expanded' : '__collapsed'} ${isLoaded ? 'animate' : ''}`}/>;
};

export default ExpandIcon;