import Button from "./reusable_form_components/Button";
import ExpirationInput from "./reusable_form_components/ExpirationInput";
import Form from "./reusable_form_components/Form";
import Input from "./reusable_form_components/Input";
import Option from "./reusable_form_components/Option";
import Select from "./reusable_form_components/Select";
import useUser from '../../data/use-user'
import { useState } from "react";
import { getCookie, setCookie } from "cookies-next";


const CreateApiKeyForm = ({ refresh }) => {
    const {user} = useUser();
    const token = getCookie('token');
    const [isExpirationVisible, setIsExpirationVisible] = useState(false);
    const [startDate, setStartDate] = useState(new Date());
    const [formData, setFormData] = useState({
        name: '',
        hasExpiration: false,
        expiration: "",
        username: ""
    });
    
    const handleSubmit = async (event) => {
        event.preventDefault();
        formData.username = user.username
        const { name, hasExpiration, expiration, username} = formData;

        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/create`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': `Bearer ${token}`    
            },
            body: JSON.stringify({ name, hasExpiration, expiration, username }),
        });

        if (res.ok) {
            const data = await res.json();
            setCookie("api_key", data)
            // handle successful creation of api key
        } else {
            console.error("error", res.json())
            // handle error
        }
        refresh
    };


    const handleHasExpirationChange = (e) => {
        setFormData({ ...formData, hasExpiration: Boolean(e.target.value)});
        (e.target.value === "true") ? setIsExpirationVisible(true) : setIsExpirationVisible(false)
    };

    const handleNameChange = (e) => {
        setFormData({ ...formData, name: e.target.value });
    };

    const handleDateChange = (date) => {
        setStartDate(date);
        setFormData({ ...formData, expiration: date});
    };
    
        
    return (
            
            <Form onSubmit={handleSubmit} className='form-content'>
            <section className='form-fillable api-new'>
                <Input
                    type="text"
                    name="name"
                    placeholder="Key Name"
                    onChange={handleNameChange}
                    value={formData.name}
                    required
                />


                <Select
                    name="hasExpiration"
                    label= "Set Expiration Date"
                    placeholder="Expiration"
                    onChange={handleHasExpirationChange}
                    selected={formData.hasExpiration.valueOf()}
                >
                    <Option value={false} label="No"/>
                    <Option value={true} label="Yes" />
                </Select>
                {formData.hasExpiration && isExpirationVisible &&
                    <ExpirationInput 
                        handleDateChange={handleDateChange}
                        startDate={startDate}
                        placeholderText="Select a date and time"
                        dateFormat="Pp"
                        showTimeSelect
                    />
                }


            </section>

            <Button type="submit" className='btnSubmit' btnText={"Create Key"}/>

        </Form>
    );
}
export default CreateApiKeyForm;