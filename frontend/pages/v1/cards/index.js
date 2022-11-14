import { useEffect, useState } from "react";
import { getCookie } from 'cookies-next'

export default function Cards(){
    const [cards, setCards] = useState([])
    
    useEffect(() => {
        const token = getCookie('token');

        async function getCards(){
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards`, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })        

            if (res.status == 200) {
                const result = await res.json();
                setCards(result)
            }
        }
        getCards();
    }, [])

    return(
        <div>
            <h1>All Cards</h1>
            {cards.map((card, index) => {
                return(
                    <div key={index}>
                        <h2>{card.count}</h2>
                        {card.cards.map((card, index) => {
                            return(
                                <div key={index}>
                                    <h3>{card.name}</h3>
                                    <p>{card.url}</p>
                                </div>
                            )
                        })}
                    </div>

                )
            })}
        </div>
    )

}
