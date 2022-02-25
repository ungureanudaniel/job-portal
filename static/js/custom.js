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

// var alert = (function() {
    // Config
    // ======
//
//     var alertLifetime = 6000;
//
//     // Methods
//     // =======
//
//     var generate = function(type, message) {
//         var newAlert = $(
//             '<div class="alert alert-' +
//                 type +
//                 ' fade in" id="page-alert">' +
//                 message +
//                 "</div>"
//         );
//
//         // Append new alert
//         $("body").append(newAlert);
//
//         // Remove new alert
//         setTimeout(function() {
//             newAlert.alert("close");
//         }, alertLifetime);
//     };
// })();


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
		this.blocks[0].getElementsByTagName('form')[0].addEventListener('submit', function(event){
			event.preventDefault();
			self.toggleError(document.getElementById('signin-email'), true);
		});
		this.blocks[1].getElementsByTagName('form')[0].addEventListener('submit', function(event){
			event.preventDefault();
			self.toggleError(document.getElementById('signup-username'), true);
		});
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

	// toggle main navigation on mobile
	var mainNav = document.getElementsByClassName('js-main-nav')[0];
	if(mainNav) {
		mainNav.addEventListener('click', function(event){
			if( hasClass(event.target, 'js-main-nav') ){
				var navList = mainNav.getElementsByTagName('ul')[0];
				toggleClass(navList, 'cd-main-nav__list--is-visible', !hasClass(navList, 'cd-main-nav__list--is-visible'));
			}
		});
	}

	//class manipulations - needed if classList is not supported
	function hasClass(el, className) {
	  	if (el.classList) return el.classList.contains(className);
	  	else return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'));
	}
	function addClass(el, className) {
		var classList = className.split(' ');
	 	if (el.classList) el.classList.add(classList[0]);
	 	else if (!hasClass(el, classList[0])) el.className += " " + classList[0];
	 	if (classList.length > 1) addClass(el, classList.slice(1).join(' '));
	}
	function removeClass(el, className) {
		var classList = className.split(' ');
	  	if (el.classList) el.classList.remove(classList[0]);
	  	else if(hasClass(el, classList[0])) {
	  		var reg = new RegExp('(\\s|^)' + classList[0] + '(\\s|$)');
	  		el.className=el.className.replace(reg, ' ');
	  	}
	  	if (classList.length > 1) removeClass(el, classList.slice(1).join(' '));
	}
	function toggleClass(el, className, bool) {
		if(bool) addClass(el, className);
		else removeClass(el, className);
	}

	//credits http://css-tricks.com/snippets/jquery/move-cursor-to-end-of-textarea-or-input/
	function putCursorAtEnd(el) {
    	if (el.setSelectionRange) {
      		var len = el.value.length * 2;
      		el.focus();
      		el.setSelectionRange(len, len);
    	} else {
      		el.value = el.value;
    	}
	};
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
    nav: true,
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
      loop: true,
      addClassActive: true,
      dots: false,
      lazyLoad: true,
      autoplay: true,
      autoplaySpeed: 2000,
      autoplayTimeout: 4000,
      autoplayHoverPause: true,
      responsive:{
        0:{
            items:1,
            stagePadding: 10,

        },
        600:{
            items:1,
            stagePadding: 100,

        },
        1000:{
            items:1,
            stagePadding: 200,
        },
        1330:{
            items:1,
            stagePadding: 330,
        }
    }
  })
});
// $(document).ready(function () {
//     $("#owl-carousel-testim").owlCarousel({
//
//         autoPlay: 3000, //Set AutoPlay to 3 seconds
//         responsive: true,
//         addClassActive: true,
//         items: 3,
//         itemsDesktop: [1199, 3],
//         itemsDesktopSmall: [979, 3],
//         stopOnHover:true,
//         afterMove:function(){
//             //reset transform for all item
//             $(".owl-item").css({
//                 transform:"none"
//             })
//             //add transform for 2nd active slide
//             $(".active").eq(1).css({
//                 transform:"scale(1.9)",
//                 zIndex:3000,
//
//             })
//
//         },
//         //set init transform
//         afterInit:function(){
//             $(".active").eq(1).css({
//                 transform:"scale(1.9)",
//                 zIndex:3000,
//
//             })
//         }
//
//     });
//
// })
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
