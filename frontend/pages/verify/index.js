import { useRouter } from 'next/router'
import { useEffect } from 'react'
import verifyUser from '../../libs/auth'

const VerificationPage = async ({email, token}) => {
    const router = useRouter()
    const { email, token } = router.query
    const result = await verifyUser(email, token);

    if (result.error){
        return <ResponseMessage messageType="error" message="Invalid token" />
    } else if (result.message){
        return <ResponseMessage messageType="success" message="Account verified" />
    } else{
        return <div>Loading...</div>
    }
}

export default VerificationPage