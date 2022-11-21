import { getCookie } from 'cookies-next'
import { useRouter } from 'next/router'
import {useState, useEffect} from 'react'


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
            console.log(query)
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

    let parsed =
            cards?.cards.forEach(card => {
                Object.entries(card).forEach(item => {
                    <>
                        <h3>{item[0]}</h3>
                        {(Object.prototype.toString.call(item[1]) === '[object Array]') ? Object.entries(item[1]).forEach(i => {
                            <p>{i[0]}: {i[1]}</p>
                        })
        
                        : (Object.prototype.toString.call(item[1]) === '[object Object]') ? Object.entries(item[1]).forEach(i => {
                                <>
                                    <h4>{i[0]}</h4>
                                    {
                                        (Object.prototype.toString.call(i[1]) === '[object Array]') ? Object.entries(i[1]).forEach(a => {
                                            <p>{a[0]}: {a[1]}</p>
                                        })
                                                                    
                                        :<p>{i[1]}</p>
                                    }
                                </>
                        })
        
                        : <p>{item[1]}</p>
                        }
                    </>
                })
            })

    return (
        <main>
            <h1>Cards</h1>
            {(cards === undefined)? <p>No items</p> :
                <>
                    <p>yay</p>
                    {parsed}
                </>
            }
        </main>
    );
}
export default CardSearch