const slides = document.querySelectorAll('.slide')
slidesPlugin(getRandomInt(slides.length))

function getRandomInt(range) {
    return Math.floor(Math.random() * (range));
  }

function slidesPlugin (activeSlideNum=0) {

    slides[activeSlideNum].classList.add('active')
    for (const slide of slides){
        slide.addEventListener('click', () => {
            clearActiveClasses()
            slide.classList.add('active')
        })
    }

    function clearActiveClasses(){
        slides.forEach((slide) => {
            slide.classList.remove('active')
        })
    }
}