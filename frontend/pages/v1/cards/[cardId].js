import { useRouter } from 'next/router'
import {useState, useEffect, useMemo, useContext} from 'react'
import Card from '../../../components/cards/Card'
import TextBox from '../../../components/textbox/TextBox'
import { AuthContext } from "../../_app";



export async function getServerSideProps({params}){
    let cardId = params.cardId
     //checks if the id is a card number or card name and changes the type if it's a card number
    cardId = Number(cardId) !== NaN ? Number(cardId) : String(cardId);

    return { props: { cardId } }
}


const CardId = () => {
    const router = useRouter()
    const { user, apiKeys } = useContext(AuthContext);
    const [card, setCard] = useState([])
    const [isLoading, setIsLoading] = useState(false);
    const {cardId} = router.query
    
    useEffect(() => {
        async function getCard(){
            setIsLoading(true);

            const activeKey = apiKeys && apiKeys.find(key => key.key_status === 'active');
            
            if (!activeKey) {
                // Handle the case when there are no active API keys
                setIsLoading(false);
                setCard([]);
                return;
            }

            const key = JSON.stringify(activeKey)
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards/${cardId}`, {
                headers: {
                    'api-key': `${key}`,
                }
            })        

            if (res.status == 200) {
                const result = await res.json();
                setCard(result)
            }
            setIsLoading(false);
        }
        getCard();
    }, [apiKeys, user.token])

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