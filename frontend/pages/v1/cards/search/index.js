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

    let parsedCards =
        cards?.cards.map((card, index) => {
            return (
                <section key={`card-${index}`}>
                    {Object.entries(card).map((item, index) => {
                        return(
                            <>
                                {
                                    (Object.prototype.toString.call(item[1]) === '[object Array]') 
                                        ?   <dl key={`${item[1]}-${index}`}>
                                                <dt>{item[0]}</dt>
                                                {
                                                    Object.entries(item[1]).map((i, index) => {
                                                        return(
                                                            <dd key={`${i[0]}-${index}`}>{i[1]}</dd>
                                                        )
                                                    })
                                                }
                                            </dl>  
                
                                    :   (Object.prototype.toString.call(item[1]) === '[object Object]') 
                                            ?   <dl key={`${item[1]}-${index}`}>
                                                    <dt>{item[0]}</dt>
                                                    {Object.entries(item[1]).map((i, index) => {
                                                        return(
                                                            <>
                                                                {
                                                                    (Object.prototype.toString.call(i[1]) === '[object Array]') 
                                                                        ?   <dd key={`${i[1]}-${index}`}>
                                                                                <dl>
                                                                                    <dt>{i[0]}</dt>
                                                                                    {
                                                                                        Object.entries(i[1]).map((a, index) => {
                                                                                            return(
                                                                                                <dd key={`${a[1]}-${index}`}>{`${a[0]}: ${a[1]}`}</dd>
                                                                                            )
                                                                                        })
                                                                                    }
                                                                                </dl>
                                                                            </dd>
                                                                
                                                                    //:   (Object.prototype.toString.call(i[1]) === ('[object Null]' ||'[object Undefined]')) ? <dd>{`${i[0]}: Null`}</dd>                         
                                                                
                                                                    :   <dd>{`${i[0]}: ${i[1]}`}</dd>
                                                                
                                                                }
                                                            </>
                                                        )
                                                    })}
                                                </dl>
                
                                : <p>{`${item[0]}: ${item[1]}`}</p>
                                }
                            </>
                        )}
                    )}
                </section>
            )
        })
        

    return (
        <main>
            <h1>Cards</h1>
            {parsedCards}
        </main>
    );
}
export default CardSearch