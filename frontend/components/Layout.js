import Navbar from "./navbar";
import Footer from "./Footer";

const Layout = ({children}) => {
    return (
        <div className='container'>
            <div className='content'>
                <Navbar />
                {children}
            </div>
            <Footer />
        </div>
    );
}
 
export default Layout;
