# --------------------------------------------------------------------------------------------------
# (C) Copyright 2021- United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration. All Rights Reserved.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.


# --------------------------------------------------------------------------------------------------


from swell.utilities.swell_questions import SuiteQuestionList
import swell.suites.suite_questions as sq


# --------------------------------------------------------------------------------------------------

_3dfgat_atmos = SuiteQuestionList(
    name="3dfgat_atmos",
    questions=[
        sq.cycle_times,
        sq.final_cycle_point,
        sq.model_components,
        sq.runahead_limit,
        sq.start_cycle_point
    ]
)


# --------------------------------------------------------------------------------------------------

_3dfgat_cycle = SuiteQuestionList(
    name="3dfgat_cycle",
    questions=[
        sq.cycle_times,
        sq.final_cycle_point,
        sq.marine_models,
        sq.model_components,
        sq.runahead_limit,
        sq.start_cycle_point
    ]
)


# --------------------------------------------------------------------------------------------------

_3dvar = SuiteQuestionList(
    name="3dvar",
    questions=[
        sq.cycle_times,
        sq.final_cycle_point,
        sq.marine_models,
        sq.model_components,
        sq.runahead_limit,
        sq.start_cycle_point
    ]
)


# --------------------------------------------------------------------------------------------------

_3dvar_atmos = SuiteQuestionList(
    name="3dvar_atmos",
    questions=[
        sq.cycle_times,
        sq.final_cycle_point,
        sq.model_components,
        sq.runahead_limit,
        sq.start_cycle_point
    ]
)


# --------------------------------------------------------------------------------------------------

_3dvar_cycle = SuiteQuestionList(
    name="3dvar_cycle",
    questions=[
        sq.cycle_times,
        sq.final_cycle_point,
        sq.marine_models,
        sq.model_components,
        sq.runahead_limit,
        sq.start_cycle_point
    ]
)


# --------------------------------------------------------------------------------------------------

all_suites = SuiteQuestionList(
    name="all_suites",
    questions=[
        sq.experiment_id,
        sq.experiment_root
    ]
)


# --------------------------------------------------------------------------------------------------

convert_ncdiags = SuiteQuestionList(
    name="convert_ncdiags",
    questions=[
        sq.cycle_times,
        sq.final_cycle_point,
        sq.model_components,
        sq.runahead_limit,
        sq.start_cycle_point
    ]
)


# --------------------------------------------------------------------------------------------------

forecast_geos = SuiteQuestionList(
    name="forecast_geos",
    questions=[
        sq.cycle_times,
        sq.final_cycle_point,
        sq.start_cycle_point
    ]
)


# --------------------------------------------------------------------------------------------------

hofx = SuiteQuestionList(
    name="hofx",
    questions=[
        sq.cycle_times,
        sq.final_cycle_point,
        sq.marine_models,
        sq.model_components,
        sq.runahead_limit,
        sq.start_cycle_point,
        sq.window_type
    ]
)


# --------------------------------------------------------------------------------------------------

localensembleda = SuiteQuestionList(
    name="localensembleda",
    questions=[
        sq.cycle_times,
        sq.ensemble_hofx_packets,
        sq.ensemble_hofx_strategy,
        sq.final_cycle_point,
        sq.marine_models,
        sq.model_components,
        sq.runahead_limit,
        sq.skip_ensemble_hofx,
        sq.start_cycle_point
    ]
)


# --------------------------------------------------------------------------------------------------

ufo_testing = SuiteQuestionList(
    name="ufo_testing",
    questions=[
        sq.cycle_times,
        sq.final_cycle_point,
        sq.model_components,
        sq.runahead_limit,
        sq.start_cycle_point
    ]
)


# --------------------------------------------------------------------------------------------------
