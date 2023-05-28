import { useCallback, useMemo, useState } from 'react';
import { createContext } from 'react';
import { getCookie } from "cookies-next";
import Layout from '../components/Layout'
import useSWR from "swr";
import userFetcher from "../libs/api-user"
import keyFetcher from "../libs/api-user.js";
import '../styles/globals.css'
import '../styles/app.scss'


export const AuthContext = createContext();

function MyApp({ Component, pageProps }) {
  const [currentUser, setCurrentUser] = useState(null);

  const {data: userData, mutate: mutateUser, error: userError} = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/login/me`, userFetcher);
  const loading = !userData && !userError;
  const loggedOut = userError && userError.status === 401

  // Retrieve API keys
  const {data: apiKeysData, mutate: mutateApiKeys} = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/list-keys`, keyFetcher);
  const loadingKeys = !apiKeysData;

  // Retrieve auth token from cookie
  const token = getCookie("token");

  const login = useCallback((response) => {
    setCurrentUser(response.user);
  }, []);

  const deleteKey = async (currentKey) => {
    try {
      const updatedApiKeys = apiKeysData.filter(
        (key) => key.api_key !== currentKey
      );

      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/api_keys/delete-key?key=${currentKey}`,
        {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (res.status !== 200) {
        throw new Error("Failed to delete the key");
      }

      mutateApiKeys(updatedApiKeys);
    } catch (error) {
      // Handle error
    }
  };

  const updateKey = async (currentKey, { updateStatus = null, updateName = null }) => {
    try {
      const updatedApiKeys = apiKeysData.map((item) => {
        if (item.api_key === currentKey) {
          if (updateStatus) {
            item.key_status = updateStatus;
          }
          if (updateName) {
            item.key_name = updateName;
          }
        }
        return item;
      });

      let url = `${process.env.NEXT_PUBLIC_API_URL}/api_keys/edit-key?key=${currentKey}`;
      if (updateStatus) {
        url += `&status=${updateStatus}`;
      }
      if (updateName) {
        url += `&name=${updateName}`;
      }

      const res = await fetch(url, {
        method: "PATCH",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (res.status !== 200) {
        throw new Error("Failed to update the key");
      }

      mutateApiKeys(updatedApiKeys);
    } catch (error) {
      // Handle error
    }
  };

  const contextValue = useMemo(() => ({
    currentUser,
    login,
    loading,
    loggedOut,
    user: {
      ...userData,
      token,
    },
    mutateUser,
    apiKeys: apiKeysData,
    loadingKeys,
    deleteKey,
    updateKey,
  }), [currentUser, login, loading, loggedOut, userData, token, mutateUser, apiKeysData, loadingKeys]);
  
  return (
    <AuthContext.Provider value={contextValue}>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </AuthContext.Provider>
  );
}
export default MyApp