$.ajax({
    type: "GET",
    url: "https://swapi-api.hbtn.io/api/films/?format=json",
    success: function(data) {
        for (movie of data.results) {
            $('UL#list_movies').append("<li>" + movie.title + "</li>");
        }
    }
})
