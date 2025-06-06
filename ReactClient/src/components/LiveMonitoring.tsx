import { useState } from 'react'
import { List, X, MagnifyingGlass } from "@phosphor-icons/react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer} from 'recharts';

function LiveMonitoring() {
    const liStyle = "px-1 py-1"
    const [isOpen, setIsOpen] = useState(true);

    const [searchTerm, setSearchTerm] = useState('');
    const handleInputChange = (event:any) => {
      setSearchTerm(event.target.value);
      console.log("Current search term:", event.target.value);
    };

    const data = [
      { name: 'Page A', uv: 420, pv: 2400, amt: 2450 },
      { name: 'Page B', uv: 380, pv: 2750, amt: 2600 },
      { name: 'Page C', uv: 500, pv: 2300, amt: 2900 },
      { name: 'Page D', uv: 450, pv: 3100, amt: 2700 },
      { name: 'Page E', uv: 520, pv: 2900, amt: 3000 },
      { name: 'Page F', uv: 410, pv: 3250, amt: 2800 }
    ];
    
    return (
      <div className="flex h-full w-full text-base font-bold">
        {/* rest of the page content  */}
        <div className={`bg-gray-800 text-white relative  ${isOpen ? "w-40" : "w-34"} 
          transition-all duration-300 ease-in-out overflow-hidden`} style={{border:"1px solid black"}}>
            <div className="p-4 text-lg font-bold border-gray-700">
              <button onClick={() => setIsOpen(!isOpen)}
                  className={`mb-2 p-1.5 border bg-transparent rounded absolute top-2 ${isOpen ? "border-red-500 text-red-500 right-2" : "border-blue-500 text-blue-500 left-2"}`}>
                {isOpen ? <X  weight="bold" size={20} />: <List  weight="bold" size={20} />}
              </button>
            </div>
          <ul className="mt-10 p-2 space-y-4">
            <li className={liStyle}><a href="#" className="hover:text-gray-300">Django </a></li>
            <li className={liStyle}><a href="#" className="hover:text-gray-300">Laravel</a></li>
            <li className={liStyle}><a href="#" className="hover:text-gray-300">Spring</a></li>
            <li className={liStyle}><a href="#" className="hover:text-gray-300">EC2 instance</a></li>
          </ul>
        </div>  

        {/* rest of the page content  */}
        <div className="monitor flex-1 bg-gray-100 p-6 flex flex-col">
          <div>
            <h1 className="text-2xl text-black font-bold">System Performance monitoring</h1>
            <p className="mt-0 text-gray-700">Take a look at your system key metrics and logs in real-time.</p>
          </div>
          <div className='mt-5 flex-1 flex w-full gap-4 bg-gray-100'>
            <div className="w-[70%] h-full rounded-lg p-4 shadow-lg bg-[#E5E4E2] flex justify-between">
              <div>
                <h2 className="text-xl font-bold mb-2">Log tracker</h2>
              </div>
              <div>
                  <div className="relative flex items-center w-full max-w-sm">
                    {/* Input Field */}
                    <input
                        type="text"
                        placeholder="Search..."
                        value={searchTerm}
                        onChange={handleInputChange}
                        className="bg-white block w-full py-2 pl-10 pr-3 border border-gray-300 rounded-md shadow-sm
                          focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent
                          text-gray-900 placeholder-gray-500 text-sm leading-6
                          transition-all duration-200 ease-in-out"
                      />

                    {/* Search Icon */}
                    <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <MagnifyingGlass  weight="bold" size={18} />
                    </div>
                  </div>
              </div>
            </div>
            <div className="w-[30%] h-full rounded-lg p-4 shadow-lg bg-[#E5E4E2] flex flex-col">
              <div className='mb-2'>
                <h2 className="text-xl font-bold mb-2">System metrics</h2>
              </div>
              <div className="mt-3">
                <ResponsiveContainer width="100%" height={200}>
                  <LineChart data={data} margin={{ top: 0, right: 0, left: -10, bottom: 5 }}>
                    <Tooltip />
                    <Legend /> 
                    <Line type="monotone" dataKey="uv" stroke="#8884d8" />
                    <Line type="monotone" dataKey="pv" stroke="#82ca9d" />
                    <CartesianGrid stroke="#ccc" strokeDasharray="3 3" />
                    <XAxis dataKey="name" interval={0}/>
                    <YAxis />
                  </LineChart>
                </ResponsiveContainer>
              </div>
              <div className="mt-6">
                <ResponsiveContainer width="100%" height={200}>
                  <LineChart data={data} margin={{ top: 0, right: 0, left: -10, bottom: 5 }}>
                    <Tooltip />
                    <Legend /> 
                    <Line type="monotone" dataKey="uv" stroke="#8884d8" />
                    <Line type="monotone" dataKey="pv" stroke="#82ca9d" />
                    <CartesianGrid stroke="#ccc" strokeDasharray="3 3" />
                    <XAxis dataKey="name" interval={0}/>
                    <YAxis />
                  </LineChart>
                </ResponsiveContainer>
              </div>
              <div className='system-key-metrics mt-8 flex gap-4'>
                <div className="w-50% bg-white shadow-md rounded-lg p-4 w-full max-w-sm">
                  <div className="flex items-start justify-between gap-1">
                    <div className="flex flex-col text-gray-800">
                      <div className="text-xl mb-1">
                        <MagnifyingGlass weight="bold" size={48} />
                      </div>
                      <div className="text-4xl font-bold">
                        1,234
                      </div>
                    </div>
                    <div className="text-right text-sm self-center text-gray-500 w-1/2 break-words">
                      Pageviews cumulative count for the last 24 hours
                    </div>
                  </div>
                </div>
                <div className="w-50% bg-white shadow-md rounded-lg p-4 w-full max-w-sm">
                  <div className="flex items-start justify-between gap-1">
                  <div className="text-left text-sm self-center text-gray-500 w-1/2 break-words">
                      Pageviews cumulative count for the last 24 hours
                    </div>
                    <div className="flex flex-col items-end text-gray-800">
                      <div className="text-xl mb-1">
                        <MagnifyingGlass className="scale-x-[-1]" weight="bold" size={48} />
                      </div>
                      <div className="text-4xl font-bold">
                        1,234
                      </div>
                    </div>
                    
                  </div>
                </div>
                </div>
              </div>
              </div>
            </div>
          </div>
    )
}

export default LiveMonitoring

// <button 
//   className="bg-green-500 text-white font-bold py-2 px-4 rounded hover:bg-green-700"
//   onClick = {handleClick}
//   >
//     Start monitoring your system
// </button>