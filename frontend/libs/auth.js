import { deleteCookie, getCookie } from 'cookies-next'


export function logout(cookie) {
    deleteCookie(cookie)
}

export async function resetPassword({ email, token, password }) {
    try {
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/verification/reset-password?token=${token}&email=${email}&password=${password}`)
        return res.status
    } catch (error) {
        return error
    }
}

export async function deleteKey(key) {
    try {
        const token = getCookie("token");
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/delete-key?key=${key}`, {
            method: "DELETE",
            headers: {
                'Authorization': `Bearer ${token}`,
            }
        })
        return res.status
    } catch (error) {
        return error
    }
}

export function updateKey({currentKey, updateStatus = null, updateName = null}){
    try{
        const token = getCookie("token");
        let url = `${process.env.NEXT_PUBLIC_API_URL}/api_keys/edit-key?key=${currentKey}`;
        if (updateStatus) {
            url += `&status=${updateStatus}`;
        }
        if (updateName) {
            url += `&name=${updateName}`;
        }
        const res = fetch(url, {
            method:"PATCH",
            headers: {
                'Authorization': `Bearer ${token}`,
            }
        })
        return res.status
    } catch(error) {
        return error
    }
}


