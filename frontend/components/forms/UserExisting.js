import { useEffect, useState } from 'react';
import { setCookie, hasCookie } from 'cookies-next';
import { useRouter } from 'next/router';


const UserExisting = ({currentForm}) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const router = useRouter();
    const token = hasCookie('token')
  
    function handleUsernameChange(e) {
        setUsername(e.target.value);
    }

      function handlePasswordChange(e) {
        setPassword(e.target.value);
    }
    
    async function handleSubmit(e) {
        e.preventDefault();
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/login`, {
          mode: 'cors',
          method: 'POST',
          headers: {
            'Accept': 'application/json',
          },
          body: formData,
        });
    
        (res.status === 200) 
          ? await res.json().then(res => {setCookie('token', res.access_token)})
          : await res.json().then(res => {alert(res.detail)})
      }
    
    useEffect(() => {
        if (token){
          router.push('/')
        }
    }, [])
    
    return (
        <>
            <form action="#" method="POST" onSubmit={handleSubmit} className= {(currentForm === "Login") ? 'form-content': 'form-invisible'}>
                <section className='form-fillable user-existing'>
                <input
                    id="username"
                    name="username"
                    type="text"
                    autoComplete="username"
                    aria-label='Username'
                    placeholder="Username"
                    required
                    value={username}
                    onChange={handleUsernameChange}
                />
                <input
                    id="password"
                    name="password"
                    type="password"
                    autoComplete="current-password"
                    aria-label='Password'
                    placeholder='Password'
                    required
                    value={password}
                    onChange={handlePasswordChange}
                />
                </section>
                <p className="forgot"><a href="#">Forgot password?</a></p>
                <button type="submit" className='btn'>Log In</button>
            </form>
        </>
    );
}
 
export default UserExisting;