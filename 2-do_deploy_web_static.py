#!/usr/bin/python3
"""
Fabric script that generates archive
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ["ubuntu@44.200.177.244", "ubuntu@3.234.240.140"]


def do_deploy(archive_path):
    """
        Distribute an archive to our web servers
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        print(archived_file)
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/", use_sudo=True)
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False



