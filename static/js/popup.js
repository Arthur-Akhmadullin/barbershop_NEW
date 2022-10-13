var link = document.querySelector(".login");
var popup = document.querySelector(".modal-content");
var overlay = document.querySelector(".modal-overlay");
var close = popup.querySelector(".modal-content-close");
var form = popup.querySelector("form");
var login = popup.querySelector("[name=username]");
var password = popup.querySelector("[name=password]");
var storage = localStorage.getItem("login");


link.addEventListener("click", function(event) {
    event.preventDefault();
    overlay.classList.add("modal-overlay-show");
    popup.classList.add("modal-content-show");
    if (storage) {
        login.value = storage;
        password.focus();
    } 
    else {
        login.focus();
    }
});

close.addEventListener("click", function(event) {
    event.preventDefault();
    overlay.classList.remove("modal-overlay-show");
    popup.classList.remove("modal-content-show");    
    popup.classList.remove("modal-error");    
});

form.addEventListener("submit", function(event) {
    if (!login.value || !password.value) {
        event.preventDefault();
        popup.classList.add("modal-error");
		login.required = true;
		password.required=true;
    } 
    else {
        localStorage.setItem("login", login.value);
    }
});

window.addEventListener("keydown", function(event) {
    if (event.keyCode === 27) {
        if (popup.classList.contains("modal-content-show")) {
            popup.classList.remove("modal-content-show");
            popup.classList.remove("modal-error");
            overlay.classList.remove("modal-overlay-show");
        }
    }
});