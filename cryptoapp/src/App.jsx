import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ConnectionPage from './components/walletconnectionpage/ConnectionPage'
import DashboardPage from './components/Dashboard Page/DashboardPage'
import Navbar from './components/Navbar/Navbar'

function App() {
  return (
    <>
    {/* <ConnectionPage></ConnectionPage> */}
    <DashboardPage></DashboardPage>
    {/* <Navbar></Navbar> */}
    </>
  )
}

export default App
