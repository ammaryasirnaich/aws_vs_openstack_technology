from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

import plotly.graph_objects as go


BASE_DIR = Path(__file__).resolve().parent
AWS_ICON_DIR = BASE_DIR / "aws-icons" / "light-bg"
OPENSTACK_ICON_DIR = BASE_DIR / "openstack-icons" / "new-icon"
OUTPUT_DIR = BASE_DIR / "out"


# High-level categories and sub-categories used in the diagrams
CATEGORY_CONFIG = {
    "iaas": {
        "title": "IaaS — Compute / Network / Storage",
        "subcats": {
            "compute": "Compute",
            "network": "Network",
            "storage": "Storage",
        },
    },
    "paas": {
        "title": "PaaS — Databases / Streaming / Analytics",
        "subcats": {
            "databases": "Databases",
            "streaming": "Streaming",
            "analytics": "Analytics",
        },
    },
    "caas": {
        "title": "CaaS — Containers",
        "subcats": {
            "containers": "Containers",
        },
    },
    "faas": {
        "title": "FaaS — Serverless",
        "subcats": {
                "serverless": "Serverless",
        },
    },
    "saas": {
        "title": "SaaS — End‑user / BI",
        "subcats": {
            "enduser_bi": "End‑user / BI",
        },
    },
}


# Services taken from aws_vs_openstack_services.txt, grouped into the
# normalized category / subcategory structure above.
SERVICES: Dict[str, Dict[str, Dict[str, List[str]]]] = {
    "aws": {
        "iaas": {
            "compute": [
                "EC2",
                "EC2 Auto Scaling",
                "Outposts",
                "Local Zones",
                "Wavelength",
            ],
            "network": [
                "VPC",
                "Transit Gateway",
                "Direct Connect",
                "Site-to-Site VPN",
                "Elastic IP",
                "NAT Gateway",
                "CloudFront",
                "Route 53",
            ],
            "storage": [
                "S3",
                "S3 Glacier",
                "EBS",
                "EFS",
                "FSx",
                "Storage Gateway",
                "Snow Family",
                "DataSync",
                "AWS Backup",
            ],
        },
        "paas": {
            "databases": [
                "RDS",
                "Aurora",
                "DynamoDB",
                "ElastiCache",
                "MemoryDB for Redis",
                "DocumentDB",
                "Neptune",
                "Keyspaces",
            ],
            "streaming": [
                "Kinesis",
                "MSK",
            ],
            "analytics": [
                "Redshift",
                "OpenSearch Service",
                "EMR",
                "AWS Glue",
                "Athena",
                "Lake Formation",
                "DataBrew",
            ],
        },
        "caas": {
            "containers": [
                "ECS",
                "EKS",
                "Fargate",
                "ECR",
                "EKS Anywhere",
                "App Mesh",
                "Lightsail containers",
            ],
        },
        "faas": {
            "serverless": [
                "Lambda",
                "Step Functions",
                "EventBridge",
                "API Gateway",
                "AppSync",
                "Lambda@Edge",
                "CloudFront Functions",
            ],
        },
        "saas": {
            "enduser_bi": [
                "QuickSight",
                "Amazon Connect",
                "WorkDocs",
                "WorkMail",
                "WorkSpaces",
                "WorkSpaces Secure Browser",
                "WorkSpaces applications / AppStream 2.0",
                "AWS Wickr",
                "Amazon Managed Grafana",
                "Amazon Chime",
            ],
        },
    },
    "openstack": {
        "iaas": {
            "compute": [
                "Nova",
                "Ironic",
                "Cyborg",
                "Placement",
            ],
            "network": [
                "Neutron",
                "Octavia",
                "Designate",
            ],
            "storage": [
                "Swift",
                "Cinder",
                "Manila",
                "Freezer",
            ],
        },
        "paas": {
            "databases": [
                "Trove",
                "Barbican",
            ],
            "streaming": [
                "Zaqar",
            ],
            "analytics": [
                "Telem. / Ceilometer",
                "Aodh",
                "Aetos",
                "Venus",
                "Cloudkitty",
                "Watcher",
                "Vitrage",
            ],
        },
        "caas": {
            "containers": [
                "Magnum",
                "Zun",
            ],
        },
        "faas": {
            # No core OpenStack FaaS; keep a placeholder to highlight the gap.
            "serverless": [
                "No native FaaS (use Knative / OpenFaaS on Kubernetes)",
            ],
        },
        "saas": {
            "enduser_bi": [
                "Horizon",
                "Skyline",
            ],
        },
    },
}


