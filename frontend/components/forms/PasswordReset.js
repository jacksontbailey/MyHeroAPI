import { useState } from 'react';
import { useRef } from 'react';
import ResponseMessage from '../ResponseMessage';


const PasswordReset = ({token, email}) => {
    const [newPassword, setNewPassword] = useState('');
    const [isSubmitting, setIsSubmitting] = useState(false);
    const formRef = useRef(null)

    function handlePasswordChange(e) {
        setNewPassword(e.target.value);
    }
    
    async function handleNewSubmit(e) {
        e.preventDefault();
        setIsSubmitting(true);
    
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/verification/forgot-password`, {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({"token": token, "email": email, "password": password})
        })
        
        formRef.current.reset();

        return (<ResponseMessage messageType="success" message={`Your password has been reset.`} />)
      }


    return (
        <>
            <form ref={formRef} action="#" method="POST" onSubmit={handleNewSubmit} className='form-forgot-password'>
                <section className='form-fillable user-new'>
                <input
                        id="newPassword"
                        name="password"
                        type="password"
                        placeholder="Password*"
                        aria-label='Password'
                        required
                        value={newPassword}
                        onChange={handlePasswordChange}
                    />
                </section>
                <button type="submit" className='btnSubmit' disabled={isSubmitting}>Create Account</button>
            </form>
        </>
    );
}
 
export default PasswordReset;