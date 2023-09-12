document.addEventListener("DOMContentLoaded", () => {
    const hello = document.querySelector("#hello");

    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
        .then(response => {
            return response.json();
        })
        .then(data => {
            hello.textContent = data.hello;
        })
})
