import { createContext, useContext} from 'react';
import useUser from '../data/use-user';

const UserContext = createContext();

export function UserProvider({ children }) {
  const [user, revalidate] = useUser(null);

  useEffect(() => {
    // Revalidate the user data whenever the provider mounts or the user data changes
    revalidate();
  }, [revalidate]);

  return (
    <UserContext.Provider value={{ user }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUserContext() {
  return useContext(UserContext);
}
