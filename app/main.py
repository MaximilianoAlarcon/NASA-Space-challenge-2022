from flask import Flask
from flask import request
from flask.templating import render_template


import os, pandas as pd

import sys


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == 'GET':
		table_results = []
		table_results.append({
			"mat":"",
			"type":"",
			"volume":"",
			"mass":"",
		})
		table_results.append({
			"mat":"",
			"type":"",
			"volume":"",
			"mass":"",
		})
		table_results.append({
			"mat":"",
			"type":"",
			"volume":"",
			"mass":"",
		})
		return (render_template('index.html',table_results=table_results))
	if request.method == 'POST':

		table_results = []

		metal_element = request.form["metal-element"]
		metal_volume = request.form["metal-volume"]
		df_metals_densities = pd.read_excel("data/metals densities.xlsx")
		df_metals_densities.set_index(inplace=True, keys=["mat"])
		metal_mass = 0
		if metal_element != "":
			metal_density = df_metals_densities.loc[metal_element]["density"]
			metal_mass = float(metal_volume)*float(metal_density)

		table_results.append({
			"mat":"Metal",
			"type":str(metal_element),
			"volume":str(round(float(metal_volume),2))+" cm3",
			"mass":str(round(float(metal_mass),2))+" gr",
		})
		"""
		print("Metal")
		print("="*64)
		print("element: "+str(metal_element))
		print("volume: "+str(metal_volume))
		print("mass: "+str(metal_mass))
		print("")
		"""

		plastic_element = request.form["plastic-filament"]
		plastic_volume = request.form["plastic-volume"]
		df_plastic_densities = pd.read_excel("data/plastic densities.xlsx")
		df_plastic_densities.set_index(inplace=True, keys=["mat"])
		plastic_mass = 0
		plastic_alias = ""
		if plastic_element != "":
			plastic_density = df_plastic_densities.loc[plastic_element]["density"]
			plastic_alias = df_plastic_densities.loc[plastic_element]["alias"]
			plastic_mass = float(plastic_volume)*float(plastic_density)


		table_results.append({
			"mat":"Plastic",
			"type":str(plastic_element),
			"volume":str(round(float(plastic_volume),2))+" cm3",
			"mass":str(round(float(plastic_mass),2))+" gr",
		})
		"""
		print("Plastic")
		print("="*64)
		print("fylament: "+str(plastic_alias))
		print("volume: "+str(plastic_volume))
		print("mass: "+str(plastic_mass))
		print("")
		"""

		concrete_volume = request.form["concrete-volume"]
		concrete_volume = float(concrete_volume)
		concrete_mass = 0
		if concrete_volume > 0:
			concrete_mass = 2300*concrete_volume

		table_results.append({
			"mat":"Concrete",
			"type":"Normal",
			"volume":str(round(float(concrete_volume),2))+" m3",
			"mass":str(round(float(concrete_mass),2))+" kg",
		})
		"""
		print("Concrete")
		print("volume: "+str(concrete_volume))
		print("mass: "+str(concrete_mass))
		"""


		return (render_template('index.html',table_results=table_results, 
			metal_element = metal_element,
			metal_volume = float(metal_volume),
			plastic_element = plastic_element,
			plastic_volume = float(plastic_volume),
			concrete_volume =float(concrete_volume)
			))

"""
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
"""