# Map logical service names to specific icon files on disk.
AWS_SERVICE_ICON_MAP: Dict[str, str] = {
    # IaaS
    "EC2": "Amazon_Elastic_Compute_Cloud_(Amazon_EC2).png",
    "EC2 Auto Scaling": "Amazon_EC2\u000bAuto_Scaling.png",
    "Outposts": "AWS_Outposts_Family.png",
    "Local Zones": "AWS_Local_Zones.png",
    "Wavelength": "AWS_Wavelength.png",
    "VPC": "Amazon_Virtual_Private_Cloud_(Amazon_VPC).png",
    "Transit Gateway": "AWS_Transit_Gateway.png",
    "Direct Connect": "AWS_Direct_Connect.png",
    "Site-to-Site VPN": "AWS_Site-to-Site_VPN.png",
    "Elastic IP": "Amazon_Virtual_Private_Cloud_(Amazon_VPC).png",
    "NAT Gateway": "NAT_gateway.png",
    "CloudFront": "Amazon_CloudFront.png",
    "Route 53": "Amazon_Route_53.png",
    "S3": "Amazon_Simple_Storage_Service_(Amazon_S3).png",
    "S3 Glacier": "Amazon_S3_Glacier.png",
    "EBS": "Amazon_Elastic_Block_Store_(Amazon_EBS).png",
    "EFS": "Amazon_Elastic_File_System_(Amazon_EFS).png",
    "FSx": "Amazon_FSx.png",
    "Storage Gateway": "AWS_Storage\u000bGateway.png",
    "Snow Family": "AWS_Snowball.png",
    "DataSync": "AWS_DataSync.png",
    "AWS Backup": "AWS_Backup.png",
    # PaaS
    "RDS": "Amazon_Relational_Database_Service_(Amazon_RDS).png",
    "Aurora": "Amazon_Aurora.png",
    "DynamoDB": "Amazon_DynamoDB.png",
    "ElastiCache": "Amazon_ElastiCache.png",
    "MemoryDB for Redis": "Amazon_MemoryDB.png",
    "DocumentDB": "Amazon_DocumentDB_\u000b(with_MongoDB_compatibility).png",
    "Neptune": "Amazon_Neptune.png",
    "Keyspaces": "Amazon_Keyspaces_\u000b(for_Apache_Cassandra).png",
    "Redshift": "Amazon_Redshift.png",
    "OpenSearch Service": "Amazon_OpenSearch_Service.png",
    "EMR": "Amazon_EMR.png",
    "AWS Glue": "AWS_Glue.png",
    "Athena": "Amazon_Athena.png",
    "Lake Formation": "AWS_Lake_Formation.png",
    "DataBrew": "AWS_Glue_DataBrew.png",
    "Kinesis": "Amazon_Kinesis.png",
    "MSK": "Amazon_Managed_Streaming_for_Apache_Kafka\u000b(Amazon_MSK).png",
    # CaaS
    "ECS": "Amazon_Elastic_Container_Service_(Amazon_ECS).png",
    "EKS": "Amazon_Elastic_Kubernetes_Service_(Amazon_EKS).png",
    "Fargate": "AWS_Fargate.png",
    "ECR": "Amazon_Elastic_Container_Registry_(Amazon_ECR).png",
    "EKS Anywhere": "Amazon_EKS_Anywhere.png",
    "App Mesh": "AWS_App_Mesh.png",
    "Lightsail containers": "Amazon_Lightsail.png",
    # FaaS
    "Lambda": "AWS_Lambda.png",
    "Step Functions": "AWS_Step_Functions.png",
    "EventBridge": "Amazon_EventBridge.png",
    "API Gateway": "Amazon_API_Gateway.png",
    "AppSync": "AWS_AppSync.png",
    "Lambda@Edge": "Amazon_CloudFront.png",
    "CloudFront Functions": "Amazon_CloudFront.png",
    # SaaS
    "QuickSight": "Amazon_QuickSight.png",
    "Amazon Connect": "Amazon_Connect.png",
    "WorkDocs": "Amazon_WorkDocs.png",
    "WorkMail": "Amazon_WorkMail.png",
    "WorkSpaces": "Amazon_WorkSpaces.png",
    "WorkSpaces Secure Browser": "Amazon_WorkSpaces_Secure_Browser.png",
    "WorkSpaces applications / AppStream 2.0": "Amazon_AppStream_2.0.png",
    "AWS Wickr": "AWS_Wickr.png",
    "Amazon Managed Grafana": "Amazon_Managed_Grafana.png",
    "Amazon Chime": "Amazon_Chime.png",
}


