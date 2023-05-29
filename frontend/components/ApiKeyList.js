import { useState, useEffect } from 'react';
import { TbEdit, TbX } from 'react-icons/tb'
import ToggleButton from './forms/reusable_form_components/ToggleButton';
import { useContext } from 'react';
import { AuthContext } from '../pages/_app';


const ApiKeyList = () => {
    const { loading, mutateApiKeys, apiKeys, deleteKey, updateKey } = useContext(AuthContext);
    const [keys, setKeys] = useState(apiKeys);
    const [keyName, setKeyName] = useState('');
    const [selectedItem, setSelectedItem] = useState({});

    useEffect(() => {
        setKeys(apiKeys);
    }, [apiKeys]);

    const handleToggleStatus = async (index) => {
        const updatedApiKeys = [...keys];
        const keyToUpdate = updatedApiKeys[index]['api_key']
        const newStatus = (updatedApiKeys[index]['key_status'] === 'active') ? 'inactive' : 'active';
        await updateKey( keyToUpdate, {updateStatus: newStatus });
    }
 
    const handleDelete = async (index) => {
        const keyToDelete = keys[index]['api_key'];
        try {
            await deleteKey(keyToDelete);
            const updatedApiKeys = [...keys];
            updatedApiKeys.splice(index, 1);
            setKeys(updatedApiKeys);
        } catch (error) {
            mutateApiKeys(keys)
        }
    };
      
    const handleEdit = async (key, newKeyName) => {
        await updateKey(key, { updateName: newKeyName })
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
                                <label className='dialog__label'>Rename Key:</label>
                                <input className='dialog__input' type="text" value={keyName} onChange={(e) => setKeyName(e.target.value)} autoFocus/>
                            </section>
                            <button className='dialog__cancel btnCancel' value="cancel">Cancel</button>
                            <button className='dialog__submit btnSubmit' onClick={handlePopupSubmit} value="submit">Submit</button>
                        </form>
                    </dialog>
                </section>
            )}
            </>
    );
}

export default ApiKeyList;