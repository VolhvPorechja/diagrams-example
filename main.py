from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.network import Istio
from diagrams.onprem.network import Nginx
from diagrams.programming.language import Go, Python
from diagrams.saas.cdn import Cloudflare

from pathlib import Path

IMAGES_FOLDER = "./images"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with Diagram("Advanced Web Service with On-Premise", show=False):
        cloudflare = Cloudflare("Cloudflare")

        with Cluster("Cloud"):
            with Cluster("ingress"):
                istio_gw = Istio("Istio Gateway")

            with Cluster("Client Back"):
                istion_vs = Istio("Istio VirtualService")

                nginx = Nginx("gateway")

                with Cluster("Custom Gateway"):
                    gateway_go = Go("gateway-service")

                with Cluster("Users Pod"):
                    user_info = Python("users-service")

                with Cluster("Receipts Pod"):
                    support_hints = Python("receipts-service")

        cloudflare >> istio_gw >> istion_vs >> nginx >> gateway_go
        nginx >> Edge(color="orange") >> user_info
        nginx >> Edge(color="orange") >> support_hints
        gateway_go >> user_info
        gateway_go >> support_hints

    images_folder = Path(IMAGES_FOLDER)
    current_folder = Path(".")
    for file in current_folder.glob("*.png"):
        file.rename(images_folder / file.relative_to(current_folder))
