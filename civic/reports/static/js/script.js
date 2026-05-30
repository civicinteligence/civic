function getLocation() {
    const locationInput = document.getElementById("location");

    if (!navigator.geolocation) {
        locationInput.placeholder = "Geolocation not supported by your browser";
        return;
    }

    navigator.geolocation.getCurrentPosition(
        async function(position) {
            let latitude = position.coords.latitude;
            let longitude = position.coords.longitude;

            if (latitude && longitude) {
                document.getElementById("coordinates").value = `${latitude},${longitude}`;
                locationInput.value = "Fetching address components...";
                const addressText = await getPlaceName(latitude, longitude);
                locationInput.value = addressText;
            } else {
                locationInput.placeholder = "Failed to pinpoint coordinates.";
            }
        },
        function(error) {
            console.error("Geolocation Error:", error);
            locationInput.placeholder = "Location permission denied/unavailable";
        }
    );
}

async function getPlaceName(lat, lon) {
    const url = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lon}`;

    try {
        const response = await fetch(url, {
            headers: {
                'User-Agent': 'Civic-Intelligence-App/1.0'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        if (data && data.address) {
            const road = data.address.road || '';
            const suburb = data.address.suburb || '';
            const urbanArea = data.address.city || data.address.town || data.address.village || '';
            const county = data.address.county || '';
            
            return [road, suburb, urbanArea, county].filter(Boolean).join(', ');
        } else {
            return 'Location mapped, details missing';
        }
    } catch (error) {
        console.error("Error fetching reverse geocode location data:", error);
        return 'Lookup Error';
    }
}