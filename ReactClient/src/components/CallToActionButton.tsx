function CallToActionButton() {

  const handleClick = () =>{
    console.log("yeah man!");
  }

  return (
    <div className="flex justify-center items-center h-screen">
        <button 
          className="bg-green-500 text-white font-bold py-2 px-4 rounded hover:bg-red-700"
          onClick = {handleClick}
          >
            Start monitoring
        </button>
    </div>
  )
}

export default CallToActionButton;