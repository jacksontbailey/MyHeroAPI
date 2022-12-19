import UserExisting from "./UserExisting";
import UserNew from "./UserNew";
import { useState } from 'react';



const UserCombo = () => {
    const [currentForm, setCurrentForm] = useState('Login')

    function handleCurrentFormChange(e){
        setCurrentForm((e.target.value === 'New')? 'New': 'Login')
        console.log(e.target.value)
      }
    
    return (
        <>
            <div className='form'>
                <div className='form-box'>
                    <section className='current-form-options'>
                        <button onClick={handleCurrentFormChange} value='Login'>Login</button>
                        <button onClick={handleCurrentFormChange} value='New'>New User</button>
                    </section>
                    <UserExisting currentForm={currentForm}/>
                    <UserNew currentForm={currentForm}/>
                </div>
            </div>
        </>

    );
}
 
export default UserCombo;