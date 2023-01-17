const ErrorMessage = ({ errors, name }) => {
    return (
        <div className="error-message">
            {errors[name] && errors[name].message}
        </div>
    );
}
  
export default ErrorMessage;