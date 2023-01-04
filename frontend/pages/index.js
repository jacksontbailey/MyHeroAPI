import Head from 'next/head'
import Link from 'next/link'
import styles from '../styles/Home.module.css'
import useUser from '../data/use-user'
import UserCombo from '../components/forms/UserCombo'
import { logout } from '../libs/auth'


function Home(){
  const {loading, user, mutate, loggedOut} = useUser();

  if(loading) return <div className='loader'></div>

  console.log(user)
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
                className= "btn-main" 
                onClick={() =>{
                  logout('token');
                  mutate();
                }}>
                  Logout
                </button>
            </>
          )}

          {loggedOut && (<UserCombo/>)}
          
        </section>
      
      </main>
    </>
  )
}

export default Home;