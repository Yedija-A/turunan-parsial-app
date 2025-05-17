import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("Aplikasi Turunan parsial")
st.markdown("## Studi Kasus: Analisis Biaya Produksi Berdasarkan Jumlah Tenaga Kerja dan Waktu Kerja")

st.latex(r""" C(x, y) = x^2 + y^2 + 2xy """)

# Input fungsi manual
st.subheader("Masukkan fungsi f(x, y):")
fungsi_input = st.text_input()

# Inisialisasi simbol
x, y = sp.symbols('x y')
try:
    f = sp.sympify(fungsi_input)
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    st.subheader("🔹 Turunan Parsial:")
    st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")

    st.subheader("🔹 Titik untuk Bidang Singgung:")
    x0 = st.number_input("Nilai x₀", value=1.0)
    y0 = st.number_input("Nilai y₀", value=1.0)

    z0 = f.subs({x: x0, y: y0})
    fx_val = fx.subs({x: x0, y: y0})
    fy_val = fy.subs({x: x0, y: y0})

    # Bidang singgung
    tangent_plane = z0 + fx_val * (x - x0) + fy_val * (y - y0)

    st.markdown("### 🟦 Persamaan Bidang Singgung:")
    st.latex(f"z = {sp.latex(tangent_plane)}")

    # Plot 3D
    x_vals = np.linspace(x0 - 5, x0 + 5, 50)
    y_vals = np.linspace(y0 - 5, y0 + 5, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    f_lambd = sp.lambdify((x, y), f, modules='numpy')
    t_lambd = sp.lambdify((x, y), tangent_plane, modules='numpy')
    Z = f_lambd(X, Y)
    T = t_lambd(X, Y)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis', label="Permukaan")
    ax.plot_surface(X, Y, T, color='red', alpha=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.set_title("Grafik 3D Permukaan & Bidang Singgung")

    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
