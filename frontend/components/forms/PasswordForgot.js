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
    
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/new/password`, {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({"email": email})
        })
        
        formRef.current.reset();

        return (<ResponseMessage messageType="success" message={`A password reset has been sent to ${email}.`} />)
      }


    return (
        <>
            <form ref={formRef} action="#" method="POST" onSubmit={handleNewSubmit} className='form-forgot-password'>
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
                <button type="submit" className='btnSubmit' disabled={isSubmitting}>Create Account</button>
            </form>
        </>
    );
}
 
export default ForgotPassword;