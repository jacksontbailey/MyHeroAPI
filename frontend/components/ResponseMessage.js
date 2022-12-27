import {useRouter} from "next/router";

const ResponseMessage = ({ messageType, message }) => {
    const router = useRouter()
    let boxColor = messageType === 'error' ? 'red' : 'green';
    let timeout = messageType === 'error' ? 5000 : 3000;

    setTimeout(() => {
        router.push('/');
    }, timeout);

    return (
        <div style={{ backgroundColor: boxColor, color: 'white', padding: '20px', textAlign: 'center' }}>
            {message}
        </div>
    );
};

export default ResponseMessage;