
'use strict';
/*** Button to top page ***/

var toTopButton = (function() {

    // Variables
    var topButton = $('#back-to-top');
    var scrollTop = $(window).scrollTop();
    var isActive = false;
    if (scrollTop > 100) {
        isActive = true;
    }
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
/***  Dropdown ***/
$(function () {
  $( '.js-side-nav-trigger' ).click(function(){
  $('#body').toggleClass('menu-shown')
  })
});
/*** Side Navbar ***/
jQuery(function($){
   // $( '.js-side-nav-trigger' ).click(function(){
   // $('#body').toggleClass('menu-shown')
   // })
   // Close collapsed navbar on click
   $( '.sidebar-overlay' ).click(function(){
   $('#body').toggleClass('menu-shown')
   })
   $( '.tab-title-wrap' ).click(function(){
   $('.resources-tab-popover-box').toggleClass('hidden')
   })
   $( '.title-label' ).click(function(){
   $('#lang-box').toggleClass('shown')
   })
   $( '.currency-selection-title' ).click(function(){
   $('#currency-box').toggleClass('shown')
   })
   // Close collapsed navbar on click
   $( '.main-content' ).click(function(){
   $('.resources-tab-popover-box').addClass('hidden')
   $('#lang-box').removeClass('shown')
   $('#currency-box').removeClass('shown')
   })
});
/*** Change Navbar color ***/
$(function () {
  $(document).scroll(function () {
    var $nav = $(".dincolo-header");
    $nav.toggleClass('header-transparent', $(this).scrollTop() < $nav.height());
  });
});
/*** Show categories in navbar ***/
$(function () {
  $(document).scroll(function () {
    var $nav = $(".categories-menu-wrapper");
    $nav.toggleClass('shown', $(this).scrollTop() > $nav.height());
  });
});

/*** Smooth scrolling ***/
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
/*** Slick slider on popular categories ***/
$('.categories-slider').slick({
  dots: false,
  lazyLoad: 'ondemand',
  cssEase: 'ease',
  prevArrow: false,
  nextArrow: false,
  infinite: true,
  mobileFirst: true,
  adaptiveHeight: true,
  initialSlide: 1,
  centerMode: true,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});
/*** Testimonials Carousel ***/
$('.testimonials-slider').slick({
  centerMode: true,
  centerPadding: '60px',
  lazyLoad: 'ondemand',
  cssEase: 'ease',
  prevArrow: false,
  nextArrow: false,
  infinite: true,
  mobileFirst: true,
  slidesToShow: 3,
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 1
      }
    }
  ]
});
/*** Slick slider on personalized gigs ***/
$(document).ready(function() {
  $(".gigs-slider").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    prevArrow: true,
    nextArrow: true,
    infinite: true,
    responsive: [
      {
        breakpoint: 639,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });
});
/*** Gigs Slick slider deactivation on resize as a backup plan ***/
// jQuery(window).on('resize', function() {
//     var viewportWidth = jQuery(window).width();
//
//     if (viewportWidth < 530) {
//         $('.gigs-slider').slick('unslick');
//     } else {
//       $(".gigs-slider").slick({
//         slidesToShow: 3,
//         slidesToScroll: 1,
//         arrows: true,
//         infinite: true,
//         responsive: [
//           {
//             breakpoint: 639,
//             settings: {
//               slidesToShow: 1,
//               slidesToScroll: 1
//             }
//           }
//         ]
//       });
//     }
// });