OPENSTACK_SERVICE_ICON_MAP: Dict[str, str] = {
    "Keystone": "keystone.png",
    "Glance": "glance.png",
    "Placement": "placement.png",
    "Nova": "nova.png",
    "Ironic": "ironic.png",
    "Cyborg": "cyborg.png",
    "Neutron": "neutron.png",
    "Octavia": "octavia.png",
    "Designate": "designate.png",
    "Swift": "swift.png",
    "Cinder": "cinder.png",
    "Manila": "manila.png",
    "Freezer": "freezer.png",
    "Heat": "heat.png",
    "Mistral": "mistral.png",
    "Trove": "trove.png",
    "Zaqar": "zaqar.png",
    "Barbican": "barbican.png",
    "Aodh": "aodh.png",
    "Cloudkitty": "cloudkitty.png",
    "Watcher": "watcher.png",
    "Vitrage": "vitrage.png",
    "Magnum": "magnum.png",
    "Zun": "zun.png",
    "Horizon": "horizon.png",
    "Skyline": "openstack-diagram.png",
    "Storlets": "storlets.png",
    "Masakari": "masakari.png",
}


def _icon_path(platform: str, service: str) -> Path | None:
    if platform == "aws":
        filename = AWS_SERVICE_ICON_MAP.get(service)
        base = AWS_ICON_DIR
    else:
        filename = OPENSTACK_SERVICE_ICON_MAP.get(service)
        base = OPENSTACK_ICON_DIR

    if not filename:
        return None

    path = base / filename
    return path if path.exists() else None


