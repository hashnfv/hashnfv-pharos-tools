##############################################################################
# Copyright (c) 2016 Max Breitenfeldt and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################


from celery import shared_task

from dashboard.models import Resource
from jenkins.models import JenkinsSlave, JenkinsStatistic
from .adapter import *


@shared_task
def sync_jenkins():
    update_jenkins_slaves()


def update_jenkins_slaves():
    JenkinsSlave.objects.all().update(active=False)

    jenkins_slaves = get_all_slaves()
    for slave in jenkins_slaves:
        jenkins_slave, created = JenkinsSlave.objects.get_or_create(name=slave['displayName'],
                                                                    url=get_slave_url(slave))
        jenkins_slave.active = True
        jenkins_slave.ci_slave = is_ci_slave(slave['displayName'])
        jenkins_slave.dev_pod = is_dev_pod(slave['displayName'])
        jenkins_slave.status = get_slave_status(slave)

        # if this is a new slave and a pod, check if there is a resource for it, create one if not
        if  created and 'pod' in slave['displayName']:
            # parse resource name from slave name
            # naming example: orange-pod1, resource name: Orange POD 1
            tokens = slave['displayName'].split('-')
            name = tokens[0].capitalize() + ' POD '# company name
            name += tokens[1][3:] # remove 'pod'
            resource, created = Resource.objects.get_or_create(name=name)
            resource.slave = jenkins_slave
            resource.save()

        last_job = get_jenkins_job(jenkins_slave.name)
        if last_job is not None:
            last_job = parse_job(last_job)
            jenkins_slave.last_job_name = last_job['name']
            jenkins_slave.last_job_url = last_job['url']
            jenkins_slave.last_job_scenario = last_job['scenario']
            jenkins_slave.last_job_branch = last_job['branch']
            jenkins_slave.last_job_installer = last_job['installer']
            jenkins_slave.last_job_result = last_job['result']
        jenkins_slave.save()

        jenkins_statistic = JenkinsStatistic(slave=jenkins_slave)
        if jenkins_slave.status == 'online' or jenkins_slave.status == 'building':
            jenkins_statistic.online = True
        if jenkins_slave.status == 'offline':
            jenkins_statistic.offline = True
        if jenkins_slave.status == 'online / idle':
            jenkins_statistic.idle = True
        jenkins_statistic.save()
