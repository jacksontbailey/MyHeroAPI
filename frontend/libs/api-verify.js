import { useRouter } from 'next/router'

export async function getServerSideProps(context){
    return {
        props: {}
    }
}

export default async (url) => {
   return await fetch(url, {headers: {'mode': `no-cors`}}).then(res => (res.status === 202) ? res.json() : alert(res.json().detail))
}