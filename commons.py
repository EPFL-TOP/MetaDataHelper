data_dirs=["other_files", "raw_files"]

data_types={"microscopy":["cell_culture", "explants", "fixed_embryos", "live_embryos"], "sequencing":["CUTandTAG","scRNA-seq","scMultiome-seq"]}


metadata_common = {
    "authors":[],
    "laboratory_contributors":[],
    "external_contributors":[],
    "experiment_name":"",
    "starting_date":{
        "year":"",
        "month":"",
        "day":""},
    "status":[],
    "experimental_tags":[],
    "fish_lines":[],
    "mutations":[],
    "phenotypes":[],
    "slim_ids":[],
    "pyrat_ids":[],
    "bioarxiv_tags":[],
    "journal_tags":[],
    "zenodo_tags":[]
}

metadata_invitro = {
    "coating":[],
    "treatment":[],
    "npositions":""
}

metadata_invivo = {
    "coating":[],
    "treatment":[],
    "npositions":""
}

metadata_scrna = {
}

metadata_scmultiome = {

}

metadata_cutandtag = {

}