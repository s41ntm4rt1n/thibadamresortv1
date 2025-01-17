<div class="rd-reviews">
                        <h4>Reviews</h4>
                        <div class="review-item">
                            <div class="ri-pic">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="50px"><path d="M16.5 6a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0M18 6A6 6 0 1 0 6 6a6 6 0 0 0 12 0M3 23.25a9 9 0 1 1 18 0 .75.75 0 0 0 1.5 0c0-5.799-4.701-10.5-10.5-10.5S1.5 17.451 1.5 23.25a.75.75 0 0 0 1.5 0"></path></svg>
                            </div>
                            <div class="ri-text">
                                <span>27 Aug 2019</span>
                                <div class="rating">
                                    <i class="icon_star"></i>
                                    <i class="icon_star"></i>
                                    <i class="icon_star"></i>
                                    <i class="icon_star"></i>
                                    <i class="icon_star-half_alt"></i>
                                </div>
                                <h5>Brandon Kelley</h5>
                                <p>Neque porro qui squam est, qui dolorem ipsum quia dolor sit amet, consectetur,
                                    adipisci velit, sed quia non numquam eius modi tempora. incidunt ut labore et dolore
                                    magnam.</p>
                            </div>
                        </div>
                    </div>
                    <div class="review-add">
                        <h4>Add Review</h4>
                        <form action="#" class="ra-form">
                            <div class="row">
                                <div class="col-lg-6">
                                    <input type="text" placeholder="Name*">
                                </div>
                                <div class="col-lg-6">
                                    <input type="text" placeholder="Email*">
                                </div>
                                <div class="col-lg-12">
                                    <div>
                                        <h5>You Rating:</h5>
                                        <div class="rating">
                                            <i class="icon_star"></i>
                                            <i class="icon_star"></i>
                                            <i class="icon_star"></i>
                                            <i class="icon_star"></i>
                                            <i class="icon_star-half_alt"></i>
                                        </div>
                                    </div>
                                    <textarea placeholder="Your Review"></textarea>
                                    <button type="submit">Submit Now</button>
                                </div>
                            </div>
                        </form>
                    </div>

<form id="availability-form" method="POST">
    <div class="check-date">
        <label for="date-in">Check In:</label>
        <input type="text" class="date-input" id="date-in" name="check_in_date" required>
        <i class="icon_calendar"></i>
    </div>
    <div class="check-date">
        <label for="date-out">Check Out:</label>
        <input type="text" class="date-input" id="date-out" name="check_out_date" required>
        <i class="icon_calendar"></i>
    </div>
    <div class="select-option">
        <label for="guest">Guests:</label>
        <select id="guest" name="guests" required>
            <option value="1">1 Adult</option>
            <option value="2">2 Adults</option>
            <option value="3">3 Adults</option>
            <option value="4">4 Adults</option>
        </select>
    </div>

    <div class="select-option">
        <label for="room">Room:</label>
        <select id="room" name="room" required>
            {% for room in available_rooms %}
                <option value="{{ room.id }}" {% if room.id == selected_room.id %}selected{% endif %}>
                    {{ room.name }} - Available Units: {{ room.units }}
                </option>
            {% endfor %}
        </select>
    </div>

    <!-- Show available units for the selected room -->
    <div class="available-units">
        <p><strong>Available Units:</strong> {{ available_units }}</p>
    </div>

    <button type="submit">Check Availability</button>
</form>

<!-- Bootstrap alert container to show feedback -->
<div id="availability-response" class="mt-3"></div>


    document.getElementById('check-availability-btn').addEventListener('click', () => {
    // Gather form data
    const checkInDate = document.getElementById('date-in').value;
    const checkOutDate = document.getElementById('date-out').value;
    const roomId = document.getElementById('room').value; 
    const slug = document.getElementById('slug').value;
    const guestCount = document.getElementById('guest').value;

    // Validate data before sending
    if (!checkInDate || !checkOutDate || !guestCount) {
        alert("Please fill out all required fields.");
        return;
    }

    // Submit data via fetch
    fetch('/check-room-availability/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Ensure CSRF token is included
        },
        body: JSON.stringify({
            check_in_date: checkInDate,
            check_out_date: checkOutDate,
            room_id: roomId,
            guests: guestCount,
            slug: slug,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.available) {
            showAlert("The room is available!", "success");
        } else {
            showAlert("The room is not available for the selected dates.", "danger");
        }
    })
    .catch(error => {
        console.error("Error checking availability:", error);
        showAlert("An error occurred. Please try again.", "danger");
    });
});

// Helper function to get the CSRF token
function getCookie(name) {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith(name + '='))
        ?.split('=')[1];
    return cookieValue;
}
<style>
        .panel {
    background-color: #fff;
    border: 0 solid transparent;
    border-radius: 4px;
    box-shadow: 0 0 0 transparent;
    margin-bottom: 15px;
}
.single-accordion h6 a.collapsed {
    background-color: #aeaeae;
    color: #fff;
}
.single-accordion h6 a {
    background-color: #1d1d1d;
    border-radius: 0;
    color: #fff;
    display: block;
    margin: 0;
    padding: 20px 60px 20px 20px;
    position: relative;
    font-size: 16px;
    text-transform: capitalize;
    font-weight: 500;
}
[role=button], a, area, button, input:not([type=range]), label, select, summary, textarea {
    -ms-touch-action: manipulation;
    touch-action: manipulation;
}
a, a:hover, a:focus {
    -webkit-transition: all 500ms ease 0s;
    transition: all 500ms ease 0s;
    text-decoration: none;
    outline: none;
    font-size: 14px;
    color: #000;
    font-family: 'Poppins', sans-serif;
    font-weight: 400;
}
.single-accordion .accordion-content p {
    padding: 20px 15px 5px;
    margin-bottom: 0;
}
p {
    color: #838383;
    font-size: 15px;
    line-height: 2;
    font-family: 'Poppins', sans-serif;
    font-weight: 400;
    margin-bottom: 1rem;
}
.single-accordion h6 a span {
    font-size: 10px;
    position: absolute;
    right: 20px;
    text-align: center;
    top: 25px;
}.fa-minus:before {
    content: "\f068";
}
</style>