def build_category_sankey(category_key: str) -> go.Figure:
    """
    Build a single Sankey diagram for one category (IaaS/PaaS/CaaS/FaaS/SaaS)
    showing AWS and OpenStack services side by side.
    """
    category_cfg = CATEGORY_CONFIG[category_key]
    subcats = category_cfg["subcats"]

    node_labels: List[str] = []
    node_colors: List[str] = []
    node_columns: List[int] = []
    node_icons: Dict[int, Path] = {}

    links_source: List[int] = []
    links_target: List[int] = []
    links_value: List[float] = []

    def add_node(label: str, column: int, color: str = "#CCCCCC", icon: Path | None = None) -> int:
        idx = len(node_labels)
        node_labels.append(label)
        node_colors.append(color)
        node_columns.append(column)
        if icon is not None:
            node_icons[idx] = icon
        return idx

    # Platform roots
    aws_root = add_node("AWS", column=0, color="#FF9900")
    os_root = add_node("OpenStack", column=0, color="#ED1944")

    subcat_nodes: Dict[Tuple[str, str], int] = {}

    # Add subcategory nodes and connect platform -> subcategory
    for platform, root_idx, color in [
        ("aws", aws_root, "#FDBF50"),
        ("openstack", os_root, "#F78194"),
    ]:
        if platform not in SERVICES:
            continue
        platform_services = SERVICES[platform]
        if category_key not in platform_services:
            continue

        for subcat_key, subcat_label in subcats.items():
            services = platform_services[category_key].get(subcat_key, [])
            if not services:
                continue

            label = f"{subcat_label} ({'AWS' if platform == 'aws' else 'OpenStack'})"
            subcat_idx = add_node(label, column=1, color=color)
            subcat_nodes[(platform, subcat_key)] = subcat_idx

            links_source.append(root_idx)
            links_target.append(subcat_idx)
            links_value.append(max(1, len(services)))

    # Add service nodes and connect subcategory -> service
    for platform in ("aws", "openstack"):
        if platform not in SERVICES:
            continue
        platform_services = SERVICES[platform]
        if category_key not in platform_services:
            continue

        for subcat_key, subcat_label in subcats.items():
            services = platform_services[category_key].get(subcat_key, [])
            if not services:
                continue

            subcat_idx = subcat_nodes[(platform, subcat_key)]

            for service in services:
                icon = _icon_path(platform, service)
                idx = add_node(service, column=2, color="#A0A0A0", icon=icon)

                links_source.append(subcat_idx)
                links_target.append(idx)
                links_value.append(1.0)

    # Column-based layout: we place nodes in three vertical columns.
    node_x: List[float] = [0.0] * len(node_labels)
    node_y: List[float] = [0.0] * len(node_labels)

    columns = {0: [], 1: [], 2: []}
    for idx, col in enumerate(node_columns):
        columns[col].append(idx)

    x_for_col = {0: 0.05, 1: 0.35, 2: 0.75}
    for col, indices in columns.items():
        n = len(indices)
        if n == 0:
            continue
        for i, idx in enumerate(indices):
            # Evenly space nodes in the column
            y = (i + 1) / (n + 1)
            node_x[idx] = x_for_col[col]
            node_y[idx] = y

    sankey = go.Sankey(
        arrangement="snap",
        node=dict(
            pad=20,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=node_labels,
            color=node_colors,
            x=node_x,
            y=node_y,
        ),
        link=dict(
            source=links_source,
            target=links_target,
            value=links_value,
        ),
    )

    fig = go.Figure(data=[sankey])
    fig.update_layout(
        title_text=f"AWS vs OpenStack — {category_cfg['title']}",
        font=dict(size=12),
    )

    # Overlay icons near the corresponding service nodes (where available)
    images = []
    for idx, icon_path in node_icons.items():
        # Slightly shrink icons; coordinates are in [0, 1] paper space.
        images.append(
            dict(
                source=str(icon_path),
                xref="paper",
                yref="paper",
                x=node_x[idx],
                y=node_y[idx],
                sizex=0.08,
                sizey=0.08,
                xanchor="center",
                yanchor="middle",
                layer="above",
            )
        )

    if images:
        fig.update_layout(images=images)

    return fig


def main() -> None:
    """
    Generate one SVG Sankey diagram per category (IaaS, PaaS, CaaS, FaaS, SaaS)
    comparing AWS and OpenStack services, with icons overlaid where available.

    Requires:
        pip install plotly kaleido
    """
    OUTPUT_DIR.mkdir(exist_ok=True)

    for category_key in CATEGORY_CONFIG.keys():
        fig = build_category_sankey(category_key)
        out_path = OUTPUT_DIR / f"sankey_{category_key}_aws_openstack.svg"
        print(f"Writing {out_path} ...")
        fig.write_image(str(out_path), format="svg")


if __name__ == "__main__":
    main()

