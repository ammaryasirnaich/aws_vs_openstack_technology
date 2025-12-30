from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='AWS vs OpenStack Layered Stack Diagram', format='png')
dot.attr(rankdir='TB')  # Top to bottom

# AWS Swimlane
with dot.subgraph(name='cluster_aws') as aws:
    aws.attr(label='AWS', style='filled', color='lightblue')

    # SaaS Layer
    with aws.subgraph(name='cluster_aws_saas') as saas:
        saas.attr(label='SaaS', style='filled', color='lightcyan')
        saas.node('QuickSight', 'QuickSight\nWorkSpaces')

    # CaaS Layer
    with aws.subgraph(name='cluster_aws_caas') as caas:
        caas.attr(label='CaaS', style='filled', color='lightcyan')
        caas.node('ECS', 'ECS\nEKS\nECR')

    # FaaS Layer
    with aws.subgraph(name='cluster_aws_faas') as faas:
        faas.attr(label='FaaS', style='filled', color='lightgreen')
        faas.node('Lambda', 'AWS Lambda\nStep Functions\nEventBridge')

    # PaaS Layer
    with aws.subgraph(name='cluster_aws_paas') as paas:
        paas.attr(label='PaaS', style='filled', color='lightcyan')
        paas.node('RDS', 'RDS\nAurora\nSageMaker')

    # IaaS Layer
    with aws.subgraph(name='cluster_aws_iaas') as iaas:
        iaas.attr(label='IaaS', style='filled', color='lightcyan')
        iaas.node('EC2', 'EC2\nVPC\nS3\nEBS')

# OpenStack Swimlane
with dot.subgraph(name='cluster_openstack') as os:
    os.attr(label='OpenStack', style='filled', color='lightcoral')

    # SaaS Layer
    with os.subgraph(name='cluster_os_saas') as saas:
        saas.attr(label='SaaS', style='filled', color='mistyrose')
        saas.node('Horizon', 'Horizon\nSkyline')

    # CaaS Layer
    with os.subgraph(name='cluster_os_caas') as caas:
        caas.attr(label='CaaS', style='filled', color='mistyrose')
        caas.node('Magnum', 'Magnum\nZun')

    # FaaS Layer - Highlight the gap
    with os.subgraph(name='cluster_os_faas') as faas:
        faas.attr(label='FaaS', style='filled', color='yellow')
        faas.node('Gap', 'No native FaaS\nLayered via Kubernetes\n(e.g., Knative)')

    # PaaS Layer
    with os.subgraph(name='cluster_os_paas') as paas:
        paas.attr(label='PaaS', style='filled', color='mistyrose')
        paas.node('Heat', 'Heat\nTrove\nMistral')

    # IaaS Layer
    with os.subgraph(name='cluster_os_iaas') as iaas:
        iaas.attr(label='IaaS', style='filled', color='mistyrose')
        iaas.node('Nova', 'Nova\nNeutron\nSwift\nCinder')

# Add edges to show layering (optional, for flow)
dot.edge('EC2', 'RDS', style='invis')
dot.edge('Nova', 'Heat', style='invis')
# Add a visible edge for the gap
dot.edge('Gap', 'Magnum', label='Depends on', color='red', style='dashed')

# Render the diagram
dot.render('aws_vs_openstack_diagram', view=False)</content>
<parameter name="filePath">/Users/a.y.naich/Downloads/aws_vs_openstack_technology/diagram.py