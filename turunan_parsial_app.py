import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("Aplikasi Interaktif: Turunan Parsial dan Bidang Singgung")
st.markdown("## 📊 Kasus Nyata: Tingkat Kepuasan Pelanggan Berdasarkan Harga & Kualitas")

st.latex(r""" S(x, y) = -x^2 + 4xy - y^2 + 10 """)

st.markdown("""
- **x** = Harga produk  
- **y** = Kualitas produk  
- **S(x, y)** = Tingkat kepuasan pelanggan  
""")

# Fungsi kasus nyata
x, y = sp.symbols('x y')
f = -x**2 + 4*x*y - y**2 + 10

# Turunan parsial
fx = sp.diff(f, x)
fy = sp.diff(f, y)

st.subheader("🔹 Turunan Parsial:")
st.latex(f"\\frac{{\\partial S}}{{\\partial x}} = {sp.latex(fx)}")
st.latex(f"\\frac{{\\partial S}}{{\\partial y}} = {sp.latex(fy)}")

st.subheader("🔹 Titik untuk Bidang Singgung:")
x0 = st.number_input("Nilai harga (x₀)", value=2.0)
y0 = st.number_input("Nilai kualitas (y₀)", value=3.0)

z0 = f.subs({x: x0, y: y0})
fx_val = fx.subs({x: x0, y: y0})
fy_val = fy.subs({x: x0, y: y0})

# Bidang singgung
tangent_plane = z0 + fx_val * (x - x0) + fy_val * (y - y0)

st.markdown("### 🟦 Persamaan Bidang Singgung:")
st.latex(f"z = {sp.latex(tangent_plane)}")

# Grafik 3D
x_vals = np.linspace(x0 - 5, x0 + 5, 50)
y_vals = np.linspace(y0 - 5, y0 + 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)
f_lambd = sp.lambdify((x, y), f, modules='numpy')
t_lambd = sp.lambdify((x, y), tangent_plane, modules='numpy')
Z = f_lambd(X, Y)
T = t_lambd(X, Y)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='coolwarm')
ax.plot_surface(X, Y, T, color='green', alpha=0.4)
ax.set_xlabel("Harga (x)")
ax.set_ylabel("Kualitas (y)")
ax.set_zlabel("Kepuasan (S)")
ax.set_title("Tingkat Kepuasan Pelanggan dan Bidang Singgung")

st.pyplot(fig)
