from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Gunicorn
from diagrams.onprem.client import Client
from diagrams.onprem.database import MSSQL
from diagrams.onprem.network import Nginx
from diagrams.programming.language import Python, Javascript
from diagrams.generic.os import Ubuntu
from diagrams.aws.compute import EC2
from diagrams.programming.framework import Django, React
from diagrams.onprem.vcs import Gitlab
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

graph_attr = {
    "fontsize": "24",
    "bgcolor": "white"
}

with Diagram("Technology Stack", show=False, graph_attr=graph_attr):
    client = Client("Client Side")
    react = React("React")
    js = Javascript("JavasScript")
    server = Ubuntu("Ubuntu Server")
    gitlab = Gitlab("GitLab")

    with Cluster("Server Side"):
        ubuntu = [Gunicorn("Gunicorn"),
                  Nginx("NGINX"),
                  Django("Django"),
                  EC2("Supervisor")]

    py = Python("Python")
    mssql = MSSQL("Database")

    client >> react >> js >> server >> ubuntu
    ubuntu - py - mssql
    js - gitlab
    py - gitlab
