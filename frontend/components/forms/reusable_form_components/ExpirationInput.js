import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import 'react-datepicker/dist/react-datepicker-cssmodules.css';

const ExpirationInput = ({ handleDateChange, startDate, ...props }) => {

    return ( 
        <>
            <DatePicker selected={startDate} onChange={(date) => handleDateChange(date)} isClearable {...props}/>
        </> 
     );
}
 
export default ExpirationInput;