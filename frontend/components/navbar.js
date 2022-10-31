import Link from "next/link";
const Navbar = () => {
    return ( 
        <nav>
            <div className="logo">
                <p>MHA API</p>
            </div>
            <Link href='/'>Home</Link>
            <Link href='/about'>About</Link>
            <Link href='/v1'>API Data</Link>
        </nav>
    );
}
 
export default Navbar;