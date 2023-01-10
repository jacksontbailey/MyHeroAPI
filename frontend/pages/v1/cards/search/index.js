import { getCookie } from 'cookies-next'
import { useRouter } from 'next/router'
import {useState, useEffect} from 'react'
import CardList from '../../../../components/cards/CardList'



export async function getServerSideProps(context){
    return {
        props: {}
    }
}


const CardSearch = () => {
    const router = useRouter()
    const [cards, setCards] = useState()
    const {t, r, sm, s, limit} = router.query
    
    
    useEffect(() => {
        const token = getCookie('token');
        const query = router.query
        async function getCard(){
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards/search?${new URLSearchParams(query)}`, {
                mode: 'cors',
                headers: {
                    'Authorization': `Bearer ${token}`
                },
            })        

            if (res.status == 200) {
                const result = await res.json();
                setCards(result)
            }
        }
        getCard();
    }, [])
    let parsedCards = cards?.cards

    return(
        <main>
            <h1>Cards</h1>
            {(parsedCards !== undefined) ? <CardList cards={parsedCards}/> : null}
        </main>
    )
}
export default CardSearch