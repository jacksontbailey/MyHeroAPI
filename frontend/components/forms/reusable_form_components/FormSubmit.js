import Form from "./Form";
import Button from "./Button";
import { useState, useEffect } from 'react';
import { useForm } from "react-hook-form";


const FormSubmit = ({formFields, formClass, onSubmitProp}) => {
    const { register, handleSubmit, reset, formState, formState:{isSubmitSuccessful}, errors } = useForm();    
    const [isSubmitting, setIsSubmitting] = useState(false);
    
    useEffect(() => {
        if(isSubmitSuccessful){
            reset()
        }
    }, [formState, reset])

    const onSubmit = async (data) => {
        setIsSubmitting(true);
        onSubmitProp(data)
        setIsSubmitting(false);
    }    


    return (
        <Form onSubmit={handleSubmit(onSubmit)} className={formClass}>
            {formFields.map((field, key) => {
                <field.type key={key} register={register}/>
            })}
            <Button label="btnSubmit" btnText={"Submit"} type="submit" className="btnSubmit" disabled={isSubmitting}/>
        </Form>
    );
}
 
export default FormSubmit;