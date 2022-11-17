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
                cards.cards.forEach(card => {
                    (Object.prototype.toString.call(card) === '[object Object]') ? Object.entries(card).forEach(item => {console.log(item)})
                    : (Object.prototype.toString.call(card) === '[object Array]') ? Object.entries(card).forEach(item => {console.log(item)})
                    : (Object.prototype.toString.call(card) === '[object Null]') ? console.log('Null')
                    : console.log(Object.entries(card))
                })
            
               /* Object.values(cards).map((b, g) => {
                    if(Array.isArray(b)){
                        return(
                            <div key={`${b}-${g}`}>
                            {Object.values(b).map((c, h) => {
                                console.log(c)
                                return(
                                    <div key={`${c}-${h}`}>
                                        <h2>{c}</h2>
                                        {Object.entries(c).map(([d, e], i) => {
                                            if(Array.isArray(e)){
                                                console.log(e)
                                                return(
                                                    <div key={`${d}-${i}`}>
                                                        <h3>{d}</h3>
                                                        <div>
                                                            <h4>{e}</h4>
                                                            <ul>{e.map((item, j) =>{
                                                                console.log(item)
                                                                return (
                                                                    <li key={`${item}-${j}`}>{item}</li>
                                                                )
                                                            })}</ul>
                                                        </div>
                                                    </div>
                                                )
                                            } else if (Object.prototype.toString.call(e) === '[object Object]'){
                                                Object.entries(e).map(([ea, eb], i) => {
                                                    console.log(`THIS IS AN OBJECT ${eb}`)
                                                    if(Array.isArray(eb)){
                                                        return(
                                                            <div key={`${ea}-${i}`}>
                                                                <h5>{ea}</h5>
                                                                <div>
                                                                    <h6>{eb}</h6>
                                                                    <ul>{eb.map((item, j) =>{
                                                                        console.log(item)
                                                                        return (
                                                                            <li key={`${item}-${j}`}>{item}</li>
                                                                        )
                                                                    })}</ul>
                                                                </div>
                                                            </div>
                                                        )
                                                    } else if (Object.prototype.toString.call(eb) === '[object Null]'){
                                                        return(
                                                            <div key={`${ea}-${i}`}>  
                                                                <h5>{ea}</h5>
                                                                <p>Null</p>
                                                            </div>
                                                        )
                                                    } else {
                                                        return(
                                                            <div key={`${eb}-${i}`}>
                                                                <h5>{ea}</h5>
                                                                <p>{eb}</p>
                                                            </div>
                                                        )
                                                    }
                                                })
                                            } else if (Object.prototype.toString.call(e) === '[object Null]'){
                                                return(
                                                    <div key={`${d}-${i}`}>  
                                                        <h3>{d}</h3>
                                                        <p>Null</p>
                                                    </div>
                                                )
                                            } else {
                                                return(
                                                    <div key={`${d}-${i}`}>
                                                        <h3>{d}</h3>
                                                        <p>{e}</p>
                                                    </div>
                                                )
                                            }
            
                                            }
                                        )} 
                                    </div>
                                )
                            })}
                            </div>

                        )
                    }
                })
            */}
        </>
    );
}
export default CardSearch