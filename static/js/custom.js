/**
 * Custom JS
 */

'use strict';


/*** Preloader ***/

var preloader = (function() {

    // Variables
    var $window = $(window);
    var loader = $("#loader-wrapper");

    // Methods
    $window.on({
        'load': function() {

            loader.fadeOut();

        }
    });

    // Events

})();

/*** Popular
/*** Button to top page ***/

var toTopButton = (function() {

    // Variables
    var topButton = $('#back-to-top');
    var scrollTop = $(window).scrollTop();
    var isActive = false;
    if (scrollTop > 100) {
        isActive = true;
    }

    // Methods

    // Events
    $(window).scroll(function() {
        scrollTop = $(window).scrollTop();

        if (scrollTop > 100 && !isActive) {
            isActive = true;
            topButton.fadeIn();
        } else if (scrollTop <= 100 && isActive) {
            isActive = false;
            topButton.fadeOut();
        }

    });

})();


/*** Alerts ***/

var alert = (function() {
    // Config
    // ======

    var alertLifetime = 6000;

    // Methods
    // =======

    var generate = function(type, message) {
        var newAlert = $(
            '<div class="alert alert-' +
                type +
                ' fade in" id="page-alert">' +
                message +
                "</div>"
        );

        // Append new alert
        $("body").append(newAlert);

        // Remove new alert
        setTimeout(function() {
            newAlert.alert("close");
        }, alertLifetime);
    };
})();


/*** Newsletter ***/
/*** Reservation ***/
/*** Home parallax ***/

var parallax = (function() {

    // Variables
    var elem = $(".section_welcome");
    var elemHeight = elem.height();
    var parallaxRate = 2;

    // Methods
    $(window).scroll(function() {

        var scrollTop = $(window).scrollTop(),
            elementOffsetTop = scrollTop,
            parallaxOffset = elementOffsetTop / parallaxRate;

        if (elementOffsetTop <= elemHeight) {
            $(".welcome-parallax_bg").css({
                "-webkit-transform": "translateY(" + parallaxOffset + "px)",
                        "transform": "translateY(" + parallaxOffset + "px)"
            });
        }

    });

    // Events

})();


/*** Smooth scroll to anchor ***/

var smoothScroll = (function() {

    // Variables
    var link = $('a[href^="#section_"]');
    var duration = 1000;

    // Methods
    function scrollTo(link) {
        var target = $(link.attr('href'));
        var navbar = $('.navbar');
        var navbarHeight = navbar.outerHeight();

        if ( target.length ) {
            $('html, body').animate({
                scrollTop: target.offset().top - navbarHeight + 50
            }, duration);
        }
    }

    // Events
    link.on('click', function(e) {
        e.preventDefault();
        scrollTo( $(this) );
    });

})();

/*** Navbar ***/

var navbar = (function() {

    // Variables
    var scrollTop = $(window).scrollTop();
    var navbar = $('.navbar');
    var navbarLinks = $('[href*="#section_"]');
    var navbarDefault = $(".navbar-default");
    var navbarCollapse = $(".navbar-collapse");

    // Methods
    function makeInverse() {
        navbar.removeClass('navbar-default').addClass('navbar-inverse');
    }
    function makeDefault() {
        navbar.removeClass('navbar-inverse').addClass('navbar-default');
    }

    // Events

    // Toggle navbar on page load if needed
    if (scrollTop > 0) {
        makeInverse();
    }

    // Toggle navbar on scroll
    $(window).scroll(function() {
        scrollTop = $(window).scrollTop();

        if (scrollTop > 0 && $('.navbar-default').length) {
            makeInverse();
        } else if (scrollTop === 0) {
            makeDefault();
        }

    });

    // Toggle navbar on collapse
    navbarCollapse.on({
        'show.bs.collapse': function() {
            makeInverse();
        },
        'hidden.bs.collapse': function() {
            scrollTop = $(window).scrollTop();

            if (scrollTop === 0) {
                makeDefault();
            }
        }
    });

    // Close collapsed navbar on click
    navbarLinks.on('click', function() {
        navbarCollapse.collapse('hide');
    });

})();


