import { AuthContext } from "../_app";
import { useMemo, useState, useContext } from "react";
import CardSearchForm from "../../components/forms/CardSearch"
import CardList from "../../components/cards/CardList";


const CardSearchExample = () => {
    const { user, apiKeys } = useContext(AuthContext);
    const [cards, setCards] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const activeKey = useMemo(() => {
        return apiKeys && apiKeys.find((key) => key.key_status === 'active');
    }, [apiKeys]);

    const handleCardSearch = async () => {
        setIsLoading(true);
        setCards([]); // Clear the existing cards before making the new API request

        if (!activeKey) {
            setIsLoading(false);
            return;
        }

        try {
            const key = JSON.stringify(activeKey.key)
            const data = CardSearchForm(key = key); // Call the function in CardSearchForm component to fetch the data
            setCards(data); // Set the fetched data to the cards state
        } catch (error) {
            console.error(error);
        }

        setIsLoading(false);
    };

    const rememberCards = useMemo(() => {
        return cards?.cards;
    }, [cards]);

    if (isLoading) {
        return <div className='loader'></div>;
    }

    return (
        <main>
            <h1>Cards</h1>
            <CardSearchForm apiKey={activeKey?.key} onCardSearch={handleCardSearch} />
            {rememberCards !== undefined ? <CardList cards={rememberCards} /> : null}
        </main>
    );
}

export default CardSearchExample;