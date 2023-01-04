import { getCookie } from "cookies-next";
import {isTokenExpired, refreshAccessToken} from './api-token';

export default async (url) => {
    const token = getCookie("token");
    const error = new Error("Not authorized!");
    
    if (!token){
        error.status = 401;
        throw error;
    }

    if (document.cookie.includes(`token=${token}`) && !isTokenExpired(token)) {
        console.log("not expired")
        try {
            return await fetch(url, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            }).then((res) => (res.status === 200 ? res.json() : alert(res.json().detail)));
        
        } catch (error) {    
            if (error.status === 401) {
                const refresh_token = getCookie("refresh_token");
            
                if (refresh_token) {
                    const new_token = await refreshAccessToken(refresh_token);
                    return await fetch(url, {
                        headers: {
                            'Authorization': `Bearer ${new_token}`,
                        },
                    }).then((res) => (res.status === 200 ? res.json() : alert(res.json().detail)));
                }
            }
            
            throw error;
        }
    }
    
    else if (document.cookie.includes(`token=${token}`) && isTokenExpired(token)){
        const refresh_token = getCookie("refresh_token");
        console.log("expired")

        if (refresh_token) {
            const new_token = await refreshAccessToken(refresh_token);
            return await fetch(url, {
                headers: {
                    'Authorization': `Bearer ${new_token}`,
                },
            }).then((res) => (res.status === 200 ? res.json() : alert(res.json().detail)));
        }
    }

    else {
        error.status = 401;
        throw error
    }
};

/*export default async (url) => {
    const token = getCookie('token');
    if (document.cookie.includes(`token=${token}`)){
        return(
            await fetch(url, {headers: {'Authorization': `Bearer ${token}`}}).then(res => (res.status === 200) ? res.json() : alert(res.json().detail))
        )
    }
    const error = new Error("Not authorized!");
    error.status = 401;
    throw error;
} */