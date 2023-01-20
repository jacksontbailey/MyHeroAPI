import Option from "./Option"

const Select = ({ name, label, children, ...props}) => {
  return (
    <div className="form-select">
      <label htmlFor={name}>{label}</label>
      <select id={name} name={name} aria-label={label} {...props}>
        {children}
      </select>
    </div>
  )
}
export default Select;