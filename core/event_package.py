import datetime
import datedelta


def date_to_string(d):
    return datetime.datetime.strftime(d, "%Y-%m-%d")


def generate_duedate_event(preg, client):
    return {'name': "" + client.name + " - Due date",
            'address': client.address,
            'notes': client.notes,
            'due_date': date_to_string(preg.due_date),
            }


def generate_scan_event(preg, client):
    modifiedDate = preg.due_date + datedelta.datedelta(days=10)

    return {'name': "" + client.name + " - Arrange scan",
            'address': client.address,
            'notes': client.notes,
            'due_date': date_to_string(modifiedDate),
            }


def generate_fortytwo_event(preg, client):
    modifiedDate = preg.due_date + datedelta.datedelta(days=14)

    return {'name': "" + client.name + " - 42 weeks",
            'address': client.address,
            'notes': client.notes,
            'due_date': date_to_string(modifiedDate),
            }


def generate_oncall_event(preg, client):
    modifiedDate = preg.due_date - datedelta.datedelta(days=23)

    return {'name': "" + client.name + " - On call",
            'address': client.address,
            'notes': client.notes,
            'due_date': date_to_string(modifiedDate),
            }


def generate_package_event(preg, client):
    weeks = 40 - preg.week_care_commences
    days = weeks * 7
    modifiedDate = preg.due_date - datedelta.datedelta(days=days)

    return {'name': "" + client.name + " - Care commences",
            'address': client.address,
            'notes': client.notes,
            'due_date': date_to_string(modifiedDate),
            }


def generate_initial_appt_event(preg, client):
    weeks = 40 - preg.week_care_commences
    days = (weeks * 7) + 14
    modifiedDate = preg.due_date - datedelta.datedelta(days=days)

    return {'name': "" + client.name + " - Arrange initial appt.",
            'address': client.address,
            'notes': client.notes,
            'due_date': date_to_string(modifiedDate),
            }


def generate_events(preg, client):
    e = [generate_duedate_event(preg, client),
         generate_scan_event(preg, client),
         generate_fortytwo_event(preg, client),
         generate_oncall_event(preg, client),
         generate_package_event(preg, client),
         generate_initial_appt_event(preg, client),
         ]
    return e
