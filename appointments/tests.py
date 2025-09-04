"Unit tests for appointments"
from datetime import datetime
from zoneinfo import ZoneInfo
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

SERVICE_HAIRCUT = 1
HAIRDRESSER_1 = 1


class AppointmentsIndexViewTests(TestCase):
    "Tests for the index view"

    def test_index(self):
        "Test the response when a service is selected"
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Haircut")

<<<<<<< HEAD
    @patch("django.utils.timezone.now")
=======
    @patch('django.utils.timezone.now')
>>>>>>> 32da721 (Initial commit by AWS CodeCommit)
    def test_index_hairdresser(self, mock_timezone):
        """Test selecting a service & hairdresser returns dates.
        Then create a midday appointment."""
        # Mock the current time for consistent results.
<<<<<<< HEAD
        fake_date = datetime(2010, 1, 1, 10, 0, tzinfo=ZoneInfo("America/Los_Angeles"))
        mock_timezone.return_value = fake_date
=======
        dt = datetime(2010, 1, 1, 10, 0, tzinfo=ZoneInfo("America/Los_Angeles"))
        mock_timezone.return_value = dt
>>>>>>> 32da721 (Initial commit by AWS CodeCommit)

        # Select a service and hairdresser.
        response = self.client.get(
            reverse("index-hairdresser", args=(SERVICE_HAIRCUT, HAIRDRESSER_1))
        )
        # Grab the first offered date.
        first_date = response.context["dates_all"][0][1]

        response = self.client.get(
            reverse("index-date", args=(SERVICE_HAIRCUT, HAIRDRESSER_1, first_date))
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Time")

<<<<<<< HEAD
        # Book an appt for midday.
        appt_time = "12:00"
=======
        # FIX THIS: Remember the initial count of available times.

        # Book an appt for midday.
        appt_time = '12:00'
>>>>>>> 32da721 (Initial commit by AWS CodeCommit)

        # Create an appointment.
        response = self.client.post(
            reverse("create"),
            {
                "service": SERVICE_HAIRCUT,
                "hairdresser": HAIRDRESSER_1,
                "date": first_date,
                "appointment_time": appt_time,
                "customer_contact": "+49123456789",
            },
        )

<<<<<<< HEAD
        # FIX THIS: Test that the time is no longer available.
=======
        response = self.client.get(
            reverse("index-date", args=(SERVICE_HAIRCUT, HAIRDRESSER_1, first_date))
        )
        # Build a list of the blocked times.
        blocked = [ t["time_formatted"]
                    for t in response.context["start_times_all"] if t["is_blocked"] ]
        assert appt_time in blocked, "Blocked time not found"
        # FIX THIS: Test that the number of available appointments has been reduced.
>>>>>>> 32da721 (Initial commit by AWS CodeCommit)
