from django.test import TestCase
from declaration.models import PackageStatusHistory
from declaration.factories import PackageStatusFactory, PackageDeclarationFactory, PackageStatusHistoryFactory


class TestPackageDeclaration(TestCase):
    def test_save_method_creates_status_history(self):
        package_status_1 = PackageStatusFactory.create(status_name='status1', order=1)
        package_status_2 = PackageStatusFactory.create(status_name='status2', order=2)
        package_status_3 = PackageStatusFactory.create(status_name='status3', order=3)

        package = PackageDeclarationFactory(status=package_status_1)

        PackageStatusHistoryFactory.create(package=package, status=package_status_1)

        package.status = package_status_3
        package.save()

        # Check if a new PackageStatusHistory object is created
        self.assertTrue(PackageStatusHistory.objects.filter(package=package, status=package_status_3).exists())
        history = PackageStatusHistory.objects.latest('date_changed')
        self.assertEqual(history.package, package)
        self.assertEqual(history.status,package_status_3)