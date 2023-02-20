import { useState } from 'react';
import { TbEdit, TbX } from 'react-icons/tb'
import ToggleButton from './forms/reusable_form_components/ToggleButton';
import useKeys from "../data/use-key";
import { deleteKey, updateKey } from '../libs/auth'


const ApiKeyList = () => {
    const { loading, apiKeys, mutate } = useKeys();
    const [keyName, setKeyName] = useState('');
    const [selectedItem, setSelectedItem] = useState({});

    const handleToggleStatus = async (index) => {
        const updatedApiKeys = [...apiKeys];
        const keyToUpdate = updatedApiKeys[index]['api_key']
        const newStatus = (updatedApiKeys[index]['key_status'] === 'active') ? 'inactive' : 'active';
        await updateKey({ currentKey: keyToUpdate, updateStatus: newStatus }).then(() => { mutate(updatedApiKeys) })
    }

    const handleDelete = async (index) => {
        const updatedApiKeys = [...apiKeys];
        const keyToDelete = updatedApiKeys[index]['api_key']
        await deleteKey(keyToDelete).then(() => { mutate(updatedApiKeys) })
    }

    const handleEdit = async (key, newKeyName) => {
        const updatedApiKeys = [...apiKeys];
        await updateKey({ currentKey: key, updateName: newKeyName }).then(() => { mutate(updatedApiKeys) })
    }

    const openPopup = (item) => {
        keyNameDialog.showModal()
        setSelectedItem(item);
        setKeyName(item.key_name);
    };

    const handlePopupSubmit = () => {
        handleEdit(selectedItem.api_key, keyName);
    };


    if (loading) return <div className='loader'></div>


    return (
        <>
            {!loading && apiKeys && (
                <section className="api-key__grid">
                    {apiKeys.map((item, index) => (
                        <article key={index} className="api-key__item">
                            <header className="api-key__item-section">
                                <h3 className="api-key__item-title">Key Name</h3>
                                <div className="api-key__item-content">{item.key_name}</div>
                            </header>
                            <section className="api-key__item-header">
                                <h3 className="api-key__item-title">Key</h3>
                                <div className="api-key__item-content"><pre>{item.api_key}</pre></div>
                            </section>
                            <section className="api-key__item-section">
                                <h3 className="api-key__item-title">Status</h3>
                                <div className="api-key__item-content">{item.key_status}</div>
                            </section>
                            <section className="api-key__item-section">
                                <h3 className="api-key__item-title">Expiration Date</h3>
                                <div className="api-key__item-content">{item.exp_date}</div>
                            </section>
                            <footer className="api-key__item-footer">
                                <ToggleButton toggleStatus={item.key_status} onClick={() => handleToggleStatus(index)} title="Change Key Status" />
                                {item.key_status === "inactive"
                                    ? <TbX className={"delete-key"} onClick={() => handleDelete(index)} title="Delete API Key" />
                                    : <TbEdit onClick={() => openPopup(item)} className={"edit-button"} title="Change Key Name" />
                                }
                            </footer>
                        </article>
                    ))}
                    <dialog id = "keyNameDialog" className='dialog__key-name'>
                        <form className='dialog__form' method='dialog'>
                            <section className='dialog__fillable'>
                                <label className='dialog__label'>New Key Name:</label>
                                <input className='dialog__input' type="text" value={keyName} onChange={(e) => setKeyName(e.target.value)} autoFocus/>
                            </section>
                            <button className='dialog__cancel btnCancel' value="cancel">Cancel</button>
                            <button className='dialog__submit btnSubmit' onClick={handlePopupSubmit} value="submit">Add Key</button>
                        </form>
                    </dialog>
                </section>
            )}
            </>
    );
}

export default ApiKeyList;