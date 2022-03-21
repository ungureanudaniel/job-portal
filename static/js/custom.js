
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
/*** Join/login modal window  ***/
(function(){
    //Login/Signup modal window - by CodyHouse.co
	function ModalSignin( element ) {
		this.element = element;
		this.blocks = this.element.getElementsByClassName('js-signin-modal-block');
		this.switchers = this.element.getElementsByClassName('js-signin-modal-switcher')[0].getElementsByTagName('a');
		this.triggers = document.getElementsByClassName('js-signin-modal-trigger');
		this.hidePassword = this.element.getElementsByClassName('js-hide-password');
		this.init();
	};

	ModalSignin.prototype.init = function() {
		var self = this;
		//open modal/switch form
		for(var i =0; i < this.triggers.length; i++) {
			(function(i){
				self.triggers[i].addEventListener('click', function(event){
					if( event.target.hasAttribute('data-signin') ) {
						event.preventDefault();
						self.showSigninForm(event.target.getAttribute('data-signin'));
					}
				});
			})(i);
		}

		//close modal
		this.element.addEventListener('click', function(event){
			if( hasClass(event.target, 'js-signin-modal') || hasClass(event.target, 'js-close') ) {
				event.preventDefault();
				removeClass(self.element, 'cd-signin-modal--is-visible');
			}
		});
		//close modal when clicking the esc keyboard button
		document.addEventListener('keydown', function(event){
			(event.which=='27') && removeClass(self.element, 'cd-signin-modal--is-visible');
		});

		//hide/show password
		for(var i =0; i < this.hidePassword.length; i++) {
			(function(i){
				self.hidePassword[i].addEventListener('click', function(event){
					self.togglePassword(self.hidePassword[i]);
				});
			})(i);
		}
		//IMPORTANT - REMOVE THIS - it's just to show/hide error messages in the demo
		// this.blocks[0].getElementsByTagName('form')[0].addEventListener('submit', function(event){
		// 	event.preventDefault();
		// 	self.toggleError(document.getElementById('signin-email'), true);
		// });
		// this.blocks[1].getElementsByTagName('form')[0].addEventListener('submit', function(event){
		// 	event.preventDefault();
		// 	self.toggleError(document.getElementById('signup-username'), true);
		// });
	};

	ModalSignin.prototype.togglePassword = function(target) {
		var password = target.previousElementSibling;
		( 'password' == password.getAttribute('type') ) ? password.setAttribute('type', 'text') : password.setAttribute('type', 'password');
		target.textContent = ( 'Hide' == target.textContent ) ? 'Show' : 'Hide';
		putCursorAtEnd(password);
	}

	ModalSignin.prototype.showSigninForm = function(type) {
		// show modal if not visible
		!hasClass(this.element, 'cd-signin-modal--is-visible') && addClass(this.element, 'cd-signin-modal--is-visible');
		// show selected form
		for( var i=0; i < this.blocks.length; i++ ) {
			this.blocks[i].getAttribute('data-type') == type ? addClass(this.blocks[i], 'cd-signin-modal__block--is-selected') : removeClass(this.blocks[i], 'cd-signin-modal__block--is-selected');
		}
		//update switcher appearance
		var switcherType = (type == 'signup') ? 'signup' : 'login';
		for( var i=0; i < this.switchers.length; i++ ) {
			this.switchers[i].getAttribute('data-type') == switcherType ? addClass(this.switchers[i], 'cd-selected') : removeClass(this.switchers[i], 'cd-selected');
		}
	};

	ModalSignin.prototype.toggleError = function(input, bool) {
		// used to show error messages in the form
		toggleClass(input, 'cd-signin-modal__input--has-error', bool);
		toggleClass(input.nextElementSibling, 'cd-signin-modal__error--is-visible', bool);
	}

	var signinModal = document.getElementsByClassName("js-signin-modal")[0];
	if( signinModal ) {
		new ModalSignin(signinModal);
	}
