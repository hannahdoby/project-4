const apiUrl = 'http://localhost:5000/predict';

document.getElementById('movieRatingForm').addEventListener('submit', function (event) {
  event.preventDefault();

    // Collect ratings for each genre
    const actionRating = document.querySelector('input[name="actionRating"]:checked') ? document.querySelector('input[name="actionRating"]:checked').value : 0;
    console.log(`Action: ${actionRating}`)
    const adventureRating = document.querySelector('input[name="adventureRating"]:checked') ? document.querySelector('input[name="adventureRating"]:checked').value : 0;
    console.log(`Adventure: ${adventureRating}`)
    const animationRating = document.querySelector('input[name="animationRating"]:checked') ? document.querySelector('input[name="animationRating"]:checked').value : 0;
    console.log(`Animation: ${animationRating}`)
    const childrenRating = document.querySelector('input[name="childrenRating"]:checked') ? document.querySelector('input[name="childrenRating"]:checked').value : 0;
    console.log(`Children: ${childrenRating}`)
    const comedyRating = document.querySelector('input[name="comedyRating"]:checked') ? document.querySelector('input[name="comedyRating"]:checked').value : 0;
    console.log(`Comedy: ${comedyRating}`)
    const crimeRating = document.querySelector('input[name="crimeRating"]:checked') ? document.querySelector('input[name="crimeRating"]:checked').value : 0;
    console.log(`Crime: ${crimeRating}`)
    const documentaryRating = document.querySelector('input[name="documentaryRating"]:checked') ? document.querySelector('input[name="documentaryRating"]:checked').value : 0;
    console.log(`Documentary: ${documentaryRating}`)
    const dramaRating = document.querySelector('input[name="dramaRating"]:checked') ? document.querySelector('input[name="dramaRating"]:checked').value : 0;
    console.log(`Drama: ${dramaRating}`)
    const fantasyRating = document.querySelector('input[name="fantasyRating"]:checked') ? document.querySelector('input[name="fantasyRating"]:checked').value : 0;
    console.log(`Fantasy: ${fantasyRating}`)
    const filmnoirRating = document.querySelector('input[name="filmnoirRating"]:checked') ? document.querySelector('input[name="filmnoirRating"]:checked').value : 0;
    console.log(`Film-Noir: ${filmnoirRating}`)
    const horrorRating = document.querySelector('input[name="horrorRating"]:checked') ? document.querySelector('input[name="horrorRating"]:checked').value : 0;
    console.log(`Horror: ${horrorRating}`)
    const musicalRating = document.querySelector('input[name="musicalRating"]:checked') ? document.querySelector('input[name="musicalRating"]:checked').value : 0;
    console.log(`Musical: ${musicalRating}`)
    const mysteryRating = document.querySelector('input[name="mysteryRating"]:checked') ? document.querySelector('input[name="mysteryRating"]:checked').value : 0;
    console.log(`Mystery: ${mysteryRating}`)
    const romanceRating = document.querySelector('input[name="romanceRating"]:checked') ? document.querySelector('input[name="romanceRating"]:checked').value : 0;
    console.log(`Romance: ${romanceRating}`)
    const scifiRating = document.querySelector('input[name="scifiRating"]:checked') ? document.querySelector('input[name="scifiRating"]:checked').value : 0;
    console.log(`Sci-Fi: ${scifiRating}`)
    const thrillerRating = document.querySelector('input[name="thrillerRating"]:checked') ? document.querySelector('input[name="thrillerRating"]:checked').value : 0;
    console.log(`Thriller: ${thrillerRating}`)
    const warRating = document.querySelector('input[name="warRating"]:checked') ? document.querySelector('input[name="warRating"]:checked').value : 0;
    console.log(`War: ${warRating}`)
    const westernRating = document.querySelector('input[name="westernRating"]:checked') ? document.querySelector('input[name="westernRating"]:checked').value : 0;
    console.log(`Western: ${westernRating}`)

    // Fetch new movie title
    const newMovieTitle = document.getElementById('newMovieTitle').value;

    // Perform any actions needed with the provided rating
    // Send data to Flask API (assuming an endpoint '/predict-rating' exists)
    predict(apiUrl, actionRating, adventureRating, animationRating, childrenRating, comedyRating, crimeRating, documentaryRating, dramaRating, fantasyRating, filmnoirRating, filmnoirRating, horrorRating, musicalRating, mysteryRating, romanceRating, scifiRating, thrillerRating, warRating, westernRating, newMovieTitle);


    // Clear form fields after submission
    document.getElementById('newMovieTitle').value = '';
});

function predict(apiUrl, actionRating, adventureRating, animationRating, childrenRating, comedyRating, crimeRating, documentaryRating, dramaRating, fantasyRating, filmnoirRating, horrorRating, musicalRating, mysteryRating, romanceRating, scifiRating, thrillerRating, warRating, westernRating, newMovieTitle) {
    // send data to Flask API
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            Action: actionRating,
            Adventure: adventureRating,
            Animation: animationRating,
            Children: childrenRating,
            Comedy: comedyRating,
            Crime: crimeRating,
            Documentary: documentaryRating,
            Drama: dramaRating,
            Fantasy: fantasyRating,
            "Film-Noir": filmnoirRating,
            Horror: horrorRating,
            Musical: musicalRating,
            Mystery: mysteryRating,
            Romance: romanceRating,
            "Sci-Fi": scifiRating,
            Thriller: thrillerRating,
            War: warRating,
            Western: westernRating,
            "(no genres listed)":"0",
            newMovieTitle: newMovieTitle
        })
    })
        .then(response => response.json)
        .then(data => {
            // Display predicted Rating
            document.getElementById('predictedRating').textContent = 'Your Predicted Rating for "${newMovieTitle}": ${data.predictedRating}'
        })
        .catch(error => {
            console.error('Error:', error);
        });
};