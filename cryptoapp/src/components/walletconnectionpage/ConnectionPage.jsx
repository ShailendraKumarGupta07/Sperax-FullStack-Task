import React ,{useState} from 'react'
import style from '../walletconnectionpage/connectionpage.module.css'
import {FaArrowDown} from 'react-icons/fa'
import { ethers } from "ethers";



const ConnectionPage = () =>{

  const [walletAddress, setWalletAddress] = useState("");

  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
        setWalletAddress(accounts[0]);
        console.log("Wallet connected:", accounts[0]);

        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        const signer = provider.getSigner();
      } catch (error) {
        console.error("Error connecting wallet:", error);
      }
    } else {
      alert("MetaMask not detected. Please install MetaMask.");
    }
  };

  return (
    <>
    <div className={style.contentwrapper}>
      <div className={style.connect}>
        <div className={style.box1}>Welcome to CryptoDeck!!</div>
        <div className={style.box2}>Connect a wallet and we will automatically track your portfolio and transactions</div>
        <div className={style.box3}>
          <button className={style.metamask} onClick={connectWallet}>{walletAddress ? `Successfully Connected` : "Connect Wallet"}</button>
        </div>
        <div className={style.box5}>Or paste your wallet address below <FaArrowDown></FaArrowDown> </div>
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