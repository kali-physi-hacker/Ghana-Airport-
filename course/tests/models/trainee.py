from django.test import TestCase
from django.urls import reverse 
from django.utils import timezone

from course.models.trainee import Trainee
from course.models.category import Category

trainee_data = {
    first_name = "FName"
    surname = "LName"
    other_name = "OName"
    # avatar = 
    date_of_birth = timezone.now()
    mobile_no = 0245857565
    sex = 'M'
    date_of_enrollment = timezone.now()
    status = 'D'
    company = 'Trainee Test Company'
    country = 'Gh'
    summary = 'Testing Trainee Summary field'
    start_date = timezone.now()
    end_date = timezone.now()
}

class TraineeTests(TestCase):
    def setUp(self):

        Trainee.objects.create(
            first_name=trainee_data.first_name, surname=trainee_data.surname, other_name=trainee_data.other_name, 
            status=trainee_data.status, company=trainee_data.company, date_of_birth=trainee_data.date_of_birth, mobile_number=trainee_data.mobile_no,
            sex=trainee_data.sex, date_of_enrollment=trainee_data.date_of_enrollment,  country=trainee_data.country, 
            summary=trainee_data.summary, start_date=trainee_data.start_date, end_date=trainee_data.end_date
            )


    def test_content_in_data(self):
        trainee = Trainee.objects.get(name='FName')
        expected_data = {
            trainee.first_name:trainee_data.first_name, trainee.surname:trainee_data.surname, trainee.other_name:trainee_data.other_name, 
            trainee.status:trainee_data.status, trainee.date_of_birth:trainee_data.date_of_birth, trainee.mobile_no:trainee_data.mobile_no,
            trainee.sex:trainee_data.sex, trainee.date_of_enrollment:trainee_data.date_of_enrollment, trainee.company:trainee_data.company,
            trainee.country:trainee_data.country, trainee.category:trainee_data.category,
            trainee.summary:trainee_data.summary, trainee.start_date:trainee_data.start_date, trainee.end_date:trainee_data.end_date
        }

        for data in expected_data:
            self.assertEquals(data, expected_data[data])

