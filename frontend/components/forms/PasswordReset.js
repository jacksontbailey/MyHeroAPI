import { useState, useEffect } from 'react';
import { useForm } from 'react-hook-form';
import ResponseMessage from '../ResponseMessage';


const PasswordReset = ({token, email}) => {
    const { register, handleSubmit, reset, formState, formState:{isSubmitSuccessful}, errors } = useForm();    
    const [isSubmitting, setIsSubmitting] = useState(false);
    
    useEffect(() => {
        if(isSubmitSuccessful){
            reset()
        }
    }, [formState, reset])

    const onSubmit = async(data) => {
        setIsSubmitting(true);
        
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/verification/reset-password`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({"token": token,"email": email,"password": data.password})
        })
        
        if (res.status === 200){
            return (<ResponseMessage messageType="success" message={`Your password has been reset.`} />)
        } else {
            const json = await res.json()
            alert(json.detail)
        }

      }


    return (
        <>
            <form onSubmit={handleSubmit(onSubmit)} className='form-reset-password'>
                <section className='form-fillable user-new'>
                <input
                        id="newPassword"
                        name="password"
                        type="password"
                        placeholder="Password*"
                        aria-label='Password'
                        required
                        {...register("password", {required: true, minLength: {value: 6, message: 'Password must be at least 6 characters long.'}})}
                    />
                </section>
                <button type="submit" className='btnSubmit' disabled={isSubmitting}>Create Account</button>
            </form>
        </>
    );
}
 
export default PasswordReset;