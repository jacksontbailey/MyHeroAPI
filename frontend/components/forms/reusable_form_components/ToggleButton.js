import {motion} from "framer-motion"


const ToggleButton = ({toggleStatus, ...props}) => {
    const className = `switch ${(toggleStatus === "active") ? "active" : "inactive"} table__button__key-status`;

    return (
        <motion.button animate className={className} {...props}>
            <motion.div animate />
        </motion.button>
    );
}
 
export default ToggleButton;