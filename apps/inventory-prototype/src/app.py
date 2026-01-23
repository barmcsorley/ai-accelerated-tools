import streamlit as st
import docker
import pandas as pd

# Page Config
st.set_page_config(page_title="Home Lab Inventory", page_icon="🐳", layout="wide")

st.title("🐳 Home Lab Inventory")
st.markdown("Watching local Docker Engine via `/var/run/docker.sock`")

try:
    # Connect to Docker Socket (Mounted from your Mac/NAS)
    client = docker.from_env()
    
    # Get Containers
    containers = client.containers.list(all=True)
    
    if not containers:
        st.warning("No containers found! (Is the socket mounted correctly?)")
    else:
        # Metrics
        running = len([c for c in containers if c.status == 'running'])
        total = len(containers)
        
        col1, col2 = st.columns(2)
        col1.metric("Containers Online", running)
        col2.metric("Total Containers", total)
        
        # Data Table
        data = []
        for c in containers:
            data.append({
                "Name": c.name,
                "Status": c.status,
                "Image": c.image.tags[0] if c.image.tags else c.image.id[:12],
                "ID": c.short_id
            })
            
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"⚠️ Could not connect to Docker Daemon.")
    st.code(str(e))
    st.info("Tip: Ensure '/var/run/docker.sock' is mounted in your docker-compose.yml")