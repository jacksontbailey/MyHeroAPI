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
        await User.updateKey( keyToUpdate, { key_status: newStatus }).then(() => { mutate(updatedApiKeys) })
    }

    const handleDelete = async (index) => {
        const updatedApiKeys = [...apiKeys];
        const keyToDelete = updatedApiKeys[index]['api_key']
        await User.deleteApiKey(keyToDelete).then(() => { mutate(updatedApiKeys) })
    }

    const handleEdit = async (key, newKeyName) => {
        const updatedApiKeys = [...apiKeys];
        await User.updateApiKey(key, { key_name: newKeyName }).then(() => { mutate(updatedApiKeys) })
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
                <section className="api-key">
                    {apiKeys.map((item, index) => (
                        <article key={index} className="api-key__item">
                            <header className="api-key__item-header">
                                <h2 className="api-key__item-header-title">{item.key_name}</h2>
                            </header>
                            <section className="api-key__item-section">
                                <h3 className="api-key__item-section-title">Key</h3>
                                <p className="api-key__item-section-content">{item.api_key}</p>
                            </section>
                            <section className="api-key__item-section">
                                <h3 className="api-key__item-section-title">Status</h3>
                                <p className="api-key__item-section-content">{item.key_status}</p>
                            </section>
                            <section className="api-key__item-section">
                                <h3 className="api-key__item-section-title">Expiration Date</h3>
                                <p className="api-key__item-section-content">{(item.exp_date)? item.exp_date : "No Expiration"}</p>
                            </section>
                            <section className="api-key__item-action">
                                <h3 className='api-key__item-action-title'>Actions</h3>
                                <ToggleButton toggleStatus={item.key_status} onClick={() => handleToggleStatus(index)} title="Change Key Status" />
                                {item.key_status === "inactive"
                                    ? <TbX className={"delete-key"} onClick={() => handleDelete(index)} title="Delete API Key" />
                                    : <TbEdit onClick={() => openPopup(item)} className={"edit-button"} title="Change Key Name" />
                                }
                            </section>
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