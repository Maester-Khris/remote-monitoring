import React from 'react'

function Getmore() {
    const handleClick = () =>{
        console.log("yeah man!");
    }
    
    return (
        <button 
          className="bg-yellow-500 text-white font-bold py-2 px-4 rounded hover:bg-yellow-700"
          onClick = {handleClick}
          >
            Get a cloud solution
        </button>
    )
}

export default Getmore