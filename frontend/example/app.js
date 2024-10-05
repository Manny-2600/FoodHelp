// Check if user is authenticated
window.onload = function () {
    const accessToken = localStorage.getItem('accessToken');
    if (accessToken) {
        displayRestaurantSearch();
    } else {
        displayLoginForm();
    }
};

// Display login form
function displayLoginForm() {
    document.getElementById('login-form').style.display = 'block';
    document.getElementById('restaurant-search').style.display = 'none';
}

// Display restaurant search form
function displayRestaurantSearch() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('restaurant-search').style.display = 'block';
}

// Handle login/signup
document.getElementById('login-btn').addEventListener('click', function () {
    authenticate('/auth/login');
});

document.getElementById('signup-btn').addEventListener('click', function () {
    // TODO: try catch + just say now log in in alert
    authenticate('/auth/register');
});


function authenticate(endpoint) {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch(`http://localhost:5000${endpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    })
        .then(response => response.json())
        .then(data => {
            // Check for access_token and refresh_token returned from backend
            if (data.access_token && data.refresh_token) {
                // Save tokens to local storage
                localStorage.setItem('accessToken', data.access_token);  // Update key to access_token
                localStorage.setItem('refreshToken', data.refresh_token);  // Update key to refresh_token
                displayRestaurantSearch();
            } else {
                alert('Authentication failed');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


// // Handle restaurant search
// document.getElementById('search-btn').addEventListener('click', function () {
//     // const location = document.getElementById('location').value;
//     const cuisine = document.getElementById('cuisine').value;

//     const accessToken = localStorage.getItem('accessToken');

//     if (!accessToken) {
//         alert('Please log in first.');
//         return;
//     }

//     // fetch(`http://localhost:5000/api/restaurants?location=${location}&cuisine=${cuisine}`, {
//     // TODO: convert cuisine space to + char

//     fetch(`http://localhost:5000/api/restaurants/${cuisine}`, {
//         method: 'GET',
//         headers: {
//             'Authorization': `Bearer ${accessToken}`
//         }
//     })
//         .then(response => response.json())
//         .then(data => {
//             displayRestaurants(data);
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
// });

// Handle restaurant search
document.getElementById('search-btn').addEventListener('click', function () {
    // const location = document.getElementById('location').value;
    let cuisine = document.getElementById('cuisine').value;

    const accessToken = localStorage.getItem('accessToken');

    if (!accessToken) {
        alert('Please log in first.');
        return;
    }

    // Convert spaces in cuisine to `+`
    cuisine = cuisine.replace(/\s+/g, '+');

    fetch(`http://localhost:5000/restaurants/${cuisine}`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${accessToken}`
        }
    })
        .then(response => response.json())
        .then(data => {
            displayRestaurants(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

// Display list of restaurants
function displayRestaurants(restaurants) {
    const restaurantList = document.getElementById('restaurant-list');
    restaurantList.innerHTML = '';

    if (restaurants.length === 0) {
        restaurantList.innerHTML = '<p>No restaurants found.</p>';
        return;
    }

    restaurants.forEach(restaurant => {
        const restaurantItem = document.createElement('div');
        restaurantItem.innerHTML = `<h3>${restaurant.name}</h3><p>${restaurant.address}</p>`;
        restaurantList.appendChild(restaurantItem);
    });
}
