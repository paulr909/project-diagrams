from diagrams import Cluster, Diagram
from diagrams.onprem.client import Client
from diagrams.onprem.database import MSSQL
from diagrams.programming.language import Python, Javascript
from diagrams.generic.os import Windows
from diagrams.aws.compute import EC2
from diagrams.programming.framework import Django, React
from diagrams.onprem.vcs import Gitlab
from diagrams.azure.general import Resource

graph_attr = {
    "fontsize": "24",
    "bgcolor": "white"
}

with Diagram("Windows Technology Stack", show=False, graph_attr=graph_attr):
    client = Client("Client Side")
    react = React("React")
    js = Javascript("JavasScript")
    server = Windows("Windows Server")
    gitlab = Gitlab("GitLab")

    with Cluster("Server Side"):
        windows = [Resource("IIS"),
                   EC2("WFastCGI"),
                   Django("Django")]

    py = Python("Python")
    mssql = MSSQL("Database")

    client >> react >> js >> server >> windows
    windows - py - mssql
    js - gitlab
    py - gitlab
