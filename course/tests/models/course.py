from django.test import TestCase
from django.urls import reverse 
from django.utils import timezone 

from course.models.course import Course 
from course.models.employee import Employee

from .employee import employee_data


class CourseTest(TestCase):
    def setUp(self):
        name = 'Test Course'
        description = 'Test Course Description'
        employee_one = Employee.objects.create(
            first_name=trainee_data.first_name, surname=trainee_data.surname, other_name=trainee_data.other_name, 
            status=trainee_data.status, company=trainee_data.company, date_of_birth=trainee_data.date_of_birth, mobile_number=trainee_data.mobile_no,
            sex=trainee_data.sex, date_of_enrollment=trainee_data.date_of_enrollment,  country=trainee_data.country, 
            summary=trainee_data.summary, start_date=trainee_data.start_date, end_date=trainee_data.end_date
        )
        employee_two = Employee.objects.create(
            first_name=trainee_data.first_name+"two", surname=trainee_data.surname, other_name=trainee_data.other_name, 
            status=trainee_data.status, company=trainee_data.company, date_of_birth=trainee_data.date_of_birth, mobile_number=trainee_data.mobile_no,
            sex=trainee_data.sex, date_of_enrollment=trainee_data.date_of_enrollment,  country=trainee_data.country, 
            summary=trainee_data.summary, start_date=trainee_data.start_date, end_date=trainee_data.end_date
        )

        employees = [employee_one, employee_two]

        Course.objects.create(
            name=name,
            description=description,
            employees=employees
        )

    def test_content_in_data(self):
        course = Course.objects.get(name=self.name)
        expected_employees = list(course.employees.all())
        expected_data = {
            course.name:self.name,
            course.description:self.description,
            self.employees:expected_employees
        }

        for data in expected_data:
            self.assertEquals(data, expected_data[data])