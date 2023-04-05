import factory
from django.utils import timezone
from declaration.models import PackageDeclaration, PackageStatus, PackageStatusHistory

class PackageStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PackageStatus

    status_name = factory.Sequence(lambda n: f'status{n}')
    order = factory.Sequence(lambda n: n)

class PackageDeclarationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PackageDeclaration

    status = factory.SubFactory(PackageStatusFactory)


class PackageStatusHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PackageStatusHistory
    
    package = factory.SubFactory(PackageDeclarationFactory)
    status = factory.SubFactory(PackageStatusFactory)
    date_changed = factory.LazyFunction(timezone.now)
