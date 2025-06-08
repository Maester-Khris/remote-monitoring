// import { Carousel } from "react-responsive-carousel";
// import "react-responsive-carousel/lib/styles/carousel.min.css";
import Slider from "react-slick";
import appFullLogo from '../assets/rx_monitor.png'
import DjangoBackgr from '../assets/django_background.jpg'
import ReactBackgr from '../assets/react_back.png'
import DjangoReactBackgr from '../assets/react_django.png'

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

function Home() {
    var settings = {
        dots: true,
        infinite: true,
        speed: 500,
        autoplay: true,
        autoplaySpeed: 4000,
        arrow: true,
        slidesToShow: 1,
        slidesToScroll: 1,
    };
    return (
        <div className="w-full h-full max-h-[820px] rounded-[10px]">
            <Slider className="h-[95%]" {...settings}>
                {[ReactBackgr, DjangoBackgr, DjangoReactBackgr].map((imgPath, index) => (
                    <div key={index} className="h-full flex items-center justify-center">
                        <img src={imgPath} className="w-full h-full scale-80 transform" />
                    </div>
                ))}
            </Slider>
        </div>
    )
}

export default Home
{/* <Swiper slidesPerView={1} loop>
    <SwiperSlide><img src={appFullLogo} /></SwiperSlide>
    <SwiperSlide><img src={appFullLogo} /></SwiperSlide>
</Swiper> */}
{/* <Carousel className="" showArrows={true} autoPlay interval={5000} transitionTime={5000}  infiniteLoop> 
<div><img src={appFullLogo} className="max-h-[500px] object-contain mx-auto" /></div>
<div><img src={appFullLogo} className="max-h-[500px] object-contain mx-auto" /></div>
</Carousel> */}
{/* <div className="h-[90%] border-2 border-amber-50">
    <h3 className=" font-bold text-amber-50">1</h3>
</div> */}