import { useState } from 'react';
import { useRef } from 'react';
import ResponseMessage from '../ResponseMessage';


const PasswordReset = ({token, email}) => {
    const [newPassword, setNewPassword] = useState('');
    //const [isSubmitting, setIsSubmitting] = useState(false);
    //const formRef = useRef(null)

    function handlePasswordChange(e) {
        setNewPassword(e.target.value);
    }
    
    async function handleNewSubmit(e) {
        e.preventDefault();
        //setIsSubmitting(true);
        const data = {"token": token,"email": email,"password": newPassword}
        console.log(data)
    
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/verification/reset-password`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data)
        })
        
        //formRef.current.reset();

        if (res.status === 200){
            return (<ResponseMessage messageType="success" message={`Your password has been reset.`} />)
        } else {
            const json = await res.json()
            alert(json.detail)
        }

      }


    return (
        <>
            <form /*ref={formRef}*/ action="#" method="POST" onSubmit={handleNewSubmit} className='form-reset-password'>
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
                <button type="submit" className='btnSubmit' /*disabled={isSubmitting}*/>Create Account</button>
            </form>
        </>
    );
}
 
export default PasswordReset;