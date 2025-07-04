import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom'

import './App.css'
// import reactLogo from './assets/react.svg'
import appLogo from './assets/rx_monitor_brand.png'
import Home from './Menucomponents/Home'
import LiveMonitoring from './Menucomponents/LiveMonitoring'
import Getmore from './Menucomponents/Getmore'


function App() {
  return (
    <BrowserRouter>
      <main className='mb-2'>
        <header className='main-content'>
          <div className='header-content'>
            <div className='header-content-left'>
              <img className='header-app-logo' src={appLogo} alt="" />
              <div className='header-app'>
                <h3 className='header-appname'>Welcome to Rx Monitor</h3>
                <p>Your solution to remote system monitoring</p>
              </div>
            </div>
            <div className='header-content-right'>
              <div className='header-menu'>
                <li><NavLink to="/" className={({ isActive }) => isActive ? "active-link": ""}>Home</NavLink></li>
                <li><NavLink to="/monitoring" className={({isActive}) => isActive ? "active-link": ""}>Live tracking</NavLink></li>
                <li><NavLink to="/more" className={({isActive}) => isActive ? "active-link": ""}>Get more</NavLink></li>
              </div>
            </div>
          </div>
        </header>

        <section className='main-content section-hero-home'>
          <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/monitoring" element={<LiveMonitoring />}></Route>
            <Route path="/more" element={<Getmore />}></Route>
          </Routes>
        </section>
      </main>
    </BrowserRouter>
  )
}

export default App;