import { useEffect, useState } from 'react';
import { setCookie, hasCookie } from 'cookies-next';
import { useRouter } from 'next/router';



export default function Login() {
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

    if (res.status === 200){
      const json = await res.json();
      setCookie('token', json.access_token);
      router.push("/");

    } else {
      const json = await res.json()
      alert(json.detail)
    }
  }
 
  // Checks if authentication token exists and redirects the user to the homepage if it does.
  useEffect(() => {
    if (token){
      router.push('/')
    }
  }, [])

  return (
    <>
      <div className='form'>
        <div className='form-box'>
          <div>
            <h1>Sign In</h1>
          </div>
          <form action="#" method="POST" onSubmit={handleSubmit} className="form-content">
              <section className='form-fillable'>
                <div className='field-wrap'>
                  <label htmlFor="username">
                    Username<span className='req'>*</span>
                  </label>
                  <input
                    id="username"
                    name="username"
                    type="text"
                    autoComplete="username"
                    required
                    placeholder="Username"
                    value={username}
                    onChange={handleUsernameChange}
                  />
                </div>
                <div className='field-wrap'>
                  <label htmlFor="password">
                    Password<span className='req'>*</span>
                  </label>
                  <input
                    id="password"
                    name="password"
                    type="password"
                    autoComplete="current-password"
                    required
                    value={password}
                    onChange={handlePasswordChange}
                  />
                </div>
              </section>

              <p className="forgot"><a href="#">Forgot password?</a></p>

              <button type="submit" className='btn'>Log In</button>
          </form>
        </div>
      </div>
    </>
  )
}