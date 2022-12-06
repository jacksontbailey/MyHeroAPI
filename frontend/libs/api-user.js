import { getCookie } from "cookies-next";

export default async (url) => {
    const token = getCookie('token');
    if (document.cookie.includes(`token=${token}`)){
        return(
            await fetch(url, {headers: {'Authorization': `Bearer ${token}`}}).then(res => (res.status === 200) ? res.json() : alert(res.json().detail))
        )
    }
    const error = new Error("Not authorized!");
    error.status = 401;
    throw error;
}