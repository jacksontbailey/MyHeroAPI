import CreateApiKeyForm from "../../components/forms/ApiKeyCreate";
import ApiKeyTable from "../../components/table/ApiKeyTable";
import useKeys from "../../data/use-key";
import { deleteKey, updateKey } from '../../libs/auth'

const ApiCreationPage = () => {
    const {loading, apiKeys, mutate} = useKeys();

    const handleToggleStatus = (index) => {
        const updatedApiKeys = [...apiKeys];
        const keyToUpdate = updatedApiKeys[index]['api_key'] 
        const newStatus = (updatedApiKeys[index]['key_status'] === 'active') ? 'inactive' : 'active';
        updateKey({currentKey: keyToUpdate, updateStatus: newStatus})
        mutate(updatedApiKeys);
    }

    const handleDelete = (index) => {
        const updatedApiKeys = [...apiKeys];
        const keyToDelete = updatedApiKeys[index]['api_key']
        deleteKey(keyToDelete)
        mutate(updatedApiKeys);
    }

    const handleEdit = (key, newKeyName) => {
        const updatedApiKeys = [...apiKeys];
        updateKey({currentKey: key, updateName: newKeyName})
        mutate(updatedApiKeys);
    }

    if(loading) return <div className='loader'></div>

    return(
        <main className="api-page">
        
        {!loading && apiKeys &&(
            <section className="current-api-keys">
                <ApiKeyTable data={apiKeys} handleToggleStatus={handleToggleStatus} handleDelete={handleDelete} handleEdit={handleEdit}/>
            </section>
        )}
        
            <div className='form new-api-form'>
                <div className='form-box'>
                    <h1 className='form-header'>Generate API Key</h1>
                    <CreateApiKeyForm/>
                </div>
            </div>
        </main>
    )
}

export default ApiCreationPage