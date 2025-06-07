

function Home() {
    const handleClick = () =>{
        console.log("yeah man!");
    }
    
    return (
        <div className="w-[100%] flex justify-center items-center">
            <button 
            className="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700"
            onClick = {handleClick}
            >
                Welcome Home
            </button>
        </div>
    )
}

export default Home