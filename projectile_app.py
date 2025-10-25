import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- PAGE SETUP ---
st.title("🎯 Projectile Motion Visualizer")
st.write("Explore how angle and velocity affect the trajectory of a projectile.")

# --- USER INPUTS ---
v0 = st.slider("Initial velocity (m/s)", 0.0, 100.0, 20.0, 1.0)
angle_deg = st.slider("Launch angle (°)", 0.0, 90.0, 45.0, 1.0)
g = 9.8  # acceleration due to gravity (m/s²)

# --- CALCULATIONS ---
theta = np.radians(angle_deg)
t_flight = 2 * v0 * np.sin(theta) / g
t = np.linspace(0, t_flight, 100)
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# --- PLOT ---
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Horizontal distance (m)")
ax.set_ylabel("Vertical height (m)")
ax.set_title("Projectile Trajectory")
ax.grid(True)

st.pyplot(fig)

# --- OUTPUT METRICS ---
st.write(f"**Time of flight:** {t_flight:.2f} s")
st.write(f"**Maximum height:** {(v0**2 * np.sin(theta)**2) / (2*g):.2f} m")
st.write(f"**Range:** {(v0**2 * np.sin(2*theta)) / g:.2f} m")

st.caption("Built with Streamlit and Python — by a physics teacher ✨")

st.markdown("---")  # optional separator
st.header("💎 Upgrade to Premium")

# Replace the URL with your actual Gumroad link
gumroad_url = "https://congonsalves.gumroad.com/l/projectilemotion?_gl=1*1nnxrnq*_ga*MTQ4MTQ0MDQ4LjE3NjE0MjgyODY.*_ga_6LJN6D94N6*czE3NjE0MjgyODUkbzEkZzEkdDE3NjE0MzMwMTQkajYwJGwwJGgw"

if st.button("🚀 Get the Premium Version on Gumroad"):
    # Open the link in a new browser tab
    js = f"window.open('{gumroad_url}')"
    st.components.v1.html(f"<script>{js}</script>")
