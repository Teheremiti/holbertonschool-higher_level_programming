const button = document.querySelector("#update_header");
const header = document.querySelector("header");

button.addEventListener("click", updateHeader);

function updateHeader() {
    header.textContent = "New Header!!!";
}
