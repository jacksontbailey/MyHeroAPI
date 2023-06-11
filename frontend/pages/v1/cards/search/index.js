import { useRouter } from 'next/router'
import {useState, useEffect, useMemo, useContext} from 'react'
import CardList from '../../../../components/cards/CardList'
import { AuthContext } from '../../../_app'



export async function getServerSideProps(context){
    return {
        props: {}
    }
}


const CardSearch = () => {
    const router = useRouter()
    const [cards, setCards] = useState([])
    const { user, apiKeys } = useContext(AuthContext);
    const {t, r, sm, s, limit} = router.query
    const [isLoading, setIsLoading] = useState(false);
    const query = router.query

    
    
    useEffect(() => {
        async function getCards(){
            setIsLoading(true);

            const activeKey = apiKeys && apiKeys.find(key => key.key_status === 'active');
            
            if (!activeKey) {
                // Handle the case when there are no active API keys
                setIsLoading(false);
                setCards([]);
                return;
            }

            const key = JSON.stringify(activeKey)
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards/search?${new URLSearchParams(query)}`, {
                headers: {
                    'api-key': `${key}`,
                }
            })        

            if (res.status == 200) {
                const result = await res.json();
                setCards(result)
            }
            setIsLoading(false);
        }
        getCards();
    }, [apiKeys, user.token])

    const rememberCards = useMemo(() => {
        return cards?.cards
    })


    if (isLoading) {
        return <div className='loader'></div> 
    }
    return(
        <main>
            <h1>Cards</h1>
            {(rememberCards !== undefined) ? <CardList cards={rememberCards}/> : null}
        </main>
    )
}
export default CardSearch