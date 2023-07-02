import { useState } from 'react'

const availableTypes = ['Attack', 'Asset', 'Action', 'Character', 'Foundation'];
const availableRarities = [
    'Common',
    'Uncommon',
    'Rare',
    'Ultra Rare',
    'Starter Exclusive',
    'Promo',
    'Secret Rare',
];
const availableSymbols = [
    'Air',
    'All',
    'Chaos',
    'Death',
    'Earth',
    'Evil',
    'Fire',
    'Good',
    'Infinity',
    'Life',
    'Order',
    'Void',
    'Water',
];
const availableSets = ['My Hero Academia', 'Crimson Rampage', 'Provisional Showdown'];

export default function CardSearchForm(key) {
    const [endpoint, setEndpoint] = useState('');
    const [types, setTypes] = useState([]);
    const [rarities, setRarities] = useState([]);
    const [symbols, setSymbols] = useState([]);
    const [sets, setSets] = useState([]);
    const [limit, setLimit] = useState('');

    const handleEndpointChange = (event) => {
        setEndpoint(event.target.value);
    };

    const handleTypeChange = (event) => {
        const { value } = event.target;
        if (types.includes(value)) {
            setTypes(types.filter((type) => type !== value));
        } else {
            setTypes([...types, value]);
        }
    };

    const handleRarityChange = (event) => {
        const { value } = event.target;
        if (rarities.includes(value)) {
            setRarities(rarities.filter((rarity) => rarity !== value));
        } else {
            setRarities([...rarities, value]);
        }
    };

    const handleSymbolChange = (event) => {
        const { value } = event.target;
        if (symbols.includes(value)) {
            setSymbols(symbols.filter((symbol) => symbol !== value));
        } else {
            setSymbols([...symbols, value]);
        }
    };

    const handleSetChange = (event) => {
        const { value } = event.target;
        if (sets.includes(value)) {
            setSets(sets.filter((set) => set !== value));
        } else {
            setSets([...sets, value]);
        }
    };

    const handleLimitChange = (event) => {
        setLimit(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        let apiUrl = `${process.env.NEXT_PUBLIC_API_URL}/v1/cards${endpoint}`;

        const searchParams = new URLSearchParams();
        if (types.length > 0) {
            searchParams.append('t', types.join(','));
        }
        if (rarities.length > 0) {
            searchParams.append('r', rarities.join(','));
        }
        if (symbols.length > 0) {
            searchParams.append('sm', symbols.join(','));
        }
        if (sets.length > 0) {
            searchParams.append('s', sets.join(','));
        }
        if (limit) {
            searchParams.append('limit', limit);
        }

        const queryString = searchParams.toString();
        if (queryString) {
            apiUrl += `/search?${queryString}`;
        }

        try {
            const res = await fetch(apiUrl, {
                mode: 'no-cors',
                headers: {
                    'api-key': `${key}`,
                },
            });

            // Handle the response data
            const data = await res.json();
            return (data); // Do something with the response data
        } catch (error) {
            console.error(error);
        }
    };


    return (
        <form onSubmit={handleSubmit}>
            <label>
                Endpoint:
                <input type="text" value={endpoint} onChange={handleEndpointChange} />
            </label>

            <div>
                <p>Types:</p>
                {availableTypes.map((type) => (
                    <label key={type}>
                        <input
                            type="checkbox"
                            value={type}
                            checked={types.includes(type)}
                            onChange={handleTypeChange}
                        />
                        {type}
                    </label>
                ))}
            </div>

            <div>
                <p>Rarities:</p>
                {availableRarities.map((rarity) => (
                    <label key={rarity}>
                        <input
                            type="checkbox"
                            value={rarity}
                            checked={rarities.includes(rarity)}
                            onChange={handleRarityChange}
                        />
                        {rarity}
                    </label>
                ))}
            </div>

            <div>
                <p>Symbols:</p>
                {availableSymbols.map((symbol) => (
                    <label key={symbol}>
                        <input
                            type="checkbox"
                            value={symbol}
                            checked={symbols.includes(symbol)}
                            onChange={handleSymbolChange}
                        />
                        {symbol}
                    </label>
                ))}
            </div>

            <div>
                <p>Sets:</p>
                {availableSets.map((set) => (
                    <label key={set}>
                        <input
                            type="checkbox"
                            value={set}
                            checked={sets.includes(set)}
                            onChange={handleSetChange}
                        />
                        {set}
                    </label>
                ))}
            </div>

            <label>
                Limit:
                <input type="text" value={limit} onChange={handleLimitChange} />
            </label>

            <button type="submit">Submit</button>
        </form>
    );
}