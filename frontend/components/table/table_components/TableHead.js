const TableHead = ({ className, children }) => {
    return (
        <thead className={className}>
            {children}
        </thead>
    );
};

export default TableHead;