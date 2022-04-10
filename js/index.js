var slidePosition = 0;
    var sNO=0;
    SlideShow(slidePosition);

function plusSlides(arg){
    SlideShow(slidePosition+=arg)
}
function SlideShow(sNO) {
  var i;
  var slides = document.getElementsByClassName("content");
  if (sNO > slides.length) {slidePosition = 1}
  if (sNO<1){slidePosition=slides.length}

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }  

  slides[slidePosition-1].style.display = 'flex';
}
  // Change image every 2 seconds
  function slideAuto() {
      var slide=document.getElementsByClassName("content");
      for (let i = 0; i < slide.length; i++) {
          slide[i].style.display='none';          
      }
      slidePosition++;
      if (slidePosition>slide.length){slidePosition=1}
      
      slide[slidePosition-1].style.display="flex";    
      console.log("Auto-moved slide")  
  }
  setTimeout(slideAuto(),2);
