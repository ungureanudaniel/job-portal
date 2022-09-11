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
    var $gallery = $(".menu__grid, .menu__text-grid").isotope({
        itemSelector: ".menu__item",
        layoutMode: "masonry"
    });

    // Set ititial filtering

    $gallery.isotope({ filter: ".Interior" });
    // Filter items on click
    $(".menu_nav").on('click', 'a', function(e) {
        var elem = $(this);

        // Filter items
        var filterValue = elem.attr('data-filter');
        $gallery.isotope({ filter: filterValue });

        // Change active button
        elem.parents("li").addClass("active").siblings("li").removeClass("active");

        e.preventDefault();
    });

})();
/*** Dishes Carousel ***/

var dishes = (function() {

    // Variables
    var container = $('.dishes_carousel');

    // Methods
    function init() {
        container.flickity({
            cellAlign: 'center',
            initialIndex: 1,
            imagesLoaded: true,
            wrapAround: true,
            selectedAttraction: 0.01,
            friction: 0.15
        });
    }

    // Events
    if ( container.length ) {
        init();
    }

})();
/*** Menu ***/
var menu = (function() {

    // Variables
    var $menu = $(".menu__grid, .menu__text-grid").isotope({
        itemSelector: ".menu__item",
        layoutMode: "masonry"
    });

    // Set ititial filtering

    $menu.isotope({ filter: ".paine-cu-maia" });
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
// ======== Dropdown toggle ================
// $('.dropdown-toggle').dropdown()
$('nav li').hover(
  function() {
    $('ul',this).stop().slideDown(200);
  },
  function() {
    $('ul',this).stop().slideUp(200);
  }
);
// ------ Development buttons---------------
$(function () {

  /*** Dashboard Dropdown ***/
  $( ".dashboard-trigger" ).click(function() {
    $( '.dashboard-nav' ).toggleClass( "active" );
  });
  /*** Submenus ***/
  $( "#fr-trigger" ).click(function() {
    $( '#fr-trigger' ).toggleClass( "active-submenu" );
    if ($("#fr-trigger.active-submenu")[0]) {
      $( '#fr-trigger>a>i' ).removeClass( "ion-chevron-down" );
      $( '#fr-trigger>a>i' ).addClass( "ion-chevron-up" );
    } else {
      $( '#fr-trigger>a>i' ).addClass( "ion-chevron-down" );
      $( '#fr-trigger>a>i' ).removeClass( "ion-chevron-up" );
    }
  });
  $( "#ctr-trigger" ).click(function() {
    $( '#ctr-trigger' ).toggleClass( "active-submenu" );
    if ($("#ctr-trigger.active-submenu")[0]) {
      $( '#ctr-trigger>a>i' ).removeClass( "ion-chevron-down" );
      $( '#ctr-trigger>a>i' ).addClass( "ion-chevron-up" );
    } else {
      $( '#ctr-trigger>a>i' ).addClass( "ion-chevron-down" );
      $( '#ctr-trigger>a>i' ).removeClass( "ion-chevron-up" );
    }
  });
  /*** User Statistics timeframe dropdown ***/
  $( ".timeframe-trigger" ).click(function() {
    $( '.tmfr-dropdown' ).toggleClass( "open" );
  });

});
// Check when window size is below 992 in order to change styling on dashboard links

$(window).resize(function() {
  if ($(window).width() < 992) {
     $( '.dashboard-nav' ).addClass( "mobile" );
  }
 else {
    $( '.dashboard-nav' ).removeClass( "mobile" );
 }
});
