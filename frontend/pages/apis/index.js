import CreateApiKeyForm from "../../components/forms/ApiKeyCreate";

const ApiCreationPage = () =>{
    return(
        <div className='form'>
            <div className='form-box'>
                <h1 className='form-header'>Generate API Key</h1>
                <CreateApiKeyForm />
            </div>
        </div>
    )
}

export default ApiCreationPage