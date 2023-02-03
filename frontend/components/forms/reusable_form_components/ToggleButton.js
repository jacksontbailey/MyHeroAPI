import {motion} from "framer-motion"


const ToggleButton = ({isActive, ...props}) => {
    const className = `switch ${isActive ? "active" : "inactive"}`;

    return (
        <motion.button animate className={className} {...props}>
            <motion.div animate />
        </motion.button>
    );
}
 
export default ToggleButton;