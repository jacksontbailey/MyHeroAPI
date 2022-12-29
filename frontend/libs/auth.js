import {deleteCookie} from 'cookies-next'


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