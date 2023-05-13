import { useCallback, useMemo, useState } from 'react';
import { createContext } from 'react';
import { getCookie } from "cookies-next";
import Layout from '../components/Layout'
import useSWR from "swr";
import userFetcher from "../libs/api-user"
import '../styles/globals.css'
import '../styles/app.scss'


export const AuthContext = createContext();

function MyApp({ Component, pageProps }) {
  const [currentUser, setCurrentUser] = useState(null);

  const {data, mutate, error} = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/login/me`, userFetcher);
  const loading = !data && !error;
  const loggedOut = error && error.status === 401


  // Retrieve token from cookie
  const token = getCookie("token");

  const login = useCallback((response) => {
    storeCredentials(response.credentials);
    setCurrentUser(response.user);
  }, []);

  const contextValue = useMemo(() => ({
    currentUser,
    login,
    loading,
    loggedOut,
    user: {
      ...data,
      token,
    },
    mutate
  }), [currentUser, login, loading, loggedOut, data, token, mutate]);

  return (
    <AuthContext.Provider value={contextValue}>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </AuthContext.Provider>
  );
}
export default MyApp