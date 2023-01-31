import {deleteCookie, getCookie} from 'cookies-next'


export function logout(cookie){
    deleteCookie(cookie)
}
  
export async function resetPassword({email, token, password}) {
    try{
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/verification/reset-password?token=${token}&email=${email}&password=${password}`)
        return res.status
    } catch(error) {
        return error
    }
}

export async function deleteKey(key){
    try{
        const token = getCookie("token");
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/delete-key?key=${key}`, {
            method:"DELETE",
            headers: {
                'Authorization': `Bearer ${token}`,
            }
        })
        return res.status
    } catch(error) {
        return error
    }
}

export function updateKeyName({ key }){
    try{
        const res = fetch(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/update-key?${key}`, {
            method:"DELETE"
        })
        return res.status
    } catch(error) {
        return error
    }
}

