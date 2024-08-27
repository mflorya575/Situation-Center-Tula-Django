/* Код скролла карточек в 3 секции в index.html */
document.addEventListener("DOMContentLoaded", function() {
    const wrapper = document.querySelector(".third-section__wrapper");
    let isDown = false;
    let startX;
    let scrollLeft;

    wrapper.addEventListener("mousedown", function(event) {
        isDown = true;
        startX = event.pageX - wrapper.offsetLeft;
        scrollLeft = wrapper.scrollLeft;
    });

    wrapper.addEventListener("mouseleave", function() {
        isDown = false;
    });

    wrapper.addEventListener("mouseup", function() {
        isDown = false;
    });

    wrapper.addEventListener("mousemove", function(event) {
        if (!isDown) return;
        event.preventDefault();
        const x = event.pageX - wrapper.offsetLeft;
        const walk = (x - startX) * 2; // Умножаем на 2 для более быстрой прокрутки
        wrapper.scrollLeft = scrollLeft - walk;
    });
});


/* Код скролла вверх при нажатии на кнопку в футере */
$(document).ready(function(){
    $('#button').click(function(){
        $(window).scrollTop(0);
    });

    $(document).scroll(function(){
        var scroll_pos = $(window).scrollTop();
        if(scroll_pos > 10){
            $('#button').fadeIn();
        } else {
            $('#button').fadeOut();
        }
    });
});


/* Код обработки нажатия на ЛК в шапке */
document.getElementById('personal-account-link').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default link behavior
    var dropdown = document.getElementById('dropdown-content');
    if (dropdown.style.display === 'none') {
        dropdown.style.display = 'block';
    } else {
        dropdown.style.display = 'none';
    }
});


/* Код обработки нажатия на кнопку меню и выползание его справа */
document.querySelector('.mobile-menu__button').addEventListener('click', function() {
    var menuBlock = document.querySelector('.mobile-menu__block');
    if (menuBlock.style.display === 'none') {
        menuBlock.style.display = 'block';
    } else {
        menuBlock.style.display = 'none';
    }
});


/* Код обработки нажатия на кнопку диалогового окна на странице about-us.html */
const openModal = document.querySelector('.aboutform-section__open-modal')
const closeModal = document.querySelector('.aboutform-section__close-modal')
const modal = document.querySelector('.aboutform-section__modal')

openModal.addEventListener('click', () => {
    modal.showModal()
})

closeModal.addEventListener('click', () => {
    modal.close()
})


/* Плавный скролл */
SmoothScroll({
            // Время скролла 400 = 0.4 секунды
            animationTime: 800,
            // Размер шага в пикселях
            stepSize: 75,

            // Дополнительные настройки:

            // Ускорение
            accelerationDelta: 30,
            // Максимальное ускорение
            accelerationMax: 2,

            // Поддержка клавиатуры
            keyboardSupport: true,
            // Шаг скролла стрелками на клавиатуре в пикселях
            arrowScroll: 50,

            // Pulse (less tweakable)
            // ratio of "tail" to "acceleration"
            pulseAlgorithm: true,
            pulseScale: 4,
            pulseNormalize: 1,

            // Поддержка тачпада
            touchpadSupport: true,
        })
