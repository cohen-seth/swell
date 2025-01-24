# --------------------------------------------------------------------------------------------------
# (C) Copyright 2021- United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration. All Rights Reserved.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.


# --------------------------------------------------------------------------------------------------

from swell.utilities.swell_questions import TaskQuestionList
import swell.tasks.task_questions as tq


# --------------------------------------------------------------------------------------------------

GetBackground = TaskQuestionList(
    name="GetBackground",
    questions=[
        tq.analysis_forecast_window_offset,
        tq.background_experiment,
        tq.background_frequency,
        tq.horizontal_resolution,
        tq.r2d2_local_path,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

MoveDaRestart = TaskQuestionList(
    name="MoveDaRestart",
    questions=[
        tq.analysis_forecast_window_offset,
        tq.mom6_iau,
        tq.window_length
    ]
)


# --------------------------------------------------------------------------------------------------

PrepareAnalysis = TaskQuestionList(
    name="PrepareAnalysis",
    questions=[
        tq.analysis_forecast_window_offset,
        tq.analysis_variables,
        tq.mom6_iau,
        tq.total_processors
    ]
)


# --------------------------------------------------------------------------------------------------

StoreBackground = TaskQuestionList(
    name="StoreBackground",
    questions=[
        tq.analysis_forecast_window_offset,
        tq.background_experiment,
        tq.background_frequency,
        tq.horizontal_resolution,
        tq.r2d2_local_path,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

GenerateBClimatology = TaskQuestionList(
    name="GenerateBClimatology",
    questions=[
        tq.analysis_variables,
        tq.background_error_model,
        tq.generate_yaml_and_exit,
        tq.horizontal_resolution,
        tq.marine_models,
        tq.npx_proc,
        tq.npy_proc,
        tq.swell_static_files,
        tq.swell_static_files_user,
        tq.total_processors,
        tq.vertical_resolution,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediConvertStateSoca2ciceExecutable = TaskQuestionList(
    name="RunJediConvertStateSoca2ciceExecutable",
    questions=[
        tq.analysis_variables,
        tq.cice6_domains,
        tq.generate_yaml_and_exit,
        tq.jedi_forecast_model,
        tq.marine_models,
        tq.observations,
        tq.total_processors,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediEnsembleMeanVariance = TaskQuestionList(
    name="RunJediEnsembleMeanVariance",
    questions=[
        tq.analysis_variables,
        tq.ensemble_num_members,
        tq.generate_yaml_and_exit,
        tq.horizontal_resolution,
        tq.jedi_forecast_model,
        tq.npx_proc,
        tq.npy_proc,
        tq.observations,
        tq.observing_system_records_path,
        tq.vertical_resolution,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediFgatExecutable = TaskQuestionList(
    name="RunJediFgatExecutable",
    questions=[
        tq.analysis_variables,
        tq.background_frequency,
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.generate_yaml_and_exit,
        tq.gradient_norm_reduction,
        tq.gsibec_configuration,
        tq.horizontal_resolution,
        tq.jedi_forecast_model,
        tq.marine_models,
        tq.minimizer,
        tq.npx_proc,
        tq.npy_proc,
        tq.number_of_iterations,
        tq.observations,
        tq.observing_system_records_path,
        tq.total_processors,
        tq.vertical_resolution,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediVariationalExecutable = TaskQuestionList(
    name="RunJediVariationalExecutable",
    questions=[
        tq.analysis_variables,
        tq.background_frequency,
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.generate_yaml_and_exit,
        tq.gradient_norm_reduction,
        tq.gsibec_configuration,
        tq.horizontal_resolution,
        tq.jedi_forecast_model,
        tq.minimizer,
        tq.npx_proc,
        tq.npy_proc,
        tq.number_of_iterations,
        tq.observations,
        tq.observing_system_records_path,
        tq.total_processors,
        tq.vertical_resolution,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

GenerateBClimatologyByLinking = TaskQuestionList(
    name="GenerateBClimatologyByLinking",
    questions=[
        tq.background_error_model,
        tq.horizontal_resolution,
        tq.swell_static_files,
        tq.swell_static_files_user,
        tq.vertical_resolution,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

GetBackgroundGeosExperiment = TaskQuestionList(
    name="GetBackgroundGeosExperiment",
    questions=[
        tq.background_experiment,
        tq.background_time_offset,
        tq.geos_x_background_directory
    ]
)


# --------------------------------------------------------------------------------------------------

LinkGeosOutput = TaskQuestionList(
    name="LinkGeosOutput",
    questions=[
        tq.background_frequency,
        tq.marine_models,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediHofxEnsembleExecutable = TaskQuestionList(
    name="RunJediHofxEnsembleExecutable",
    questions=[
        tq.background_frequency,
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.ensemble_hofx_packets,
        tq.ensemble_hofx_strategy,
        tq.ensemble_num_members,
        tq.generate_yaml_and_exit,
        tq.horizontal_resolution,
        tq.jedi_forecast_model,
        tq.npx_proc,
        tq.npy_proc,
        tq.observations,
        tq.total_processors,
        tq.vertical_resolution,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediHofxExecutable = TaskQuestionList(
    name="RunJediHofxExecutable",
    questions=[
        tq.background_frequency,
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.generate_yaml_and_exit,
        tq.horizontal_resolution,
        tq.jedi_forecast_model,
        tq.npx_proc,
        tq.npy_proc,
        tq.observations,
        tq.observing_system_records_path,
        tq.save_geovals,
        tq.total_processors,
        tq.vertical_resolution,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediObsfiltersExecutable = TaskQuestionList(
    name="RunJediObsfiltersExecutable",
    questions=[
        tq.background_frequency,
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.generate_yaml_and_exit,
        tq.horizontal_resolution,
        tq.jedi_forecast_model,
        tq.npx_proc,
        tq.npy_proc,
        tq.observations,
        tq.observing_system_records_path,
        tq.total_processors,
        tq.vertical_resolution,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

EvaObservations = TaskQuestionList(
    name="EvaObservations",
    questions=[
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.observations,
        tq.observing_system_records_path,
        tq.window_offset
    ]
)


# --------------------------------------------------------------------------------------------------

GetGeovals = TaskQuestionList(
    name="GetGeovals",
    questions=[
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.geovals_experiment,
        tq.geovals_provider,
        tq.observations,
        tq.r2d2_local_path,
        tq.window_length,
        tq.window_offset
    ]
)


# --------------------------------------------------------------------------------------------------

GetObservations = TaskQuestionList(
    name="GetObservations",
    questions=[
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.cycling_varbc,
        tq.obs_experiment,
        tq.obs_provider,
        tq.observations,
        tq.observing_system_records_path,
        tq.r2d2_local_path,
        tq.window_length,
        tq.window_offset
    ]
)


# --------------------------------------------------------------------------------------------------

GsiBcToIoda = TaskQuestionList(
    name="GsiBcToIoda",
    questions=[
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.observations,
        tq.observing_system_records_path,
        tq.window_offset
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediLocalEnsembleDaExecutable = TaskQuestionList(
    name="RunJediLocalEnsembleDaExecutable",
    questions=[
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.ensemble_hofx_packets,
        tq.ensemble_hofx_strategy,
        tq.ensemble_num_members,
        tq.ensmean_only,
        tq.ensmeanvariance_only,
        tq.generate_yaml_and_exit,
        tq.horizontal_localization_lengthscale,
        tq.horizontal_localization_max_nobs,
        tq.horizontal_localization_method,
        tq.horizontal_resolution,
        tq.jedi_forecast_model,
        tq.local_ensemble_inflation_mult,
        tq.local_ensemble_inflation_rtpp,
        tq.local_ensemble_inflation_rtps,
        tq.local_ensemble_save_posterior_ensemble,
        tq.local_ensemble_save_posterior_ensemble_increments,
        tq.local_ensemble_save_posterior_mean,
        tq.local_ensemble_save_posterior_mean_increment,
        tq.local_ensemble_solver,
        tq.local_ensemble_use_linear_observer,
        tq.npx_proc,
        tq.npy_proc,
        tq.observations,
        tq.observing_system_records_path,
        tq.skip_ensemble_hofx,
        tq.total_processors,
        tq.vertical_localization_apply_log_transform,
        tq.vertical_localization_function,
        tq.vertical_localization_ioda_vertical_coord,
        tq.vertical_localization_ioda_vertical_coord_group,
        tq.vertical_localization_lengthscale,
        tq.vertical_localization_method,
        tq.vertical_resolution,
        tq.window_length,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

RunJediUfoTestsExecutable = TaskQuestionList(
    name="RunJediUfoTestsExecutable",
    questions=[
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.generate_yaml_and_exit,
        tq.observations,
        tq.observing_system_records_path,
        tq.single_observations,
        tq.window_length,
        tq.window_offset
    ]
)


# --------------------------------------------------------------------------------------------------

SaveObsDiags = TaskQuestionList(
    name="SaveObsDiags",
    questions=[
        tq.background_time_offset,
        tq.crtm_coeff_dir,
        tq.observations,
        tq.observing_system_records_path,
        tq.r2d2_local_path,
        tq.window_offset
    ]
)


# --------------------------------------------------------------------------------------------------

BuildJedi = TaskQuestionList(
    name="BuildJedi",
    questions=[
        tq.bundles,
        tq.jedi_build_method
    ]
)


# --------------------------------------------------------------------------------------------------

CloneJedi = TaskQuestionList(
    name="CloneJedi",
    questions=[
        tq.bundles,
        tq.existing_jedi_source_directory,
        tq.existing_jedi_source_directory_pinned,
        tq.jedi_build_method
    ]
)


# --------------------------------------------------------------------------------------------------

CleanCycle = TaskQuestionList(
    name="CleanCycle",
    questions=[
        tq.clean_patterns
    ]
)


# --------------------------------------------------------------------------------------------------

BuildGeosByLinking = TaskQuestionList(
    name="BuildGeosByLinking",
    questions=[
        tq.existing_geos_gcm_build_path,
        tq.geos_build_method
    ]
)


# --------------------------------------------------------------------------------------------------

PrepGeosRunDir = TaskQuestionList(
    name="PrepGeosRunDir",
    questions=[
        tq.existing_geos_gcm_build_path,
        tq.forecast_duration,
        tq.geos_experiment_directory,
        tq.swell_static_files,
        tq.swell_static_files_user
    ]
)


# --------------------------------------------------------------------------------------------------

CloneGeos = TaskQuestionList(
    name="CloneGeos",
    questions=[
        tq.existing_geos_gcm_source_path,
        tq.geos_build_method,
        tq.geos_gcm_tag
    ]
)


# --------------------------------------------------------------------------------------------------

BuildJediByLinking = TaskQuestionList(
    name="BuildJediByLinking",
    questions=[
        tq.existing_jedi_build_directory,
        tq.existing_jedi_build_directory_pinned,
        tq.jedi_build_method
    ]
)


# --------------------------------------------------------------------------------------------------

MoveForecastRestart = TaskQuestionList(
    name="MoveForecastRestart",
    questions=[
        tq.forecast_duration
    ]
)


# --------------------------------------------------------------------------------------------------

BuildGeos = TaskQuestionList(
    name="BuildGeos",
    questions=[
        tq.geos_build_method
    ]
)


# --------------------------------------------------------------------------------------------------

GetGeosRestart = TaskQuestionList(
    name="GetGeosRestart",
    questions=[
        tq.geos_restarts_directory,
        tq.swell_static_files,
        tq.swell_static_files_user
    ]
)


# --------------------------------------------------------------------------------------------------

StageJedi = TaskQuestionList(
    name="StageJedi",
    questions=[
        tq.gsibec_configuration,
        tq.horizontal_resolution,
        tq.swell_static_files,
        tq.swell_static_files_user,
        tq.vertical_resolution
    ]
)


# --------------------------------------------------------------------------------------------------

EvaIncrement = TaskQuestionList(
    name="EvaIncrement",
    questions=[
        tq.marine_models,
        tq.window_offset,
        tq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

GenerateObservingSystemRecords = TaskQuestionList(
    name="GenerateObservingSystemRecords",
    questions=[
        tq.observations,
        tq.observing_system_records_mksi_path,
        tq.observing_system_records_path
    ]
)


# --------------------------------------------------------------------------------------------------

GsiNcdiagToIoda = TaskQuestionList(
    name="GsiNcdiagToIoda",
    questions=[
        tq.observations,
        tq.produce_geovals,
        tq.single_observations,
        tq.window_offset
    ]
)


# --------------------------------------------------------------------------------------------------

CloneGeosMksi = TaskQuestionList(
    name="CloneGeosMksi",
    questions=[
        tq.observing_system_records_mksi_path,
        tq.observing_system_records_mksi_path_tag
    ]
)


# --------------------------------------------------------------------------------------------------

GetEnsemble = TaskQuestionList(
    name="GetEnsemble",
    questions=[
        tq.path_to_ensemble
    ]
)


# --------------------------------------------------------------------------------------------------

GetGeosAdasBackground = TaskQuestionList(
    name="GetGeosAdasBackground",
    questions=[
        tq.path_to_geos_adas_background
    ]
)


# --------------------------------------------------------------------------------------------------

GetGsiBc = TaskQuestionList(
    name="GetGsiBc",
    questions=[
        tq.path_to_gsi_bc_coefficients,
        tq.window_length
    ]
)


# --------------------------------------------------------------------------------------------------

GetGsiNcdiag = TaskQuestionList(
    name="GetGsiNcdiag",
    questions=[
        tq.path_to_gsi_nc_diags
    ]
)


# --------------------------------------------------------------------------------------------------
