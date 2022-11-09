import {useRouter} from 'next/router'
import { useEffect, useState } from "react";

export async function getStaticPaths(){
    const cards = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards`).then(res => res.json());
    return {
        paths: cards.map(card => {
            card.cards.map(card => {
                const cardId = card.id
                const cardName = card.name.toLowerCase().replace(/ /g, '-');
                return{
                    params:{
                        cardId,
                        cardName
                    }
                }
            })
        }),
        fallback: false
    }
}

export async function getStaticProps({params}) {
    const token = localStorage.getItem('token');
    const cardId = params.cardId.replace(/\-/g, '+')
    const cardName = params.cardName.replace(/\-/g, '+')
    const results = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards?id=${cardId||cardName}`, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            }).then(res=>res.json());
    return{
        props:{
            card: results[0]
        }
    }
}

/*const CardSearch = () => {
    const router = useRouter()
    const {cardId} = router.query
    const [card, setCard] = useState([])
    console.log('CID is:', {cardId})
    
    useEffect(() => {
        const token = localStorage.getItem('token');
        async function getCard(){
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards/${{cardId}}`, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })        

            if (res.status == 200) {
                const result = await res.json();
                console.log(`Result type and result: ${type(result)}, ${result}`)
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
 
export default CardSearch; */