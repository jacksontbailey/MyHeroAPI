import { useRouter } from 'next/router'
//import { verifyUser } from '../../libs/auth'
import verifyUser from '../../data/verify-user'
import { useEffect, useState } from 'react'
import ResponseMessage from '../../components/ResponseMessage'

/* export async function getServerSideProps(context){
    return {
        props: {}
    }
} */

const VerificationPage = () => {
    const router = useRouter();
    const { email, token } = router.query;
    const {loading, expiredToken, alreadyVerified, verified} = verifyUser({email, token});

    if(loading) return <div className='loader'></div>
    console.log(verified)

    return(
        <>
            {alreadyVerified && (<ResponseMessage messageType="error" message="Account already verified" />)}
            {expiredToken && (<ResponseMessage messageType="error" message="Token couldn't be found or has already expired" />)}
            {verified && (<ResponseMessage messageType="success" message="Account verified" />)}
        </>
    )
    /*    const router = useRouter()
    const { email, token } = router.query
    console.log(`email and token are: ${email}, ${token}`)
    const [verifyStatus, setVerifyStatus] = useState(null)

    useEffect(() => {
      verifyUser({ email, token }).then(status => setVerifyStatus(status))
    }, [])
    
    if (verifyStatus === 409){
        return (<ResponseMessage messageType="error" message="Account already verified" />)
    } else if (verifyStatus === 404){
        return <ResponseMessage messageType="success" message="Token couldn't be found or has already expired" />
    } else if (verifyStatus === 202){
        return <ResponseMessage messageType="error" message="Account verified" />
    } else {
        return <div>Loading...</div>
    } */
}

export default VerificationPage