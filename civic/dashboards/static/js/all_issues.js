document.addEventListener("DOMContentLoaded", function () {
    /* SECURE CONTEXT DATA EXTRACTION */
    const contextDataElement = document.getElementById('dashboard-data');
    if (!contextDataElement) return;

    const context = JSON.parse(contextDataElement.textContent);
    const reports = typeof context.reports === 'string' ? JSON.parse(context.reports) : context.reports;

    /* LAST UPDATED TIMESTAMPS */
    const lastUpdatedContainer = document.getElementById('lastUpdated');
    if (lastUpdatedContainer) {
        lastUpdatedContainer.innerHTML = "Last Updated: " + new Date().toLocaleString();
    }

    /* CATEGORY BAR CHART INITIALIZATION */
    const categoryCtx = document.getElementById('categoryChart');
    if (categoryCtx) {
        new Chart(categoryCtx, {
            type: 'bar',
            data: {
                labels: ['Water', 'Roads', 'Health', 'Garbage'],
                datasets: [{
                    label: 'Reports',
                    data: [
                        parseInt(context.waterIssues) || 0,
                        parseInt(context.roadsIssues) || 0,
                        parseInt(context.healthIssues) || 0,
                        parseInt(context.garbageIssues) || 0
                    ],
                    backgroundColor: ['#3b82f6', '#f59e0b', '#10b981', '#ef4444'],
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }

    /* URGENCY PIE CHART INITIALIZATION */
    const urgencyCtx = document.getElementById('urgencyChart');
    if (urgencyCtx) {
        new Chart(urgencyCtx, {
            type: 'pie',
            data: {
                labels: ['High', 'Low'],
                datasets: [{
                    data: [
                        parseInt(context.highUrgency) || 0,
                        parseInt(context.lowUrgency) || 0
                    ],
                    backgroundColor: ['red', 'orange'],
                    borderWidth: 2,
                    borderColor: '#fff'
                }]
            }
        });
    }

    /* LEAFLET GEOLOCATION MAP OVERLAYS */
    const map = L.map('map');

    navigator.geolocation.getCurrentPosition(
        function (position) {
            map.setView([position.coords.latitude, position.coords.longitude], 10);
        },
        function (error) {
            map.setView([0.3476, 32.5825], 10);
        }
    );

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'OpenStreetMap'
    }).addTo(map);

    /* ELEMENT INJECTIONS */
    const tableBody = document.getElementById('reportTable');
    const highSelect = document.querySelector('.high-urgency-select');
    const lowSelect = document.querySelector('.low-urgency-select');

    /* SYSTEM PIPELINE LOOP */
    reports.forEach((report, index) => {
        
        /* CARD ACTION SELECTOR POPULATION */
        if (report.status === 'pending') {
            const optionText = `[${report.category.toUpperCase()}] ${report.area || 'Unknown Location'}`;
            const option = new Option(optionText, index);

            if (report.urgency === 'high' && highSelect) {
                highSelect.add(option);
            } else if (report.urgency === 'low' && lowSelect) {
                lowSelect.add(option);
            }
        }

        /* GEOLOCATION RENDER MARKERS */
        if (report.location) {
            const coords = report.location.split(',');
            const lat = parseFloat(coords[0].trim());
            const lng = parseFloat(coords[1].trim());

            if (!isNaN(lat) && !isNaN(lng)) {
                let markerColor = "green";
                if (report.urgency === "high") {
                    markerColor = "red";
                } else if (report.urgency === "medium" || report.urgency === "low") {
                    markerColor = "orange";
                }

                let marker = L.circleMarker([lat, lng], {
                    radius: 10,
                    color: markerColor,
                    fillColor: markerColor,
                    fillOpacity: 0.8
                }).addTo(map);

                marker.bindPopup(`
                    <b>${report.category}</b><br>
                    ${report.message || ''}<br>
                    Urgency: ${report.urgency}<br>
                    ${new Date(report.time).toLocaleString()}
                `);
            }
        }

        /* LIVE DATATABLE ELEMENT INJECTION */
        if (report.status === 'pending' && tableBody) {
            const row = document.createElement('tr');
            let urgencyClass = report.urgency ? report.urgency.toLowerCase() : '';
            row.classList.add(`${urgencyClass}-row`);

            row.innerHTML = `
                <td>${report.message || 'No message'}</td>
                <td>${report.category}</td>
                <td class="${urgencyClass}">${report.urgency}</td>
                <td>${report.area || 'Unknown'}</td>
                <td>${new Date(report.time).toLocaleString()}</td>
            `;
            tableBody.appendChild(row);
        }
    });

    /* REBIND SYNC FUNCTION TO GLOBAL CONTEXT */
    window.syncHiddenFields = function (selectElement, type) {
        const reportIndex = selectElement.value;
        const selectedReport = reports[reportIndex];

        if (selectedReport) {
            document.querySelector(`.${type}-location-input`).value = selectedReport.location || '';
            document.querySelector(`.${type}-category-input`).value = selectedReport.category || '';
        }
    };
});