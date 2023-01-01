import { useMemo, useEffect, useState } from "react";
import { getCookie } from 'cookies-next';
import TextBoxList from "../../../components/textbox/TextBoxList";
import TextBox from "../../../components/textbox/TextBox";

export default function Cards() {
    const [cards, setCards] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const token = getCookie('token');

    useEffect(() => {
        async function getCards() {
            setIsLoading(true);
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL }/v1/cards`, {
                headers: {
                    'Authorization': `Bearer ${token}`
            }
    });
    
        if (res.status == 200) {
            const result = await res.json();
            setCards(result);
        }
        setIsLoading(false);
    }
        getCards();
    }, [token]);

    const cardsData = useMemo(() => {
        return (
            cards.map(({ count, cards }) => (
                {total: count},
                cards.map((card, index) => ({
                    title: card.name,
                    content: card.url,
                    id: index
                }))
            )).flat()
        )
    }, [cards])

    return (
        <div>
            <h1>All Cards</h1>
            {isLoading ? <p>Loading...</p> : <TextBoxList data={cardsData} />}
        </div>
    );
}