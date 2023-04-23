import useSWR from "swr";
import { getCookie } from "cookies-next";
import userFetcher from "../libs/api-user";

export default function useUser(){
    const {data, mutate, error, revalidate} = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/login/me`, userFetcher);
    const loading = !data && !error;
    const loggedOut = error && error.status === 401

    // Retrieve token from cookie
    const token = getCookie("token");

    return {
        loading,
        loggedOut,
        user: {
            ...data,
            token,
        },
        mutate,
        revalidate,
    };
}