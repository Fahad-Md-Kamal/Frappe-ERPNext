(function ($) {
    $(document).ready(function () {

        // Pop up Function
        $(document).on('click', '.popup-close', function () {
            $('#popup').css('display', 'none');
        });

        //chat function
        $(document).on('click', '#chat', function () {
            $('#chat i').css('width', '130px');
            $('#chat i').css('padding-left', '100px');
        });

        // Slick Slider for category
        $('.category-slider-row').slick({
            arrows: true,
            autoplay: true,
            dots: false,
            nextArrow: "#category .category-slider .category-arrow a.right",
            prevArrow: "#category .category-slider .category-arrow a.left",
            slidesToShow: 10,
            slidesToScroll: 1,
            speed: 500,
            swipeToSlide: true,
            touchThreshold: 100,
            responsive: [{
                    breakpoint: 1551,
                    settings: {
                        slidesToShow: 9
                    }
                },
                {
                    breakpoint: 1451,
                    settings: {
                        slidesToShow: 8
                    }
                },
                {
                    breakpoint: 1312,
                    settings: {
                        slidesToShow: 8
                    }
                },
                {
                    breakpoint: 1173,
                    settings: {
                        slidesToShow: 7
                    }
                },
                {
                    breakpoint: 1034,
                    settings: {
                        slidesToShow: 6
                    }
                },
                {
                    breakpoint: 895,
                    settings: {
                        slidesToShow: 5
                    }
                },
                {
                    breakpoint: 757,
                    settings: {
                        slidesToShow: 4
                    }
                },
                {
                    breakpoint: 617,
                    settings: {
                        slidesToShow: 3
                    }
                },
                {
                    breakpoint: 478,
                    settings: {
                        slidesToShow: 2
                    }
                },
                {
                    breakpoint: 340,
                    settings: {
                        slidesToShow: 1
                    }
                }
            ]
        });

        // Slick Slider for banner
        $('.one-time').slick({
            arrows: false,
            autoplay: true,
            autoplaySpeed: 5000,
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            swipeToSlide: true,
            touchThreshold: 100,
        });

        // Slick Slider for service
        $('.services').slick({
            autoplay: true,
            autoplaySpeed: 5000,
            arrows: true,
            infinite: true,
            slidesToShow: 5,
            slidesToScroll: 1,
            swipeToSlide: true,
            touchThreshold: 100,
            responsive: [{
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 575,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 3,
                    }
                },
                {
                    breakpoint: 320,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 2,
                    }
                }
            ]
        });

        // Side bar
        $(document).on('click', '.sidebar-fade-effect', function (event) {
            if (event.target.matches) {
                document.getElementById("mySidenav").style.width = "0";
                document.querySelector(".sidebar-fade-effect").style.display = "none";
                document.querySelector(".sidenav .closebtn").style.display = "none";
            }
        });

        $(document).on('click', '#sidebar-close', function (event) {
            document.getElementById("mySidenav").style.width = "0";
            document.querySelector(".sidebar-fade-effect").style.display = "none";
            document.querySelector(".sidenav .closebtn").style.display = "none";
        });

        $(document).on('click', '#sidebar-open', function (event) {
            document.getElementById("mySidenav").style.width = "260px";
            document.querySelector(".sidebar-fade-effect").style.display = "block";
            document.querySelector(".sidenav .closebtn").style.display = "block";
        });

        // gallery filter list
        $(document).on('click', '#gallery .filter_lg .by_brand .list span', function () {
            $('#gallery .filter_lg .by_brand .list ul li:hidden').slice(0, 3).show();
            if ($('#gallery .filter_lg .by_brand .list ul li').length == $('#gallery .filter_lg .by_brand .list ul li:visible').length) {
                $('#gallery .filter_lg .by_brand .list span').hide();
            }
        });
        $(document).on('click', '#gallery .filter_lg .by_merchant .list span', function () {
            $('#gallery .filter_lg .by_merchant .list ul li:hidden').slice(0, 3).show();
            if ($('#gallery .filter_lg .by_merchant .list ul li').length == $('#gallery .filter_lg .by_merchant .list ul li:visible').length) {
                $('#gallery .filter_lg .by_merchant .list span').hide();
            }
        });
        $(document).on('click', '#gallery .filter_mb .by_brand .list span', function () {
            $('#gallery .filter_mb .by_brand .list ul li:hidden').slice(0, 3).show();
            if ($('#gallery .filter_mb .by_brand .list ul li').length == $('#gallery .filter_mb .by_brand .list ul li:visible').length) {
                $('#gallery .filter_mb .by_brand .list span').hide();
            }
        });
        $(document).on('click', '#gallery .filter_mb .by_merchant .list span', function () {
            $('#gallery .filter_mb .by_merchant .list ul li:hidden').slice(0, 3).show();
            if ($('#gallery .filter_mb .by_merchant .list ul li').length == $('#gallery .filter_mb .by_merchant .list ul li:visible').length) {
                $('#gallery .filter_mb .by_merchant .list span').hide();
            }
        });

        // mobile-view sort modal
        $(document).on('click', '#sortModal_close', function (e) {
            e.preventDefault();
            $('#sortModal').modal('hide');
        });
        $(document).on('click', '#filterModal_close', function (e) {
            e.preventDefault();
            $('#filterModal').modal('hide');
        });

        // Slick Slider for Single Product view
        $('.single-product-slider').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            infinite: true,
            arrows: false,
            fade: true,
            asNavFor: '.single-product-thumbnail',
            autoplay: false,
            swipe: true,
            swipeToSlide: true,
            asNavFor: '.single-product-thumbnail'
        });
        $('.single-product-thumbnail').slick({
            slidesToShow: 5,
            slidesToScroll: 1,
            infinite: true,
            asNavFor: '.single-product-slider',
            dots: false,
            centerMode: true,
            centerPadding: '0px',
            prevArrow: '.product-slider-prev',
            nextArrow: '.product-slider-next',
            focusOnSelect: true,
            autoplay: false,
            swipe: true,
            swipeToSlide: true,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 4
                    }
                        },
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 3
                    }
                        },
                {
                    breakpoint: 768,
                    centerPadding: '10px',
                    settings: {
                        slidesToShow: 5
                    }
                        },
                {
                    breakpoint: 550,
                    settings: {
                        slidesToShow: 4
                    }
                          },
                {
                    breakpoint: 430,
                    settings: {
                        slidesToShow: 3
                    }
                          }
                      ]
        });

        
    });
})(jQuery)
