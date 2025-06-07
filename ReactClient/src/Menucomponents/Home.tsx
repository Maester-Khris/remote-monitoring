import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";

import appFullLogo from '../assets/rx_monitor.png'

function Home() {
    return (
        <div className="w-full h-full border flex justify-center items-center">
            <Carousel className="" showArrows={true} autoPlay interval={5000} transitionTime={5000}  infiniteLoop> 
                <div><img src={appFullLogo} className="max-h-[500px] object-contain mx-auto" /></div>
                <div><img src={appFullLogo} className="max-h-[500px] object-contain mx-auto" /></div>
            </Carousel>
        </div>
    )
}

export default Home
{/* <Swiper slidesPerView={1} loop>
    <SwiperSlide><img src={appFullLogo} /></SwiperSlide>
    <SwiperSlide><img src={appFullLogo} /></SwiperSlide>
</Swiper> */}