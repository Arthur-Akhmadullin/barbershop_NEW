var gallery = document.querySelector(".gallery");
var btnLeft = gallery.querySelector(".btn-gallery-prev")
var btnRight = gallery.querySelector(".btn-gallery-next");
var gallery_content = gallery.querySelector(".gallery-content")
var slides = gallery_content.querySelectorAll("img");
var i = 0;
 
btnRight.addEventListener("click", function () {
	++i;	
	
	if (i === slides.length-1) {
		btnRight.disabled = true;		
	} 
	// Добавляем предыдущему слайду свойство "display: none;"	
	slides[i-1].classList.add("gallery-img-none");
	// Удаляем у текущего слайда свойство "display: none;"
	slides[i].classList.remove("gallery-img-none");
	btnLeft.disabled = false;   
})

btnLeft.addEventListener("click", function () {
	--i;
    
    if (i === 0) {
		btnLeft.disabled = true;
	}
	slides[i+1].classList.add("gallery-img-none");	
	slides[i].classList.remove("gallery-img-none");
    btnRight.disabled = false;
})