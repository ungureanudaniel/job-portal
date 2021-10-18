
// ========= switch navbar style on scroll ========= //
const navbar = document.querySelector('#header-container');
const logo = document.querySelector('.brand-name');
const nav_item = document.querySelectorAll('nav-item');
// const wide_search_box = document.querySelector('wide-form-search')
window.onscroll = () => {
    if (window.scrollY > 300) {
        navbar.classList.add('white-header');
        navbar.classList.remove('transparent-header');

    } else {
      navbar.classList.remove('white-header');
      navbar.classList.add('transparent-header');


    }
};
// ========= switch navbar style on scroll END ========= //
