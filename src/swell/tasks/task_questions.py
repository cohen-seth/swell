# (C) Copyright 2021- United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration. All Rights Reserved.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.


# --------------------------------------------------------------------------------------------------


import os
from dataclasses import dataclass

from swell.utilities.swell_questions import SwellQuestion


# --------------------------------------------------------------------------------------------------
analysis_forecast_window_offset = SwellQuestion(
    name="analysis_forecast_window_offset",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="What is the duration from the middle of the window when forecasts start?",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

analysis_variables = SwellQuestion(
    name="analysis_variables",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="What are the analysis variables?",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

background_error_model = SwellQuestion(
    name="background_error_model",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="Which background error model do you want to use?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

background_experiment = SwellQuestion(
    name="background_experiment",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "all_models"
    ],
    prompt="What is the name of the name of the experiment providing the backgrounds?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

background_frequency = SwellQuestion(
    name="background_frequency",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "all_models"
    ],
    depends={
        "window_type": "4D"
    },
    prompt="What is the frequency of the background files?",
    dtype="iso-duration"
)


# --------------------------------------------------------------------------------------------------

background_time_offset = SwellQuestion(
    name="background_time_offset",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="How long before the middle of the analysis window did" +
    " the background providing forecast begin?",
    dtype="iso-duration"
)


# --------------------------------------------------------------------------------------------------

bundles = SwellQuestion(
    name="bundles",
    question_type="task",
    default_value=[
        "fv3-jedi",
        "soca",
        "iodaconv",
        "ufo"
    ],
    ask_question=True,
    options=[
        "fv3-jedi",
        "soca",
        "iodaconv",
        "ufo",
        "ioda",
        "oops",
        "saber"
    ],
    depends={
        "jedi_build_method": "create"
    },
    prompt="Which JEDI bundles do you wish to build?",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

cice6_domains = SwellQuestion(
    name="cice6_domains",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "geos_marine"
    ],
    prompt="Which CICE6 domains do you wish to run DA for?",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

clean_patterns = SwellQuestion(
    name="clean_patterns",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="Provide a list of patterns that you wish to remove from the cycle directory.",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

crtm_coeff_dir = SwellQuestion(
    name="crtm_coeff_dir",
    question_type="task",
    default_value="defer_to_platform",
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the path to the CRTM coefficient files?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

cycling_varbc = SwellQuestion(
    name="cycling_varbc",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "geos_atmosphere"
    ],
    prompt="Do you want to use cycling VarBC option?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

ensemble_hofx_packets = SwellQuestion(
    name="ensemble_hofx_packets",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Enter number of packets in which ensemble observers should be computed.",
    dtype="integer"
)


# --------------------------------------------------------------------------------------------------

ensemble_hofx_strategy = SwellQuestion(
    name="ensemble_hofx_strategy",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Enter hofx strategy.",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

ensemble_num_members = SwellQuestion(
    name="ensemble_num_members",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="How many members comprise the ensemble?",
    dtype="integer"
)


# --------------------------------------------------------------------------------------------------

ensmean_only = SwellQuestion(
    name="ensmean_only",
    question_type="task",
    default_value=False,
    options=[
        True,
        False
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="Calculate ensemble mean only?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

ensmeanvariance_only = SwellQuestion(
    name="ensmeanvariance_only",
    question_type="task",
    default_value=False,
    options=[
        True,
        False
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="Calculate ensemble mean and variance only?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

existing_geos_gcm_build_path = SwellQuestion(
    name="existing_geos_gcm_build_path",
    question_type="task",
    default_value="defer_to_platform",
    ask_question=True,
    depends={
        "geos_build_method": "use_existing"
    },
    prompt="What is the path to the existing GEOS build directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

existing_geos_gcm_source_path = SwellQuestion(
    name="existing_geos_gcm_source_path",
    question_type="task",
    default_value="defer_to_platform",
    ask_question=True,
    depends={
        "geos_build_method": "use_existing"
    },
    prompt="What is the path to the existing GEOS source code directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

existing_jedi_build_directory = SwellQuestion(
    name="existing_jedi_build_directory",
    question_type="task",
    default_value="defer_to_platform",
    ask_question=True,
    depends={
        "jedi_build_method": "use_existing"
    },
    prompt="What is the path to the existing JEDI build directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

existing_jedi_build_directory_pinned = SwellQuestion(
    name="existing_jedi_build_directory_pinned",
    question_type="task",
    default_value="defer_to_platform",
    ask_question=True,
    depends={
        "jedi_build_method": "use_pinned_existing"
    },
    prompt="What is the path to the existing pinned JEDI build directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

existing_jedi_source_directory = SwellQuestion(
    name="existing_jedi_source_directory",
    question_type="task",
    default_value="defer_to_platform",
    ask_question=True,
    depends={
        "jedi_build_method": "use_existing"
    },
    prompt="What is the path to the existing JEDI source code directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

existing_jedi_source_directory_pinned = SwellQuestion(
    name="existing_jedi_source_directory_pinned",
    question_type="task",
    default_value="defer_to_platform",
    ask_question=True,
    depends={
        "jedi_build_method": "use_pinned_existing"
    },
    prompt="What is the path to the existing pinned JEDI source code directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

forecast_duration = SwellQuestion(
    name="forecast_duration",
    question_type="task",
    default_value="PT12H",
    ask_question=True,
    prompt="GEOS forecast duration",
    dtype="iso-duration"
)


# --------------------------------------------------------------------------------------------------

generate_yaml_and_exit = SwellQuestion(
    name="generate_yaml_and_exit",
    question_type="task",
    default_value=False,
    prompt="Generate JEDI executable YAML and exit?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

geos_build_method = SwellQuestion(
    name="geos_build_method",
    question_type="task",
    default_value="create",
    ask_question=True,
    options=[
        "use_existing",
        "create"
    ],
    prompt="Do you want to use an existing GEOS build or create a new build?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

geos_experiment_directory = SwellQuestion(
    name="geos_experiment_directory",
    question_type="task",
    default_value="defer_to_platform",
    ask_question=True,
    prompt="What is the path to the GEOS restarts directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

geos_gcm_tag = SwellQuestion(
    name="geos_gcm_tag",
    question_type="task",
    default_value="v11.6.0",
    ask_question=True,
    prompt="Which GEOS tag do you wish to clone?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

geos_restarts_directory = SwellQuestion(
    name="geos_restarts_directory",
    question_type="task",
    default_value="defer_to_platform",
    ask_question=True,
    prompt="What is the path to the GEOS restarts directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

geos_x_background_directory = SwellQuestion(
    name="geos_x_background_directory",
    question_type="task",
    default_value="/dev/null/",
    ask_question=True,
    options=[
        "/dev/null/",
        "/gpfsm/dnb05/projects/p139/dao_it/archive/"
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the path to the GEOS X-backgrounds directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

geovals_experiment = SwellQuestion(
    name="geovals_experiment",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the name of the R2D2 experiment providing the GeoVaLs?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

geovals_provider = SwellQuestion(
    name="geovals_provider",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the name of the R2D2 database providing the GeoVaLs?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

gradient_norm_reduction = SwellQuestion(
    name="gradient_norm_reduction",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="What value of gradient norm reduction for convergence?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

gsibec_configuration = SwellQuestion(
    name="gsibec_configuration",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Which GSIBEC climatological or hybrid?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

horizontal_localization_lengthscale = SwellQuestion(
    name="horizontal_localization_lengthscale",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the length scale for horizontal covariance localization?",
    dtype="float"
)


# --------------------------------------------------------------------------------------------------

horizontal_localization_max_nobs = SwellQuestion(
    name="horizontal_localization_max_nobs",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the maximum number of observations to consider"
    + " for horizontal covariance localization?",
    dtype="integer"
)


# --------------------------------------------------------------------------------------------------

horizontal_localization_method = SwellQuestion(
    name="horizontal_localization_method",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Which localization scheme should be applied in the horizontal?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

horizontal_resolution = SwellQuestion(
    name="horizontal_resolution",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="What is the horizontal resolution for the forecast model and backgrounds?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

jedi_build_method = SwellQuestion(
    name="jedi_build_method",
    question_type="task",
    default_value="create",
    ask_question=True,
    options=[
        "use_existing",
        "use_pinned_existing",
        "create",
        "pinned_create"
    ],
    prompt="Do you want to use an existing JEDI build or create a new build?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

jedi_forecast_model = SwellQuestion(
    name="jedi_forecast_model",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "all_models"
    ],
    depends={
        "window_type": "4D"
    },
    prompt="What forecast model should be used within JEDI for 4D window propagation?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

local_ensemble_inflation_mult = SwellQuestion(
    name="local_ensemble_inflation_mult",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Specify the multiplicative prior inflation coefficient (0, inf].",
    dtype="float"
)


# --------------------------------------------------------------------------------------------------

local_ensemble_inflation_rtpp = SwellQuestion(
    name="local_ensemble_inflation_rtpp",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Specify the Relaxation To Prior Perturbation (RTPP) coefficient (0, 1].",
    dtype="float"
)


# --------------------------------------------------------------------------------------------------

local_ensemble_inflation_rtps = SwellQuestion(
    name="local_ensemble_inflation_rtps",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Specify the Relaxation To Prior Spread (RTPS) coefficient (0, 1].",
    dtype="float"
)


# --------------------------------------------------------------------------------------------------

local_ensemble_save_posterior_ensemble = SwellQuestion(
    name="local_ensemble_save_posterior_ensemble",
    question_type="task",
    default_value=False,
    options=[
        True,
        False
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="Save the posterior ensemble members?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

local_ensemble_save_posterior_ensemble_increments = SwellQuestion(
    name="local_ensemble_save_posterior_ensemble_increments",
    question_type="task",
    default_value=False,
    ask_question=True,
    options=[
        True,
        False
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="Save the posterior ensemble member increments?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

local_ensemble_save_posterior_mean = SwellQuestion(
    name="local_ensemble_save_posterior_mean",
    question_type="task",
    default_value=False,
    ask_question=True,
    options=[
        True,
        False
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="Save the posterior ensemble mean?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

local_ensemble_save_posterior_mean_increment = SwellQuestion(
    name="local_ensemble_save_posterior_mean_increment",
    question_type="task",
    default_value=True,
    ask_question=True,
    options=[
        True,
        False
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="Save the posterior ensemble mean increment?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

local_ensemble_solver = SwellQuestion(
    name="local_ensemble_solver",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Which local ensemble solver type should be implemented?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

local_ensemble_use_linear_observer = SwellQuestion(
    name="local_ensemble_use_linear_observer",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Which local ensemble solver type should be implemented?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

marine_models = SwellQuestion(
    name="marine_models",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "geos_marine"
    ],
    prompt="Enter the active SOCA models for this model.",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

minimizer = SwellQuestion(
    name="minimizer",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="Which data assimilation minimizer do you wish to use?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

mom6_iau = SwellQuestion(
    name="mom6_iau",
    question_type="task",
    default_value="defer_to_model",
    options=[
        True,
        False
    ],
    models=[
        "geos_marine",
        "geos_ocean"
    ],
    prompt="Do you wish to use IAU for MOM6?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

npx_proc = SwellQuestion(
    name="npx_proc",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "geos_atmosphere"
    ],
    prompt="What number of processors do you wish to use in the x-direction?",
    dtype="integer"
)


# --------------------------------------------------------------------------------------------------

npy_proc = SwellQuestion(
    name="npy_proc",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "geos_atmosphere"
    ],
    prompt="What number of processors do you wish to use in the y-direction?",
    dtype="integer"
)


# --------------------------------------------------------------------------------------------------

number_of_iterations = SwellQuestion(
    name="number_of_iterations",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="What number of iterations do you wish to use for each outer loop?" +
    " Provide a list of integers the same length as the number of outer loops.",
    dtype="integer-list"
)


# --------------------------------------------------------------------------------------------------

obs_experiment = SwellQuestion(
    name="obs_experiment",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "all_models"
    ],
    prompt="What is the database providing the observations?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

obs_provider = SwellQuestion(
    name="obs_provider",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "all_models"
    ],
    prompt="Which group(s) provide the observations?",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

observations = SwellQuestion(
    name="observations",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="Which observations do you want to include?",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

observing_system_records_mksi_path = SwellQuestion(
    name="observing_system_records_mksi_path",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the path to the GSI formatted observing system records?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

observing_system_records_mksi_path_tag = SwellQuestion(
    name="observing_system_records_mksi_path_tag",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the GSI formatted observing system records tag?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

observing_system_records_path = SwellQuestion(
    name="observing_system_records_path",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the path to the Swell formatted observing system records?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

path_to_ensemble = SwellQuestion(
    name="path_to_ensemble",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the path to where ensemble members are stored?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

path_to_geos_adas_background = SwellQuestion(
    name="path_to_geos_adas_background",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the path to where the cubed sphere backgrounds are in the GEOSadas run?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

path_to_gsi_bc_coefficients = SwellQuestion(
    name="path_to_gsi_bc_coefficients",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the location where GSI bias correction files can be found?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

path_to_gsi_nc_diags = SwellQuestion(
    name="path_to_gsi_nc_diags",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the path to where the GSI ncdiags are stored?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

produce_geovals = SwellQuestion(
    name="produce_geovals",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options=[
        True,
        False
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="When running the ncdiag to ioda converted do you want to produce GeoVaLs files?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

r2d2_local_path = SwellQuestion(
    name="r2d2_local_path",
    question_type="task",
    default_value="defer_to_platform",
    prompt="What is the path to the R2D2 local directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

save_geovals = SwellQuestion(
    name="save_geovals",
    question_type="task",
    default_value=False,
    options=[
        True,
        False
    ],
    prompt="When running hofx do you want to output the GeoVaLs?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

single_observations = SwellQuestion(
    name="single_observations",
    question_type="task",
    default_value=False,
    options=[
        True,
        False
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="Is it a single-observation test?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

skip_ensemble_hofx = SwellQuestion(
    name="skip_ensemble_hofx",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Which local ensemble solver type should be implemented?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

swell_static_files = SwellQuestion(
    name="swell_static_files",
    question_type="task",
    default_value="defer_to_platform",
    prompt="What is the path to the Swell Static files directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

swell_static_files_user = SwellQuestion(
    name="swell_static_files_user",
    question_type="task",
    default_value="None",
    prompt="What is the path to the user provided Swell Static Files directory?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

total_processors = SwellQuestion(
    name="total_processors",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "geos_marine",
        "geos_ocean"
    ],
    prompt="What is the number of processors for JEDI?",
    dtype="integer"
)


# --------------------------------------------------------------------------------------------------

vertical_localization_apply_log_transform = SwellQuestion(
    name="vertical_localization_apply_log_transform",
    question_type="task",
    default_value=True,
    options=[
        True,
        False
    ],
    models=[
        "geos_atmosphere"
    ],
    prompt="Should a log (base 10) transformation be applied to vertical coordinate when" +
    " constructing vertical localization?",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

vertical_localization_function = SwellQuestion(
    name="vertical_localization_function",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Which localization scheme should be applied in the vertical?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

vertical_localization_ioda_vertical_coord = SwellQuestion(
    name="vertical_localization_ioda_vertical_coord",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Which coordinate should be used in constructing vertical localization?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

vertical_localization_ioda_vertical_coord_group = SwellQuestion(
    name="vertical_localization_ioda_vertical_coord_group",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="Which vertical coordinate group should be used in constructing vertical localization?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

vertical_localization_lengthscale = SwellQuestion(
    name="vertical_localization_lengthscale",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="What is the length scale for vertical covariance localization?",
    dtype="integer"
)


# --------------------------------------------------------------------------------------------------

vertical_localization_method = SwellQuestion(
    name="vertical_localization_method",
    question_type="task",
    default_value="defer_to_model",
    options="defer_to_model",
    models=[
        "geos_atmosphere"
    ],
    prompt="What localization scheme should be applied in constructing a vertical localization?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

vertical_resolution = SwellQuestion(
    name="vertical_resolution",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="What is the vertical resolution for the forecast model and background?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------

window_length = SwellQuestion(
    name="window_length",
    question_type="task",
    default_value="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="What is the duration for the data assimilation window?",
    dtype="iso-duration"
)


# --------------------------------------------------------------------------------------------------

window_offset = SwellQuestion(
    name="window_offset",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    models=[
        "all_models"
    ],
    prompt="What is the duration between the middle of the window and the beginning?",
    dtype="iso-duration"
)


# --------------------------------------------------------------------------------------------------

window_type = SwellQuestion(
    name="window_type",
    question_type="task",
    default_value="defer_to_model",
    ask_question=True,
    options=[
        "3D",
        "4D"
    ],
    models=[
        "all_models"
    ],
    prompt="Do you want to use a 3D or 4D (including FGAT) window?",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------
