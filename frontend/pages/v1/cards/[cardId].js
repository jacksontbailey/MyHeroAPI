import { getCookie } from 'cookies-next'


export async function getServerSideProps({params}){
    const token = getCookie('token');
    let cardId = params.cardId.replace(/\-/g, '+')
     //checks if the id is a card number or card name and changes the type if it's a card number
    cardId = Number(cardId) !== NaN ? Number(cardId) : String(cardId);

    console.log(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards/${cardId}`)
    
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards/${cardId}`, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    if (res.ok){
        let data = await res.json();
        return { props: { data } }
    } else {
        alert("HTTP-Error: " + res.status);
    }
}


export default function CardSearch({data}) {
    console.log(data)
    return(
        <div>
            <h1>Card: ${data.name}</h1>
        </div>
    )
}
/*
const CardSearch = () => {
    const router = useRouter()
    const {cardId} = router.query
    const [card, setCard] = useState([])
    
    useEffect(() => {
        const token = getCookie('token');
        console.log('CID is:', {cardId})
        async function getCard(){
            const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/v1/cards/${cardId}`, {
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