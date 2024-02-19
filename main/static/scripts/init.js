let navbarBtn;
let btnIcon;
let navLinks;  


function init(page){
    setHeaderElements();
    setActiveHeaderLinks(page);
    scrollNav();
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

function setActiveHeaderLinks(element){
    const links = document.querySelectorAll('nav .nav-links a');
    links.forEach(link => {
        link.classList.remove('selected');
        if(link.classList.contains(element)){
            link.classList.add('selected')
        }
    })
}

function removeAllActiveClasses(){
    const links = document.querySelectorAll('nav .nav-links a');
    links.forEach(link => {
        link.classList.remove('selected');
    })
}

function scrollNav(){
    let current = '';
    const sections = document.querySelectorAll('.scroll-section');
    let noScrollHeight = 0;
    window.onreset = () =>{
        noScrollHeight = 0;
        const topSection = document.querySelectorAll('.no-scroll-section');
        topSection.forEach(sec => {
            noScrollHeight += sec.offsetHeight;
        })
    }

    const topSection = document.querySelectorAll('.no-scroll-section');
    topSection.forEach(sec => {
        noScrollHeight += sec.offsetHeight;
    })
  
    window.addEventListener('scroll', function(){
        sections.forEach(sec => {
            const sectionTop = sec.offsetTop;
            scroll = window.scrollY * 1.3
            if(scroll > sectionTop && scroll > noScrollHeight){
                current = sec.getAttribute('id');
                
            }
            else if(scroll < noScrollHeight){
                current = ''
            }
        })
        setActiveHeaderLinks(current);
    })
}