from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django_apogee.models import Pays, Etape
from duck_examen.models import DeroulementExamenModel, RattachementCentreExamen
from duck_inscription.models import SettingsEtape
from duck_paiement_etudiant.models import SettingEtapePaiement, InsAdmEtpPaiement


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):

        for etape in Etape.objects.by_centre_gestion('IED'):
            SettingEtapePaiement.objects.get_or_create(etape=etape, cod_anu=2015)

        for s in SettingsEtape.objects.all():
            b = SettingEtapePaiement.objects.get_or_create(etape=Etape.objects.get(cod_etp=s.cod_etp), cod_anu=2015)[0]
            b.tarif = s.frais
            b.demi_tarif = s.demi_tarif
            b.demi_annee = s.semestre
            b.nb_paiment_max = s.nb_paiement
            b.save()
