from __future__ import absolute_import
from . import plotters
from . import collections
from . import selections

tp_plotters = [
    # TPPlotter(collections.tp_def, selections.tp_id_selections),
    # TPPlotter(collections.tp_truth, selections.tp_id_selections),
    # TPPlotter(selections.tp_def_uncalib, selections.tp_id_selections),
    # TPPlotter(selections.tp_def_calib, selections.tp_id_selections)
    # TPPlotter(selections.tp_hm, selections.tp_id_selections),
    plotters.TPPlotter(collections.tp_hm_vdr, selections.tp_id_selections),
    # TPPlotter(collections.tp_hm_fixed, selections.tp_id_selections),
    plotters.TPPlotter(collections.tp_hm_emint, selections.tp_id_selections),
    plotters.TPPlotter(collections.tp_hm_emint_merged, selections.tp_id_selections),
    # TPPlotter(collections.tp_hm_cylind10, selections.tp_id_selections),
    # TPPlotter(collections.tp_hm_cylind5, selections.tp_id_selections),
    # TPPlotter(collections.tp_hm_cylind2p5, selections.tp_id_selections),
    # TPPlotter(collections.tp_hm_vdr_rebin, selections.tp_id_selections),
    # TPPlotter(collections.tp_hm_vdr_stc, selections.tp_id_selections),
    # TPPlotter(selections.tp_def_nc, selections.tp_id_selections),
    # TPPlotter(selections.tp_hm_vdr_nc0, selections.tp_id_selections),
    # TPPlotter(selections.tp_hm_vdr_nc1, selections.tp_id_selections),
    # TPPlotter(selections.tp_hm_vdr_uncalib, selections.tp_id_selecti
    # TPPlotter(selections.tp_hm_vdr_merged, selections.tp_id_selections),
]

track_plotters = [plotters.TrackPlotter(collections.tracks, selections.tracks_selections)]
tkeg_plotters = [plotters.TkEGPlotter(collections.tkegs, selections.tkeg_qual_selections)]
rate_plotters = [
    plotters.RatePlotter(collections.cl3d_hm, selections.tp_rate_selections),
    plotters.RatePlotter(collections.cl3d_hm_calib, selections.tp_rate_selections),
    plotters.RatePlotter(collections.cl3d_hm_shapeDr, selections.tp_rate_selections),
    plotters.RatePlotter(collections.cl3d_hm_shapeDr_calib, selections.tp_rate_selections),
    plotters.RatePlotter(collections.cl3d_hm_shapeDr_calib_new, selections.tp_rate_selections),
    plotters.RatePlotter(collections.cl3d_hm_shapeDtDu_calib, selections.tp_rate_selections),
    # plotters.RatePlotter(collections.cl3d_hm_emint, selections.tp_rate_selections),
]

eg_rate_plotters = [
    plotters.RatePlotter(
        collections.egs, selections.eg_rate_selections),
    plotters.RatePlotter(
        collections.egs_brl, selections.eg_barrel_rate_selections),
    plotters.RatePlotter(
        collections.egs_all, selections.eg_all_rate_selections),
    plotters.RatePlotter(
        collections.tkelesEL, selections.tkisoeg_rate_selections),
    plotters.RatePlotter(
        collections.tkelesEL_brl, selections.barrel_rate_selections),
    plotters.RatePlotter(
        collections.tkelesEL_all, selections.all_rate_selections),
]

