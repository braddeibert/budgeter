function editMode() {
    let edittools = document.querySelectorAll(".edit")

    edittools.forEach((tool) => {
        if (tool.classList.contains("hidden")) {
            tool.classList.remove("hidden")
        }
        else {
            tool.classList.add("hidden")
        }
    })
}

function backPage() {
    window.history.back()
}