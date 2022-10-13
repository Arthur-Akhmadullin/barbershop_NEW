var overlay = document.querySelector(".modal-overlay");
var mapOpen = document.querySelector(".js-open-map");
var mapPopup = document.querySelector(".modal-content-map");
var mapClose = mapPopup.querySelector(".modal-content-close");
var mapFooter = document.querySelector(".footer-contacts");
var mapFooterOpen = mapFooter.querySelector("a");


mapOpen.addEventListener("click", function(event) {
    event.preventDefault();
    overlay.classList.add("modal-overlay-show");
    mapPopup.classList.add("modal-content-show");
});

mapClose.addEventListener("click", function(event) {
    event.preventDefault();
    overlay.classList.remove("modal-overlay-show");
    mapPopup.classList.remove("modal-content-show");
});

mapFooterOpen.addEventListener("click", function(event) {
    event.preventDefault();
    overlay.classList.add("modal-overlay-show");
    mapPopup.classList.add("modal-content-show");
});

window.addEventListener("keydown", function(event) {
    if (event.keyCode === 27) {
        if (mapPopup.classList.contains("modal-content-show")) {
            mapPopup.classList.remove("modal-content-show");
            overlay.classList.remove("modal-overlay-show");
        }
    }
});