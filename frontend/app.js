// app.js

document.addEventListener('DOMContentLoaded', function () {
    // Check if user is authenticated
    if (isAuthenticated()) {
        showSearch();
    } else {
        showLogin();
    }

    // Event listeners for switching between login and register
    document.getElementById('show-register').addEventListener('click', function (event) {
        event.preventDefault();
        showRegister();
    });

    document.getElementById('show-login').addEventListener('click', function (event) {
        event.preventDefault();
        showLogin();
    });

    // Event listener for login form
    document.getElementById('login-form').addEventListener('submit', function (event) {
        event.preventDefault();
        login();
    });

    // Event listener for register form
    document.getElementById('register-form').addEventListener('submit', function (event) {
        event.preventDefault();
        register();
    });

    // Event listener for search form
    document.getElementById('search-form').addEventListener('submit', function (event) {
        event.preventDefault();
        searchRestaurants();
    });

    // Event listener for logout button
    document.getElementById('logout-button').addEventListener('click', function () {
        logout();
    });
});

function isAuthenticated() {
    return localStorage.getItem('access_token') !== null;
}

function showLogin() {
    document.getElementById('login-container').style.display = 'block';
    document.getElementById('register-container').style.display = 'none';
    document.getElementById('search-container').style.display = 'none';
}

function showRegister() {
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('register-container').style.display = 'block';
    document.getElementById('search-container').style.display = 'none';
}

function showSearch() {
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('register-container').style.display = 'none';
    document.getElementById('search-container').style.display = 'block';
}

function login() {
    var email = document.getElementById('login-email').value;
    var password = document.getElementById('login-password').value;

    fetch('http://localhost:5000/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: password })
    })
        .then(function (response) {
            if (!response.ok) {
                return response.json().then(function (data) {
                    throw new Error(data.message || 'Login failed');
                });
            }
            return response.json();
        })
        .then(function (data) {
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);
            showSearch();
        })
        .catch(function (error) {
            alert(error.message);
        });
}

function register() {
    var username = document.getElementById('signup-name').value;
    var email = document.getElementById('signup-email').value;
    var password = document.getElementById('signup-password').value;

    fetch('http://localhost:5000/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            email: email,
            password: password
        })
    })
        .then(function (response) {
            if (!response.ok) {
                return response.json().then(function (data) {
                    throw new Error(data.message || 'Registration failed');
                });
            }
            return response.json();
        })
        .then(function (data) {
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);
            showSearch();
        })
        .catch(function (error) {
            alert(error.message);
        });
}

function searchRestaurants() {
    var location = document.getElementById('location').value;
    var cuisine = document.getElementById('cuisine').value;

    var accessToken = localStorage.getItem('access_token');

    return fetch(`http://localhost:5000/api/restaurants?location=${encodeURIComponent(location)}&cuisine=${encodeURIComponent(cuisine)}`, {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + accessToken
        }
    })
        .then(function (response) {
            if (response.status === 401) {
                // Unauthorized, try refreshing token
                return refreshToken().then(function (success) {
                    if (success) {
                        // Retry original request
                        return searchRestaurants();
                    } else {
                        throw new Error('Session expired. Please login again.');
                    }
                });
            } else if (!response.ok) {
                return response.json().then(function (data) {
                    throw new Error(data.message || 'Error fetching restaurants');
                });
            }
            return response.json();
        })
        .then(function (data) {
            displayResults(data);
        })
        .catch(function (error) {
            alert(error.message);
        });
}

function displayResults(restaurants) {
    var resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    if (restaurants.length === 0) {
        resultsDiv.innerHTML = '<p>No restaurants found.</p>';
        return;
    }

    var ul = document.createElement('ul');

    restaurants.forEach(function (restaurant) {
        var li = document.createElement('li');
        li.textContent = restaurant.name + ' - ' + restaurant.address;
        ul.appendChild(li);
    });

    resultsDiv.appendChild(ul);
}

function refreshToken() {
    var refreshToken = localStorage.getItem('refresh_token');

    return fetch('http://localhost:5000/auth/refresh', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + refreshToken
        }
    })
        .then(function (response) {
            if (!response.ok) {
                return false;
            }
            return response.json();
        })
        .then(function (data) {
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);
            return true;
        })
        .catch(function () {
            logout();
            return false;
        });
}

function logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    showLogin();
}
