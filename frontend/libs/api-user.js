import { getCookie, deleteCookie } from "cookies-next";
import {isTokenExpired, refreshAccessToken} from './api-token';

export default async (url) => {
    const token = getCookie("token");
    const error = new Error("Not authorized!");
    
    if (!token){
        error.status = 401;
        throw error;
    }

    if (document.cookie.includes(`token=${token}`) && !isTokenExpired(token)) {
        return await fetch(url, {headers: {'Authorization': `Bearer ${token}`}}).then((res) => (res.status === 200 ? res.json() : alert(res.json().detail)));
    }
    
    else if (document.cookie.includes(`token=${token}`) && isTokenExpired(token)){
        const refresh_token = getCookie("refresh_token");

        if (refresh_token && !isTokenExpired(refresh_token)) {
            const new_token = await refreshAccessToken(refresh_token);
            return await fetch(url, {
                headers: {
                    'Authorization': `Bearer ${new_token}`,
                },
            }).then((res) => (res.status === 200 ? res.json() : alert(res.json().detail)));
        }
        
        else{
            deleteCookie("refresh_token")
            error.status = 401;
            throw error
        }
    }

    else {
        error.status = 401;
        throw error
    }
};