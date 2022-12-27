import {deleteCookie} from 'cookies-next'


export function logout(cookie){
    deleteCookie(cookie)
}

export async function verifyUser({email, token}) {
    try{
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/verification/verify?token=${token}&email=${email}`)
        return res.status
    } catch(error) {
        return error
    }
}
  
  