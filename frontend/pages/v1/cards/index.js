import { useMemo, useEffect, useState, useContext } from "react";
import { getCookie } from 'cookies-next';
import TextBoxList from "../../../components/textbox/TextBoxList";
import { AuthContext } from "../../_app";


export default function Cards() {
    const { user, apiKeys } = useContext(AuthContext);
    const [cards, setCards] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        async function getCards() {
            setIsLoading(true);
            // Find an active API key
            const activeKey = apiKeys && apiKeys.find(key => key.key_status === 'active');
            
            if (!activeKey) {
                // Handle the case when there are no active API keys
                setIsLoading(false);
                setCards([]);
                return;
            }
            console.log(`active key is: ${JSON.stringify(activeKey)}\n token is: ${JSON.stringify(user.token)}`)
            const key = JSON.stringify(activeKey)
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards`, {
                headers: {
                    'api-key': `${key}`,
                }
            });
    
            if (res.status === 200) {
                const result = await res.json();
                setCards(result);
            } else {
                // Handle the case when the API request fails
                setCards([]);
            }
        
            setIsLoading(false);
        }
        
        getCards();
    }, [apiKeys, user.token]);
        

    const cardsData = useMemo(() => {
        return (
            cards.map(({ count, cards }) => (
                {total: count},
                cards.map((card, index) => ({
                    title: card.name,
                    content: <p>{card.url}</p>,
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