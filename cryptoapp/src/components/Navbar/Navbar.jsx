import React from 'react'
import style from '../Navbar/Navbar.module.css'
const Navbar = () => {
  return (
    <>
    <div className={style.navbar_wrapper}>
        <div className={style.navbar_left}>
            <div className={style.navabr_left_header}>
                CryptoDeck
            </div>
        </div>
        <div className={style.navbar_right}>
            <ul className= {style.navbar_navigate}>
                <li>
                    <a href="">
                        Portfolio
                    </a>
                </li>
                <li>
                    <a href="">
                        Watchlists
                    </a>
                </li>
                <li>
                    <a href="">
                        Disconnect
                    </a>
                    </li>
                <li>
                    <a href="">
                        History
                    </a>
                </li>
                <li>
                    <a href="">
                        Transfer
                    </a>
                </li>
            </ul>
        </div>
    </div>
    </>
  )
}

export default Navbar