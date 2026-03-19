document.addEventListener("DOMContentLoaded", function () {

    const weddingDate = new Date("2026-10-11T18:30:00").getTime();

    const daysEl = document.getElementById("days");
    const hoursEl = document.getElementById("hours");
    const minutesEl = document.getElementById("minutes");
    const secondsEl = document.getElementById("seconds");
    const countdownEl = document.getElementById("countdown");

    if (!daysEl || !hoursEl || !minutesEl || !secondsEl || !countdownEl) return;

    function pad(num) {
        return num.toString().padStart(2, "0");
    }

    const timer = setInterval(function () {

        const now = new Date().getTime();
        const distance = weddingDate - now;

        if (distance < 0) {
            clearInterval(timer);
            countdownEl.textContent = "🎉 ¡Hoy es el gran día! 🎉";
            return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        daysEl.textContent = pad(days);
        hoursEl.textContent = pad(hours);
        minutesEl.textContent = pad(minutes);
        secondsEl.textContent = pad(seconds);

    }, 1000);

    // Inicializar mapa de Leaflet
    const mapElement = document.getElementById('map');
    if (mapElement) {
        const lat = -33.3068777;
        const lng = -70.698663;
        const locationName = "Centro de Eventos Santa Catalina de Chicureo";
        
        const map = L.map('map').setView([lat, lng], 15);
        
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors',
            maxZoom: 19
        }).addTo(map);
        
        const marker = L.marker([lat, lng]).addTo(map);
        marker.bindPopup("<b>Centro de Eventos</b><br>Santa Catalina de Chicureo").openPopup();
        
        function openNativeMap() {
            const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
            
            if (isIOS) {
                window.location.href = `maps://maps.apple.com/?q=${encodeURIComponent(locationName)}&ll=${lat},${lng}&z=15`;
                setTimeout(() => {
                    window.open(`https://maps.apple.com/?q=${encodeURIComponent(locationName)}&ll=${lat},${lng}&z=15`, "_blank");
                }, 1000);
            } else {
                window.location.href = `geo:${lat},${lng}?q=${encodeURIComponent(locationName)}`;
                setTimeout(() => {
                    window.open(`https://www.google.com/maps/search/?api=1&query=${lat},${lng}`, "_blank");
                }, 1000);
            }
        }
        
        marker.on('click', openNativeMap);
        map.on('click', openNativeMap);
    }

});

function openMaps() {
    window.open("https://maps.app.goo.gl/wk6jfHPB2rBRsfKT9", "_blank");
}