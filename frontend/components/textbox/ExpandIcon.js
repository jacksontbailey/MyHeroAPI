import { useState } from 'react';
import { FaChevronDown } from 'react-icons/fa';

const ExpandIcon = ({isExpanded }) => {    

    return <FaChevronDown className={`expand-icon${isExpanded ? '__expanded' : '__collapsed'}`}/>;
};

export default ExpandIcon;