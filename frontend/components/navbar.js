import Link from "next/link";
import { AuthContext } from "../pages/_app";
import { useContext } from "react";

const Navbar = () => {
    const { user } = useContext(AuthContext);

    return ( 
        <nav>
            <div className="logo">
                <p>MHA API</p>
            </div>
            <div className="links">
                <Link href='/'>Home</Link>
                <Link href='/about'>About</Link>
                <Link href='/v1'>API Data</Link>
                {user && (
                    <Link href='/apis'>My Keys</Link>
                )}
            </div>
        </nav>
    );
}
 
export default Navbar;