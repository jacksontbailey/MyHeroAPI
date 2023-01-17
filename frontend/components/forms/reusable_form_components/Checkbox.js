const Checkbox = ({ name, label, onChange, ...rest }) => {
    return (
        <div className="form-checkbox">
            <input type="checkbox" id={name} name={name} onChange={onChange} {...rest} />
            <label htmlFor={name}>{label}</label>
        </div>
    );
}

export default Checkbox;