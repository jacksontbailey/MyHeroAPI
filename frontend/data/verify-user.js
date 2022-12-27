import useSWR from "swr";
import { useRouter } from "next/router";
import apiVerify from "../libs/api-verify";

export default function verifyUser({email, token}) {
  const { data, error, revalidate } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/verification/verify?token=${token}&email=${email}`, apiVerify
  );

  const loading = !data && !error;
  const expiredToken = error === 404;
  const alreadyVerified = error === 409;

  return {
    loading,
    expiredToken,
    alreadyVerified,
    verified: data,
    revalidate,
  };
}