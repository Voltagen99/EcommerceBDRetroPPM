from django.db import migrations


def setup_groups_and_permissions(apps, schema_editor):
    # Importa i modelli necessari
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    # Crea il gruppo 'Store Manager'
    manager_group, created = Group.objects.get_or_create(name='Store Manager')

    # Definisci i modelli che il manager può gestire
    models_to_manage = ['product', 'category', 'order']

    # Trova i permessi per i modelli specificati
    permissions = []
    for model_name in models_to_manage:
        try:
            # Trova il content type per il modello
            content_type = ContentType.objects.get(app_label='bottega_retrogaming', model=model_name)

            # Trova tutti i permessi associati a questo modello
            model_permissions = Permission.objects.filter(content_type=content_type)
            permissions.extend(model_permissions)
        except ContentType.DoesNotExist:
            # Potrebbe accadere se il modello non esiste, per sicurezza
            print(f"Attenzione: ContentType per il modello {model_name} non trovato.")
            continue

    # Assegna i permessi al gruppo
    manager_group.permissions.set(permissions)
    if created:
        print("Gruppo 'Store Manager' creato e permessi assegnati.")
    else:
        print("Gruppo 'Store Manager' già esistente, permessi aggiornati.")


class Migration(migrations.Migration):
    dependencies = [
        ('bottega_retrogaming', '0002_alter_shippingaddress_options_alter_product_price'),
        # Assicurati che il nome della migrazione precedente sia corretto
    ]

    operations = [
        migrations.RunPython(setup_groups_and_permissions),
    ]
