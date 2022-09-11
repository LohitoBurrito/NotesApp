
let heading1 = document.getElementById('scrollWords1');
let heading2 = document.getElementById('scrollWords2');
let contact = document.getElementById('contact');
let donation = document.getElementsByClassName('donationWords')
let contactContainer = document.getElementById('contact-container')
let donationContainer = document.getElementsByClassName('donation-container')
let page1 = document.getElementById('Page1');
let page2 = document.getElementById('Page2');
let imagineWord = document.getElementById('ImagineWord');
let imagine = document.getElementById('imagine');
let restOfWordsContainer = document.getElementsByClassName('RestOfWordsContainer');
let restOfWords = document.getElementsByClassName('RestOfWords');


window.addEventListener('load', function pageFullyLoaded() {
    heading1.style.animation = 'anim1 2s forwards ease-out';
    heading2.style.animation = 'anim2 2s forwards ease-out';
});

const observer1 = new IntersectionObserver((entries) => {
    if (entries[0].intersectionRatio > 0) {
        contact.style.animation = 'contactAnim 1.25s forwards ease-out';
    } else {
        contact.style.animation = 'none';
    }
});

const observer2 = new IntersectionObserver((entries) => {
        console.log(entries);
        if (entries[0].intersectionRatio > 0) {
            donation[0].style.animation = 'donateAnim 1s forwards ease-out';
        } else {
            donation[0].style.animation = 'none';
        }
    },
    {
        threshold: [0, 0.25, 0.5, 0.75, 1]
    }
);
const observer3 = new IntersectionObserver((entries) => {
    console.log(entries);
    if (entries[0].intersectionRatio > 0) {
        donation[1].style.animation = 'donateAnim 1s forwards ease-out';
    } else {
        donation[1].style.animation = 'none';
    }   
    },
    {
        threshold: [0, 0.25, 0.5, 0.75, 1]
    }
);
const observer4 = new IntersectionObserver((entries) => {
    console.log(entries);
    if (entries[0].intersectionRatio > 0) {
        donation[2].style.animation = 'donateAnim 1s forwards ease-out';
    } else {
        donation[2].style.animation = 'none';
    }
    },
    {
        threshold: [0, 0.25, 0.5, 0.75, 1]
    }
);
const observer5 = new IntersectionObserver((entries) => {
    console.log(entries);
    if (entries[0].intersectionRatio > 0) {
        donation[3].style.animation = 'donateAnim 1s forwards ease-out';
    } else {
        donation[3].style.animation = 'none';
    }
    },
    {
        threshold: [0, 0.25, 0.5, 0.75, 1]
    }
);
const observer6 = new IntersectionObserver((entries) => {
    console.log(entries);
    if (entries[0].intersectionRatio > 0) {
        donation[4].style.animation = 'donateAnim 1s forwards ease-out';
    } else {
        donation[4].style.animation = 'none';
    }
    }, 
    {
        threshold: [0, 0.25, 0.5, 0.75, 1]
    }
);
const observer7 = new IntersectionObserver((entries) => {
    if (entries[0].intersectionRatio > 0) {
        imagineWord.style.animation = 'page2Anim1 1.5s forwards ease-out';
    } else {
        imagineWord.style.animation = 'none';
    }
});
window.addEventListener('scroll', function scrollingEffect() {
    let val = window.scrollY;
    heading1.style.transform = 'translateY(' + -val * 0.2 + 'px)';
    heading2.style.transform = 'translateY(' + -val * 0.2 + 'px)';
    if (window.pageYOffset > 0) {
        var divOffsetTop = page2.offsetTop;
        let opacityVal = 1 - window.pageYOffset / divOffsetTop;
        page1.style.opacity = opacityVal;
    }
    if (this.screen.width < 550) {
        if (imagine.getBoundingClientRect().top <= 1700) {
            imagineWord.style.animation = 'page2Anim1 1.5s forwards ease-out';
        } else {
            imagineWord.style.animation = 'none';
        }  
        for (let i = 0; i < restOfWordsContainer.length; i++) {
            if (restOfWordsContainer[i].getBoundingClientRect().top <= 1500) {
                restOfWords[i].style.animation = 'page2Anim2 1s forwards ease-out';
            } else {
                restOfWords[i].style.animation = 'none';
            }     
        }
    } else {
        if (imagine.getBoundingClientRect().top <= 600) {
            imagineWord.style.animation = 'page2Anim1 1.5s forwards ease-out';
        } else {
            imagineWord.style.animation = 'none';
        }  
        for (let i = 0; i < restOfWordsContainer.length; i++) {
            if (restOfWordsContainer[i].getBoundingClientRect().top <= 650) {
                restOfWords[i].style.animation = 'page2Anim2 1s forwards ease-out';
            } else {
                restOfWords[i].style.animation = 'none';
            }     
        }
    }
});
observer1.observe(contactContainer);
observer2.observe(donationContainer[0]);
observer3.observe(donationContainer[1]);
observer4.observe(donationContainer[2]);
observer5.observe(donationContainer[3]);
observer6.observe(donationContainer[4]);





