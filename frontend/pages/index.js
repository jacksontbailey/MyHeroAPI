import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <>
      <Head>
          <title>My Hero API</title>
          <meta name="description" content="Fan made API for the My Hero Academia card game" />
          <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <section className={styles.header}>
          <h1 className={styles.title}>
            My Hero API
          </h1>
            <p>
              All the MHA card game data you'll ever need in one place,
              <br/> easily accessible through a modern RESTful API.
            </p>
            <Link href='/v1'>Check out the docs!</Link>
        </section>
        <section className={styles.login}>
          <Link href='/new' className={styles.btn}>
            New User
          </Link>
          <Link href='/login' className={styles.btn}>
            Existing User
          </Link>
        </section>
      </main>
    </>
  )
}
