import Option from "./Option"

const Select = ({ name, label, placeholder, options, onChange, ...rest }) => {
  return (
    <div className="form-select">
      <label htmlFor={name}>{label}</label>
      <select id={name} name={name} aria-label={label} placeholder={placeholder} onChange={onChange} {...rest}>
        {options.map(option => (
          <Option key={option.value} value={option.value} label={option.label} />
        ))}
      </select>
    </div>
  )
}
export default Select;