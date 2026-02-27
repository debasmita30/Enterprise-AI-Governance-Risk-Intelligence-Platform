import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import bcrypt
import json
import time
import requests
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

st.set_page_config(page_title="Enterprise AI Governance & Risk Intelligence Platform", layout="wide")

st.markdown("""
<style>
body { background-color: #0e1117; color: white; }
section[data-testid="stSidebar"] { background-color: #111827; }
div.stButton > button { background-color: #2563eb; color: white; border-radius: 8px; }
div.stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# ---------------- DATABASE ----------------

def init_db():
    conn = sqlite3.connect("tools.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            security REAL,
            data_residency REAL,
            compliance REAL,
            cost REAL,
            lock_in REAL,
            sla REAL,
            final_score REAL,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def clean_db():
    conn = sqlite3.connect("tools.db")
    c = conn.cursor()
    c.execute("DELETE FROM vendors WHERE name IS NULL OR name = ''")
    conn.commit()
    conn.close()

def insert_vendor(data):
    if data["name"].strip() == "":
        return
    conn = sqlite3.connect("tools.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO vendors
        (name, security, data_residency, compliance, cost, lock_in, sla, final_score, category)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        data["name"], data["security"], data["data_residency"],
        data["compliance"], data["cost"], data["lock_in"],
        data["sla"], data["final_score"], data["category"]
    ))
    conn.commit()
    conn.close()

def fetch_vendors():
    conn = sqlite3.connect("tools.db")
    c = conn.cursor()
    c.execute("SELECT * FROM vendors ORDER BY final_score ASC")
    rows = c.fetchall()
    conn.close()
    return rows

init_db()
clean_db()

# ---------------- AUTH ----------------

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

users = {
    "admin": hash_password("admin123"),
    "analyst": hash_password("analyst123"),
    "viewer": hash_password("viewer123")
}

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("AI Governance SaaS Platform")
    st.subheader("Secure Login")

    col1, col2 = st.columns(2)

    with col1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username in users and verify_password(password, users[username]):
                st.session_state.authenticated = True
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Invalid credentials")

    with col2:
        st.subheader("Demo Access")
        st.write("admin / admin123")
        st.write("analyst / analyst123")
        st.write("viewer / viewer123")
        if st.button("Enter as Admin"):
            st.session_state.authenticated = True
            st.session_state.user = "admin"
            st.rerun()

    st.stop()

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

st.sidebar.write("User:", st.session_state.user)

page = st.sidebar.selectbox(
    "Navigation",
    ["Executive Dashboard", "Vendor Evaluation", "Vendor Comparison", "API Benchmarking", "Leaderboard"]
)

# ---------------- EXECUTIVE DASHBOARD ----------------

if page == "Executive Dashboard":
    st.title("Executive AI Risk Dashboard")

    data = fetch_vendors()
    if len(data) == 0:
        st.info("No vendors evaluated yet.")
    else:
        df = pd.DataFrame(data, columns=[
            "ID","Name","Security","Data Residency","Compliance",
            "Cost","Lock-in","SLA","Final Score","Category","Created"
        ])

        total_vendors = len(df)
        avg_risk = round(df["Final Score"].mean(),2)
        lowest = df.iloc[0]["Name"]

        c1,c2,c3 = st.columns(3)
        c1.metric("Total Vendors Evaluated", total_vendors)
        c2.metric("Average Risk Score", avg_risk)
        c3.metric("Safest Vendor", lowest)

       
        chart_df = df.copy()
        chart_df["DisplayName"] = chart_df["Name"] + " (ID " + chart_df["ID"].astype(str) + ")"
        st.bar_chart(chart_df.set_index("DisplayName")["Final Score"])
# ---------------- VENDOR EVALUATION ----------------

if page == "Vendor Evaluation":
    st.title("Vendor Risk Evaluation Engine")

    if st.button("Load Default Vendor"):
        st.session_state.vendor_name = "OpenAI GPT-4"

    vendor_name = st.text_input("Vendor Name", value=st.session_state.get("vendor_name",""))

    encryption = st.checkbox("Encryption")
    audit = st.checkbox("Audit Logs")
    pii = st.checkbox("PII Protection")
    gdpr = st.checkbox("GDPR")
    soc2 = st.checkbox("SOC2")
    iso = st.checkbox("ISO27001")
    monthly_cost = st.number_input("Monthly Cost", min_value=0.0)
    budget = st.number_input("Budget", min_value=1.0)
    uptime = st.slider("Uptime %", 90.0, 100.0, 99.0)
    open_source = st.checkbox("Open Source")
    export = st.checkbox("Data Export")

    if st.button("Evaluate Vendor"):
        if vendor_name.strip()=="":
            st.error("Vendor name required.")
        else:
            sec = 100 - (30 if encryption else 0) - (30 if audit else 0) - (20 if pii else 0)
            comp = 100 - (30 if gdpr else 0) - (30 if soc2 else 0) - (30 if iso else 0)
            lock = 100 - (50 if open_source else 0) - (30 if export else 0)
            sla = 10 if uptime >= 99.9 else 40 if uptime >= 99 else 80

            sims = []
            for _ in range(300):
                fluct = np.random.normal(0, 0.1)
                ratio = (monthly_cost*(1+fluct))/budget
                sims.append(20 if ratio<=0.5 else 50 if ratio<=1 else 90)

            cost_score = np.mean(sims)
            final = round((sec+comp+lock+sla+cost_score)/5,2)
            cat = "Low" if final<=30 else "Moderate" if final<=60 else "High"

            insert_vendor({
                "name": vendor_name,
                "security": sec,
                "data_residency": 30,
                "compliance": comp,
                "cost": cost_score,
                "lock_in": lock,
                "sla": sla,
                "final_score": final,
                "category": cat
            })

            st.metric("Final Risk Score", final)
            st.metric("Risk Category", cat)

            st.subheader("Monte Carlo Cost Simulation")
            fig, ax = plt.subplots()
            ax.hist(sims, bins=20)
            st.pyplot(fig)

            st.subheader("Risk Radar Visualization")
            labels = ["Security","Compliance","Lock-in","SLA","Cost"]
            values = [sec, comp, lock, sla, cost_score]
            values += values[:1]
            angles = np.linspace(0,2*np.pi,len(labels),endpoint=False).tolist()
            angles += angles[:1]
            fig2 = plt.figure()
            ax2 = fig2.add_subplot(111,polar=True)
            ax2.plot(angles,values)
            ax2.fill(angles,values,alpha=0.25)
            ax2.set_xticks(angles[:-1])
            ax2.set_xticklabels(labels)
            st.pyplot(fig2)

            pdf_name = f"{vendor_name}_Executive_Report.pdf"
            doc = SimpleDocTemplate(pdf_name)
            elements=[]
            styles=getSampleStyleSheet()
            elements.append(Paragraph(f"Executive AI Risk Report - {vendor_name}",styles["Heading1"]))
            elements.append(Spacer(1,0.3*inch))
            table_data=[["Metric","Score"],["Final Risk",final],["Category",cat]]
            elements.append(Table(table_data))
            doc.build(elements)

            with open(pdf_name,"rb") as f:
                st.download_button("Download Executive PDF Report",f,file_name=pdf_name)

# ---------------- VENDOR COMPARISON ----------------

if page == "Vendor Comparison":
    st.title("Side-by-Side Vendor Comparison")

    data = fetch_vendors()
    if len(data)<2:
        st.info("Need at least 2 vendors.")
    else:
        df = pd.DataFrame(data, columns=[
            "ID","Name","Security","Data Residency","Compliance",
            "Cost","Lock-in","SLA","Final Score","Category","Created"
        ])

        v1 = st.selectbox("Select Vendor 1", df["Name"])
        v2 = st.selectbox("Select Vendor 2", df["Name"], index=1)

        d1 = df[df["Name"]==v1].iloc[0]
        d2 = df[df["Name"]==v2].iloc[0]

        comp_df = pd.DataFrame({
            "Metric":["Security","Compliance","Cost","Lock-in","SLA","Final Score"],
            v1:[d1["Security"],d1["Compliance"],d1["Cost"],d1["Lock-in"],d1["SLA"],d1["Final Score"]],
            v2:[d2["Security"],d2["Compliance"],d2["Cost"],d2["Lock-in"],d2["SLA"],d2["Final Score"]]
        })

        st.dataframe(comp_df)
        st.bar_chart(comp_df.set_index("Metric"))

# ---------------- API BENCHMARKING ----------------

if page == "API Benchmarking":
    st.title("Enterprise API Benchmarking")

    st.write("""
    This module simulates production-grade API benchmarking.
    It evaluates:
    - Latency performance
    - Stability (uptime probability)
    - Throughput capacity
    - SLA classification
    """)

    test_runs = st.slider("Number of Test Requests", 10, 500, 100)

    if st.button("Run Benchmark Simulation"):

        latencies = np.random.normal(loc=0.65, scale=0.15, size=test_runs)
        latencies = np.clip(latencies, 0.2, 2.0)

        avg_latency = round(np.mean(latencies), 3)
        p95_latency = round(np.percentile(latencies, 95), 3)
        uptime = round(np.random.uniform(96.5, 99.99), 2)
        throughput = round(np.random.uniform(120, 450), 2)

        sla_tier = (
            "Enterprise Grade"
            if uptime > 99.5
            else "Production Ready"
            if uptime > 98
            else "Degrading"
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Average Latency (s)", avg_latency)
        col2.metric("P95 Latency (s)", p95_latency)
        col3.metric("Uptime (%)", uptime)
        col4.metric("Throughput (req/min)", throughput)

        st.success(f"SLA Classification: {sla_tier}")

        st.subheader("Latency Distribution")
        fig, ax = plt.subplots()
        ax.hist(latencies, bins=20)
        ax.set_xlabel("Latency (seconds)")
        ax.set_ylabel("Request Count")
        st.pyplot(fig)

        st.subheader("System Health Summary")

        st.json({
            "Average Latency (seconds)": avg_latency,
            "P95 Latency (seconds)": p95_latency,
            "Uptime (%)": uptime,
            "Throughput (requests/minute)": throughput,
            "SLA Tier": sla_tier,
            "Status": "Healthy" if uptime > 98 else "Monitor"
        })

# ---------------- LEADERBOARD ----------------

if page == "Leaderboard":
    st.title("Vendor Leaderboard")

    data = fetch_vendors()
    if len(data) == 0:
        st.info("No vendors available.")
    else:
        df = pd.DataFrame(data, columns=[
            "ID","Name","Security","Data Residency","Compliance",
            "Cost","Lock-in","SLA","Final Score","Category","Created"
        ])

        df = df.sort_values("ID")

        # Latest evaluation per vendor
        latest_df = df.drop_duplicates("Name", keep="last")
        latest_df = latest_df.sort_values("Final Score").reset_index(drop=True)
        latest_df["Rank"] = latest_df.index + 1

        # ---------------- FILTER ----------------
        st.subheader("Filter Vendors")
        category_filter = st.selectbox(
            "Filter by Risk Category",
            ["All", "Low", "Moderate", "High"]
        )

        if category_filter != "All":
            filtered_df = latest_df[latest_df["Category"] == category_filter]
        else:
            filtered_df = latest_df.copy()

        # ---------------- COLOR CODING ----------------
        def color_category(val):
            if val == "Low":
                return "color: #22c55e; font-weight: bold;"
            elif val == "Moderate":
                return "color: #facc15; font-weight: bold;"
            else:
                return "color: #ef4444; font-weight: bold;"

        styled_df = filtered_df[["Rank","Name","Final Score","Category"]].style.map(
            color_category, subset=["Category"]
        )

        st.subheader("Current Vendor Rankings (Latest Evaluations)")
        st.dataframe(styled_df, width="stretch")

        # ---------------- CHART ----------------
        if len(filtered_df) > 0:
            st.subheader("Risk Comparison Chart")
            st.bar_chart(
                filtered_df.set_index("Name")["Final Score"]
            )

        # ---------------- DELETE / ROLLBACK ----------------
        st.subheader("Evaluation Management")

        selected_vendor = st.selectbox(
            "Select Vendor for Action",
            latest_df["Name"].unique()
        )

        col1, col2 = st.columns(2)

        # DELETE LATEST
        if col1.button("Delete Latest Evaluation"):
            conn = sqlite3.connect("tools.db")
            c = conn.cursor()
            c.execute("""
                DELETE FROM vendors
                WHERE id = (
                    SELECT id FROM vendors
                    WHERE name = ?
                    ORDER BY id DESC
                    LIMIT 1
                )
            """, (selected_vendor,))
            conn.commit()
            conn.close()
            st.success("Latest evaluation deleted.")
            st.rerun()

        # ROLLBACK (delete latest if more than 1 exists)
        if col2.button("Rollback to Previous Evaluation"):
            vendor_history = df[df["Name"] == selected_vendor]
            if len(vendor_history) > 1:
                conn = sqlite3.connect("tools.db")
                c = conn.cursor()
                c.execute("""
                    DELETE FROM vendors
                    WHERE id = (
                        SELECT id FROM vendors
                        WHERE name = ?
                        ORDER BY id DESC
                        LIMIT 1
                    )
                """, (selected_vendor,))
                conn.commit()
                conn.close()
                st.success("Rollback successful.")
                st.rerun()
            else:
                st.warning("No previous evaluation to rollback.")

        # ---------------- AUDIT TRAIL ----------------
        st.subheader("Evaluation History (Audit Trail)")
        st.dataframe(
            df[["ID","Name","Final Score","Category","Created"]],
            width="stretch"
        )