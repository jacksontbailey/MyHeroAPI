import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';

export default function Profile() {
  const [user, setUser] = useState(null);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem('token');
    async function fetchUser() {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/login/me`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      if (res.status == 200) {
        const json = await res.json();
        setUser(json);
      } else {
        router.push('login');
      }
    }
    fetchUser();
  }, []);

  return (
    <div>
      <h1>Your Info</h1>
      {user && (<p>{user.username}</p>)}
      {user && (<p>{user.email}</p>)}
    </div>
  )
}