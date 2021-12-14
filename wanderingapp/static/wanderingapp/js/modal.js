const modal = document.querySelector(".modal");
const trigger = document.querySelectorAll(".trigger").forEach(link => link.addEventListener('click', () => {
    return toggleModal();
}));
const closeButton = document.querySelectorAll(".close-button").forEach(link => link.addEventListener('click', () => {
    return toggleModal()
}));

function toggleModal() {
    modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);