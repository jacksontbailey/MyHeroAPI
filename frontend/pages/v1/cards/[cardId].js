import { getCookie } from 'cookies-next'
import { useRouter } from 'next/router'
import {useState, useEffect} from 'react'


export async function getServerSideProps({params}){
    let cardId = params.cardId
     //checks if the id is a card number or card name and changes the type if it's a card number
    cardId = Number(cardId) !== NaN ? Number(cardId) : String(cardId);

    return { props: { cardId } }
}


const CardId = ({res, req}) => {
    const router = useRouter()
    const [card, setCard] = useState([])
    const {cardId} = router.query
    
    useEffect(() => {
        const token = getCookie('token', {res, req});
        async function getCard(){
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards/${cardId}`, {
                mode: 'cors',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })        

            if (res.status == 200) {
                const result = await res.json();
                setCard(result)
            }
        }
        getCard();
    }, [])


    return (
        <>
            <h1>{card.name}</h1>
        </>
    );
}
 
export default CardId;