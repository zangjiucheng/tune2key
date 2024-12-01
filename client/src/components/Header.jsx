
import logo from '../images/logo.png'
import './Header.css'
import {useNavigate}     from 'react-router-dom'
const Header = () => {
    const navigate = useNavigate()
    
    return <>
        <img src={logo} alt="" className='logo' onClick={() => navigate('/')}/>
    </>
}
export default Header