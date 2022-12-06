import useSWR from "swr";
import userFetcher from "../libs/api-user";

export default function useUser(){
    const {data, mutate, error} = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/login/me`, userFetcher);
    const loading = !data && !error;
    const loggedOut = error && error.status === 401

    return{
        loading,
        loggedOut,
        user: data,
        mutate
    };
}