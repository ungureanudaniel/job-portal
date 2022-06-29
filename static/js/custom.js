

/*** Sort popular service posts ***/
var listing = (function() {

    // Variables
    var listing = $(".listing__grid").isotope({
        itemSelector: ".listing__item",
        layoutMode: "masonry"
    });

    // Set ititial filtering

    listing.isotope({ filter: ".web-development" });
    // Filter items on click
    $(".listing_nav").on('click', 'button', function(e) {
        var elem = $(this);

        // Filter items
        var filterValue = elem.attr('data-filter');
        listing.isotope({ filter: filterValue });
        e.preventDefault();
    });

});
// // init Isotope
// var $grid = $('.grid').isotope({
//   itemSelector: '.element-item',
//   layoutMode: 'fitRows'
// });
// // filter functions
// var filterFns = {
//   // show if number is greater than 50
//   numberGreaterThan50: function() {
//     var number = $(this).find('.number').text();
//     return parseInt( number, 10 ) > 50;
//   },
//   // show if name ends with -ium
//   ium: function() {
//     var name = $(this).find('.name').text();
//     return name.match( /ium$/ );
//   }
// };
// // bind filter button click
// $('.filters-button-group').on( 'click', 'button', function() {
//   var filterValue = $( this ).attr('data-filter');
//   // use filterFn if matches value
//   filterValue = filterFns[ filterValue ] || filterValue;
//   $grid.isotope({ filter: filterValue });
// });
// // change is-checked class on buttons
// $('.button-group').each( function( i, buttonGroup ) {
//   var $buttonGroup = $( buttonGroup );
//   $buttonGroup.on( 'click', 'button', function() {
//     $buttonGroup.find('.is-checked').removeClass('is-checked');
//     $( this ).addClass('is-checked');
//   });
// });
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

// ======== Navbar change color ============
// $(function () {
//   $(document).scroll(function () {
//     var $nav = $(".navbar");
//     var $nav_links = $(".nav-link");
//     var $nav_icons = $(".title-icon");
//     var $nav_logo = $(".site-logo");
//     $nav.toggleClass('header-transparent', $(this).scrollTop() < $nav.height());
//     // $nav_icons.toggleClass('white-title-icon', $(this).scrollTop() > $nav.height());
//     // $nav_logo.toggleClass('white-logo', $(this).scrollTop() > $nav.height());
//
//   });
//   // $(document).ready(function () {
//   //       if($(window).width() > 600) {
//   //          $(".categories-list").addClass("categs-slider");
//   //       } else {
//   //         $(".categories-list").removeClass("categs-slider");
//   //       }
//   //   });
// });
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
  infinite: true,
  autoplay: true,
  autoplaySpeed: 6000,
  speed: 800,
  slidesToShow: 1,
  adaptiveHeight: true
});
/*** Slick slider on logged in page categories  ***/
$('.categs-slider').slick({
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
  slidesToShow: 3,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1
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


// ------ Development buttons---------------
$(function () {
  // $(document).scroll(function () {
  //   var $nav = $(".navbar");
  //
  //   $nav.toggleClass('header-transparent', $(this).scrollTop() < $nav.height());
  // });
  $( "#toggle-border" ).click(function() {
    $( '.nav-link' ).toggleClass( "show-border" );
  });
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
$('#ex-basic').picker();
// Check when window size is below 992 in order to change styling on dashboard links
$(window).resize(function() {
  if ($(window).width() < 992) {
     $( '.dashboard-nav' ).addClass( "mobile" );
  }
 else {
    $( '.dashboard-nav' ).removeClass( "mobile" );
 }
});
// Show notification when hovering over something
$(".ion-star").hover(function() {
        $(this).css('cursor','pointer').attr('title', 'Basic membership.');
    }, function() {
        $(this).css('cursor','auto');
});
// Update select dropdown for service category
// const prices = {"programming":[{value:1,desc:"Websites Builders;"},{value:2,desc:"Wordpress;"},{value:3,desc:"Games;"},{value:4,desc:"E-commerce;"},{value:5,desc:"Mobile applications;"}],
//              "accounting":[{value:1,desc:"Websites Builders;"},{value:2,desc:"Wordpress;"},{value:3,desc:"Games;"},{value:4,desc:"E-commerce;"},{value:5,desc:"Mobile applications;"}],
//              "writing":[{value:1,desc:"Websites Builders;"},{value:2,desc:"Wordpress;"},{value:3,desc:"Games;"},{value:4,desc:"E-commerce;"},{value:5,desc:"Mobile applications;"}],
//              "translation":[{value:1,desc:"Websites Builders;"},{value:2,desc:"Wordpress;"},{value:3,desc:"Games;"},{value:4,desc:"E-commerce;"},{value:5,desc:"Mobile applications;"}],
//              "video":[{value:1,desc:"Animated explainers;"},{value:2,desc:"Wordpress;"},{value:3,desc:"Games;"},{value:4,desc:"E-commerce;"},{value:5,desc:"Mobile applications;"}],
//              "audio":[{value:1,desc:"Websites Builders;"},{value:2,desc:"Wordpress;"},{value:3,desc:"Games;"},{value:4,desc:"E-commerce;"},{value:5,desc:"Mobile applications;"}],
//              "business":[{value:1,desc:"CRM management;"},{value:2,desc:"Customer Care;"},{value:3,desc:"HR consulting;"},{value:4,desc:"Event management;"},{value:5,desc:"Career Counseling;"}],
//              "marketing":[{value:1,desc:"Websites Builders;"},{value:2,desc:"Wordpress;"},{value:3,desc:"Games;"},{value:4,desc:"E-commerce;"},{value:5,desc:"Mobile applications;"}],
//              "lifestyle":[{value:1,desc:"Websites Builders;"},{value:2,desc:"Wordpress;"},{value:3,desc:"Games;"},{value:4,desc:"E-commerce;"},{value:5,desc:"Mobile applications;"}],
//              "graphic":[{value:1,desc:"Websites Builders;"},{value:2,desc:"Wordpress;"},{value:3,desc:"Games;"},{value:4,desc:"E-commerce;"},{value:5,desc:"Mobile applications;"}]}
//
// const price = document.querySelector('[name=subcategory]');
// document.querySelector('[name=category]').addEventListener('change', function(e) {
//   price.innerHTML = prices[this.value].reduce((acc, elem) => `${acc}<option value="${elem.value}">${elem.desc}</option>`, "");
// });
var document = window.document;
    $(document).ready(function(){

        var $field1var=$("#field1");
        var $field2var=$("#field2");

        var $field2options=$field2var.find('option');

        $field2var.html($field2options.filter('[value=""]'));

        $field1var.on('change',function(){
            $field2var.html($field2options.filter('[parent="'+this.value+'"],[value=""]'));
            $('#field2 option[value=""]').prop('selected', true);

        });
    });
