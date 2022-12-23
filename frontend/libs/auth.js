import {deleteCookie} from 'cookies-next'

export function logout(cookie){
    deleteCookie(cookie)
}

async function verifyUser({email, token}) {
    try {
        const response = await fetch(`/api/verify?email=${email}&token=${token}`);
        const data = await response.json();
        return data

    } catch (error) {
        // Log the error message for debugging purposes
        console.error(error);
        
        // Display an error message to the user
        displayError("There was an error verifying your account. Please try again later.");
    }
}
  
  