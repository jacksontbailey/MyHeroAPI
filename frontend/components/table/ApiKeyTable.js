import Table from './table_components/Table'
import TableData from './table_components/TableData'
import TableHead from './table_components/TableHead'
import TableHeading from './table_components/TableHeading'
import TableRow from "./table_components/TableRow"


const ApiKeyTable = ({ data,  handleToggleStatus, handleDelete, handleEdit }) => {
    return (
        <Table>
            <TableHead>
                <TableRow>
                    <TableHeading>Key</TableHeading>
                    <TableHeading>Key Name</TableHeading>
                    <TableHeading>Status</TableHeading>
                    <TableHeading>Expiration Date</TableHeading>
                    <TableHeading>Buttons</TableHeading>
                </TableRow>
            </TableHead>
            <tbody>
                {data.map((item, index) => (
                    <TableRow key={index}>
                        <TableData>{item.api_key}</TableData>
                        <TableData>{item.key_name}</TableData>
                        <TableData>{item.key_status}</TableData>
                        <TableData>{item.exp_date}</TableData>
                        <TableData>
                            <button onClick={() => handleToggleStatus(item)}>Toggle Status</button>
                            <button onClick={() => handleDelete(item)}>Delete</button>
                            <button onClick={() => handleEdit(item)}>Edit</button>
                        </TableData>
                    </TableRow>
                ))}
            </tbody>
        </Table>
    );
}
 
export default ApiKeyTable;