/*** Mobile hover ***/

var mobileHover = (function() {

    // Variables
    var item = $('.menu__item_hover, .events, .events__item');

    // Methods
    function trigger(elem) {
        elem.trigger('hover');
    }

    // Events
    item.on({
        'touchstart': function() {
            trigger( $(this) );
        },
        'touchend': function() {
            trigger( $(this) );
        }
    });

})();


/*** Gallery ***/

var gallery = (function() {

    // Variables
    var gallery = $('.gallery__grid');
    var galleryItemSelector = '.gallery__item';
    var grid;

    // Methods
    function initGallery() {
        grid = gallery.isotope({
            itemSelector: galleryItemSelector
        });
        grid.imagesLoaded().progress( function() {
            grid.isotope('layout');
        });
    };

    // Init menu
    initGallery();

})();
/*** Hero Carousel ***/
$('.carousel').carousel()
/*** Popular Services Carousel ***/
$(document).ready(function() {
  $('#owl-carousel').owlCarousel({
    nav: false,
    items: 1,
    loop  : true,
    dots: false,
    autoHeight : true,
    stagePadding: 0.2,
    mouseDrag: true,
    animateIn: true,
    fallbackEasing: 'swing',
    responsiveClass: true,
    responsive: {
        768:{
          items: 3
        },
        1000:{
          items: 4
        },
        1400:{
          items: 6
        }
    }
  });

});
/*** Testimonials Carousel ***/
$(document).ready(function() {
  $('#owl-carousel-testim').owlCarousel({
      stagePadding: 300,
      items: 1,
      nav: false,
      navText: ["<i class='las la-chevron-left'></i>","<i class='las la-chevron-right'></i>"],
      loop: true,
      dots: false,
      lazyLoad: true,
      autoplay: true,
      autoplaySpeed: 2000,
      autoplayTimeout: 4000,
      autoplayHoverPause: true,
      responsive:{
        0:{
            items:1,
        },
        500:{
            items:1,
        },
        768:{
            items:1,
            loop:true
        }
    }
  })
});
/*** Menu ***/
var menu = (function() {

    // Variables
    var $menu = $(".menu__grid, .menu__text-grid").isotope({
        itemSelector: ".menu__item",
        layoutMode: "masonry"
    });

    // Set ititial filtering
    $menu.imagesLoaded().progress( function() {
        $menu.isotope({ filter: "paine-cu-maia" });
    });

    // Filter items on click
    $(".menu_nav").on('click', 'a', function(e) {
        var elem = $(this);

        // Filter items
        var filterValue = elem.attr('data-filter');
        $menu.isotope({ filter: filterValue });

        // Change active button
        elem.parents("li").addClass("active").siblings("li").removeClass("active");

        e.preventDefault();
    });

})();
// =============== switch theme colors ========================= //
const setTheme = theme => document.documentElement.className = theme;
document.getElementById('theme-select').addEventListener('change', function() {
  setTheme(this.value);
});
// =================filterSelection("all") ================== //
function filterSelection(c) {
 var x, i;
 x = document.getElementsByClassName("filterElements");
 if (c == "all") c = "";
 for (i = 0; i < x.length; i++) {
   w3RemoveClass(x[i], "show");
   if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
 }
}

function w3AddClass(element, name) {
 var i, arr1, arr2;
 arr1 = element.className.split(" ");
 arr2 = name.split(" ");
 for (i = 0; i < arr2.length; i++) {
   if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
 }
}

function w3RemoveClass(element, name) {
 var i, arr1, arr2;
 arr1 = element.className.split(" ");
 arr2 = name.split(" ");
 for (i = 0; i < arr2.length; i++) {
   while (arr1.indexOf(arr2[i]) > -1) {
     arr1.splice(arr1.indexOf(arr2[i]), 1);
   }
 }
 element.className = arr1.join(" ");
}

// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
 btns[i].addEventListener("click", function(){
   var current = document.getElementsByClassName("active");
   current[0].className = current[0].className.replace(" active", "");
   this.className += " active";
 });
}
