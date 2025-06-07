

function Getmore() {
    const handleClick = () => {
        console.log("yeah man!");
    }

    return (
        <div className="w-[100%] flex justify-center items-center p-4 gap-4">
            <div className="w-[70%] md:w-[75%] p-4 flex h-full rounded-lg shadow-lg shadow-lg bg-[url(/monitoring.png)] bg-no-repeat bg-cover bg-left bg-[length:20%] bg-[position:-300px_0]">
            </div>
            <div className="w-[30%] md:w-[75%] p-4 flex flex-col h-full rounded-lg shadow-lg bg-[#E5E4E2] ">
            <div className="max-w-md mx-auto ">
                    <h2 className="text-2xl font-semibold text-gray-800">Contact Us</h2>
                    <form className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-600 mb-1">Name</label>
                            <input
                                type="text"
                                className="w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400 shadow-sm"
                                placeholder="Your name"
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-600 mb-1">Email</label>
                            <input
                                type="email"
                                className="w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400 shadow-sm"
                                placeholder="you@example.com"
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-600 mb-1">Message</label>
                            <textarea
                                rows={4}
                                className="w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400 shadow-sm"
                                placeholder="Write your message..."
                            ></textarea>
                        </div>

                        <button
                            type="submit"
                            className="w-full py-2 px-4 bg-blue-500 text-white font-semibold rounded-xl shadow-md hover:bg-blue-600 transition"
                        >
                            Send
                        </button>
                    </form>
                </div>
            </div>
        </div>


        // <div className="relative w-full flex justify-start items-center p-4">
        //     <div className="w-[70%] md:w-[50%] p-4 h-full rounded-lg shadow-lg bg-[url(/monitoring.png)] bg-no-repeat bg-cover bg-left bg-[length:20%] bg-[position:-300px_0]">
        //     </div>

            
        //     <div className="absolute top-[20%] left-[50%] translate-x-[-20%] translate-y-[-20%] w-[300px] md:w-[400px] p-6 rounded-2xl shadow-xl bg-amber-100">
                
                
        //         <div className="max-w-md mx-auto p-6 space-y-6">
        //             <h2 className="text-2xl font-semibold text-gray-800">Contact Us</h2>
        //             <form className="space-y-4">
        //                 <div>
        //                     <label className="block text-sm font-medium text-gray-600 mb-1">Name</label>
        //                     <input
        //                         type="text"
        //                         className="w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400 shadow-sm"
        //                         placeholder="Your name"
        //                     />
        //                 </div>

        //                 <div>
        //                     <label className="block text-sm font-medium text-gray-600 mb-1">Email</label>
        //                     <input
        //                         type="email"
        //                         className="w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400 shadow-sm"
        //                         placeholder="you@example.com"
        //                     />
        //                 </div>

        //                 <div>
        //                     <label className="block text-sm font-medium text-gray-600 mb-1">Message</label>
        //                     <textarea
        //                         rows={4}
        //                         className="w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400 shadow-sm"
        //                         placeholder="Write your message..."
        //                     ></textarea>
        //                 </div>

        //                 <button
        //                     type="submit"
        //                     className="w-full py-2 px-4 bg-blue-500 text-white font-semibold rounded-xl shadow-md hover:bg-blue-600 transition"
        //                 >
        //                     Send
        //                 </button>
        //             </form>
        //         </div>
        //     </div>
        // </div>

    )
}

export default Getmore