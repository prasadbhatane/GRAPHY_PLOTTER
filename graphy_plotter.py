# Created By : Prasad Bhatane #

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Dictionary used to map string into valid string
to_be_replaced = {
	'sin' : "np.sin",
	'cos' : 'np.cos',
	'log' : 'np.log',
	'tan' : "np.tan",
	'^' : "**",
	'exp' : 'np.exp',
	'sqrt' : 'np.sqrt'
}

st.title("GRAPHY PLOTTER")
if st.checkbox("Show User Guide", False, key='123'):	#User Guide
	st.markdown("- GRAPHY PLOTTER is an app that lets you plot as many equations you want on the same graph")
	st.markdown("- Look into sidebar to enter the no. of equations you want to plot")
	st.markdown("- As you enter the number it creates a text box where you can type your equation in x")
	st.markdown("- After entering all equations you have to click on SHOW GRAPH button")
	st.markdown("- You can also adjust the range of x variable by checking Enter The X Range in sidebar")
	st.markdown("- Once you read all instructions above, you may want to uncheck the SHhow User Guide")

st.sidebar.title("GRAPHY PLOTTER : MENU")          # Sidebar title

# Defaut values of x
X_from = -100 
X_to = 100

if st.sidebar.checkbox("Enter The X Range", False, key='1'):
	X_from = st.sidebar.number_input(label="X_from", format="%.0f", value=-100)
	X_to = st.sidebar.number_input(label="X_to", format="%.0f", value=100)

x = np.linspace(X_from, X_to)


st.sidebar.markdown("### How many Equations you want to plot ?")
n_eqn = st.sidebar.number_input(label="", format="%.0f", value=0, min_value=0)
eqn_arr = [None] * n_eqn
for i in range(n_eqn):
	eqn_arr[i] = st.sidebar.text_input("Equation {}".format(i+1), "")


	

show_graph_button = st.sidebar.button("SHOW GRAPH")
if show_graph_button:
	try:
		for ind in range(len(eqn_arr)):
			lb = str(eqn_arr[ind])
			if eqn_arr[ind].isnumeric():
				eqn_arr[ind] = "0*x + {}".format(eqn_arr[ind])
			for old_keyword in to_be_replaced:
				eqn_arr[ind] = eqn_arr[ind].replace(old_keyword, to_be_replaced[old_keyword])
			plt.plot(x, eval(eqn_arr[ind]), label=lb)
	except SyntaxError:
		st.markdown("### 🔔  Please enter a valid equation in Equation Box {} !!!!".format(ind+1))   # Notification 
	
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.legend()
	plt.title("Total : {} Equations".format(len(eqn_arr)))
	st.pyplot()
else:
	st.markdown("### Click on the SHOW GRAPH in the sidebar")
