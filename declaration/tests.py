from django.test import TestCase
from declaration.models import PackageStatusHistory
from declaration.factories import PackageStatusFactory, PackageDeclarationFactory, PackageStatusHistoryFactory


class TestPackageDeclaration(TestCase):
    def test_save_method_creates_status_history(self):
        package_status_1 = PackageStatusFactory()
        package_status_2 = PackageStatusFactory()
        package_status_3 = PackageStatusFactory()
        package_status_4 = PackageStatusFactory()

        package = PackageDeclarationFactory(status=package_status_1)

        PackageStatusHistoryFactory.create(package=package, status=package_status_1)

        package.status = package_status_4
        package.save()

        # Check if a new PackageStatusHistory object is created
        self.assertTrue(PackageStatusHistory.objects.filter(package=package, status=package_status_4).exists())
        history = PackageStatusHistory.objects.latest('date_changed')
        self.assertEqual(history.package, package)
        self.assertEqual(history.status,package_status_4)