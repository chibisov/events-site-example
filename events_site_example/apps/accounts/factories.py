# -*- coding: utf-8 -*-
import factory

from apps.accounts.models import Profile


class ProfileFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Profile

    name = factory.Sequence(lambda n: u'Petr {n}'.format(n=n))
    study_place = factory.Sequence(lambda n: u'College {n}'.format(n=n))
    job_place = factory.Sequence(lambda n: u'Yandex {n}'.format(n=n))