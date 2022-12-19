import UserExisting from "./UserExisting";
import UserNew from "./UserNew";
import { useState } from 'react';



const UserCombo = () => {
    const [currentForm, setCurrentForm] = useState('Login')

    function handleCurrentFormChange(e){
        setCurrentForm((e.target.value === 'New')? 'New': 'Login')
    }
    
    return (
        <>
            <div className='form'>
                <div className='form-box'>
                    <section className='form-multiple-options'>
                        <button className={(currentForm ==='Login') ? 'btn active' : 'btn'} onClick={handleCurrentFormChange} value='Login'>Login</button>
                        <button className={(currentForm !=='Login') ? 'btn active' : 'btn'} onClick={handleCurrentFormChange} value='New'>New User</button>
                    </section>
                    <UserExisting currentForm={currentForm}/>
                    <UserNew currentForm={currentForm}/>
                </div>
            </div>
        </>

    );
}
 
export default UserCombo;