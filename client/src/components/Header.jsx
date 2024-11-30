
import logo from '../images/logo.png'
import './Header.css'
const Header = () => {

    
    return <>
        <img src={logo} alt="" className='logo' onClick={() => window.location.href='/'}/>
    </>
}
export default Header