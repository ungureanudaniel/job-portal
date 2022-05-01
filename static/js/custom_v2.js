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
/*** Side Navbar ***/
$(function () {
  $( '.js-side-nav-trigger' ).click(function(){
  $('#body').toggleClass('menu-shown')
  })
  $( '.main-content' ).click(function(){
  $('#body').toggleClass('menu-shown')
  })
});
/*** Login Window ***/
$(function(){
  $( '.js-login-trigger' ).click(function(l){
    $('.site-login').addClass('shown');
  })
  $( '.main-content' ).click(function(){
    $('.site-login').removeClass('shown')
  })
});
/*** Join us Window ***/
$(function(){
  $( '.js-join-trigger' ).click(function(l){
    $('.site-join').addClass('shown');
  })
  $( '.main-content' ).click(function(){
    $('.site-join').removeClass('shown')
  })
});
/*** Dropdowns ***/
// $(function () {
//   $( '.tab-title-wrap' ).click(function(){
//   $('.resources-tab-popover-box').toggleClass('hidden')
//   })
//   $( '.profile-icon-wrap' ).click(function(){
//   $('.profile-popover-box').toggleClass('hidden')
//   })
  // $('.title-label').click(function(){
  // $('#lang-box').toggleClass('shown')
  // })
  // $( '.currency-selection-title' ).click(function(){
  // $('#currency-box').toggleClass('shown')
  // })
  // // Close collapsed navbar on click
  // $( '.main-content' ).click(function(){
  // $('.resources-tab-popover-box').addClass('hidden')
  // $('#lang-box').removeClass('shown')
  // $('#currency-box').removeClass('shown')
  // $('#profile-popover-box').removeClass('shown')
  // })
// });
/*** Change Navbar color ***/
$(function () {
  $(document).scroll(function () {
    var $nav = $(".dincolo-header");
    var $nav_links = $(".nav-link");
    var $nav_icons = $(".title-icon");
    var $nav_logo = $(".site-logo");
    $nav.toggleClass('header-transparent', $(this).scrollTop() < $nav.height());
    $nav_links.toggleClass('white-menu', $(this).scrollTop() > $nav.height());
    $nav_icons.toggleClass('white-title-icon', $(this).scrollTop() > $nav.height());
    $nav_logo.toggleClass('white-logo', $(this).scrollTop() > $nav.height());

  });
});
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
  slidesToShow: 1,
  slidesToScroll: 1,
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
/*** Slick slider on reviews ***/
$('.testimonials-slider').slick({
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
  slidesToShow: 1,
  slidesToScroll: 1,
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
