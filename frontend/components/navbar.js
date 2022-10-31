import Link from "next/link";
const Navbar = () => {
    return ( 
        <nav>
            <div className="logo">
                <p>MHA API</p>
            </div>
            <Link href='/'><a>Home</a></Link>
            <Link href='/about'><a>About</a></Link>
            <Link href='/v1'><a>API Data</a></Link>
            
        </nav>
    );
}
 
export default Navbar;