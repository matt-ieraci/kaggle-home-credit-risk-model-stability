.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y home_credit || :
	@pip install -e .

#################### TESTS ###################
test_gcp_setup:
	# @pytest

# Data sources: targets for monthly data imports
# ML_DIR=~/.lewagon/mlops
# HTTPS_DIR=https://storage.googleapis.com/datascience-mlops/taxi-fare-ny/
# GS_DIR=gs://datascience-mlops/taxi-fare-ny

