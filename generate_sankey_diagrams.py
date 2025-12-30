#!/usr/bin/env python3
"""
Generate Sankey diagrams for AWS and OpenStack services.
Shows flow: Category → Subcategory → Service
"""

import plotly.graph_objects as go
from parse_services import parse_aws_services, parse_openstack_services


def create_sankey_diagram(services_data: dict, platform_name: str) -> go.Figure:
    """
    Create a Sankey diagram from services data.
    
    Args:
        services_data: Dictionary with structure {Category: {Subcategory: [Services]}}
        platform_name: Name of the platform (AWS or OpenStack)
    
    Returns:
        Plotly figure object
    """
    # Build node lists and link data
    nodes = []
    node_labels = []
    source_indices = []
    target_indices = []
    values = []
    
    # Color scheme for categories
    category_colors = {
        "IaaS": "#FF9900",      # Orange
        "PaaS": "#146EB4",      # Blue
        "FaaS": "#D13212",      # Red
        "CaaS": "#232F3E",      # Dark gray
        "SaaS": "#8C4FFF"       # Purple
    }
    
    # Track node indices
    node_index_map = {}
    current_index = 0
    
    # First pass: create category nodes
    category_indices = {}
    for category in ["IaaS", "PaaS", "FaaS", "CaaS", "SaaS"]:
        if category in services_data and services_data[category]:
            node_labels.append(category)
            nodes.append({
                "color": category_colors.get(category, "#808080")
            })
            category_indices[category] = current_index
            node_index_map[f"category_{category}"] = current_index
            current_index += 1
    
    # Second pass: create subcategory nodes and links from categories
    subcategory_indices = {}
    for category, subcats in services_data.items():
        if not subcats:
            continue
        category_idx = category_indices[category]
        
        for subcat, services in subcats.items():
            if not services:
                continue
            
            # Create subcategory node
            subcat_key = f"{category}_{subcat}"
            if subcat_key not in subcategory_indices:
                node_labels.append(subcat)
                nodes.append({
                    "color": category_colors.get(category, "#808080")
                })
                subcategory_indices[subcat_key] = current_index
                node_index_map[subcat_key] = current_index
                current_index += 1
            
            # Link category to subcategory
            subcat_idx = subcategory_indices[subcat_key]
            source_indices.append(category_idx)
            target_indices.append(subcat_idx)
            values.append(len(services))  # Weight by number of services
    
    # Third pass: create service nodes and links from subcategories
    service_indices = {}
    for category, subcats in services_data.items():
        if not subcats:
            continue
        
        for subcat, services in subcats.items():
            if not services:
                continue
            
            subcat_key = f"{category}_{subcat}"
            subcat_idx = subcategory_indices[subcat_key]
            
            for service in services:
                # Clean service name (remove notes in parentheses)
                service_clean = service.split('(')[0].strip()
                if not service_clean or len(service_clean) < 2:
                    continue
                
                # Create service node
                service_key = f"{subcat_key}_{service_clean}"
                if service_key not in service_indices:
                    node_labels.append(service_clean)
                    nodes.append({
                        "color": category_colors.get(category, "#808080")
                    })
                    service_indices[service_key] = current_index
                    node_index_map[service_key] = current_index
                    current_index += 1
                
                # Link subcategory to service
                service_idx = service_indices[service_key]
                source_indices.append(subcat_idx)
                target_indices.append(service_idx)
                values.append(1)  # Each service gets weight 1
    
    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=node_labels,
            color=[node.get("color", "#808080") for node in nodes]
        ),
        link=dict(
            source=source_indices,
            target=target_indices,
            value=values,
            color="rgba(128, 128, 128, 0.4)"  # Light gray for links
        )
    )])
    
    # Update layout
    fig.update_layout(
        title_text=f"{platform_name} Services - Category → Subcategory → Service",
        font_size=12,
        height=1200,
        width=1800
    )
    
    return fig


def main():
    """Main function to generate Sankey diagrams."""
    # Parse services
    with open('aws_vs_openstack_services.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    aws_services = parse_aws_services(content)
    openstack_services = parse_openstack_services(content)
    
    # Generate AWS Sankey diagram
    print("Generating AWS Sankey diagram...")
    aws_fig = create_sankey_diagram(aws_services, "AWS")
    aws_fig.write_image("aws_sankey_diagram.svg", format="svg", width=1800, height=1200)
    print("✓ AWS diagram saved to aws_sankey_diagram.svg")
    
    # Generate OpenStack Sankey diagram
    print("Generating OpenStack Sankey diagram...")
    openstack_fig = create_sankey_diagram(openstack_services, "OpenStack")
    openstack_fig.write_image("openstack_sankey_diagram.svg", format="svg", width=1800, height=1200)
    print("✓ OpenStack diagram saved to openstack_sankey_diagram.svg")
    
    print("\nDone! SVG files are ready for import into Figma.")


if __name__ == "__main__":
    main()



