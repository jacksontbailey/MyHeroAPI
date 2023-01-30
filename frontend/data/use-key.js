import useSWR from "swr";
import keyFetcher from "../libs/api-user.js";

export default function useKeys(){
    const {data, mutate, error, revalidate} = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/api_keys/list`, keyFetcher);
    const loading = !data && !error;

    return{
        loading,
        apiKeys: data,
        mutate,
        revalidate
    };
}