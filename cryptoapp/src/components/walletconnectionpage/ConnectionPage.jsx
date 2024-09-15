import React from 'react'
import style from '../walletconnectionpage/connectionpage.module.css'

const ConnectionPage = () =>{
  return (
    <>
    <div className={style.contentwrapper}>
      <div className={style.connect}>
        <div className={style.box1}>Welcome to CryptoDeck!!</div>
        <div className={style.box2}>Connect a wallet and we will automatically track your portfolio and transactions</div>
        <div className={style.box3}>
          <button className={style.metamask}>Connect Metamask</button>
        </div>
        <div className={style.box4}>
        <button className={style.wallet}>Connect any other wallets</button> {/*try to implemet a  list here */}
        </div>
        <div className={style.box5}>Or paste your wallet address below </div>
        <div className={style.box6}>
          <input type="text"  placeholder="Enter the address here"/>
        </div>
        <div className={style.box7}>
          <button className={style.connect_button}>Connect</button>
        </div>
      </div>
    </div>
    </>
  )
}

export default ConnectionPage