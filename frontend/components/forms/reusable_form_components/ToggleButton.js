import {motion} from "framer-motion"


const ToggleButton = ({isActive, ...props}) => {
    const className = `switch ${isActive ? "active" : "inactive"}`;

    return (
        <motion.div animate className={className} {...props}>
            <motion.div animate />
        </motion.div>
    );
}
 
export default ToggleButton;