import { useState } from 'react';
import { TbEdit } from 'react-icons/tb'
import {IoToggleSharp} from 'react-icons/io5'
import ToggleButton from '../forms/reusable_form_components/ToggleButton';
import Table from './table_components/Table';
import TableData from './table_components/TableData';
import TableHead from './table_components/TableHead';
import TableHeading from './table_components/TableHeading';
import TableRow from './table_components/TableRow';
import useKeys from "../../data/use-key";
import { deleteKey, updateKey } from '../../libs/auth'


const ApiKeyTable = () => {
    const {loading, apiKeys, mutate} = useKeys();
    const [isOpen, setIsOpen] = useState(false);
    const [keyName, setKeyName] = useState('');
    const [selectedItem, setSelectedItem] = useState({});

    const handleToggleStatus = async (index) => {
        const updatedApiKeys = [...apiKeys];
        const keyToUpdate = updatedApiKeys[index]['api_key']
        const newStatus = (updatedApiKeys[index]['key_status'] === 'active') ? 'inactive' : 'active';
        await updateKey({currentKey: keyToUpdate, updateStatus: newStatus}).then(() =>{mutate(updatedApiKeys)})
    }

    const handleDelete = async (index) => {
        const updatedApiKeys = [...apiKeys];
        const keyToDelete = updatedApiKeys[index]['api_key']
        await deleteKey(keyToDelete).then(() => {mutate(updatedApiKeys)})
    }

    const handleEdit = async (key, newKeyName) => {
        const updatedApiKeys = [...apiKeys];
        await updateKey({currentKey: key, updateName: newKeyName}).then(() => {mutate(updatedApiKeys)})
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


    if(loading) return <div className='loader'></div>


    return (
        <>
            {!loading && apiKeys && (<Table className={"table__api-key"}>
                <TableHead className={"table__head"}>
                    <TableRow className={"table__row"}>
                        <TableHeading className={"table__heading"}>Key</TableHeading>
                        <TableHeading className={"table__heading"}>Key Name</TableHeading>
                        <TableHeading className={"table__heading"}>Status</TableHeading>
                        <TableHeading className={"table__heading"}>Expiration Date</TableHeading>
                        <TableHeading className={"table__heading"}>Buttons</TableHeading>
                    </TableRow>
                </TableHead>
                <tbody className='className={"table__body"}'>
                    {apiKeys
                        ? apiKeys.map((item, index) => (
                            <TableRow key={index} className={"table__row"}>
                                <TableData className={"table__data__api-key"}>{item.api_key}</TableData>
                                <TableData className={"table__data__key-name"}>{item.key_name}</TableData>
                                <TableData className={"table__data__key-status"}>{item.key_status}</TableData>
                                <TableData className={"table__data__exp-date"}>{item.exp_date}</TableData>
                                <TableData>
                                    <ToggleButton toggleStatus={item.key_status} onClick={() => handleToggleStatus(index)}/>
                                    {item.key_status === "inactive" ? (
                                        <button className={"table__button__delete-api-key"} onClick={() => handleDelete(index)}>Delete</button>
                                        ) : null
                                    }

                                    <TbEdit onClick={() => openPopup(item)} className={"table__button__edit-button"}/>
                                </TableData>
                            </TableRow>
                        ))
                        : null}
                </tbody>
            </Table>)}
            {isOpen && (
                <div style={{ position: 'fixed', top: '0', bottom: '0', left: '0', right: '0', backgroundColor: 'rgba(0, 0, 0, 0.5)' }}>
                    <div style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', backgroundColor: 'white', color: 'black', padding: '20px', borderRadius: '10px' }}>
                        <div>
                            <label>Key Name:</label>
                            <input type="text" style={{color: 'black'}} value={keyName} onChange={(e) => setKeyName(e.target.value)} />
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
