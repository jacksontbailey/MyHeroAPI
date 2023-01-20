import Button from "./reusable_form_components/Button";
import Form from "./reusable_form_components/Form";
import Input from "./reusable_form_components/Input";
import Option from "./reusable_form_components/Option";
import Select from "./reusable_form_components/Select";
import useUser from '../../data/use-user'
import DatePicker from "react-datepicker";
import { useState } from "react";
import { getCookie } from "cookies-next";

import "react-datepicker/dist/react-datepicker.css";
import 'react-datepicker/dist/react-datepicker-cssmodules.css';


const CreateApiKeyForm = () => {
    const {user} = useUser();
    const token = getCookie('token');
    const [formData, setFormData] = useState({
        name: '',
        hasExpiration: false,
        expiration: "",
        time: "",
        username: ""
    });
    const [selectedDate, setSelectedDate] = useState(new Date());
    const [selectedTime, setSelectedTime] = useState("");
    
    const handleSubmit = async (event) => {
        event.preventDefault();
        username = user.username
        const { name, hasExpiration, expiration, time, username } = formData;
        console.log(formData, token)

        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/create`, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': token    
            },
            body: JSON.stringify({ name, hasExpiration, expiration, time, username }),
        });

        if (res.ok) {
            const data = await res.json();
            console.log(data)
            // handle successful creation of api key
        } else {
            console.error("error", res.json())
            // handle error
        }
    };


    const handleHasExpirationChange = (e) => {
        setFormData({ ...formData, hasExpiration: e.target.value});
    };

    const handleNameChange = (e) => {
        setFormData({ ...formData, name: e.target.value });
    };

    const handleDateChange = (date) => {
        setSelectedDate(date);
        setFormData({ ...formData, expiration: date});
    };
    
    const handleTimeChange = (e) => {
        setSelectedTime(e.target.value);
        setFormData({ ...formData, time: e.target.value });
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
                    value={formData.hasExpiration}
                    required
                >
                    <Option value={false} label="No"/>
                    <Option value={true} label = "Yes" />
                </Select>

                {formData.hasExpiration && (
                    <DatePicker
                        selected={selectedDate}
                        onChange={handleDateChange}
                        placeholderText="Select expiration date"
                    />,
                    <Input
                        type="time"
                        placeholder="Select time"
                        onChange={handleTimeChange}
                        value={selectedTime}
                    />
                )}
            </section>

            <Button type="submit" className='btnSubmit'>
                Create Key
            </Button>

        </Form>
    );
}
export default CreateApiKeyForm;