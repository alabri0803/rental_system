from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from contracts.models import Contract
from tenants.models import Tenant


@receiver(post_migrate)
def create_usr_groups(sender, **kwargs):
  admin_group, _ = Group.objects.get_or_create(name='مشرف')
  staff_group, _ = Group.objects.get_or_create(name='موظف')
  contract_ct = ContentType.objects.get_for_model(Contract)
  tenant_ct = ContentType.objects.get_for_model(Tenant)

  view_contract = Permission.objects.get(codename='view_contract', content_type=contract_ct)
  add_contract = Permission.objects.get(codename='add_contract', content_type=contract_ct)
  change_contract = Permission.objects.get(codename='change_contract', content_type=contract_ct)

  view_tenant = Permission.objects.get(codename='view_tenant', content_type=tenant_ct)
  add_tenant = Permission.objects.get(codename='add_tenant', content_type=tenant_ct)
  change_tenant = Permission.objects.get(codename='change_tenant', content_type=tenant_ct)

  staff_group.permissions.set([
    view_contract,
    add_contract,
    change_contract,
    view_tenant,
    add_tenant,
    change_tenant
  ])