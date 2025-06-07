

function Getmore() {
    const handleClick = () =>{
        console.log("yeah man!");
    }
    
    return (
        <div className="w-[100%] flex justify-center items-center">
            <button 
            className="bg-yellow-500 text-white font-bold py-2 px-4 rounded hover:bg-yellow-700"
            onClick = {handleClick}
            >
                Get a cloud solution
            </button>
        </div>
    )
}

export default Getmore