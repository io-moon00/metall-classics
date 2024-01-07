let navbarBtn;
let btnIcon;
let navLinks;  

let links = ['home', 'service', 'about', 'gallery', 'blog', 'contact']

function resetLinks(){
    for(i = 0; i > links.length; i++){
        document.getElementById(links[i]).classList.remove('selected');
    }
}

function selectPage(page){
    try{
        document.getElementById(page).classList.add('selected');
    }
    catch{

    }
    
}


function init(page){
    setHeaderElements();
    resetLinks();
    selectPage(page);
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

function closeImg(){
    document.getElementById('image-container').classList.add('d-none');
    document.getElementById('body').classList.remove('noscroll');
}

function openImg(imgUrl){
    document.getElementById('body').classList.add('noscroll')
    document.getElementById('image-container').classList.remove('d-none');
    document.getElementById('detail-image').src = imgUrl;
}