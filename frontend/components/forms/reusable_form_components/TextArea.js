const TextArea = ({ name, label, onChange, ...rest }) => {
    return (
        <div className="form-textarea">
            <label htmlFor={name}>{label}</label>
            <textarea id={name} name={name} onChange={onChange} {...rest} />
        </div>
    );
}

export default TextArea;