import Image from 'next/image'
import styles from './page.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to My Hero API
        </h1>
        <div>  
          <p>
            All of the My Hero Academia card game data you'll ever need, easily accessible through a modern RESTful API.
          </p>
          <a href="docs/v1">Check out the docs!</a>
        </div>
        <section>
          <button>New User</button>
          <button>Existing User</button>
        </section>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  )
}
