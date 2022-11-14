import { getCookie } from 'cookies-next'
import { useRouter } from 'next/router'
import {useState, useEffect} from 'react'


export async function getServerSideProps({params, req, res}){
    const token = getCookie('token', {req, res});
    console.log(`my token is ${token} and is type ${typeof(token)}`)
    let cardId = params.cardId.replace(/\-/g, '+')
     //checks if the id is a card number or card name and changes the type if it's a card number
    cardId = Number(cardId) !== NaN ? Number(cardId) : String(cardId);

    return { props: { cardId } }
}


const CardSearch = ({res, req}) => {
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
 
export default CardSearch;