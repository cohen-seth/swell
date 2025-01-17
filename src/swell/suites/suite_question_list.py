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
        "cycle_times",
        "ensemble_hofx_packets",
        "ensemble_hofx_strategy",
        "skip_ensemble_hofx",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

geos_marine = QuestionList(
    list_type="model_dependent",
    name="geos_marine",
    questions=[
        "marine_models"
    ]
)


# --------------------------------------------------------------------------------------------------

_3dfgat_atmos = QuestionList(
    list_type="suite",
    name="3dfgat_atmos",
    questions=[
        "cycle_times",
        "final_cycle_point",
        "model_components",
        "runahead_limit",
        "start_cycle_point"
    ]
)


# --------------------------------------------------------------------------------------------------

_3dfgat_cycle = QuestionList(
    list_type="suite",
    name="3dfgat_cycle",
    questions=[
        "cycle_times",
        "final_cycle_point",
        "marine_models",
        "model_components",
        "runahead_limit",
        "start_cycle_point"
    ]
)


# --------------------------------------------------------------------------------------------------

_3dvar = QuestionList(
    list_type="suite",
    name="3dvar",
    questions=[
        "cycle_times",
        "final_cycle_point",
        "marine_models",
        "model_components",
        "runahead_limit",
        "start_cycle_point"
    ]
)


# --------------------------------------------------------------------------------------------------

_3dvar_atmos = QuestionList(
    list_type="suite",
    name="3dvar_atmos",
    questions=[
        "cycle_times",
        "final_cycle_point",
        "model_components",
        "runahead_limit",
        "start_cycle_point"
    ]
)


# --------------------------------------------------------------------------------------------------

_3dvar_cycle = QuestionList(
    list_type="suite",
    name="3dvar_cycle",
    questions=[
        "cycle_times",
        "final_cycle_point",
        "marine_models",
        "model_components",
        "runahead_limit",
        "start_cycle_point"
    ]
)


# --------------------------------------------------------------------------------------------------

all_suites = QuestionList(
    list_type="suite",
    name="all_suites",
    questions=[
        "experiment_id",
        "experiment_root"
    ]
)


# --------------------------------------------------------------------------------------------------

convert_ncdiags = QuestionList(
    list_type="suite",
    name="convert_ncdiags",
    questions=[
        "cycle_times",
        "final_cycle_point",
        "model_components",
        "runahead_limit",
        "start_cycle_point"
    ]
)


# --------------------------------------------------------------------------------------------------

forecast_geos = QuestionList(
    list_type="suite",
    name="forecast_geos",
    questions=[
        "cycle_times",
        "final_cycle_point",
        "start_cycle_point"
    ]
)


# --------------------------------------------------------------------------------------------------

hofx = QuestionList(
    list_type="suite",
    name="hofx",
    questions=[
        "cycle_times",
        "final_cycle_point",
        "marine_models",
        "model_components",
        "runahead_limit",
        "start_cycle_point",
        "window_type"
    ]
)


# --------------------------------------------------------------------------------------------------

localensembleda = QuestionList(
    list_type="suite",
    name="localensembleda",
    questions=[
        "cycle_times",
        "ensemble_hofx_packets",
        "ensemble_hofx_strategy",
        "final_cycle_point",
        "marine_models",
        "model_components",
        "runahead_limit",
        "skip_ensemble_hofx",
        "start_cycle_point"
    ]
)


# --------------------------------------------------------------------------------------------------

ufo_testing = QuestionList(
    list_type="suite",
    name="ufo_testing",
    questions=[
        "cycle_times",
        "final_cycle_point",
        "model_components",
        "runahead_limit",
        "start_cycle_point"
    ]
)


# --------------------------------------------------------------------------------------------------
