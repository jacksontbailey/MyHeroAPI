import { useMemo, useEffect, useState, useContext } from "react";
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
            cards
                .flatMap(({ count, cards }) => {
                    if (!cards) {
                        return [];
                    }
                    return [
                        { total: count },
                        ...cards.map((card) => ({
                            title: card.name,
                            content: <a href={card.url}>{card.url}</a>,
                            cardNumber: card.id,
                            cardKey: card.key,
                        }))
                    ];
                })
                .sort((a, b) => a.cardNumber - b.cardNumber) // Sort the cards based on the "id" in ascending order
        );
    }, [cards]);
        
    if (isLoading) {
        return <div className='loader'></div>;
    }

    return (
        <main>
            <h1>All Cards</h1>
            <TextBoxList data={cardsData} />
        </main>
    );
}