const Form = ({ children, onSubmit, ...formParams }) => {
    return (
        <form onSubmit={onSubmit} {...formParams}>
            {children}
        </form>
    );
}

export default Form;