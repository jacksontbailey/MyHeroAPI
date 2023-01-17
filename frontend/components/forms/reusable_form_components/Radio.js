const Radio = ({ name, label, options, onChange, ...rest }) => {
    return (
        <div className="form-radio">
            <label>{label}</label>
            {options.map(option => (
                <div key={option.value}>
                    <input type="radio" id={`${name}-${option.value}`} name={name} value={option.value} onChange={onChange} {...rest} />
                    <label htmlFor={`${name}-${option.value}`}>{option.label}</label>
                </div>
            ))}
        </div >
    )
}

export default Radio;