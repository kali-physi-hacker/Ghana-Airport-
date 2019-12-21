from django.test import TestCase
from django.urls import reverse 
from django.utils import timezone

from course.models.employee import Employee
from course.models.category import Category

employee_data = {
    first_name:"FName"
    surname:"LName"
    other_name:"OName"
    # avatar:
    staff_id:"Staff_id"
    date_of_birth:timezone.now()
    mobile_no:0245857565
    sex:'M'
    date_of_enrollment:timezone.now()
    station:'Test Station'
    course_name:'Test Course'
    country:'Gh'
    category:Category.objects.create(name='Cat Name', description='Testing Category')
    summary:'Testing Employee Summary field'
    start_date:timezone.now()
    end_date:timezone.now()
}


class EmployeeTests(TestCase):
    def setUp(self):

        Employee.objects.create(
            first_name=employee_data.first_name, surname=employee_data.surname, other_name=employee_data.other_name, 
            staff_id=employee_data.staff_id, date_of_birth=employee_data.date_of_birth, mobile_number=employee_data.mobile_no,
            sex=employee_data.sex, date_of_enrollment=employee_data.date_of_enrollment, station=employee_data.station,
            course_name=employee_data.course_name, country=employee_data.country, category=employee_data.category, summary=employee_data.summary,
            start_date=employee_data.start_date, end_date=employee_data.end_date
            )


    def test_content_in_data(self):
        employee = Employee.objects.get(name='FName')
        expected_data = {
            employee.first_name:employee_data.first_name, employee.surname:employee_data.surname, employee.other_name:employee_data.other_name, 
            employee.staff_id:employee_data.staff_id, employee.date_of_birth:employee_data.date_of_birth, employee.mobile_no:employee_data.mobile_no,
            employee.sex:employee_data.sex, employee.date_of_enrollment:employee_data.date_of_enrollment, employee.station:employee_data.station,
            employee.course_name:employee_data.course_name, employee.country:employee_data.country, employee.category:employee_data.category,
            employee.summary:employee_data.summary, employee.start_date:employee_data.start_date, employee.end_date:employee_data.end_date
        }

        for data in expected_data:
            self.assertEquals(data, expected_data[data])
            
        # self.assertEquals()            

