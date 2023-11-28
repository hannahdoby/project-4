
const apiUrl = 'http://localhost:5000/predict';

document.getElementById('movieRatingForm').addEventListener('submit', function (event) {
  event.preventDefault();

    // Collect ratings for each genre
    const actionRating = document.querySelector('input[name="actionRating"]:checked') ? document.querySelector('input[name="actionRating"]:checked').value : null;
    const adventureRating = document.querySelector('input[name="adventureRating"]:checked') ? document.querySelector('input[name="adventureRating"]:checked').value : null;
    const animationRating = document.querySelector('input[name="animationRating"]:checked') ? document.querySelector('input[name="animationRating"]:checked').value : null;
    const comedyRating = document.querySelector('input[name="comedyRating"]:checked') ? document.querySelector('input[name="comedyRating"]:checked').value : null;      
    const crimeRating = document.querySelector('input[name="crimeRating"]:checked') ? document.querySelector('input[name="crimeRating"]:checked').value : null;          
    const documentaryRating = document.querySelector('input[name="documentaryRating"]:checked') ? document.querySelector('input[name="documentaryRating"]:checked').value : null;
    const dramaRating = document.querySelector('input[name="dramaRating"]:checked') ? document.querySelector('input[name="dramaRating"]:checked').value : null;
    const fantasyRating = document.querySelector('input[name="fantasyRating"]:checked') ? document.querySelector('input[name="fantasyRating"]:checked').value : null;        
    const filmnoirRating = document.querySelector('input[name="filmnoirRating"]:checked') ? document.querySelector('input[name="filmnoirRating"]:checked').value : null;    
    const horrorRating = document.querySelector('input[name="horrorRating"]:checked') ? document.querySelector('input[name="horrorRating"]:checked').value : null;    
    const musicalRating = document.querySelector('input[name="musicalRating"]:checked') ? document.querySelector('input[name="musicalRating"]:checked').value : null;         
    const mysteryRating = document.querySelector('input[name="mysteryRating"]:checked') ? document.querySelector('input[name="mysteryRating"]:checked').value : null;
    const romanceRating = document.querySelector('input[name="romanceRating"]:checked') ? document.querySelector('input[name="romanceRating"]:checked').value : null;
    const scifiRating = document.querySelector('input[name="scifiRating"]:checked') ? document.querySelector('input[name="scifiRating"]:checked').value : null;
    const thrillerRating = document.querySelector('input[name="thrillerRating"]:checked') ? document.querySelector('input[name="thrillerRating"]:checked').value : null;
    const warRating = document.querySelector('input[name="warRating"]:checked') ? document.querySelector('input[name="warRating"]:checked').value : null;        
    const westernRating = document.querySelector('input[name="westernRating"]:checked') ? document.querySelector('input[name="westernRating"]:checked').value : null;

    // Fetch new movie title
    const newMovieTitle = document.getElementById('newMovieTitle').value;

    // Perform any actions needed with the provided rating
    // Send data to Flask API (assuming an endpoint '/predict-rating' exists)
    predict();


    // Clear form fields after submission
    document.getElementById('movieGenre').selectedIndex = 0;
    document.getElementById('movieRating').value = '';
});

function predict() {
    // send data to Flask API
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application.json'
        },
        body: JSON.stringify({
            Action: actionRating,
            Adventure: adventureRating,
            Animation: animationRating,
            Comedy: comedyRating,
            Crime: crimeRating,
            Documentary: documentaryRating,
            Drama: dramaRating,
            Fantasy: fantasyRating,
            Horror: horrorRating,
            Musical: musicalRating,
            Mystery: mysteryRating,
            Romance: romanceRating,
            "Sci-Fi": scifiRating,
            Thriller: thrillerRating,
            War: warRating,
            Westeren: westernRating,
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