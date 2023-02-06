import CreateApiKeyForm from "../../components/forms/ApiKeyCreate";
import ApiKeyTable from "../../components/table/ApiKeyTable";

const ApiCreationPage = () => {

    return(
        <main className="api-page">
        
        
            <section className="current-api-keys">
                <ApiKeyTable />
            </section>
        
        
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