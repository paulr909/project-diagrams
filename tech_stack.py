from diagrams import Diagram
from diagrams.generic.os import Ubuntu
from diagrams.onprem.client import Client
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.vcs import Github
from diagrams.programming.framework import Django, React
from diagrams.programming.language import Python, Javascript

graph_attr = {"fontsize": "24", "bgcolor": "white"}

with Diagram("Technology Stack", show=False, graph_attr=graph_attr):
    fe = Client("Front End")
    react = React("React")
    js = Javascript("JavaScript")
    server = Ubuntu("Ubuntu Server")
    github = Github("GitHub")
    py = Python("Python")
    django = Django("Django")
    sql = PostgreSQL("Database")

    fe - react - js - server
    server - py - django
    server - sql
    js - github
    django - github
