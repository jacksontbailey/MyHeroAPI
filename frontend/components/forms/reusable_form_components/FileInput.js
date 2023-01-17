const FileInput = ({ name, label, onChange, ...rest }) => {
    return (
        <div className="form-file">
            <label htmlFor={name}>{label}</label>
            <input type="file" id={name} name={name} onChange={onChange} {...rest} />
        </div>
    )
}

export default FileInput;