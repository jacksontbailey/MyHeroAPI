import { useState } from 'react';
import { TbEdit, TbX } from 'react-icons/tb'
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
        keyNameDialog.showModal()
        setSelectedItem(item);
        setKeyName(item.key_name);
    };

    const handlePopupSubmit = () => {
        handleEdit(selectedItem.api_key, keyName);
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
                        <TableHeading className={"table__heading"}>Actions</TableHeading>
                    </TableRow>
                </TableHead>
                <tbody className='table__body'>
                    {apiKeys
                        ? apiKeys.map((item, index) => (
                            <TableRow key={index} className={"table__row"}>
                                <TableData className={"table__data__api-key"}><pre>{item.api_key}</pre></TableData>
                                <TableData className={"table__data__key-name"}>{item.key_name}</TableData>
                                <TableData className={"table__data__key-status"}>{item.key_status}</TableData>
                                <TableData className={"table__data__exp-date"}>{item.exp_date}</TableData>
                                <TableData className={"table__data__actions"}>
                                    <ToggleButton toggleStatus={item.key_status} onClick={() => handleToggleStatus(index)} title="Change Key Status"/>
                                    {item.key_status === "inactive" ? (
                                        <TbX className={"delete-key"} onClick={() => handleDelete(index)} title="Delete API Key" />
                                        ) : <TbEdit onClick={() => openPopup(item)} className={"edit-button"} title="Change Key Name"/>
                                    }

                                </TableData>
                            </TableRow>
                        ))
                        : null}
                </tbody>
            </Table>)}
                <dialog id = "keyNameDialog" className='dialog__key-name'>
                    <form className='dialog__form' method='dialog' >
                        <section className='dialog__fillable'>
                            <label className='dialog__label'>New Key Name:</label>
                            <input className='dialog__input' type="text" value={keyName} onChange={(e) => setKeyName(e.target.value)} autoFocus/>
                        </section>
                        <button className='dialog__cancel btnCancel' value="cancel">Cancel</button>
                        <button className='dialog__submit btnSubmit' value="submit" onClick={handlePopupSubmit}>Submit</button>
                    </form>
                </dialog>
        </>
    );
};

export default ApiKeyTable;
