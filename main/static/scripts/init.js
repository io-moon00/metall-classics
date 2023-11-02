let navbarBtn;
let btnIcon;
let navLinks;  


function init(){
    setHeaderElements();
}

function setHeaderElements(){
    navbarBtn = document.getElementById('navbar-btn');
    btnIcon = document.getElementById('btn-icon');
    navLinks = document.querySelectorAll('.nav-links')[0];
}

function toggleNavbar() {
    btnIcon.classList.toggle('open');
    navLinks.classList.toggle('open');
    document.getElementById('body').classList.toggle('no-scroll');
}

// the navigation menu disappears when clicked, except when a link is clicked
document.onclick = function (e) {
    if (e.target !== navbarBtn && e.target !== navLinks && e.target !== btnIcon) {
        btnIcon.classList.remove('open');
        navLinks.classList.remove('open');
        document.getElementById('body').classList.remove('no-scroll');
    }
}