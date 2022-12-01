import Link from 'next/link'
const Success = () => {
    return (
        <>
            <h1>Success</h1>
            <p>Your account has been created!</p>
            <Link href={'/login'}>Login</Link>
        </>
    );
}
 
export default Success