import { useRouter } from 'next/router'
import resetPassword from '../../libs/auth'
import { useEffect, useState } from 'react'
import ResponseMessage from '../../components/ResponseMessage'
import PasswordReset from '../../components/forms/PasswordReset'

export async function getServerSideProps(context){
    return {
        props: {}
    }
}

const ResetPasswordPage = () => {
    const router = useRouter();
    const { email, token } = router.query;
    const [verifyStatus, setVerifyStatus] = useState(null)

    useEffect(() => {
      resetPassword({ email, token, password }).then(status => setVerifyStatus(status))
    }, [])
    
    if (verifyStatus === null) return <div className='loader'></div>
    if (verifyStatus === 202) return <ResponseMessage messageType="success" message="Account verified" />
    if (verifyStatus === 403) return <ResponseMessage messageType="error" message="Token has already been used" />
    if (verifyStatus === 404) return <ResponseMessage messageType="error" message="Token couldn't be found or has already expired" />
    if (verifyStatus === 409) return <ResponseMessage messageType="error" message="Account has already been verified" />
    
    return(
        <div className='form'>
            <div className='form-box'>
                <h1 className='form-header'>Forgot Password</h1>
                <PasswordReset />
            </div>
        </div>
    )
}

export default ResetPasswordPage