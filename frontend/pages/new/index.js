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

        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/new`, {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({"username": username, "email": email, "password": password})
        })

        if (res.status === 200){
            const json = await res.json()
            console.log(json)
            router.push('/new/success')
        } else {
            const json = await res.json()
            alert(json.detail)
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