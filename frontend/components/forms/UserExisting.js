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
          ? await res.json().then(res => {setCookie('token', res.access_token)}).then(() => {router.reload()})
          : await res.json().then(res => {alert(res.detail)})
      }
    
    useEffect(() => {
        if (token){
          router.push('/')
        }
    }, [])
    
    return (
        <>
            <form action="#" 
                  className= {(currentForm === "Login") ? 'form-content': 'form-invisible'}
                  method="POST" 
                  name= "login-form" 
                  onSubmit={handleSubmit} 
              >
                <section className='form-fillable user-existing'>
                  <input
                      aria-label='Username'
                      autoComplete="username"
                      id="username"
                      placeholder="Username"
                      required
                      name="username"
                      onChange={handleUsernameChange}
                      type="text"
                      value={username}
                  />
                  <input
                      aria-label='Password'
                      autoComplete="current-password"
                      id="password"
                      placeholder='Password'
                      required
                      name="password"
                      onChange={handlePasswordChange}
                      type="password"
                      value={password}
                  />
                </section>
                <p className="forgot"><a href="#">Forgot password?</a></p>
                <button type="submit" className='btnSubmit'>Log In</button>
            </form>
        </>
    );
}
 
export default UserExisting;