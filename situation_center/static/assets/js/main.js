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


/* Прелоадер */
window.onload = function() {
    let preloader = document.getElementById('preloader');
    preloader.classList.add('hide-preloader');
    setInterval(function() {
          preloader.classList.add('preloader-hidden');
    }, 2990);
}


/* Маска для номера телефона */
function maskPhone(selector, masked = '+7 (___) ___-__-__') {
	const elems = document.querySelectorAll(selector);

	function mask(event) {
		const keyCode = event.keyCode;
		const template = masked,
			def = template.replace(/\D/g, ""),
			val = this.value.replace(/\D/g, "");
		console.log(template);
		let i = 0,
			newValue = template.replace(/[_\d]/g, function (a) {
				return i < val.length ? val.charAt(i++) || def.charAt(i) : a;
			});
		i = newValue.indexOf("_");
		if (i !== -1) {
			newValue = newValue.slice(0, i);
		}
		let reg = template.substr(0, this.value.length).replace(/_+/g,
			function (a) {
				return "\\d{1," + a.length + "}";
			}).replace(/[+()]/g, "\\$&");
		reg = new RegExp("^" + reg + "$");
		if (!reg.test(this.value) || this.value.length < 5 || keyCode > 47 && keyCode < 58) {
			this.value = newValue;
		}
		if (event.type === "blur" && this.value.length < 5) {
			this.value = "";
		}

	}

	for (const elem of elems) {
		elem.addEventListener("input", mask);
		elem.addEventListener("focus", mask);
		elem.addEventListener("blur", mask);
	}
	
}
