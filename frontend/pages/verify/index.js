import { useRouter } from 'next/router'
import verifyUser from '../../libs/api-verify'
import { useEffect, useState } from 'react'
import ResponseMessage from '../../components/ResponseMessage'

export async function getServerSideProps(context){
    return {
        props: {}
    }
}

const VerificationPage = () => {
    const router = useRouter();
    const { email, token } = router.query;
    const [verifyStatus, setVerifyStatus] = useState(null)

    useEffect(() => {
      verifyUser({ email, token }).then(status => setVerifyStatus(status))
    }, [])
    
    if (verifyStatus === null) return <div className='loader'></div>
    if (verifyStatus === 202) return <ResponseMessage messageType="success" message="Account verified" />
    if (verifyStatus === 403) return <ResponseMessage messageType="error" message="Token has already been used" />
    if (verifyStatus === 404) return <ResponseMessage messageType="error" message="Token couldn't be found or has already expired" />
    if (verifyStatus === 409) return <ResponseMessage messageType="error" message="Account has already been verified" />
    
}

export default VerificationPage