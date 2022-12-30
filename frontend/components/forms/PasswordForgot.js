import { useState } from 'react';
import { useRef } from 'react';
import ResponseMessage from '../ResponseMessage';


const ForgotPassword = () => {
    const [email, setEmail] = useState('');
    const [isSubmitting, setIsSubmitting] = useState(false);
    const formRef = useRef(null)

    function handleEmailChange(e) {
        setEmail(e.target.value);
    }
    
    async function handleNewSubmit(e) {
        e.preventDefault();
        setIsSubmitting(true);
        
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/new/password/${email}`, {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        })
        
        formRef.current.reset();

        if (res.status === 200){
            return (<ResponseMessage messageType="success" message={`A password reset has been sent to ${email}.`} />)
        } else {
            const json = await res.json()
            alert(json.detail)
        }

    }


    return (
        <>
            <form ref={formRef} action="#" method="POST" onSubmit={handleNewSubmit} name='forgot-password' className='form-content forgot-password'>
                
                <section className='form-fillable user-new'>
                    <input
                        id="email"
                        name="email"
                        type="email"
                        placeholder="Email*"
                        aria-label='Email'
                        required
                        value={email}
                        onChange={handleEmailChange}
                    />
                </section>
                <button type="submit" className='btnSubmit' disabled={isSubmitting}>Submit</button>
            </form>
        </>
    );
}
 
export default ForgotPassword;