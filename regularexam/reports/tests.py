from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from regularexam.reports.models import Report, Comment


# Create your tests here.

class ReportModelTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='vasko1',
            email='testemail@gmail.com',
            password='testing123',

        )

    def test_report_fields(self):
        report = Report.objects.create(
            title='Data breach',
            body='1 millions passwords are on the dark web',
            author=self.user,
            additional_materials='https://www.google.com',
            common_vulnerability_scoring_system=5
        )

        self.assertEqual(report.title, 'Data breach')
        self.assertEqual(report.body,'1 millions passwords are on the dark web')
        self.assertEqual(report.author,self.user)
        self.assertEqual(report.common_vulnerability_scoring_system,5)

    def test_report_str_representation(self):
        report = Report.objects.create(
            title='Data breach',
            body='1 millions passwords are on the dark web',
            author=self.user,
            additional_materials='https://www.google.com',
            common_vulnerability_scoring_system=5
        )
        self.assertEqual(report.__str__(),report.title)


    def test_absolute_url(self):
        report = Report.objects.create(
            title='Data breach',
            body='1 millions passwords are on the dark web',
            author=self.user,
            additional_materials='https://www.google.com',
            common_vulnerability_scoring_system=5
        )

        expected_url = reverse('report_detail', kwargs={'pk': report.pk})
        self.assertEqual(report.get_absolute_url(),expected_url)

class CommentModelTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='vasko1',
            email='testemail@gmail.com',
            password='testing123',

        )
        self.report = Report.objects.create(
            title='Data breach',
            body='1 millions passwords are on the dark web',
            author=self.user,
            additional_materials='https://www.google.com',
            common_vulnerability_scoring_system=5
        )

    def test_comment_fields(self):
        comment = Comment.objects.create(
            report=self.report,
            author=self.user,
            comment='Microsoft Database is compromised.',
        )

        self.assertEqual(comment.report,self.report)
        self.assertEqual(comment.author,self.user)
        self.assertEqual(comment.comment,'Microsoft Database is compromised.')

    def test_str_representation(self):
        comment = Comment.objects.create(
            report=self.report,
            author=self.user,
            comment='Microsoft Database is compromised.',
        )

        self.assertEqual(str(comment),'Microsoft Database is compromised.')

    def test_post_data(self):
        comment = Comment.objects.create(
            report=self.report,
            author=self.user,
            comment='Microsoft Database is compromised.',
        )
        self.assertTrue(comment.post_date)