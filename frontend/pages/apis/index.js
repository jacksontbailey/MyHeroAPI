import CreateApiKeyForm from "../../components/forms/ApiKeyCreate";
import ApiKeyList from "../../components/ApiKeyList";

const ApiCreationPage = () => {

    return(
        <main className="api-page">
        
            <section className="current-api-keys">
                <ApiKeyList />
            </section>
            
            <section className="new-key__section">
                <div className='new-key__form'>
                    <div className='new-key__form-box'>
                        <h2 className='new-key__form-header'>Generate API Key</h2>
                        <CreateApiKeyForm/>
                    </div>
                </div>
            </section>
        
        </main>
    )
}

export default ApiCreationPage