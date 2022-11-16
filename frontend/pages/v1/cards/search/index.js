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
    return (
        <>
            <h1>Cards</h1>
            {(cards === undefined)? <p>No items</p> :
                Object.values(cards).map((b) => {
                    if(Array.isArray(b)){
                        console.log(b)
                        {Object.values(b).map((c) => {
                            console.log(c)
                            return(
                                <>
                                    <h2 key={c}>{c}</h2>
                                    {Object.entries(c).map((d, e) => {
                                        if(Array.isArray(e)){
                                            console.log(e)
                                            return(
                                                <>
                                                    <h3 key={d}>{d}</h3>
                                                    <div key={e}>
                                                        <h4>{e}</h4>
                                                        <ul>{e.map(item =>{
                                                            console.log(item)
                                                            return <li key={item}>{item}</li>
                                                        })}</ul>
                                                    </div>
                                                </>
                                            )
                                        } else if (Object.prototype.toString.call(e) === '[object Object]'){
                                            Object.entries(e).map((ea, eb) => {
                                                if(Array.isArray(eb)){
                                                    console.log(eb)
                                                    return(
                                                        <>
                                                            <h5 key={ea}>{ea}</h5>
                                                            <div key={eb}>
                                                                <h6>{eb}</h6>
                                                                <ul>{eb.map(item =>{
                                                                    console.log(item)
                                                                    return <li key={item}>{item}</li>
                                                                })}</ul>
                                                            </div>
                                                        </>
                                                    )
                                                } else if (Object.prototype.toString.call(eb) === '[object Null]'){
                                                    return(
                                                        <>  
                                                            <h5>{ea}</h5>
                                                            <p>Null</p>
                                                        </>
                                                    )
                                                } else {
                                                    return(
                                                        <>
                                                            <h5>{ea}</h5>
                                                            <p>{eb}</p>
                                                        </>
                                                    )
                                                }
                                            })
                                        } else if (Object.prototype.toString.call(e) === '[object Null]'){
                                            return(
                                                <>  
                                                    <h3>{d}</h3>
                                                    <p>Null</p>
                                                </>
                                            )
                                        } else {
                                            return(
                                                <>
                                                    <h3>{d}</h3>
                                                    <p>{e}</p>
                                                </>
                                            )
                                        }
        
                                        }
                                    )}
                                </>
                            )
                        })}
                    }
                })
            }
        </>
    );
}
export default CardSearch