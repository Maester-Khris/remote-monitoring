import React from 'react'

function LiveMonitoring() {
    const handleClick = () =>{
        console.log("yeah man!");
    }
    
    return (
        <button 
          className="bg-green-500 text-white font-bold py-2 px-4 rounded hover:bg-green-700"
          onClick = {handleClick}
          >
            Start monitoring your system
        </button>
    )
}

export default LiveMonitoring