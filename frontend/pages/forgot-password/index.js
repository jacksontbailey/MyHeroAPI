import { useRouter } from 'next/router'
import ForgotPassword from '../../components/forms/PasswordForgot'


const ForgotPasswordPage = () => {
    return(
        <div className='form'>
            <div className='form-box'>
                <h1 className='form-header'>Forgot Password</h1>
                <ForgotPassword />
            </div>
        </div>

    )
    
}

export default ForgotPasswordPage