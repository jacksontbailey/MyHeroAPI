import CreateApiKeyForm from "../../components/forms/ApiKeyCreate";
import ApiKeyTable from "../../components/table/ApiKeyTable";
import useKeys from "../../data/use-key";

const ApiCreationPage = () => {
    const {loading, apiKeys, mutate} = useKeys();

    if(loading) return <div className='loader'></div>

    return(
        <main className="api-page">
            {apiKeys ? (
                <section className="current-api-keys">
                    <ApiKeyTable data={apiKeys}/>
                </section>
            ) : <p>No keys</p>}
            <div className='form new-api-form'>
                <div className='form-box'>
                    <h1 className='form-header'>Generate API Key</h1>
                    <CreateApiKeyForm refresh={mutate()}/>
                </div>
            </div>
        </main>
    )
}

export default ApiCreationPage