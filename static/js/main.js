window.onload = function openHamburgerMenu() {
    document.getElementById("burger").addEventListener("click", () => {
        menu = document.getElementById("menu")
        
        if (menu.style.display == "block") {
            menu.style.display = "none"
        }
        else {
            menu.style.display = "block"
        }
    })
}