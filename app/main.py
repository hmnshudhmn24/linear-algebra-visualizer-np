import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🔢 Linear Algebra Visualizer")
st.write("Visualize 2D matrix transformations using NumPy + Matplotlib.")

# Create a grid of vectors
x_vals = np.linspace(-2, 2, 20)
y_vals = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x_vals, y_vals)
orig_vectors = np.stack([X.flatten(), Y.flatten()], axis=1)

# User-defined transformation matrix
st.subheader("🎛️ Define Transformation Matrix")
a11 = st.number_input("a11", value=1.0)
a12 = st.number_input("a12", value=0.0)
a21 = st.number_input("a21", value=0.0)
a22 = st.number_input("a22", value=1.0)

transformation_matrix = np.array([[a11, a12], [a21, a22]])

# Apply transformation
transformed_vectors = orig_vectors @ transformation_matrix.T

# Plotting
st.subheader("📈 Vector Field Transformation")
fig, ax = plt.subplots(figsize=(8, 8))
ax.quiver(orig_vectors[:, 0], orig_vectors[:, 1],
          transformed_vectors[:, 0] - orig_vectors[:, 0],
          transformed_vectors[:, 1] - orig_vectors[:, 1],
          angles='xy', scale_units='xy', scale=1, color="blue", width=0.003)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_aspect('equal')
ax.grid(True)
st.pyplot(fig)