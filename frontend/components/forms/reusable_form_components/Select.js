const Select = ({ name, className, label, children, ...props}) => {
  return (
    <div className={className}>
      <label htmlFor={name}>{label}</label>
      <select id={name} name={name} aria-label={label} {...props}>
        {children}
      </select>
    </div>
  )
}
export default Select;