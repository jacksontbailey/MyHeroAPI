import { getCookie } from 'cookies-next'
import { useRouter } from 'next/router'
import {useState, useEffect, useMemo} from 'react'
import Card from '../../../components/cards/Card'
import TextBox from '../../../components/textbox/TextBox'


export async function getServerSideProps({params}){
    let cardId = params.cardId
     //checks if the id is a card number or card name and changes the type if it's a card number
    cardId = Number(cardId) !== NaN ? Number(cardId) : String(cardId);

    return { props: { cardId } }
}


const CardId = ({res, req}) => {
    const router = useRouter()
    const [card, setCard] = useState([])
    const [isLoading, setIsLoading] = useState(false);
    const {cardId} = router.query
    
    useEffect(() => {
        const token = getCookie('token', {res, req});
        async function getCard(){
            setIsLoading(true);
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
            setIsLoading(false);
        }
        getCard();
    }, [])

    const rememberCards = useMemo(() => {
        return <Card data={card}/>
    })

    
    return (
        <>
            {isLoading ? <p>Loading...</p> : <TextBox key={card.id} title={card.name} content={rememberCards}/>}
        </>
    );
}
 
export default CardId;