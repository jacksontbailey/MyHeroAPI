const Switch = ({ name, label, onChange, ...rest }) => {
    return (
        <div className="form-switch">
            <label htmlFor={name}>{label}</label>
            <switch id={name} name={name} onChange={onChange} {...rest} />
        </div>
    );
};
export default Switch;