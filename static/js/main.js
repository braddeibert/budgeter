window.onload = function setupListeners() {
    document.getElementById("burger").addEventListener("click", () => {
        menu = document.getElementById("menu")
        
        if (menu.style.display == "block") {
            menu.style.display = "none"
        }
        else {
            menu.style.display = "block"
        }
    })

    let editbutton = document.querySelector(".edit")
    let edittools = document.querySelectorAll(".edit-mode")

    editbutton.addEventListener('click', () => {
        edittools.forEach((tool) => {
            tool.style.display = (tool.style.display == '' || tool.style.display == 'none') ? 'table-cell' : 'none'
        })
    })
}

function backPage() {
    console.log('here')
    window.history.back()
}
    