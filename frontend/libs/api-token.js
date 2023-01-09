import jwtDecode from 'jwt-decode'

export async function refreshAccessToken(refresh_token){
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/login/refresh?refresh_token=${refresh_token}`,{
        method: "POST"
    });

    const data = await response.json();
    
    if (response.status === 200) {
        document.cookie = `token=${data.access_token}; path=/;`;
        return data.access_token;
    } 
    
    else {
        const error = new Error("Could not refresh access token");
        error.status = response.status;
        throw error;
    }
}


export function isTokenExpired(token){
    try {
      const decodedToken = jwtDecode(token);
      const currentTime = Date.now() / 1000;
  
      return decodedToken.exp < currentTime;
    } catch (error) {
      return false;
    }
};