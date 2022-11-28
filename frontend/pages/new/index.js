import { useState } from 'react';
import { useRouter } from 'next/router';

const NewAccount = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('');
    const router = useRouter();
    
    function handleUsernameChange(e) {
        setUsername(e.target.value);
    }

    function handleEmailChange(e) {
        setEmail(e.target.value);
    }
    
    function handlePasswordChange(e) {
        setPassword(e.target.value);
    }
    
    async function handleSubmit(e) {
        e.preventDefault();
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);
        formData.append('email', email);

        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/new`, {
          method: 'POST',
          body: formData
        })

        if (res.ok){
            router.push('/new/success')
        }
    }
    
    return (
        <>
            <form action="#" method="POST" onSubmit={handleSubmit}>
                <div>
                    <div className="formUsername">
                        <label htmlFor="username">Username</label>
                        <input
                            id="username"
                            name="username" 
                            type="text"
                            required
                            placeholder="Username"
                            value={username} 
                            onChange={handleUsernameChange}
                        />
                    </div>
                    <div className="formEmail">
                        <label htmlFor="email">Email Address</label>
                        <input
                            id="email"
                            name="email"
                            type="email"
                            required
                            value={email}
                            onChange={handleEmailChange}
                        />
                    </div>
                    <div className="formPassword">
                        <label htmlFor="password">Password</label>
                        <input
                            id="password"
                            name="password"
                            type="password"
                            required
                            value={password}
                            onChange={handlePasswordChange}
                        />
                    </div>
                </div>
                <div>
                    <button type="submit">Create Account</button>
                </div>
            </form>
        </>
    );
}
 
export default NewAccount;