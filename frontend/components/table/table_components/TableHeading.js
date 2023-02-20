const TableHeading = ({className, children}) => {
    return (
        <th className={className}>
            {children}
        </th>
    );
};

export default TableHeading;