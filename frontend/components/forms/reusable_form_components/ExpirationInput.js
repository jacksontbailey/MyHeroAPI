import DatePicker from "react-datepicker";

const ExpirationInput = ({ handleDateChange, startDate, ...props }) => {

    return ( 
        <DatePicker 
            form="external-form"
            isClearable {...props} 
            onChange={(date) => handleDateChange(date)} 
            selected={startDate} 
            showIcon 
        />
     );
}
 
export default ExpirationInput;