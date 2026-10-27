import os
from flask import Flask, render_template

app = Flask(__name__)

def get_simulated_cloud_resources():
   
    analyzed_resources = [
        {
            "name": "prod-api-server-01", 
            "type": "Compute Instance", 
            "status": "RUNNING", 
            "zone": "us-central1-a", 
            "recommendation": "OPTIMIZED (Right-sized)", 
            "savings": "$0.00"
        },
        {
            "name": "dev-legacy-app-vm", 
            "type": "Compute Instance", 
            "status": "RUNNING", 
            "zone": "us-central1-a", 
            "recommendation": "SCHEDULE AUTO-STOP (Idle outside work hours)", 
            "savings": "$65.50"
        },
        {
            "name": "old-backup-snapshot-disk", 
            "type": "Unattached Storage Disk", 
            "status": "UNATTACHED", 
            "zone": "us-central1-a", 
            "recommendation": "DELETE (Unused for 45 days)", 
            "savings": "$34.20"
        },
        {
            "name": "staging-db-replica", 
            "type": "Compute Instance", 
            "status": "STOPPED", 
            "zone": "us-central1-a", 
            "recommendation": "ARCHIVE / CLEANUP", 
            "savings": "$42.00"
        }
    ]
    return analyzed_resources

@app.route("/")
def dashboard():
    resources = get_simulated_cloud_resources()
    # حساب إجمالي التوفير المتوقع تلقائياً
    total_savings = sum([float(res["savings"].replace("$", "")) for res in resources])
    
    return render_template(
        "index.html", 
        resources=resources, 
        total_savings=round(total_savings, 2)
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)