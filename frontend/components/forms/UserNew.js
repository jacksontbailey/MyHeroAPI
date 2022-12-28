import { useState } from 'react';
import { useRouter } from 'next/router';


const UserNew = ({currentForm}) => {
    const [newUsername, setNewUsername] = useState('');
    const [newEmail, setNewEmail] = useState('')
    const [newPassword, setNewPassword] = useState('');
    const router = useRouter();

    function handleNewUsernameChange(e) {
        setNewUsername(e.target.value);
    }
    
    function handleNewPasswordChange(e) {
        setNewPassword(e.target.value);
    }
    
    function handleNewEmailChange(e) {
        setNewEmail(e.target.value);
    }

    async function handleNewSubmit(e) {
        e.preventDefault();
    
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/new`, {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({"username": newUsername, "email": newEmail, "password": newPassword})
        })
    
        if (res.status === 200){
            const json = await res.json()
            router.push('/new/success')
        } else {
            const json = await res.json()
            alert(json.detail)
        }
      }

    return (
        <>
            <form action="#" method="POST" onSubmit={handleNewSubmit} className= {(currentForm !== "Login") ? 'form-content': 'form-invisible'}>
                <section className='form-fillable user-new'>
                    <input
                        id="email"
                        name="email"
                        type="email"
                        placeholder="Email*"
                        aria-label='Email'
                        required
                        value={newEmail}
                        onChange={handleNewEmailChange}
                    />
                    <input
                        id="newUsername"
                        name="username" 
                        type="text"
                        placeholder="Username*"
                        aria-label='Username'
                        required
                        value={newUsername} 
                        onChange={handleNewUsernameChange}
                    />
                    <input
                        id="newPassword"
                        name="password"
                        type="password"
                        placeholder="Password*"
                        aria-label='Password'
                        required
                        value={newPassword}
                        onChange={handleNewPasswordChange}
                    />
                </section>
                <button type="submit" className='btnSubmit'>Create Account</button>
            </form>
        </>
    );
}
 
export default UserNew;