$(".landing-module__79oWsG__burgerBtn").click(() => {
    $('body').css({'overflow': 'hidden'});
    $(".landing-module__79oWsG__mobileMenuOverlay").addClass("landing-module__79oWsG__mobileMenuOverlayOpen");
    $(".landing-module__79oWsG__mobileMenu ").addClass("landing-module__79oWsG__mobileMenuOpen");
});

$(".landing-module__79oWsG__mobileMenuOverlay").click(() => {
    $('body').css({'overflow': ''});
    $(".landing-module__79oWsG__mobileMenuOverlay").removeClass("landing-module__79oWsG__mobileMenuOverlayOpen");
    $(".landing-module__79oWsG__mobileMenu ").removeClass("landing-module__79oWsG__mobileMenuOpen");
})


$(".cookie-consent-module__sWgoKG__button").click(() => {
    $(".cookie-consent-module__sWgoKG__wrapper").hide()
    localStorage.setItem("__cookieConsent", "hide");
})