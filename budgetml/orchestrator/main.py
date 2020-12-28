import logging
import os

import googleapiclient.discovery

compute = googleapiclient.discovery.build('compute', 'v1')


def start_instance(project, zone, instance_name):
    res = compute.instances().start(
        project=project,
        zone=zone,
        instance=instance_name
    ).execute()
    logging.info(f"Start instance response: {res}")
    return res


def launch():
    project = os.environ['BUDGET_PROJECT']
    zone = os.environ['BUDGET_ZONE']
    instance = os.environ['BUDGET_INSTANCE']

    start_instance(project, zone, instance)
