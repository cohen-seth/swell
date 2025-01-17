# (C) Copyright 2021- United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration. All Rights Reserved.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.


# --------------------------------------------------------------------------------------------------


import os
from dataclasses import dataclass

from swell.utilities.swell_questions import QuestionList


# --------------------------------------------------------------------------------------------------

all_models = QuestionList(
    list_type="model_dependent",
    name="all_models",
    questions=[
        "analysis_forecast_window_offset",
        "analysis_variables",
        "background_error_model",
        "background_experiment",
        "background_frequency",
        "background_time_offset",
        "clean_patterns",
        "gradient_norm_reduction",
        "horizontal_resolution",
        "jedi_forecast_model",
        "minimizer",
        "number_of_iterations",
        "obs_experiment",
        "obs_provider",
        "observations",
        "vertical_resolution",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

geos_atmosphere = QuestionList(
    list_type="model_dependent",
    name="geos_atmosphere",
    questions=[
        "crtm_coeff_dir",
        "cycling_varbc",
        "ensemble_hofx_packets",
        "ensemble_hofx_strategy",
        "ensemble_num_members",
        "ensmean_only",
        "ensmeanvariance_only",
        "geos_x_background_directory",
        "geovals_experiment",
        "geovals_provider",
        "gsibec_configuration",
        "horizontal_localization_lengthscale",
        "horizontal_localization_max_nobs",
        "horizontal_localization_method",
        "local_ensemble_inflation_mult",
        "local_ensemble_inflation_rtpp",
        "local_ensemble_inflation_rtps",
        "local_ensemble_save_posterior_ensemble",
        "local_ensemble_save_posterior_ensemble_increments",
        "local_ensemble_save_posterior_mean",
        "local_ensemble_save_posterior_mean_increment",
        "local_ensemble_solver",
        "local_ensemble_use_linear_observer",
        "npx_proc",
        "npy_proc",
        "observing_system_records_mksi_path",
        "observing_system_records_mksi_path_tag",
        "observing_system_records_path",
        "path_to_ensemble",
        "path_to_geos_adas_background",
        "path_to_gsi_bc_coefficients",
        "path_to_gsi_nc_diags",
        "produce_geovals",
        "single_observations",
        "skip_ensemble_hofx",
        "vertical_localization_apply_log_transform",
        "vertical_localization_function",
        "vertical_localization_ioda_vertical_coord",
        "vertical_localization_ioda_vertical_coord_group",
        "vertical_localization_lengthscale",
        "vertical_localization_method"
    ]
)


# --------------------------------------------------------------------------------------------------

geos_marine = QuestionList(
    list_type="model_dependent",
    name="geos_marine",
    questions=[
        "cice6_domains",
        "marine_models",
        "mom6_iau",
        "total_processors"
    ]
)


# --------------------------------------------------------------------------------------------------

geos_ocean = QuestionList(
    list_type="model_dependent",
    name="geos_ocean",
    questions=[
        "mom6_iau",
        "total_processors"
    ]
)


# --------------------------------------------------------------------------------------------------

GetBackground = QuestionList(
    list_type="task",
    name="GetBackground",
    questions=[
        "analysis_forecast_window_offset",
        "background_experiment",
        "background_frequency",
        "horizontal_resolution",
        "r2d2_local_path",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

MoveDaRestart = QuestionList(
    list_type="task",
    name="MoveDaRestart",
    questions=[
        "analysis_forecast_window_offset",
        "mom6_iau",
        "window_length"
    ]
)


# --------------------------------------------------------------------------------------------------

PrepareAnalysis = QuestionList(
    list_type="task",
    name="PrepareAnalysis",
    questions=[
        "analysis_forecast_window_offset",
        "analysis_variables",
        "mom6_iau",
        "total_processors"
    ]
)


# --------------------------------------------------------------------------------------------------

StoreBackground = QuestionList(
    list_type="task",
    name="StoreBackground",
    questions=[
        "analysis_forecast_window_offset",
        "background_experiment",
        "background_frequency",
        "horizontal_resolution",
        "r2d2_local_path",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

GenerateBClimatology = QuestionList(
    list_type="task",
    name="GenerateBClimatology",
    questions=[
        "analysis_variables",
        "background_error_model",
        "generate_yaml_and_exit",
        "horizontal_resolution",
        "marine_models",
        "npx_proc",
        "npy_proc",
        "swell_static_files",
        "swell_static_files_user",
        "total_processors",
        "vertical_resolution",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediConvertStateSoca2ciceExecutable = QuestionList(
    list_type="task",
    name="RunJediConvertStateSoca2ciceExecutable",
    questions=[
        "analysis_variables",
        "cice6_domains",
        "generate_yaml_and_exit",
        "jedi_forecast_model",
        "marine_models",
        "observations",
        "total_processors",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediEnsembleMeanVariance = QuestionList(
    list_type="task",
    name="RunJediEnsembleMeanVariance",
    questions=[
        "analysis_variables",
        "ensemble_num_members",
        "generate_yaml_and_exit",
        "horizontal_resolution",
        "jedi_forecast_model",
        "npx_proc",
        "npy_proc",
        "observations",
        "observing_system_records_path",
        "vertical_resolution",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediFgatExecutable = QuestionList(
    list_type="task",
    name="RunJediFgatExecutable",
    questions=[
        "analysis_variables",
        "background_frequency",
        "background_time_offset",
        "crtm_coeff_dir",
        "generate_yaml_and_exit",
        "gradient_norm_reduction",
        "gsibec_configuration",
        "horizontal_resolution",
        "jedi_forecast_model",
        "marine_models",
        "minimizer",
        "npx_proc",
        "npy_proc",
        "number_of_iterations",
        "observations",
        "observing_system_records_path",
        "total_processors",
        "vertical_resolution",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediVariationalExecutable = QuestionList(
    list_type="task",
    name="RunJediVariationalExecutable",
    questions=[
        "analysis_variables",
        "background_frequency",
        "background_time_offset",
        "crtm_coeff_dir",
        "generate_yaml_and_exit",
        "gradient_norm_reduction",
        "gsibec_configuration",
        "horizontal_resolution",
        "jedi_forecast_model",
        "minimizer",
        "npx_proc",
        "npy_proc",
        "number_of_iterations",
        "observations",
        "observing_system_records_path",
        "total_processors",
        "vertical_resolution",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

GenerateBClimatologyByLinking = QuestionList(
    list_type="task",
    name="GenerateBClimatologyByLinking",
    questions=[
        "background_error_model",
        "horizontal_resolution",
        "swell_static_files",
        "swell_static_files_user",
        "vertical_resolution",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

GetBackgroundGeosExperiment = QuestionList(
    list_type="task",
    name="GetBackgroundGeosExperiment",
    questions=[
        "background_experiment",
        "background_time_offset",
        "geos_x_background_directory"
    ]
)


# --------------------------------------------------------------------------------------------------

LinkGeosOutput = QuestionList(
    list_type="task",
    name="LinkGeosOutput",
    questions=[
        "background_frequency",
        "marine_models",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediHofxEnsembleExecutable = QuestionList(
    list_type="task",
    name="RunJediHofxEnsembleExecutable",
    questions=[
        "background_frequency",
        "background_time_offset",
        "crtm_coeff_dir",
        "ensemble_hofx_packets",
        "ensemble_hofx_strategy",
        "ensemble_num_members",
        "generate_yaml_and_exit",
        "horizontal_resolution",
        "jedi_forecast_model",
        "npx_proc",
        "npy_proc",
        "observations",
        "total_processors",
        "vertical_resolution",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediHofxExecutable = QuestionList(
    list_type="task",
    name="RunJediHofxExecutable",
    questions=[
        "background_frequency",
        "background_time_offset",
        "crtm_coeff_dir",
        "generate_yaml_and_exit",
        "horizontal_resolution",
        "jedi_forecast_model",
        "npx_proc",
        "npy_proc",
        "observations",
        "observing_system_records_path",
        "save_geovals",
        "total_processors",
        "vertical_resolution",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediObsfiltersExecutable = QuestionList(
    list_type="task",
    name="RunJediObsfiltersExecutable",
    questions=[
        "background_frequency",
        "background_time_offset",
        "crtm_coeff_dir",
        "generate_yaml_and_exit",
        "horizontal_resolution",
        "jedi_forecast_model",
        "npx_proc",
        "npy_proc",
        "observations",
        "observing_system_records_path",
        "total_processors",
        "vertical_resolution",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

EvaObservations = QuestionList(
    list_type="task",
    name="EvaObservations",
    questions=[
        "background_time_offset",
        "crtm_coeff_dir",
        "observations",
        "observing_system_records_path",
        "window_offset"
    ]
)


# --------------------------------------------------------------------------------------------------

GetGeovals = QuestionList(
    list_type="task",
    name="GetGeovals",
    questions=[
        "background_time_offset",
        "crtm_coeff_dir",
        "geovals_experiment",
        "geovals_provider",
        "observations",
        "r2d2_local_path",
        "window_length",
        "window_offset"
    ]
)


# --------------------------------------------------------------------------------------------------

GetObservations = QuestionList(
    list_type="task",
    name="GetObservations",
    questions=[
        "background_time_offset",
        "crtm_coeff_dir",
        "cycling_varbc",
        "obs_experiment",
        "obs_provider",
        "observations",
        "observing_system_records_path",
        "r2d2_local_path",
        "window_length",
        "window_offset"
    ]
)


# --------------------------------------------------------------------------------------------------

GsiBcToIoda = QuestionList(
    list_type="task",
    name="GsiBcToIoda",
    questions=[
        "background_time_offset",
        "crtm_coeff_dir",
        "observations",
        "observing_system_records_path",
        "window_offset"
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediLocalEnsembleDaExecutable = QuestionList(
    list_type="task",
    name="RunJediLocalEnsembleDaExecutable",
    questions=[
        "background_time_offset",
        "crtm_coeff_dir",
        "ensemble_hofx_packets",
        "ensemble_hofx_strategy",
        "ensemble_num_members",
        "ensmean_only",
        "ensmeanvariance_only",
        "generate_yaml_and_exit",
        "horizontal_localization_lengthscale",
        "horizontal_localization_max_nobs",
        "horizontal_localization_method",
        "horizontal_resolution",
        "jedi_forecast_model",
        "local_ensemble_inflation_mult",
        "local_ensemble_inflation_rtpp",
        "local_ensemble_inflation_rtps",
        "local_ensemble_save_posterior_ensemble",
        "local_ensemble_save_posterior_ensemble_increments",
        "local_ensemble_save_posterior_mean",
        "local_ensemble_save_posterior_mean_increment",
        "local_ensemble_solver",
        "local_ensemble_use_linear_observer",
        "npx_proc",
        "npy_proc",
        "observations",
        "observing_system_records_path",
        "skip_ensemble_hofx",
        "total_processors",
        "vertical_localization_apply_log_transform",
        "vertical_localization_function",
        "vertical_localization_ioda_vertical_coord",
        "vertical_localization_ioda_vertical_coord_group",
        "vertical_localization_lengthscale",
        "vertical_localization_method",
        "vertical_resolution",
        "window_length",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediUfoTestsExecutable = QuestionList(
    list_type="task",
    name="RunJediUfoTestsExecutable",
    questions=[
        "background_time_offset",
        "crtm_coeff_dir",
        "generate_yaml_and_exit",
        "observations",
        "observing_system_records_path",
        "single_observations",
        "window_length",
        "window_offset"
    ]
)


# --------------------------------------------------------------------------------------------------

SaveObsDiags = QuestionList(
    list_type="task",
    name="SaveObsDiags",
    questions=[
        "background_time_offset",
        "crtm_coeff_dir",
        "observations",
        "observing_system_records_path",
        "r2d2_local_path",
        "window_offset"
    ]
)


# --------------------------------------------------------------------------------------------------

BuildJedi = QuestionList(
    list_type="task",
    name="BuildJedi",
    questions=[
        "bundles",
        "jedi_build_method"
    ]
)


# --------------------------------------------------------------------------------------------------

CloneJedi = QuestionList(
    list_type="task",
    name="CloneJedi",
    questions=[
        "bundles",
        "existing_jedi_source_directory",
        "existing_jedi_source_directory_pinned",
        "jedi_build_method"
    ]
)


# --------------------------------------------------------------------------------------------------

CleanCycle = QuestionList(
    list_type="task",
    name="CleanCycle",
    questions=[
        "clean_patterns"
    ]
)


# --------------------------------------------------------------------------------------------------

BuildGeosByLinking = QuestionList(
    list_type="task",
    name="BuildGeosByLinking",
    questions=[
        "existing_geos_gcm_build_path",
        "geos_build_method"
    ]
)


# --------------------------------------------------------------------------------------------------

PrepGeosRunDir = QuestionList(
    list_type="task",
    name="PrepGeosRunDir",
    questions=[
        "existing_geos_gcm_build_path",
        "forecast_duration",
        "geos_experiment_directory",
        "swell_static_files",
        "swell_static_files_user"
    ]
)


# --------------------------------------------------------------------------------------------------

CloneGeos = QuestionList(
    list_type="task",
    name="CloneGeos",
    questions=[
        "existing_geos_gcm_source_path",
        "geos_build_method",
        "geos_gcm_tag"
    ]
)


# --------------------------------------------------------------------------------------------------

BuildJediByLinking = QuestionList(
    list_type="task",
    name="BuildJediByLinking",
    questions=[
        "existing_jedi_build_directory",
        "existing_jedi_build_directory_pinned",
        "jedi_build_method"
    ]
)


# --------------------------------------------------------------------------------------------------

MoveForecastRestart = QuestionList(
    list_type="task",
    name="MoveForecastRestart",
    questions=[
        "forecast_duration"
    ]
)


# --------------------------------------------------------------------------------------------------

BuildGeos = QuestionList(
    list_type="task",
    name="BuildGeos",
    questions=[
        "geos_build_method"
    ]
)


# --------------------------------------------------------------------------------------------------

GetGeosRestart = QuestionList(
    list_type="task",
    name="GetGeosRestart",
    questions=[
        "geos_restarts_directory",
        "swell_static_files",
        "swell_static_files_user"
    ]
)


# --------------------------------------------------------------------------------------------------

StageJedi = QuestionList(
    list_type="task",
    name="StageJedi",
    questions=[
        "gsibec_configuration",
        "horizontal_resolution",
        "swell_static_files",
        "swell_static_files_user",
        "vertical_resolution"
    ]
)


# --------------------------------------------------------------------------------------------------

EvaIncrement = QuestionList(
    list_type="task",
    name="EvaIncrement",
    questions=[
        "marine_models",
        "window_offset",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

GenerateObservingSystemRecords = QuestionList(
    list_type="task",
    name="GenerateObservingSystemRecords",
    questions=[
        "observations",
        "observing_system_records_mksi_path",
        "observing_system_records_path"
    ]
)


# --------------------------------------------------------------------------------------------------

GsiNcdiagToIoda = QuestionList(
    list_type="task",
    name="GsiNcdiagToIoda",
    questions=[
        "observations",
        "produce_geovals",
        "single_observations",
        "window_offset"
    ]
)


# --------------------------------------------------------------------------------------------------

CloneGeosMksi = QuestionList(
    list_type="task",
    name="CloneGeosMksi",
    questions=[
        "observing_system_records_mksi_path",
        "observing_system_records_mksi_path_tag"
    ]
)


# --------------------------------------------------------------------------------------------------

GetEnsemble = QuestionList(
    list_type="task",
    name="GetEnsemble",
    questions=[
        "path_to_ensemble"
    ]
)


# --------------------------------------------------------------------------------------------------

GetGeosAdasBackground = QuestionList(
    list_type="task",
    name="GetGeosAdasBackground",
    questions=[
        "path_to_geos_adas_background"
    ]
)


# --------------------------------------------------------------------------------------------------

GetGsiBc = QuestionList(
    list_type="task",
    name="GetGsiBc",
    questions=[
        "path_to_gsi_bc_coefficients",
        "window_length"
    ]
)


# --------------------------------------------------------------------------------------------------

GetGsiNcdiag = QuestionList(
    list_type="task",
    name="GetGsiNcdiag",
    questions=[
        "path_to_gsi_nc_diags"
    ]
)


# --------------------------------------------------------------------------------------------------
