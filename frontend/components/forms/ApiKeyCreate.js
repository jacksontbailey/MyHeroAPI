import Button from "./reusable_form_components/Button";
import Form from "./reusable_form_components/Form";
import Select from "./reusable_form_components/Select";
import Item from "./reusable_form_components/Item";
import Input from "./reusable_form_components/Input";
//import { useRouter } from 'next/router';
import { useState } from "react";


const CreateApiKeyForm = () => {
    const [formData, setFormData] = useState({
        name: '',
        expiration: '',
        hasExpiration: false,
        timeLimit: null,
    });
    //const router = useRouter();

    const handleSubmit = async (event) => {
        event.preventDefault();
        const { name, expiration, timeLimit } = formData;
        const user = getCurrentUser();
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/create`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, expiration, timeLimit, user }),
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

    /*    const handleExpirationChange = (value) => {
            setFormData({ ...formData, expiration: value });
        }; */

    const handleHasExpirationChange = (e) => {
        setFormData({ ...formData, hasExpiration: e});
        console.log(formData.hasExpiration)
    };

    const handleNameChange = (e) => {
        setFormData({ ...formData, name: e.target.value });
    };

    const handleTimeLimitChange = (e) => {
        setFormData({ ...formData, timeLimit: e.target.options.HTMLOptionsCollection.selectedIndex});
        console.log(formData.timeLimit)
    };

    return (

        <Form onSubmit={handleSubmit} className='form-content'>
            <section className='form-fillable api-new'>
                <Input
                    type="text"
                    name="name"
                    placeholder="Name"
                    onChange={handleNameChange}
                    value={formData.name}
                    required
                />


                <Select
                    name="hasExpiration"
                    label= "Set Expiration Date"
                    placeholder="Expiration"
                    options={[
                        { value: true, label: "Yes" },
                        { value: false, label: "No" }
                    ]}
                    onChange={handleHasExpirationChange}
                    value={formData.hasExpiration}
                />

                {formData.hasExpiration && (
                    <Select
                        name="timeLimit"
                        label={"Time Limit"}
                        placeholder="Time Limit"
                        options={[
                            { value: "days", label: "Days" },
                            { value: "months", label: "Months" },
                            { value: "years", label: "Years" }
                        ]}
                        onChange={handleTimeLimitChange}
                        value={formData.timeLimit}
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