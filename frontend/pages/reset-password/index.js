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
    
    
    return(
        <div className='form'>
            <div className='form-box'>
                <h1 className='form-header'>Reset Password</h1>
                <PasswordReset email={email} token={token}/>
            </div>
        </div>
    )
}

export default ResetPasswordPage