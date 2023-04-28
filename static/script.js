const headerBtn = document.querySelector("#headerbtn")
const headerNav = document.querySelector("#nav")
const headerul = headerNav.querySelector(".list")
let isNavbarExpanded = headerBtn.getAttribute("aria-expanded") === "true";

const toggleNavbarVisibility = () => {
    isNavbarExpanded = !isNavbarExpanded;
    headerBtn.setAttribute("aria-expanded", isNavbarExpanded);
};

headerBtn.addEventListener("click", toggleNavbarVisibility);

headerul.addEventListener("click", (e) => e.stopPropagation());
headerNav.addEventListener("click", toggleNavbarVisibility);
