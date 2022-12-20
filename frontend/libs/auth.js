import {deleteCookie} from 'cookies-next'

export function logout(cookie){
    deleteCookie(cookie)
}