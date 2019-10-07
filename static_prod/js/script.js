/*JS way for setting height: 100vh to slides' height*/
/*const $slides = $(".owl-carousel .owl-slide");
$slides.css("height", $(window).height());
$(window).resize(() => {
  $slides.css("height", $(window).height());
});*/

$(".owl-carousel").on("initialized.owl.carousel", () => {
    setTimeout(() => {
        $(".owl-item.active .owl-slide-animated").addClass("is-transitioned");
        $("section").show();
    }, 200);
});


const $owlCarousel = $(".owl-carousel").owlCarousel({
    items: 1,
    // loop: true,
    // nav: true,
    navText: [
        '<svg width="50" height="50" viewBox="0 0 24 24"><path d="M16.67 0l2.83 2.829-9.339 9.175 9.339 9.167-2.83 2.829-12.17-11.996z"/></svg>',
        '<svg width="50" height="50" viewBox="0 0 24 24"><path d="M5 3l3.057-3 11.943 12-11.943 12-3.057-3 9-9z"/></svg>' /* icons from https://iconmonstr.com */
    ]
});

$owlCarousel.on("changed.owl.carousel", e => {
    $(".owl-slide-animated").removeClass("is-transitioned");

    const $currentOwlItem = $(".owl-item").eq(e.item.index);
    $currentOwlItem.find(".owl-slide-animated").addClass("is-transitioned");

    const $target = $currentOwlItem.find(".owl-slide-text");
    doDotsCalculations($target);
});

$owlCarousel.on("resize.owl.carousel", () => {
    setTimeout(() => {
        setOwlDotsPosition();
    }, 50);
});

/*if there isn't content underneath the carousel*/
//$owlCarousel.trigger("refresh.owl.carousel");

setOwlDotsPosition();

function setOwlDotsPosition() {
    const $target = $(".owl-item.active .owl-slide-text");
    doDotsCalculations($target);
}

function doDotsCalculations(el) {
    const height = el.height();
    const {top, left} = el.position();
    const res = height + top + 20;

    $(".owl-carousel .owl-dots").css({
        top: `${res}px`,
        left: `${left}px`
    });
}


function myAccFunc(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

$(".carusel").owlCarousel({});


// SLIDE SHOW

var slideIndex = 1;
showSlides(slideIndex, 'mySlides');
// showSlides(slideIndex, 'partner');
// showSlides(slideIndex, 'chlen');

function plusSlides(n, myclass) {
    showSlides(slideIndex += n, myclass);
}

function currentSlide(n, myclass) {
    showSlides(slideIndex = n, myclass);
}

function showSlides(n, myclass) {
    var i;
    var slides = document.getElementsByClassName(myclass);
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}


// search form js
// Open the full screen search box
function openOverlay(id) {
    document.getElementById(id).style.display = "block";
}

// Close the full screen search box
function closeOverlay(id) {
    document.getElementById(id).style.display = "none";
}


function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();


// slider
// ...тут будет вызываться наш плагин
$('.slide-content').myCarousel({
    btnNext: '.next',
    btnPrev: '.prev',
    visible: 5,
    rotateBy: 2,
    auto: 2500,
});
