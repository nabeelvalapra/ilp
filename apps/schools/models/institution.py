from django.contrib.gis.db import models


class InstitutionCategory(models.Model):
    """ Category for institution """
    name = models.CharField(max_length=300)
    institution_type = models.ForeignKey('common.InstitutionType')

    def __unicode__(self):
        return "%s" % self.name


class Management(models.Model):
    """ The school management """
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return "%s" % self.name


class PinCode(models.Model):
    """ Pincodes """
    geom = models.GeometryField()

    def __unicode__(self):
        return "%s" % self.geom


class Institution(models.Model):
    """ An educational institution """
    dise_code = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300)
    category = models.ForeignKey('InstitutionCategory')
    gender = models.ForeignKey('common.InstitutionGender')
    institution_type = models.ForeignKey('common.InstitutionType')
    management = models.ForeignKey('Management')
    year_established = models.CharField(max_length=5, null=True, blank=True)
    rural_urban = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    area = models.CharField(max_length=1000, null=True, blank=True)
    village = models.CharField(max_length=1000, null=True, blank=True)
    pincode = models.ForeignKey('PinCode', null=True, blank=True)
    landmark = models.CharField(max_length=1000, null=True, blank=True)
    instidentification = models.CharField(
        max_length=1000, null=True, blank=True)
    instidentification2 = models.CharField(
        max_length=1000, null=True, blank=True)
    route_information = models.CharField(
        max_length=1000, null=True, blank=True)
    admin3 = models.ForeignKey(
            'boundary.Boundary', related_name='institution_admin3')
    admin2 = models.ForeignKey(
            'boundary.Boundary', related_name='institution_admin2')
    admin1 = models.ForeignKey(
            'boundary.Boundary', related_name='institution_admin1')
    admin0 = models.ForeignKey(
            'boundary.Boundary', related_name='institution_admin0')
    mp = models.ForeignKey(
            'boundary.ElectionBoundary', related_name='institution_mp', null=True)
    mla = models.ForeignKey(
            'boundary.ElectionBoundary', related_name='institution_mla', null=True)
    gp = models.ForeignKey(
            'boundary.ElectionBoundary', related_name='institution_gp', null=True)
    ward = models.ForeignKey(
            'boundary.ElectionBoundary', related_name='institution_ward', null=True)
    coord = models.GeometryField(null=True)
    last_verified_year = models.ForeignKey('common.AcademicYear', null=True)
    status = models.ForeignKey('common.Status')

    class Meta:
        unique_together = (('name', 'dise_code', 'admin3'), )

    def __unicode__(self):
        return "%s" % self.name


class InstitutionLanguage(models.Model):
    institution = models.ForeignKey('Institution')
    moi = models.ForeignKey('common.Language')

    class Meta:
        unique_together = (('institution', 'moi'), )


class InstitutionAggregation(models.Model):
    """Data aggregation per institution"""
    institution = models.ForeignKey('Institution')
    name = models.CharField(max_length=300)
    academic_year = models.ForeignKey('common.AcademicYear')
    gender = models.ForeignKey('common.Gender')
    moi = models.ForeignKey('common.Language', related_name='inst_agg_moi')
    mt = models.ForeignKey('common.Language', related_name='inst_agg_mt')
    religion = models.ForeignKey('common.Religion')
    category = models.ForeignKey('common.StudentCategory')
    num = models.IntegerField()

    class Meta:
        unique_together = (('id','academic_year','gender','moi','mt','religion',
            'category'), )
