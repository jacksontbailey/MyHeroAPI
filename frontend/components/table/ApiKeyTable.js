import { useState } from 'react';
import { TbEdit } from 'react-icons/tb'
import {IoToggleSharp} from 'react-icons/io5'
import ToggleButton from '../forms/reusable_form_components/ToggleButton';
import Table from './table_components/Table';
import TableData from './table_components/TableData';
import TableHead from './table_components/TableHead';
import TableHeading from './table_components/TableHeading';
import TableRow from './table_components/TableRow';

const ApiKeyTable = ({ data, handleToggleStatus, handleDelete, handleEdit }) => {
    const [isActive, setIsActive] = useState(false);
    const [isOpen, setIsOpen] = useState(false);
    const [keyName, setKeyName] = useState('');
    const [selectedItem, setSelectedItem] = useState({});

    const handleActiveButton = (status, index) => {
        (status === 'active') ? setIsActive(false) : setIsActive(true)
        handleToggleStatus(index)
    }

    const openPopup = (item) => {
        setIsOpen(true);
        setSelectedItem(item);
        setKeyName(item.key_name);
    };

    const handlePopupSubmit = () => {
        handleEdit(selectedItem.api_key, keyName);
        setIsOpen(false);
    };

    const handlePopupCancel = () => {
        setIsOpen(false);
    };

    return (
        <>
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
                    {data
                        ? data.map((item, index) => (
                            <TableRow key={index}>
                                <TableData>{item.api_key}</TableData>
                                <TableData>{item.key_name}</TableData>
                                <TableData>{item.key_status}</TableData>
                                <TableData>{item.exp_date}</TableData>
                                <TableData>
                                    <ToggleButton isActive={isActive} onClick={() => handleActiveButton(item.key_status, index)}/>
                                    {item.key_status === "inactive" ? (
                                        <button onClick={() => handleDelete(index)}>Delete</button>
                                        ) : null
                                    }

                                    <button onClick={() => openPopup(item)}><TbEdit onClick={() => openPopup(item)}/></button>
                                </TableData>
                            </TableRow>
                        ))
                        : null}
                </tbody>
            </Table>
            {isOpen && (
                <div style={{ position: 'fixed', top: '0', bottom: '0', left: '0', right: '0', backgroundColor: 'rgba(0, 0, 0, 0.5)' }}>
                    <div style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', backgroundColor: 'white', color: 'black', padding: '20px', borderRadius: '10px' }}>
                        <div>
                            <label>Key Name:</label>
                            <input type="text" value={keyName} onChange={(e) => setKeyName(e.target.value)} />
                        </div>
                        <button onClick={handlePopupSubmit}>Submit</button>
                        <button onClick={handlePopupCancel}>Cancel</button>
                    </div>
                </div>
            )}
        </>
    );
};

export default ApiKeyTable;
