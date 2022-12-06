import Head from 'next/head'
import Link from 'next/link'
import styles from '../styles/Home.module.css'
import {deleteCookie, getCookie} from 'cookies-next'
import useUser from '../data/use-user'


function Home(){
  const {user, mutate, loggedOut} = useUser();

  return(
    <>
      <Head>
        <title>My Hero API</title>
        <meta name="description" content="Fan made API for the My Hero Academia card game" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <section className={styles.header}>

          <h1>Easy Login</h1>
        </section>
        <section className={styles.login}>
          {user && !loggedOut && (
            <>
              <p>Welcome {user.email}!</p>
              <Link href='/v1'>Check out the docs!</Link>
              <button
                onClick={() =>{
                  deleteCookie('token');
                  mutate();
                }}>
                  Logout
                </button>
            </>
          )}
          {loggedOut && (
            <>
              <Link href='/login'>Login</Link>
              <p>or</p>
              <Link href='/new'>Sign Up</Link>
            </>
          )}
        </section>
      </main>
    </>
  )
}

export default Home;