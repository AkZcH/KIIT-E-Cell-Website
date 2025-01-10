const form = document.querySelector('form');
form.addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent the default form submission
    const review = document.querySelector('#review').value; // Get the input value
    
    // Make sure the review is not empty
    if (review.trim() === '') {
        alert("Review cannot be empty.");
        return;
    }
    
    // Send GET request with query parameter 'review'
    fetch(`/predict?review=${encodeURIComponent(review)}`, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response (display result, etc.)
        console.log(data);
    });
});
