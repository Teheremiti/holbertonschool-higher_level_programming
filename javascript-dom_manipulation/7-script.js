const movies_list = document.querySelector("#list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => {
        return response.json();
    })
    .then(data => {
        for (movie of data.results) {
            var node = document.createElement("li");
            var textnode = document.createTextNode(movie.title);
            node.appendChild(textnode);
            movies_list.appendChild(node);
        }
    })
