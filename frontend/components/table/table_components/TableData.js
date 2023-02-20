const TableData = ({className, children}) => {
    return (
        <td className={className}>
            {children}
        </td>
    );
};

export default TableData;