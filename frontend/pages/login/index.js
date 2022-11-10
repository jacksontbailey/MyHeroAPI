import { useState } from 'react';
import { setCookie } from 'cookies-next';
import { useRouter } from 'next/router';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [remember, setRemember] = useState(false);
  const router = useRouter();


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
      method: 'POST',
      body: formData
    });

    if ((res.status == 200) && (remember === true)) {
      const json = await res.json();
      setCookie('token', json.access_token);
      setCookie('username', username);
      setCookie('password', password);
      router.push("profile");

    } else if (res.status == 200) {
      const json = await res.json();
      setCookie('token', json.access_token);
      router.push("profile");

    } else {
      alert('Login failed.')
    }
  }

  return (
    <>
      <div>
        <div>
          <div>
            <h2>Sign in to your account</h2>
          </div>
          <form action="#" method="POST" onSubmit={handleSubmit}>
            <input type="hidden" name="remember" defaultValue="true" />
            <div>
              <div>
                <label htmlFor="username">
                  Username
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
              <div>
                <label htmlFor="password">
                  Password
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
            </div>

            <div>
              <div>
                <input
                  id="remember-me"
                  name="remember-me"
                  type="checkbox"
                  value={remember}
                  onClick={() => setRemember(!remember)}
                />
                <label htmlFor="remember-me">
                  Remember me
                </label>
              </div>

              <div>
                <a href="#">
                  Forgot your password?
                </a>
              </div>
            </div>

            <div>
              <button type="submit">
                Sign in
              </button>
            </div>
          </form>
        </div>
      </div>
    </>
  )
}