tp_calib_plotters = [
    plotters.CalibrationPlotter(
        collections.tp_hm_vdr, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    plotters.CalibrationPlotter(
        collections.tp_hm_calib, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    plotters.CalibrationPlotter(
        collections.tp_hm_shapeDr, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    plotters.CalibrationPlotter(
        collections.tp_hm_shapeDr_calib, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    plotters.CalibrationPlotter(
        collections.tp_hm_shapeDtDu, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
]

tp_genmatched_plotters = [
    plotters.TPGenMatchPlotter(
        collections.tp_hm_vdr, collections.gen_parts,
        selections.tp_match_selections, selections.gen_part_selections),
    plotters.TPGenMatchPlotter(
        collections.tp_hm_calib, collections.gen_parts,
        selections.tp_match_selections, selections.gen_part_selections),
    plotters.TPGenMatchPlotter(
        collections.tp_hm_shapeDr, collections.gen_parts,
        selections.tp_match_selections, selections.gen_part_selections),
    plotters.TPGenMatchPlotter(
        collections.tp_hm_shapeDr_calib, collections.gen_parts,
        selections.tp_match_selections, selections.gen_part_selections),
    plotters.TPGenMatchPlotter(
        collections.tp_hm_shapeDr_calib_new, collections.gen_parts,
        selections.tp_match_selections, selections.gen_part_selections),
    # plotters.TPGenMatchPlotter(
    #     collections.tp_hm_emint, collections.gen_parts,
    #     selections.tp_match_selections, selections.gen_part_selections),
    plotters.TPGenMatchPlotter(
        collections.tp_hm_shapeDtDu_calib, collections.gen_parts,
        selections.tp_match_selections, selections.gen_part_selections),
                          ]

eg_plotters = [
    plotters.EGPlotter(collections.egs_EE, selections.eg_qpt_ee_selections),
    plotters.EGPlotter(collections.egs_EE_pf, selections.eg_qpt_ee_selections),
    plotters.TkElePlotter(collections.tkeles_EE, selections.eg_qpt_ee_selections),
    plotters.TkElePlotter(collections.tkeles_EB, selections.eg_qpt_eb_selections),
    plotters.TkElePlotter(collections.tkeles_EE_pf, selections.eg_qpt_ee_selections),
    plotters.TkElePlotter(collections.tkeles_EB_pf, selections.eg_qpt_eb_selections)
    ]



# NOTE: collections and selections have been revised (and trimmed)
eg_genmatched_plotters = [
    plotters.EGGenMatchPlotter(
        collections.egs_EE, collections.gen_parts,
        selections.eg_qpt_ee_selections, selections.gen_part_ee_selections),
    plotters.EGGenMatchPlotter(
        collections.egs_EB, collections.gen_parts,
        selections.eg_qpt_eb_selections, selections.gen_part_eb_selections),
    plotters.EGGenMatchPlotter(
        collections.egs_EE_pf, collections.gen_parts,
        selections.eg_qpt_ee_selections, selections.gen_part_ee_selections),
    # plotters.EGGenMatchPlotter(
    #     collections.egs_all, collections.gen_parts,
    #     selections.egqual_pt_selections_barrel, selections.gen_part_be_selections),
    plotters.EGGenMatchPlotter(
        collections.tkeles_EE, collections.gen_parts,
        selections.eg_qpt_ee_selections, selections.gen_part_tkee_selections),
    plotters.EGGenMatchPlotter(
        collections.tkeles_EB, collections.gen_parts,
        selections.eg_qpt_eb_selections, selections.gen_part_eb_selections),
    plotters.EGGenMatchPlotter(
        collections.tkeles_EE_pf, collections.gen_parts,
        selections.eg_qpt_ee_selections, selections.gen_part_tkee_selections),
    plotters.EGGenMatchPlotter(
        collections.tkeles_EB_pf, collections.gen_parts,
        selections.eg_qpt_eb_selections, selections.gen_part_eb_selections),
    # plotters.EGGenMatchPlotter(
    #     collections.tkelesEL_all, collections.gen_parts,
    #     selections.tkisoeg_pt_selections_barrel, selections.gen_part_be_selections),
]


ele_genmatched_plotters = [
    plotters.EGGenMatchPlotter(
        collections.egs, collections.gen_parts,
        selections.eg_pt_selections, selections.gen_part_ele_selections),
    plotters.EGGenMatchPlotter(
        collections.egs_brl, collections.gen_parts,
        selections.egqual_pt_selections_barrel, selections.gen_part_barrel_selections),
    plotters.EGGenMatchPlotter(
        collections.egs_all, collections.gen_parts,
        selections.egqual_pt_selections_barrel,
        selections.gen_part_be_selections),
    # TkEGGenMatchPlotter(collections.tkegs, collections.gen_parts,
    #                     selections.tkeg_pt_selections,
    #                     selections.gen_part_selections),
    # TkEGGenMatchPlotter(collections.tkegs_emu, collections.gen_parts,
    #                     selections.tkeg_pt_selections,
    #                     selections.gen_part_selections),
    plotters.EGGenMatchPlotter(
        collections.tkelesEL, collections.gen_parts,
        selections.tkisoeg_pt_selections,
        selections.gen_part_ele_selections_tketa),
    # EGGenMatchPlotter(collections.tkeles_brl, collections.gen_parts,
    #                   selections.eg_pt_selections_barrel,
    #                   selections.gen_part_barrel_selections),
    plotters.EGGenMatchPlotter(
        collections.tkelesEL_brl, collections.gen_parts,
        selections.eg_pt_selections_barrel,
        selections.gen_part_barrel_selections),
    # EGGenMatchPlotter(collections.tkeles_all, collections.gen_parts,
    #                   selections.tkisoeg_pt_selections_barrel,
    #                   selections.gen_part_be_selections),
    plotters.EGGenMatchPlotter(
        collections.tkelesEL_all, collections.gen_parts,
        selections.tkisoeg_pt_selections_barrel,
        selections.gen_part_be_selections),
    # TPGenMatchPlotter(collections.tp_hm_emint_merged, collections.gen_parts,
    #                   selections.tp_match_selections,
    #                   selections.gen_part_selections),
    # EGGenMatchPlotter(collections.tkisoeles, collections.gen_parts,
    #                   selections.tkisoeg_pt_selections,
    #                   selections.gen_part_selections),
                  ]


eg_resotuples_plotters = [
    plotters.ResoNtupleMatchPlotter(
        collections.egs, collections.gen_parts,
        selections.eg_qual_selections,
        selections.gen_part_selections),
    # plotters.ResoNtupleMatchPlotter(
    #     collections.egs_brl, collections.gen_parts,
    #     selections.barrel_quality_selections,
    #     selections.gen_part_barrel_selections),
    # plotters.ResoNtupleMatchPlotter(
    #     collections.tkelesEL, collections.gen_parts,
    #     selections.tkisoeg_selections,
    #     selections.gen_part_selections_tketa),
    # plotters.ResoNtupleMatchPlotter(
    #     collections.tkelesEL_brl, collections.gen_parts,
    #     selections.barrel_quality_selections,
    #     selections.gen_part_barrel_selections),
    ]


tp_resotuples_plotters = [
    plotters.ResoNtupleMatchPlotter(
        collections.tp_hm_vdr, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    plotters.ResoNtupleMatchPlotter(
        collections.tp_hm_calib, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    plotters.ResoNtupleMatchPlotter(
        collections.tp_hm_shapeDr, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    plotters.ResoNtupleMatchPlotter(
        collections.tp_hm_shapeDr_calib, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    plotters.ResoNtupleMatchPlotter(
        collections.tp_hm_shapeDr_calib_new, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    plotters.ResoNtupleMatchPlotter(
        collections.tp_hm_emint, collections.gen_parts,
        selections.tp_calib_selections,
        selections.gen_part_selections_calib),
    # plotters.ResoNtupleMatchPlotter(
    #     collections.tp_hm_shapeDtDu_calib, collections.gen_parts,
    #     selections.tp_calib_selections,
    #     selections.gen_part_selections_calib),
    ]


track_genmatched_plotters = [
    plotters.TrackGenMatchPlotter(
        collections.tracks, collections.gen_parts,
        selections.tracks_selections,
        selections.gen_part_selections),
    plotters.TrackGenMatchPlotter(
        collections.tracks_emu, collections.gen_parts,
        selections.tracks_selections,
        selections.gen_part_selections)]

genpart_plotters = [
    plotters.GenPlotter(
        collections.gen_parts, selections.genpart_ele_genplotting)]

ttower_plotters = [
    plotters.TTPlotter(collections.towers_tcs),
    plotters.TTPlotter(collections.towers_sim),
    plotters.TTPlotter(collections.towers_hgcroc),
    plotters.TTPlotter(collections.towers_wafer)
]

ttower_genmatched_plotters = [
    plotters.TTGenMatchPlotter(
        collections.towers_tcs, collections.gen_parts,
        [selections.Selection('all')], selections.gen_part_selections),
    plotters.TTGenMatchPlotter(
        collections.towers_sim, collections.gen_parts,
        [selections.Selection('all')], selections.gen_part_selections),
    plotters.TTGenMatchPlotter(
        collections.towers_hgcroc, collections.gen_parts,
        [selections.Selection('all')], selections.gen_part_selections),
    plotters.TTGenMatchPlotter(
        collections.towers_wafer, collections.gen_parts,
        [selections.Selection('all')], selections.gen_part_selections)
]

correlator_occupancy_plotters = [
    plotters.CorrOccupancyPlotter(collections.tk_pfinputs, selections.pftkinput_selections),
]

pftrack_plotters = [
    plotters.TrackPlotter(collections.tk_pfinputs, selections.pftkinput_selections)]


tp_cluster_tc_match_plotters = [
    plotters.ClusterTCGenMatchPlotter(
        collections.tp_hm_vdr,
        collections.gen_parts,
        data_selections=selections.tp_tccluster_match_selections,
        gen_selections=selections.gen_part_ee_eta_brem_sel)
]

eg_isotuples_plotters = [
    plotters.IsoTuplePlotter(
        collections.tkelesEL,
        collections.gen_parts,
        selections.eg_qual_selections,
        selections.gen_part_ee_sel
        )
]
