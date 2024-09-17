import React from 'react'
import DatePicker from "react-datepicker";
import style from '../Dashboard Page/DashboardPage.module.css'

const DashboardPage = () => {
  return (
    <>
    <div className={style.dashbaord_wrapper}>
        <div className={style.left}>
            <div className={style.left_header}>
                Your Portfolio
            </div>
            <div className={style.balances}>
                <div className={style.balance}>
                    <div className={style.b1}>Balance</div>
                    <div className={style.b2}>$2000</div>
                    <div className={style.b3}>+0.00%</div>
                </div>
                <div className={style.p_l}>
                    <div className={style.p_l_1}>Profit/Loss</div>
                    <div className={style.p_l_2}>$0.00</div>
                    <div className={style.p_l_3}>+0.00</div>
                </div>
            </div>
            <div className={style.current_list}></div>
        </div>
        <divv className={style.right}>
            <div className={style.watchlist}>
                <div className={style.header}></div>
                <div className={style.list}></div>
            </div>
        </divv>
    </div>
    </>
  )
}

export default DashboardPage