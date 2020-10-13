$(document).ready(function () {
    $('.img_container').lightSlider({
        item: 4,
        loop: true,
        keyPress: true,
        slideMove: 2,
        easing: 'cubic-bezier(0.25, 0, 0.25, 1)',
        speed: 600,
        responsive: [
            {
                breakpoint: 800,
                settings: {
                    item: 3,
                    slideMove: 1,
                    slideMargin: 6,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    item: 1,
                    // slideMove: 1
                }
            }
        ]
    });
});