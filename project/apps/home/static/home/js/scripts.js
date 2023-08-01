/*!
* Start Bootstrap - Small Business v5.0.6 (https://startbootstrap.com/template/small-business)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-small-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

let HideText_btn= document.getElementById('HideText_btn');

let HideText= document.getElementById('HideText');

HideText_btn.addEventListener('click', toggleText)

function toggleText() {
    HideText.classList.toggle('visible');

    if (HideText.classList.contains("visible")) {
        HideText_btn.innerHTML= "menos detalles";
    }
    else {
        detalles
    }
}