import Link from "next/link";

const NotFound = () => {

    return (
        <div className="not-found">
            <h1>Oooooops...</h1>
            <p>That page cannot be found. <br />
            Go back to the <Link href='/'>Homepage</Link>.
            </p>
        </div>
    );
}
 
export default NotFound