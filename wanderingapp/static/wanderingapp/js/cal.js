    document.addEventListener('DOMContentLoaded', function () {
        var calendarEL = document.getElementById('calendar');

        var calendar = new FullCalendar.Calendar(calendarEL, {
            height: "auto",
            width: "100%",
            handleWindowResize: true,
            themeSystem: 'standard',
            googleCalendarApiKey: 'AIzaSyCNtXiz0hFqZTRlvdAeAQvf5-40hJRphBM',
            eventSources: [
                {
                    googleCalendarId: '6ulbb1tb1o050qsak7lf9sp77k@group.calendar.google.com',
                }
            ],
            initialView: 'dayGridMonth'
        });
        calendar.render();
    });