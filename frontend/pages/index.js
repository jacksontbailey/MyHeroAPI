import Head from 'next/head'
import Link from 'next/link'
import { AuthContext } from './_app'
import UserCombo from '../components/forms/UserCombo'
import { logout } from '../libs/auth'
import { useContext } from 'react'

function Home() {
  const { user, loading, mutateUser } = useContext(AuthContext);
  
  if (loading) {
    return <div className='loader'></div>;;
  }

  return (
    <>
      <Head>
        <title>My Hero API</title>
        <meta name="description" content="Fan made API for the My Hero Academia card game" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="main">
        <section className="login">
          {user.token && (
            <>
              <p>Welcome {user.email}!</p>
              <Link href="/v1">Check out the docs!</Link>
              <button
                className="btn-main"
                onClick={() => {
                  logout('token');
                  mutateUser(null);
                }}
              >
                Logout
              </button>
            </>
          )}
          {!user.token &&(
            <>
              <h1>Welcome to MyHeroAPI</h1>
              <UserCombo />
            </>
          )}
        </section>
      </main>
    </>
  );
}


export default Home;
