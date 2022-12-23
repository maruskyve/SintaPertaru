const homeNavbarBtn = '.homeNavbarBtn'
const serviceNavbarBtn = '.serviceNavbarBtn'
const helpCenterNavbarBtn = '.helpCenterNavbarBtn'
const homeSection = '#homeSection'
const serviceSection = '#serviceSection'
const helpCenterSection = '#helpCenterSection'

scrollCaller = [homeNavbarBtn, serviceNavbarBtn, helpCenterNavbarBtn]
scrollSection = [homeSection, serviceSection, helpCenterSection]

$(document).ready(() => {
    for (let i = 0; i < scrollCaller.length; i++) {
        $(scrollCaller[i]).click(() => {
            $([document.documentElement, document.body]).animate({
                scrollTop: $(scrollSection[i]).offset().top - 100
            }, 1500)
        })
    }
})