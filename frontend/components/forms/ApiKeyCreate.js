import Button from "./reusable_form_components/Button";
import ExpirationInput from "./reusable_form_components/ExpirationInput";
import Form from "./reusable_form_components/Form";
import Input from "./reusable_form_components/Input";
import Option from "./reusable_form_components/Option";
import Select from "./reusable_form_components/Select";
import useUser from '../../data/use-user'
import { useState } from "react";
import { getCookie, setCookie } from "cookies-next";


const CreateApiKeyForm = () => {
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
            window.location.reload()
            // handle successful creation of api key
        } else {
            console.error("error", res.json())
            // handle error
        }
    };


    const handleHasExpirationChange = async (e) => {
        setFormData({ ...formData, hasExpiration: Boolean(e.target.value)});
        (e.target.value === "true") ? setIsExpirationVisible(true) : setIsExpirationVisible(false)
    };

    const handleNameChange = async (e) => {
        setFormData({ ...formData, name: e.target.value });
    };

    const handleDateChange = async (date) => {
        setStartDate(date);
        setFormData({ ...formData, expiration: date});
    };
    
        
    return (
            
        <Form onSubmit={handleSubmit} className='new-key__form-content' id="external-form">
            <section className='new-key__form-fillable'>
                <Input
                    className="new-key__form-key"
                    name="name"
                    onChange={handleNameChange}
                    placeholder="Key Name"
                    required
                    type="text"
                    value={formData.name}
                />

                <Select
                    className="new-key__form-select"
                    name="hasExpiration"
                    label= "Do you want this key to expire?"
                    placeholder="Do you want this key to expire?"
                    onChange={handleHasExpirationChange}
                    selected={formData.hasExpiration.valueOf()}
                    required
                >
                    <Option value={false} label="No"/>
                    <Option value={true} label="Yes" />
                </Select>

                {formData.hasExpiration && isExpirationVisible &&
                    <ExpirationInput
                        className="new-key__form-calendar"
                        dateFormat="Pp"
                        handleDateChange={handleDateChange}
                        placeholderText="Select a date and time"
                        showTimeSelect
                        startDate={startDate}
                        required
                    />
                }


            </section>

            <Button type="submit" className='new-key__form-submit' btnText={"Create Key"}/>

        </Form>
    );
}
export default CreateApiKeyForm;