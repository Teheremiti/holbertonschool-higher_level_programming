const toggle_header = document.querySelector("#toggle_header");

toggle_header.addEventListener("click", toggleClass);

function toggleClass() {
    if (toggle_header.className == "red") {
        toggle_header.className = "green";
    }
    else {
        toggle_header.className = "red";
    }
}
